"""
Layer Sweep Visualization for MedGemma Prompt Strategies.

This script creates comprehensive plots showing answer probability
across all layers for each prompting strategy, visually confirming
the early vs late commitment pattern.
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
    PROMPT_STRATEGIES, MEDICAL_CASES,
    CONTRARIAN_COMMIT_LAYER, COT_COMMIT_LAYER, DIRECT_COMMIT_LAYER
)
from utils import (
    create_prompt, get_answer_token_ids, get_token_probability, get_token_rank,
    save_results, load_model_and_tokenizer,
    clear_gpu_memory, get_gpu_memory_usage, 
    setup_plot_style, save_plot
)

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def run_full_layer_sweep(
    model,
    prompt: str,
    answer_token_ids: List[int],
) -> Dict:
    """
    Run a complete layer sweep, computing answer probability at every layer.
    
    Args:
        model: HookedTransformer model
        prompt: Formatted prompt string
        answer_token_ids: Token IDs to track
        
    Returns:
        Dict with per-layer probabilities, ranks, and logits
    """
    with torch.no_grad():
        logits, cache = model.run_with_cache(
            prompt,
            prepend_bos=True,
            return_type="logits",
        )
    
    n_layers = model.cfg.n_layers
    ln_final = model.ln_final
    W_U = model.W_U
    b_U = model.b_U if hasattr(model, 'b_U') else None
    
    probabilities = []
    ranks = []
    answer_logits = []
    
    for layer in range(n_layers):
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
        
        # Get the raw logit for the answer token
        answer_logit = max(layer_logits[0, -1, tid].item() for tid in answer_token_ids)
        
        probabilities.append(prob)
        ranks.append(rank)
        answer_logits.append(answer_logit)
    
    del cache
    clear_gpu_memory()
    
    # Compute probability gradients (rate of change)
    prob_gradient = np.gradient(probabilities)
    
    return {
        'probabilities': probabilities,
        'ranks': ranks,
        'answer_logits': answer_logits,
        'probability_gradient': prob_gradient.tolist(),
    }


def create_comprehensive_layer_plot(
    case_data: Dict,
    case_name: str,
):
    """
    Create a comprehensive multi-panel visualization for a single case.
    
    Args:
        case_data: Dict with results for each strategy
        case_name: Name of the medical case
    """
    setup_plot_style()
    
    fig = plt.figure(figsize=(18, 14))
    gs = GridSpec(3, 2, figure=fig, hspace=0.3, wspace=0.25)
    
    # Color scheme
    colors = {
        'contrarian': '#27ae60',
        'chain_of_thought': '#3498db',
        'direct_answer': '#e74c3c',
    }
    
    strategies = list(case_data.keys())
    expected_commits = {
        'contrarian': CONTRARIAN_COMMIT_LAYER,
        'chain_of_thought': COT_COMMIT_LAYER,
        'direct_answer': DIRECT_COMMIT_LAYER,
    }
    
    # Panel 1: Probability across layers (main plot)
    ax1 = fig.add_subplot(gs[0, :])
    
    for strategy in strategies:
        probs = case_data[strategy]['probabilities']
        color = colors.get(strategy, '#95a5a6')
        ax1.plot(range(len(probs)), probs, 
                label=strategy.replace('_', ' ').title(),
                color=color, linewidth=2.5)
        
        # Mark expected commitment layer
        exp_layer = expected_commits.get(strategy)
        if exp_layer and exp_layer < len(probs):
            ax1.axvline(x=exp_layer, color=color, linestyle='--', alpha=0.5, linewidth=1.5)
            ax1.scatter([exp_layer], [probs[exp_layer]], color=color, s=100, 
                       zorder=5, edgecolors='black', linewidths=1.5)
    
    ax1.set_xlabel('Layer', fontsize=12)
    ax1.set_ylabel('Answer Probability', fontsize=12)
    ax1.set_title(f'Answer Probability Across Layers - {case_name.title()} Case', fontsize=14)
    ax1.legend(loc='upper left', fontsize=11)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, N_LAYERS - 1)
    ax1.set_ylim(0, 1)
    
    # Panel 2: Answer Rank across layers
    ax2 = fig.add_subplot(gs[1, 0])
    
    for strategy in strategies:
        ranks = case_data[strategy]['ranks']
        color = colors.get(strategy, '#95a5a6')
        ax2.plot(range(len(ranks)), ranks,
                label=strategy.replace('_', ' ').title(),
                color=color, linewidth=2)
    
    ax2.axhline(y=10, color='gray', linestyle=':', alpha=0.7, label='Top-10 Threshold')
    ax2.set_xlabel('Layer', fontsize=11)
    ax2.set_ylabel('Answer Rank (log scale)', fontsize=11)
    ax2.set_title('Answer Rank Evolution', fontsize=12)
    ax2.set_yscale('log')
    ax2.legend(loc='upper right', fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, N_LAYERS - 1)
    
    # Panel 3: Probability Gradient
    ax3 = fig.add_subplot(gs[1, 1])
    
    for strategy in strategies:
        gradient = case_data[strategy]['probability_gradient']
        color = colors.get(strategy, '#95a5a6')
        ax3.plot(range(len(gradient)), gradient,
                label=strategy.replace('_', ' ').title(),
                color=color, linewidth=2)
    
    ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax3.set_xlabel('Layer', fontsize=11)
    ax3.set_ylabel('Probability Change Rate', fontsize=11)
    ax3.set_title('Rate of Probability Change per Layer', fontsize=12)
    ax3.legend(loc='upper right', fontsize=9)
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(0, N_LAYERS - 1)
    
    # Panel 4: Raw Answer Logits
    ax4 = fig.add_subplot(gs[2, 0])
    
    for strategy in strategies:
        logits = case_data[strategy]['answer_logits']
        color = colors.get(strategy, '#95a5a6')
        ax4.plot(range(len(logits)), logits,
                label=strategy.replace('_', ' ').title(),
                color=color, linewidth=2)
    
    ax4.set_xlabel('Layer', fontsize=11)
    ax4.set_ylabel('Answer Token Logit', fontsize=11)
    ax4.set_title('Raw Logit Value for Answer Token', fontsize=12)
    ax4.legend(loc='upper left', fontsize=9)
    ax4.grid(True, alpha=0.3)
    ax4.set_xlim(0, N_LAYERS - 1)
    
    # Panel 5: Commitment Layer Summary
    ax5 = fig.add_subplot(gs[2, 1])
    
    # Find actual commitment layers (first time rank < 10)
    actual_commits = {}
    for strategy in strategies:
        ranks = case_data[strategy]['ranks']
        for layer, rank in enumerate(ranks):
            if rank < 10:
                actual_commits[strategy] = layer
                break
        else:
            actual_commits[strategy] = -1
    
    labels = [s.replace('_', ' ').title() for s in strategies]
    expected = [expected_commits.get(s, 0) for s in strategies]
    observed = [actual_commits.get(s, -1) for s in strategies]
    
    x = np.arange(len(strategies))
    width = 0.35
    
    bars1 = ax5.bar(x - width/2, expected, width, label='Expected', alpha=0.7)
    bars2 = ax5.bar(x + width/2, observed, width, label='Observed', alpha=0.9)
    
    ax5.set_xlabel('Strategy', fontsize=11)
    ax5.set_ylabel('Commitment Layer', fontsize=11)
    ax5.set_title('Expected vs Observed Commitment Layer', fontsize=12)
    ax5.set_xticks(x)
    ax5.set_xticklabels(labels, fontsize=10)
    ax5.legend()
    
    # Color bars by strategy
    for bar, strategy in zip(bars1, strategies):
        bar.set_color(colors.get(strategy, '#95a5a6'))
    for bar, strategy in zip(bars2, strategies):
        bar.set_color(colors.get(strategy, '#95a5a6'))
        bar.set_edgecolor('black')
        bar.set_linewidth(1.5)
    
    fig.suptitle(f'Complete Layer Analysis: {case_name.title()} Case', fontsize=16, y=1.02)
    plt.tight_layout(rect=[0, 0, 1, 0.98])
    save_plot(fig, f'layer_sweep_complete_{case_name}')
    plt.close()


def create_combined_summary_plot(all_results: Dict):
    """
    Create a summary plot combining results across all cases.
    
    Args:
        all_results: Results for all cases
    """
    setup_plot_style()
    
    # Collect average probabilities
    avg_probs = {}
    for strategy in PROMPT_STRATEGIES.keys():
        all_probs = []
        for case_data in all_results.values():
            if strategy in case_data:
                all_probs.append(case_data[strategy]['probabilities'])
        if all_probs:
            avg_probs[strategy] = np.mean(all_probs, axis=0)
    
    # Main summary figure
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    colors = {
        'contrarian': '#27ae60',
        'chain_of_thought': '#3498db',
        'direct_answer': '#e74c3c',
    }
    
    # Panel 1: Average probability across cases
    ax1 = axes[0, 0]
    
    for strategy, probs in avg_probs.items():
        color = colors.get(strategy, '#95a5a6')
        ax1.plot(range(len(probs)), probs,
                label=strategy.replace('_', ' ').title(),
                color=color, linewidth=2.5)
    
    # Add vertical lines for expected commitment layers
    ax1.axvline(x=CONTRARIAN_COMMIT_LAYER, color=colors['contrarian'], 
               linestyle='--', alpha=0.7, label=f'Contrarian Commit (L{CONTRARIAN_COMMIT_LAYER})')
    ax1.axvline(x=COT_COMMIT_LAYER, color=colors['chain_of_thought'],
               linestyle='--', alpha=0.7, label=f'CoT Commit (L{COT_COMMIT_LAYER})')
    
    ax1.set_xlabel('Layer')
    ax1.set_ylabel('Average Answer Probability')
    ax1.set_title('Average Probability Across All Cases')
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, N_LAYERS - 1)
    ax1.set_ylim(0, 1)
    
    # Panel 2: Per-case comparison at key layers
    ax2 = axes[0, 1]
    
    key_layers = [0, CONTRARIAN_COMMIT_LAYER, COT_COMMIT_LAYER, N_LAYERS - 1]
    case_names = list(all_results.keys())
    
    for i, strategy in enumerate(PROMPT_STRATEGIES.keys()):
        values = []
        for case_name in case_names:
            if strategy in all_results[case_name]:
                probs = all_results[case_name][strategy]['probabilities']
                # Get prob at contrarian commitment layer
                values.append(probs[CONTRARIAN_COMMIT_LAYER])
        
        x = np.arange(len(case_names))
        offset = (i - 1) * 0.25
        ax2.bar(x + offset, values, 0.25, 
               label=strategy.replace('_', ' ').title(),
               color=colors.get(strategy, '#95a5a6'))
    
    ax2.set_xticks(x)
    ax2.set_xticklabels([c.title() for c in case_names])
    ax2.set_ylabel(f'Probability at Layer {CONTRARIAN_COMMIT_LAYER}')
    ax2.set_title(f'Answer Probability at Contrarian Commitment Layer (L{CONTRARIAN_COMMIT_LAYER})')
    ax2.legend()
    ax2.set_ylim(0, 1)
    
    # Panel 3: Commitment layer distribution
    ax3 = axes[1, 0]
    
    for strategy in PROMPT_STRATEGIES.keys():
        commit_layers = []
        for case_data in all_results.values():
            if strategy in case_data:
                ranks = case_data[strategy]['ranks']
                for layer, rank in enumerate(ranks):
                    if rank < 10:
                        commit_layers.append(layer)
                        break
        
        if commit_layers:
            ax3.hist(commit_layers, bins=20, alpha=0.6, 
                    label=strategy.replace('_', ' ').title(),
                    color=colors.get(strategy, '#95a5a6'))
    
    ax3.axvline(x=CONTRARIAN_COMMIT_LAYER, color='red', linestyle='--', alpha=0.7)
    ax3.set_xlabel('Commitment Layer')
    ax3.set_ylabel('Count')
    ax3.set_title('Distribution of Commitment Layers')
    ax3.legend()
    
    # Panel 4: Text summary
    ax4 = axes[1, 1]
    ax4.axis('off')
    
    summary_text = "LAYER SWEEP SUMMARY\n" + "=" * 40 + "\n\n"
    
    for strategy in PROMPT_STRATEGIES.keys():
        probs = avg_probs.get(strategy, [])
        if len(probs) > 0:
            # Find first layer where prob > 0.1
            early_signal = next((l for l, p in enumerate(probs) if p > 0.1), -1)
            final_prob = probs[-1] if len(probs) > 0 else 0
            
            summary_text += f"{strategy.replace('_', ' ').title()}:\n"
            summary_text += f"  First signal (prob>0.1): Layer {early_signal}\n"
            summary_text += f"  Final probability: {final_prob:.4f}\n\n"
    
    summary_text += "\nKey Finding:\n"
    if 'contrarian' in avg_probs and 'chain_of_thought' in avg_probs:
        c_probs = avg_probs['contrarian']
        cot_probs = avg_probs['chain_of_thought']
        if c_probs[CONTRARIAN_COMMIT_LAYER] > cot_probs[CONTRARIAN_COMMIT_LAYER]:
            summary_text += f"✓ Contrarian shows higher probability at L{CONTRARIAN_COMMIT_LAYER}\n"
            summary_text += f"  ({c_probs[CONTRARIAN_COMMIT_LAYER]:.4f} vs {cot_probs[CONTRARIAN_COMMIT_LAYER]:.4f})"
    
    ax4.text(0.1, 0.9, summary_text, transform=ax4.transAxes, fontsize=11,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    fig.suptitle('Complete Layer Sweep Analysis Summary', fontsize=16)
    plt.tight_layout()
    save_plot(fig, 'layer_sweep_summary')
    plt.close()


def main():
    """Main entry point for layer sweep visualization."""
    print("=" * 70)
    print("Layer Sweep Visualization")
    print("=" * 70)
    print(f"GPU Memory: {get_gpu_memory_usage()}")
    
    # Load model
    model, tokenizer = load_model_and_tokenizer(MODEL_NAME)
    
    all_results = {}
    
    for case in tqdm(MEDICAL_CASES, desc="Processing cases"):
        print(f"\n{'='*60}")
        print(f"Layer sweep: {case.name}")
        print(f"{'='*60}")
        
        answer_token_ids = get_answer_token_ids(tokenizer, case.answer_tokens)
        print(f"Answer: {case.expected_answer}")
        
        case_results = {}
        
        for strategy_name, strategy in PROMPT_STRATEGIES.items():
            print(f"  Processing {strategy_name}...")
            
            prompt = create_prompt(strategy, case)
            sweep_results = run_full_layer_sweep(model, prompt, answer_token_ids)
            case_results[strategy_name] = sweep_results
            
            print(f"    Final prob: {sweep_results['probabilities'][-1]:.4f}")
        
        all_results[case.name] = case_results
        
        # Create comprehensive plot for this case
        create_comprehensive_layer_plot(case_results, case.name)
    
    # Create combined summary
    create_combined_summary_plot(all_results)
    
    # Save results
    save_results(all_results, "layer_sweep_results")
    
    # Summary statistics
    print("\n" + "=" * 70)
    print("LAYER SWEEP SUMMARY")
    print("=" * 70)
    
    for strategy in PROMPT_STRATEGIES.keys():
        print(f"\n{strategy.replace('_', ' ').title()}:")
        
        all_probs = []
        all_commits = []
        
        for case_results in all_results.values():
            if strategy in case_results:
                probs = case_results[strategy]['probabilities']
                all_probs.append(probs)
                
                # Find commitment
                ranks = case_results[strategy]['ranks']
                for l, r in enumerate(ranks):
                    if r < 10:
                        all_commits.append(l)
                        break
        
        if all_probs:
            avg_probs = np.mean(all_probs, axis=0)
            print(f"  Prob at L18: {avg_probs[18]:.4f}")
            print(f"  Prob at L57: {avg_probs[57]:.4f}")
            print(f"  Final prob:  {avg_probs[-1]:.4f}")
        
        if all_commits:
            print(f"  Mean commitment layer: {np.mean(all_commits):.1f}")
    
    print("\n" + "=" * 70)
    print("Layer sweep visualization complete!")
    print("=" * 70)
    
    return all_results


if __name__ == "__main__":
    results = main()
