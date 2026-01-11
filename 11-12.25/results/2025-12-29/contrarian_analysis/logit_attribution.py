"""
Direct Logit Attribution for MedGemma Prompt Strategies.

This script identifies which attention heads and MLP layers contribute most
to pushing the correct answer token, comparing between prompt strategies.

Key question: What components drive the correct answer in contrarian vs CoT?
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
    CONTRARIAN_COMMIT_LAYER, COT_COMMIT_LAYER
)
from utils import (
    create_prompt, get_answer_token_ids, get_token_probability,
    save_results, load_model_and_tokenizer,
    clear_gpu_memory, get_gpu_memory_usage, 
    setup_plot_style, save_plot
)

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def get_logit_direction(
    model,
    answer_token_ids: List[int],
) -> torch.Tensor:
    """
    Get the unembedding direction for the answer tokens.
    
    This is the direction in residual stream space that increases
    the probability of the answer tokens.
    
    Args:
        model: HookedTransformer model
        answer_token_ids: Token IDs for the answer
        
    Returns:
        Tensor of shape [d_model] representing the answer direction
    """
    # W_U is [d_model, d_vocab]
    # Average the unembedding vectors for all answer tokens
    W_U = model.W_U
    answer_directions = W_U[:, answer_token_ids]  # [d_model, n_tokens]
    
    # Average across answer token variations
    answer_direction = answer_directions.mean(dim=1)  # [d_model]
    
    # Normalize
    answer_direction = answer_direction / answer_direction.norm()
    
    return answer_direction


def compute_direct_logit_attribution(
    model,
    prompt: str,
    answer_direction: torch.Tensor,
    position: int = -1,
) -> Dict:
    """
    Compute how much each component (attention heads and MLPs) contributes
    to the answer logit via direct logit attribution.
    
    For attention heads, we look at the output of each head projected onto
    the answer direction.
    
    For MLPs, we look at the MLP output projected onto the answer direction.
    
    Args:
        model: HookedTransformer model
        prompt: Formatted prompt string
        answer_direction: Unembedding direction for answer
        position: Position to analyze (default -1 for last)
        
    Returns:
        Dict with attribution scores for heads and MLPs
    """
    with torch.no_grad():
        logits, cache = model.run_with_cache(
            prompt,
            prepend_bos=True,
            return_type="logits",
        )
    
    n_layers = model.cfg.n_layers
    n_heads = model.cfg.n_heads
    
    # Move answer direction to correct device
    answer_direction = answer_direction.to(model.cfg.device)
    
    # Attribution scores
    head_attribution = np.zeros((n_layers, n_heads))
    mlp_attribution = np.zeros(n_layers)
    
    for layer in range(n_layers):
        # Attention head contributions
        # hook_z contains the attention output per head: [batch, pos, n_heads, d_head]
        # We project through W_O to get residual stream contribution per head
        
        hook_z_key = f'blocks.{layer}.attn.hook_z'
        if hook_z_key in cache:
            # hook_z: [batch, pos, n_heads, d_head]
            attn_z = cache[hook_z_key]
            
            # Get the output at the position of interest
            attn_at_pos = attn_z[0, position]  # [n_heads, d_head]
            
            # Project through W_O to get residual stream contribution per head
            W_O = model.blocks[layer].attn.W_O  # [n_heads, d_head, d_model]
            
            for head in range(n_heads):
                head_output = einops.einsum(
                    attn_at_pos[head], W_O[head],
                    "d_head, d_head d_model -> d_model"
                )
                # Project onto answer direction
                contribution = (head_output @ answer_direction).item()
                head_attribution[layer, head] = contribution
        
        # MLP contribution
        if f'blocks.{layer}.hook_mlp_out' in cache:
            mlp_out = cache[f'blocks.{layer}.hook_mlp_out']
            mlp_at_pos = mlp_out[0, position]  # [d_model]
            contribution = (mlp_at_pos @ answer_direction).item()
            mlp_attribution[layer] = contribution
    
    del cache
    clear_gpu_memory()
    
    return {
        'head_attribution': head_attribution,
        'mlp_attribution': mlp_attribution,
    }


def find_top_contributors(
    head_attribution: np.ndarray,
    mlp_attribution: np.ndarray,
    top_k: int = 10,
) -> Dict:
    """
    Find the top contributing components.
    
    Args:
        head_attribution: [n_layers, n_heads] array of head contributions
        mlp_attribution: [n_layers] array of MLP contributions
        top_k: Number of top components to return
        
    Returns:
        Dict with top positive and negative contributors
    """
    # Flatten head attribution
    n_layers, n_heads = head_attribution.shape
    head_flat = head_attribution.flatten()
    
    # Create labels
    head_labels = [f"L{l}H{h}" for l in range(n_layers) for h in range(n_heads)]
    mlp_labels = [f"MLP{l}" for l in range(n_layers)]
    
    # Combine
    all_values = np.concatenate([head_flat, mlp_attribution])
    all_labels = head_labels + mlp_labels
    
    # Sort by absolute value
    sorted_indices = np.argsort(np.abs(all_values))[::-1]
    
    top_positive = []
    top_negative = []
    
    for idx in sorted_indices:
        label = all_labels[idx]
        value = all_values[idx]
        
        if value > 0 and len(top_positive) < top_k:
            top_positive.append((label, value))
        elif value < 0 and len(top_negative) < top_k:
            top_negative.append((label, value))
        
        if len(top_positive) >= top_k and len(top_negative) >= top_k:
            break
    
    return {
        'top_positive': top_positive,
        'top_negative': top_negative,
    }


def analyze_case_attribution(
    model,
    case,
) -> Dict:
    """
    Analyze direct logit attribution for a single case across all strategies.
    
    Args:
        model: HookedTransformer model
        case: MedicalCase object
        
    Returns:
        Dict with attribution results for each strategy
    """
    print(f"\n{'='*60}")
    print(f"Direct Logit Attribution: {case.name}")
    print(f"{'='*60}")
    
    # Get answer direction
    answer_token_ids = get_answer_token_ids(model.tokenizer, case.answer_tokens)
    answer_direction = get_logit_direction(model, answer_token_ids)
    
    print(f"Answer tokens: {[model.tokenizer.decode([tid]) for tid in answer_token_ids]}")
    
    results = {}
    
    for strategy_name, strategy in PROMPT_STRATEGIES.items():
        print(f"\n--- {strategy_name} ---")
        
        prompt = create_prompt(strategy, case)
        
        # Compute attribution
        attribution = compute_direct_logit_attribution(
            model, prompt, answer_direction
        )
        
        # Find top contributors
        top = find_top_contributors(
            attribution['head_attribution'],
            attribution['mlp_attribution'],
        )
        
        results[strategy_name] = {
            'head_attribution': attribution['head_attribution'],
            'mlp_attribution': attribution['mlp_attribution'],
            'top_positive': top['top_positive'],
            'top_negative': top['top_negative'],
        }
        
        print(f"\nTop positive contributors:")
        for label, value in top['top_positive'][:5]:
            print(f"  {label}: {value:.4f}")
        
        print(f"\nTop negative contributors:")
        for label, value in top['top_negative'][:5]:
            print(f"  {label}: {value:.4f}")
    
    return results


def plot_attribution_heatmap(
    results: Dict,
    case_name: str,
):
    """Create heatmap visualizations of attribution patterns."""
    setup_plot_style()
    
    strategies = list(results.keys())
    n_strategies = len(strategies)
    
    # Create subplot for each strategy
    fig, axes = plt.subplots(1, n_strategies, figsize=(6 * n_strategies, 10))
    
    if n_strategies == 1:
        axes = [axes]
    
    # Find global min/max for consistent colorscale
    all_attrs = [results[s]['head_attribution'] for s in strategies]
    vmax = max(np.abs(a).max() for a in all_attrs)
    if vmax == 0:
        vmax = 1  # Avoid division by zero
    vmin = -vmax
    
    for ax, strategy in zip(axes, strategies):
        attr = results[strategy]['head_attribution']
        
        im = ax.imshow(
            attr,
            cmap='RdBu_r',
            aspect='auto',
            vmin=vmin, vmax=vmax
        )
        
        ax.set_xlabel('Head')
        ax.set_ylabel('Layer')
        ax.set_title(strategy.replace('_', ' ').title())
        
        # Mark important layers
        ax.axhline(y=CONTRARIAN_COMMIT_LAYER, color='green', linestyle='--', alpha=0.7)
        ax.axhline(y=COT_COMMIT_LAYER, color='blue', linestyle='--', alpha=0.7)
        
        plt.colorbar(im, ax=ax, label='Logit Contribution')
    
    fig.suptitle(f'Direct Logit Attribution - {case_name.title()}', fontsize=14)
    plt.tight_layout()
    save_plot(fig, f'logit_attribution_{case_name}')
    plt.close()
    
    # MLP attribution comparison
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for strategy in strategies:
        mlp_attr = results[strategy]['mlp_attribution']
        ax.plot(range(len(mlp_attr)), mlp_attr, 
                label=strategy.replace('_', ' ').title(),
                linewidth=2, marker='o', markersize=3)
    
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax.axvline(x=CONTRARIAN_COMMIT_LAYER, color='green', linestyle='--', 
               alpha=0.7, label=f'Contrarian L{CONTRARIAN_COMMIT_LAYER}')
    ax.axvline(x=COT_COMMIT_LAYER, color='blue', linestyle='--',
               alpha=0.7, label=f'CoT L{COT_COMMIT_LAYER}')
    
    ax.set_xlabel('Layer')
    ax.set_ylabel('MLP Logit Contribution')
    ax.set_title(f'MLP Direct Logit Attribution - {case_name.title()}')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_plot(fig, f'mlp_attribution_{case_name}')
    plt.close()


def compare_head_importance(
    all_results: Dict,
) -> Dict:
    """
    Compare head importance rankings between strategies across cases.
    
    Returns:
        Dict with analysis of head importance patterns
    """
    # Aggregate attribution across cases
    aggregated = {}
    
    for strategy in PROMPT_STRATEGIES.keys():
        head_attrs = []
        mlp_attrs = []
        
        for case_results in all_results.values():
            if strategy in case_results:
                head_attrs.append(case_results[strategy]['head_attribution'])
                mlp_attrs.append(case_results[strategy]['mlp_attribution'])
        
        if head_attrs:
            aggregated[strategy] = {
                'mean_head_attribution': np.mean(head_attrs, axis=0),
                'std_head_attribution': np.std(head_attrs, axis=0),
                'mean_mlp_attribution': np.mean(mlp_attrs, axis=0),
            }
    
    # Find consistently important heads for each strategy
    comparison = {}
    
    for strategy, data in aggregated.items():
        mean_attr = data['mean_head_attribution']
        
        # Find heads with consistent positive contribution
        positive_heads = []
        negative_heads = []
        
        for layer in range(mean_attr.shape[0]):
            for head in range(mean_attr.shape[1]):
                val = mean_attr[layer, head]
                if val > 0.001:  # Lower threshold - heads contribute less than MLPs
                    positive_heads.append((f"L{layer}H{head}", float(val)))
                elif val < -0.001:
                    negative_heads.append((f"L{layer}H{head}", float(val)))
        
        positive_heads.sort(key=lambda x: -x[1])
        negative_heads.sort(key=lambda x: x[1])
        
        comparison[strategy] = {
            'top_positive_heads': positive_heads[:10],
            'top_negative_heads': negative_heads[:10],
        }
    
    return comparison, aggregated


def main():
    """Main entry point for direct logit attribution analysis."""
    print("=" * 70)
    print("Direct Logit Attribution Analysis")
    print("=" * 70)
    print(f"GPU Memory: {get_gpu_memory_usage()}")
    
    # Load model
    model, tokenizer = load_model_and_tokenizer(MODEL_NAME)
    
    all_results = {}
    
    for case in MEDICAL_CASES:
        case_results = analyze_case_attribution(model, case)
        all_results[case.name] = case_results
        
        # Create visualizations
        plot_attribution_heatmap(case_results, case.name)
    
    # Compare head importance across strategies
    comparison, aggregated = compare_head_importance(all_results)
    
    # Create aggregated plot
    setup_plot_style()
    fig, axes = plt.subplots(1, 3, figsize=(18, 8))
    
    for ax, (strategy, data) in zip(axes, aggregated.items()):
        attr = data['mean_head_attribution']
        vmax = np.abs(attr).max()
        if vmax == 0:
            vmax = 1  # Avoid division by zero
        
        im = ax.imshow(
            attr,
            cmap='RdBu_r',
            aspect='auto',
            vmin=-vmax, vmax=vmax
        )
        
        ax.set_xlabel('Head')
        ax.set_ylabel('Layer')
        ax.set_title(strategy.replace('_', ' ').title())
        ax.axhline(y=CONTRARIAN_COMMIT_LAYER, color='green', linestyle='--', alpha=0.7)
        plt.colorbar(im, ax=ax)
    
    fig.suptitle('Average Head Attribution Across Cases', fontsize=14)
    plt.tight_layout()
    save_plot(fig, 'logit_attribution_aggregated')
    plt.close()
    
    # Summary
    print("\n" + "=" * 70)
    print("ATTRIBUTION SUMMARY")
    print("=" * 70)
    
    for strategy, data in comparison.items():
        print(f"\n{strategy.replace('_', ' ').title()}:")
        print(f"  Top positive contributing heads:")
        for head, val in data['top_positive_heads'][:5]:
            print(f"    {head}: {val:.4f}")
        print(f"  Top negative contributing heads:")
        for head, val in data['top_negative_heads'][:5]:
            print(f"    {head}: {val:.4f}")
    
    # Save results (convert numpy arrays to lists for JSON)
    save_data = {
        case_name: {
            strategy: {
                'head_attribution': results['head_attribution'].tolist(),
                'mlp_attribution': results['mlp_attribution'].tolist(),
                'top_positive': results['top_positive'],
                'top_negative': results['top_negative'],
            }
            for strategy, results in case_results.items()
        }
        for case_name, case_results in all_results.items()
    }
    save_results(save_data, "logit_attribution_results")
    save_results(comparison, "logit_attribution_comparison")
    
    print("\n" + "=" * 70)
    print("Attribution analysis complete!")
    print("=" * 70)
    
    return all_results, comparison


if __name__ == "__main__":
    results, comparison = main()
