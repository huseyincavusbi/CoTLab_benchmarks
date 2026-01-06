"""
Activation Patching Experiment for MedGemma.

This script tests whether early commitment is the mechanism behind contrarian's
superior performance by patching Layer 18 activations from contrarian into CoT.

Key hypothesis: If patching L18 from contrarian into CoT improves CoT's answer
probability, this proves early commitment is the causal mechanism.
"""

import sys
sys.path.insert(0, '/home/ubuntu/TransformerLens')

import torch
import numpy as np
from typing import Dict, List, Tuple, Optional, Callable
from tqdm import tqdm
from functools import partial

from config import (
    MODEL_NAME, N_LAYERS,
    PROMPT_STRATEGIES, MEDICAL_CASES,
    CONTRARIAN_COMMIT_LAYER, PATCH_LAYERS
)
from utils import (
    create_prompt, get_answer_token_ids, get_token_probability,
    save_results, load_model_and_tokenizer,
    clear_gpu_memory, get_gpu_memory_usage, setup_plot_style, save_plot
)

import matplotlib.pyplot as plt


def get_activation_hook(
    cache_dict: Dict,
    hook_name: str,
) -> Callable:
    """
    Create a hook function that stores activations in cache_dict.
    
    Args:
        cache_dict: Dictionary to store activations
        hook_name: Name to use as key in cache_dict
        
    Returns:
        Hook function
    """
    def hook_fn(activation, hook):
        cache_dict[hook_name] = activation.clone()
        return activation
    return hook_fn


def patch_activation_hook(
    patched_activation: torch.Tensor,
) -> Callable:
    """
    Create a hook function that replaces activation with patched version.
    
    Args:
        patched_activation: Activation to patch in
        
    Returns:
        Hook function that returns the patched activation
    """
    def hook_fn(activation, hook):
        # Match shape - patch only works if sequence lengths are compatible
        if activation.shape == patched_activation.shape:
            return patched_activation.clone()
        else:
            # If shapes don't match, patch what we can
            # Take the minimum sequence length
            min_pos = min(activation.shape[1], patched_activation.shape[1])
            result = activation.clone()
            result[:, :min_pos] = patched_activation[:, :min_pos]
            return result
    return hook_fn


def run_with_patching(
    model,
    base_prompt: str,
    source_prompt: str,
    answer_token_ids: List[int],
    patch_layer: int = 18,
    hook_type: str = "resid_post",
) -> Dict:
    """
    Run the model with activations patched from source into base prompt.
    
    Args:
        model: HookedTransformer model
        base_prompt: The prompt to run (e.g., CoT prompt)
        source_prompt: The prompt to get activations from (e.g., contrarian)
        answer_token_ids: Token IDs for the correct answer
        patch_layer: Layer to patch
        hook_type: Type of hook (resid_pre, resid_mid, resid_post)
        
    Returns:
        Dict with baseline, patched, and source probabilities
    """
    results = {}
    hook_name = f"blocks.{patch_layer}.hook_{hook_type}"
    
    with torch.no_grad():
        # 1. Get baseline probability for base prompt (no patching)
        base_logits = model(base_prompt, prepend_bos=True)
        base_prob = get_token_probability(base_logits, answer_token_ids)
        results['base_probability'] = base_prob
        
        # 2. Get source activation from source prompt
        source_cache = {}
        source_logits = model.run_with_hooks(
            source_prompt,
            prepend_bos=True,
            fwd_hooks=[(hook_name, get_activation_hook(source_cache, 'activation'))]
        )
        source_prob = get_token_probability(source_logits, answer_token_ids)
        results['source_probability'] = source_prob
        
        source_activation = source_cache['activation']
        
        # 3. Run base prompt with patched activation from source
        patched_logits = model.run_with_hooks(
            base_prompt,
            prepend_bos=True,
            fwd_hooks=[(hook_name, patch_activation_hook(source_activation))]
        )
        patched_prob = get_token_probability(patched_logits, answer_token_ids)
        results['patched_probability'] = patched_prob
        
        # 4. Compute improvement
        results['improvement'] = patched_prob - base_prob
        results['normalized_improvement'] = (
            (patched_prob - base_prob) / (source_prob - base_prob + 1e-10)
            if source_prob > base_prob else 0
        )
    
    clear_gpu_memory()
    return results


def sweep_patch_layers(
    model,
    base_prompt: str,
    source_prompt: str,
    answer_token_ids: List[int],
    layers: List[int],
    hook_type: str = "resid_post",
) -> Dict:
    """
    Sweep across multiple layers to find the most impactful layer to patch.
    
    Returns:
        Dict mapping layer to patching results
    """
    results = {}
    
    for layer in tqdm(layers, desc="Patching layers"):
        layer_results = run_with_patching(
            model, base_prompt, source_prompt, 
            answer_token_ids, patch_layer=layer, hook_type=hook_type
        )
        results[layer] = layer_results
    
    return results


def run_patching_experiment(
    model,
    case,
) -> Dict:
    """
    Run activation patching experiment for a single case.
    
    Tests patching from contrarian into CoT and direct answer prompts.
    
    Args:
        model: HookedTransformer model
        case: MedicalCase object
        
    Returns:
        Dict with patching results
    """
    print(f"\n{'='*60}")
    print(f"Patching Experiment: {case.name}")
    print(f"{'='*60}")
    
    # Get answer token IDs
    answer_token_ids = get_answer_token_ids(model.tokenizer, case.answer_tokens)
    
    # Create prompts
    contrarian_prompt = create_prompt(PROMPT_STRATEGIES['contrarian'], case)
    cot_prompt = create_prompt(PROMPT_STRATEGIES['chain_of_thought'], case)
    direct_prompt = create_prompt(PROMPT_STRATEGIES['direct_answer'], case)
    
    results = {
        'case_name': case.name,
        'answer_token_ids': answer_token_ids,
    }
    
    # Test 1: Patch L18 from contrarian into CoT
    print("\n--- Patching Contrarian L18 -> CoT ---")
    cot_patch_results = run_with_patching(
        model, cot_prompt, contrarian_prompt,
        answer_token_ids, patch_layer=CONTRARIAN_COMMIT_LAYER
    )
    results['contrarian_to_cot'] = cot_patch_results
    
    print(f"CoT baseline prob: {cot_patch_results['base_probability']:.4f}")
    print(f"Contrarian prob: {cot_patch_results['source_probability']:.4f}")
    print(f"CoT with L18 patch: {cot_patch_results['patched_probability']:.4f}")
    print(f"Improvement: {cot_patch_results['improvement']:.4f}")
    
    # Test 2: Patch L18 from contrarian into direct answer
    print("\n--- Patching Contrarian L18 -> Direct ---")
    direct_patch_results = run_with_patching(
        model, direct_prompt, contrarian_prompt,
        answer_token_ids, patch_layer=CONTRARIAN_COMMIT_LAYER
    )
    results['contrarian_to_direct'] = direct_patch_results
    
    print(f"Direct baseline prob: {direct_patch_results['base_probability']:.4f}")
    print(f"Direct with L18 patch: {direct_patch_results['patched_probability']:.4f}")
    print(f"Improvement: {direct_patch_results['improvement']:.4f}")
    
    # Test 3: Layer sweep for CoT patching
    print("\n--- Layer Sweep: Contrarian -> CoT ---")
    sweep_layers = list(range(0, N_LAYERS, 5)) + [CONTRARIAN_COMMIT_LAYER]
    sweep_layers = sorted(set(sweep_layers))
    
    layer_sweep = sweep_patch_layers(
        model, cot_prompt, contrarian_prompt,
        answer_token_ids, layers=sweep_layers
    )
    results['layer_sweep'] = layer_sweep
    
    # Find best layer
    best_layer = max(layer_sweep.keys(), key=lambda l: layer_sweep[l]['improvement'])
    print(f"\nBest patching layer: {best_layer}")
    print(f"Best improvement: {layer_sweep[best_layer]['improvement']:.4f}")
    
    return results


def plot_patching_results(all_results: Dict):
    """Create visualization of patching results."""
    setup_plot_style()
    
    # Plot 1: Layer sweep showing improvement at each layer
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Aggregate layer sweeps across cases
    for idx, (case_name, case_results) in enumerate(all_results.items()):
        if 'layer_sweep' not in case_results:
            continue
            
        ax = axes[idx // 2, idx % 2]
        sweep = case_results['layer_sweep']
        
        layers = sorted(sweep.keys())
        improvements = [sweep[l]['improvement'] for l in layers]
        patched_probs = [sweep[l]['patched_probability'] for l in layers]
        
        ax.bar(range(len(layers)), improvements, alpha=0.7, color='#2ecc71')
        ax.set_xticks(range(len(layers)))
        ax.set_xticklabels(layers)
        ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        ax.axvline(x=layers.index(CONTRARIAN_COMMIT_LAYER) if CONTRARIAN_COMMIT_LAYER in layers else -1,
                   color='red', linestyle='--', alpha=0.7, label=f'L{CONTRARIAN_COMMIT_LAYER}')
        ax.set_xlabel('Patching Layer')
        ax.set_ylabel('Probability Improvement')
        ax.set_title(f'{case_name.title()} Case')
        ax.legend()
    
    fig.suptitle('Effect of Patching Contrarian Activations into CoT', fontsize=14)
    plt.tight_layout()
    save_plot(fig, 'patching_layer_sweep')
    plt.close()
    
    # Plot 2: Summary bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    
    case_names = []
    cot_improvements = []
    direct_improvements = []
    
    for case_name, case_results in all_results.items():
        case_names.append(case_name.title())
        cot_improvements.append(case_results.get('contrarian_to_cot', {}).get('improvement', 0))
        direct_improvements.append(case_results.get('contrarian_to_direct', {}).get('improvement', 0))
    
    x = np.arange(len(case_names))
    width = 0.35
    
    ax.bar(x - width/2, cot_improvements, width, label='CoT', color='#3498db')
    ax.bar(x + width/2, direct_improvements, width, label='Direct', color='#e74c3c')
    
    ax.set_ylabel('Probability Improvement')
    ax.set_title(f'Improvement from Patching Contrarian L{CONTRARIAN_COMMIT_LAYER} Activations')
    ax.set_xticks(x)
    ax.set_xticklabels(case_names)
    ax.legend()
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    
    plt.tight_layout()
    save_plot(fig, 'patching_summary')
    plt.close()


def compute_patching_summary(all_results: Dict) -> Dict:
    """Compute summary statistics from patching experiment."""
    summary = {
        'contrarian_to_cot': {
            'mean_improvement': [],
            'mean_baseline': [],
            'mean_patched': [],
        },
        'contrarian_to_direct': {
            'mean_improvement': [],
            'mean_baseline': [],
            'mean_patched': [],
        },
        'best_patching_layers': [],
    }
    
    for case_results in all_results.values():
        if 'contrarian_to_cot' in case_results:
            r = case_results['contrarian_to_cot']
            summary['contrarian_to_cot']['mean_improvement'].append(r['improvement'])
            summary['contrarian_to_cot']['mean_baseline'].append(r['base_probability'])
            summary['contrarian_to_cot']['mean_patched'].append(r['patched_probability'])
        
        if 'contrarian_to_direct' in case_results:
            r = case_results['contrarian_to_direct']
            summary['contrarian_to_direct']['mean_improvement'].append(r['improvement'])
            summary['contrarian_to_direct']['mean_baseline'].append(r['base_probability'])
            summary['contrarian_to_direct']['mean_patched'].append(r['patched_probability'])
        
        if 'layer_sweep' in case_results:
            sweep = case_results['layer_sweep']
            best = max(sweep.keys(), key=lambda l: sweep[l]['improvement'])
            summary['best_patching_layers'].append(best)
    
    # Compute means
    for key in ['contrarian_to_cot', 'contrarian_to_direct']:
        for metric in list(summary[key].keys()):
            values = summary[key][metric]
            summary[key][metric] = {
                'mean': np.mean(values) if values else 0,
                'std': np.std(values) if values else 0,
                'values': values,
            }
    
    summary['mean_best_layer'] = np.mean(summary['best_patching_layers']) if summary['best_patching_layers'] else -1
    
    return summary


def main():
    """Main entry point for activation patching experiment."""
    print("=" * 70)
    print("Activation Patching Experiment")
    print("=" * 70)
    print(f"GPU Memory: {get_gpu_memory_usage()}")
    
    # Load model
    model, tokenizer = load_model_and_tokenizer(MODEL_NAME)
    
    # Run patching experiments
    all_results = {}
    
    for case in MEDICAL_CASES:
        case_results = run_patching_experiment(model, case)
        all_results[case.name] = case_results
    
    # Create visualizations
    plot_patching_results(all_results)
    
    # Compute summary
    summary = compute_patching_summary(all_results)
    
    print("\n" + "=" * 70)
    print("PATCHING SUMMARY")
    print("=" * 70)
    
    cot_stats = summary['contrarian_to_cot']['mean_improvement']
    print(f"\nPatching L{CONTRARIAN_COMMIT_LAYER} Contrarian -> CoT:")
    print(f"  Mean improvement: {cot_stats['mean']:.4f} ± {cot_stats['std']:.4f}")
    
    direct_stats = summary['contrarian_to_direct']['mean_improvement']
    print(f"\nPatching L{CONTRARIAN_COMMIT_LAYER} Contrarian -> Direct:")
    print(f"  Mean improvement: {direct_stats['mean']:.4f} ± {direct_stats['std']:.4f}")
    
    print(f"\nMean best patching layer: {summary['mean_best_layer']:.1f}")
    
    if cot_stats['mean'] > 0:
        print("\n✓ HYPOTHESIS SUPPORTED: Patching L18 activations improves CoT probability")
    else:
        print("\n✗ HYPOTHESIS NOT SUPPORTED: Patching does not improve CoT probability")
    
    # Save results
    save_results(all_results, "patching_full_results")
    save_results(summary, "patching_summary")
    
    print("\n" + "=" * 70)
    print("Patching experiment complete!")
    print("=" * 70)
    
    return all_results, summary


if __name__ == "__main__":
    results, summary = main()
