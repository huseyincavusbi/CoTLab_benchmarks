"""
Prompt Ablation Study for Contrarian Effectiveness.

This script tests variations of the contrarian prompt by removing different
components to find which phrase is essential for the early commitment effect.

Key question: Is "devil's advocate", "obvious", or "argue against" essential?
"""

import sys
sys.path.insert(0, '/home/ubuntu/TransformerLens')

import torch
import numpy as np
from typing import Dict, List, Tuple, Optional
from tqdm import tqdm
import einops

from config import (
    MODEL_NAME, N_LAYERS,
    ABLATION_PROMPTS, MEDICAL_CASES,
    CONTRARIAN_COMMIT_LAYER, TOP_K_PREDICTIONS
)
from utils import (
    create_prompt, format_gemma3_chat, get_answer_token_ids, 
    get_token_probability, get_token_rank, in_top_k,
    save_results, load_model_and_tokenizer,
    clear_gpu_memory, get_gpu_memory_usage, 
    setup_plot_style, save_plot
)

import matplotlib.pyplot as plt


def run_logit_lens_quick(
    model,
    prompt: str,
    answer_token_ids: List[int],
    key_layers: List[int] = None,
) -> Dict:
    """
    Run a quick logit lens analysis at key layers only.
    
    Args:
        model: HookedTransformer model
        prompt: Formatted prompt string
        answer_token_ids: Token IDs to track
        key_layers: Specific layers to analyze (if None, use all)
        
    Returns:
        Dict with probability, rank, and commitment info
    """
    if key_layers is None:
        key_layers = list(range(0, N_LAYERS, 3)) + [N_LAYERS - 1]
    
    with torch.no_grad():
        logits, cache = model.run_with_cache(
            prompt,
            prepend_bos=True,
            return_type="logits",
        )
    
    ln_final = model.ln_final
    W_U = model.W_U
    b_U = model.b_U if hasattr(model, 'b_U') else None
    
    layer_probs = []
    layer_ranks = []
    
    for layer in range(N_LAYERS):
        if layer in key_layers or layer == N_LAYERS - 1:
            resid = cache['resid_post', layer]
            resid_normed = ln_final(resid.float()).to(resid.dtype)
            
            layer_logits = einops.einsum(
                resid_normed, W_U,
                "batch pos d_model, d_model d_vocab -> batch pos d_vocab"
            )
            if b_U is not None:
                layer_logits = layer_logits + b_U
            
            prob = get_token_probability(layer_logits, answer_token_ids)
            rank = get_token_rank(layer_logits, answer_token_ids)
        else:
            prob = 0
            rank = float('inf')
        
        layer_probs.append(prob)
        layer_ranks.append(rank if rank != float('inf') else 999999)
    
    # Find commitment layer
    commitment_layer = -1
    for layer in range(N_LAYERS):
        if layer_ranks[layer] < TOP_K_PREDICTIONS:
            # Check if it stays in top-k
            remaining = layer_ranks[layer:min(layer + 4, N_LAYERS)]
            if all(r < TOP_K_PREDICTIONS for r in remaining if r != 999999):
                commitment_layer = layer
                break
    
    # Get final probability
    final_prob = layer_probs[-1]
    final_logits = model(prompt, prepend_bos=True)
    actual_final_prob = get_token_probability(final_logits, answer_token_ids)
    
    del cache
    clear_gpu_memory()
    
    return {
        'layer_probs': layer_probs,
        'layer_ranks': layer_ranks,
        'commitment_layer': commitment_layer,
        'final_probability': actual_final_prob,
    }


def run_ablation_on_case(
    model,
    case,
) -> Dict:
    """
    Run ablation study on a single medical case.
    
    Tests all prompt variations and measures their effect on:
    1. Commitment layer
    2. Final probability
    3. Layer-wise probability evolution
    
    Args:
        model: HookedTransformer model
        case: MedicalCase object
        
    Returns:
        Dict with results for each ablation variant
    """
    print(f"\n{'='*60}")
    print(f"Ablation Study: {case.name}")
    print(f"{'='*60}")
    
    answer_token_ids = get_answer_token_ids(model.tokenizer, case.answer_tokens)
    print(f"Answer: {case.expected_answer}")
    print(f"Token IDs: {answer_token_ids}")
    
    results = {}
    
    for variant_name, prompt_strategy in ABLATION_PROMPTS.items():
        print(f"\n--- {variant_name} ---")
        
        prompt = create_prompt(prompt_strategy, case)
        
        # Run logit lens
        lens_results = run_logit_lens_quick(model, prompt, answer_token_ids)
        
        results[variant_name] = {
            'commitment_layer': lens_results['commitment_layer'],
            'final_probability': lens_results['final_probability'],
            'layer_probs': lens_results['layer_probs'],
            'layer_ranks': lens_results['layer_ranks'],
        }
        
        print(f"Commitment layer: {lens_results['commitment_layer']}")
        print(f"Final probability: {lens_results['final_probability']:.4f}")
    
    return results


def analyze_ablation_impact(all_results: Dict) -> Dict:
    """
    Analyze which ablation had the most impact on commitment.
    
    Args:
        all_results: Results across all cases
        
    Returns:
        Dict with impact analysis
    """
    # Aggregate across cases
    variants = list(ABLATION_PROMPTS.keys())
    
    impact = {}
    
    for variant in variants:
        commitment_layers = []
        final_probs = []
        
        for case_results in all_results.values():
            if variant in case_results:
                cl = case_results[variant]['commitment_layer']
                if cl >= 0:
                    commitment_layers.append(cl)
                final_probs.append(case_results[variant]['final_probability'])
        
        impact[variant] = {
            'mean_commitment_layer': np.mean(commitment_layers) if commitment_layers else -1,
            'std_commitment_layer': np.std(commitment_layers) if commitment_layers else 0,
            'mean_final_probability': np.mean(final_probs),
            'cases_with_commitment': len(commitment_layers),
        }
    
    # Compare to full prompt
    full_commit = impact['full']['mean_commitment_layer']
    
    for variant, data in impact.items():
        if variant != 'full' and data['mean_commitment_layer'] >= 0:
            commit_change = data['mean_commitment_layer'] - full_commit
            data['commitment_change_vs_full'] = float(commit_change)
            data['commitment_delayed'] = bool(commit_change > 5)  # Delayed by more than 5 layers
        else:
            data['commitment_change_vs_full'] = 0.0
            data['commitment_delayed'] = False
    
    return impact


def plot_ablation_results(all_results: Dict, impact: Dict):
    """Create visualizations of ablation study results."""
    setup_plot_style()
    
    # Plot 1: Commitment layer comparison
    fig, ax = plt.subplots(figsize=(12, 6))
    
    variants = list(impact.keys())
    commit_layers = [impact[v]['mean_commitment_layer'] for v in variants]
    commit_std = [impact[v]['std_commitment_layer'] for v in variants]
    
    colors = ['#2ecc71' if v == 'full' else '#3498db' for v in variants]
    
    bars = ax.bar(range(len(variants)), commit_layers, yerr=commit_std, 
                  capsize=5, color=colors, alpha=0.8)
    
    ax.axhline(y=CONTRARIAN_COMMIT_LAYER, color='red', linestyle='--', 
               alpha=0.7, label=f'Expected (L{CONTRARIAN_COMMIT_LAYER})')
    
    ax.set_xticks(range(len(variants)))
    ax.set_xticklabels([v.replace('_', '\n') for v in variants], fontsize=9)
    ax.set_ylabel('Mean Commitment Layer')
    ax.set_title('Effect of Prompt Ablation on Commitment Layer')
    ax.legend()
    
    # Add value labels on bars
    for bar, val in zip(bars, commit_layers):
        if val >= 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                   f'{val:.1f}', ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    save_plot(fig, 'ablation_commitment_layers')
    plt.close()
    
    # Plot 2: Final probability comparison
    fig, ax = plt.subplots(figsize=(12, 6))
    
    final_probs = [impact[v]['mean_final_probability'] for v in variants]
    
    bars = ax.bar(range(len(variants)), final_probs, color=colors, alpha=0.8)
    
    ax.set_xticks(range(len(variants)))
    ax.set_xticklabels([v.replace('_', '\n') for v in variants], fontsize=9)
    ax.set_ylabel('Mean Final Probability')
    ax.set_title('Effect of Prompt Ablation on Final Answer Probability')
    ax.set_ylim(0, 1)
    
    for bar, val in zip(bars, final_probs):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
               f'{val:.3f}', ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    save_plot(fig, 'ablation_final_probability')
    plt.close()
    
    # Plot 3: Layer-wise probability for each variant (one case as example)
    example_case = list(all_results.keys())[0]
    case_results = all_results[example_case]
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    for variant in variants:
        if variant in case_results:
            probs = case_results[variant]['layer_probs']
            ax.plot(range(len(probs)), probs, label=variant.replace('_', ' '), 
                   marker='o', markersize=2, alpha=0.8)
    
    ax.axvline(x=CONTRARIAN_COMMIT_LAYER, color='red', linestyle='--', 
               alpha=0.7, label=f'Expected Commit (L{CONTRARIAN_COMMIT_LAYER})')
    
    ax.set_xlabel('Layer')
    ax.set_ylabel('Answer Probability')
    ax.set_title(f'Ablation Effect on Layer-wise Probability - {example_case.title()}')
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_plot(fig, 'ablation_layer_sweep')
    plt.close()


def identify_essential_components(impact: Dict) -> Dict:
    """
    Identify which prompt components are essential for early commitment.
    
    A component is essential if removing it significantly delays commitment.
    
    Args:
        impact: Impact analysis results
        
    Returns:
        Dict with essential component analysis
    """
    full_commit = impact['full']['mean_commitment_layer']
    
    essential = []
    non_essential = []
    
    component_map = {
        'no_devils_advocate': "devil's advocate",
        'no_obvious': "obvious",
        'no_argue_against': "argue against",
        'neutral_system': "skeptical system message",
    }
    
    for variant, component in component_map.items():
        if variant in impact:
            change = impact[variant]['commitment_change_vs_full']
            is_essential = change > 5  # Delayed by more than 5 layers
            
            if is_essential:
                essential.append((component, change))
            else:
                non_essential.append((component, change))
    
    # Sort by impact
    essential.sort(key=lambda x: -x[1])
    non_essential.sort(key=lambda x: -x[1])
    
    return {
        'essential_components': essential,
        'non_essential_components': non_essential,
        'full_commitment_layer': full_commit,
        'minimal_commitment_layer': impact.get('minimal', {}).get('mean_commitment_layer', -1),
    }


def main():
    """Main entry point for ablation study."""
    print("=" * 70)
    print("Prompt Ablation Study")
    print("=" * 70)
    print(f"GPU Memory: {get_gpu_memory_usage()}")
    
    # Load model
    model, tokenizer = load_model_and_tokenizer(MODEL_NAME)
    
    # Run ablation on all cases
    all_results = {}
    
    for case in MEDICAL_CASES:
        case_results = run_ablation_on_case(model, case)
        all_results[case.name] = case_results
    
    # Analyze impact
    impact = analyze_ablation_impact(all_results)
    
    # Create visualizations
    plot_ablation_results(all_results, impact)
    
    # Identify essential components
    essential = identify_essential_components(impact)
    
    # Summary
    print("\n" + "=" * 70)
    print("ABLATION SUMMARY")
    print("=" * 70)
    
    print(f"\nFull contrarian prompt commits at layer: {essential['full_commitment_layer']:.1f}")
    print(f"Minimal prompt commits at layer: {essential['minimal_commitment_layer']:.1f}")
    
    print("\n📌 ESSENTIAL COMPONENTS (removing delays commitment significantly):")
    if essential['essential_components']:
        for component, change in essential['essential_components']:
            print(f"  • '{component}' - removal delays commitment by {change:.1f} layers")
    else:
        print("  None identified - all components contribute similarly")
    
    print("\n📎 Non-essential components:")
    if essential['non_essential_components']:
        for component, change in essential['non_essential_components']:
            print(f"  • '{component}' - removal delays commitment by only {change:.1f} layers")
    
    print("\n" + "-" * 40)
    print("All variant results:")
    for variant, data in impact.items():
        commit = data['mean_commitment_layer']
        prob = data['mean_final_probability']
        print(f"  {variant:20s}: L{commit:5.1f}, prob={prob:.4f}")
    
    # Save results
    save_results(all_results, "ablation_full_results")
    save_results(impact, "ablation_impact")
    save_results(essential, "ablation_essential_components")
    
    print("\n" + "=" * 70)
    print("Ablation study complete!")
    print("=" * 70)
    
    return all_results, impact, essential


if __name__ == "__main__":
    results, impact, essential = main()
