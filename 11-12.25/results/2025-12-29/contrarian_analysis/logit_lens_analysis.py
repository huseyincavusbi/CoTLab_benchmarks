"""
LogitLens Analysis for MedGemma Prompt Strategies.

This script implements logit lens analysis to track when the model "commits"
to the correct diagnosis across layers for contrarian, CoT, and direct prompts.

Key question: Does contrarian really commit early (Layer 18) while others commit late?
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
    TOP_K_PREDICTIONS, KEY_LAYERS,
    CONTRARIAN_COMMIT_LAYER, COT_COMMIT_LAYER, DIRECT_COMMIT_LAYER
)
from utils import (
    create_prompt, get_answer_token_ids, get_token_probability, get_token_rank, in_top_k,
    save_results, plot_layer_sweep, load_model_and_tokenizer, 
    clear_gpu_memory, get_gpu_memory_usage
)


def run_logit_lens(
    model,
    prompt: str,
    answer_token_ids: List[int],
) -> Dict:
    """
    Run logit lens analysis on a single prompt.
    
    For each layer, we:
    1. Get the residual stream at that layer
    2. Apply the final layer norm
    3. Project to vocabulary space using the unembedding matrix
    4. Check the rank/probability of the correct answer
    
    Args:
        model: HookedTransformer model
        prompt: Formatted prompt string
        answer_token_ids: Token IDs to track
        
    Returns:
        Dict with per-layer probabilities, ranks, and top-k status
    """
    # Run with cache to get all intermediate activations
    with torch.no_grad():
        logits, cache = model.run_with_cache(
            prompt,
            prepend_bos=True,
            return_type="logits",
        )
    
    n_layers = model.cfg.n_layers
    results = {
        'probabilities': [],
        'ranks': [],
        'in_top_k': [],
        'top_predictions': [],
    }
    
    # Get the final layer norm and unembedding
    ln_final = model.ln_final
    W_U = model.W_U  # [d_model, d_vocab]
    b_U = model.b_U if hasattr(model, 'b_U') else None
    
    # Analyze each layer
    for layer in range(n_layers):
        # Get accumulated residual stream up to this layer
        # We use resid_post to get the output of this layer
        if layer == n_layers - 1:
            resid = cache['resid_post', layer]  # [batch, pos, d_model]
        else:
            resid = cache['resid_post', layer]
        
        # Apply final layer norm
        resid_normed = ln_final(resid.float()).to(resid.dtype)
        
        # Project to vocabulary space: [batch, pos, d_vocab]
        layer_logits = einops.einsum(
            resid_normed, W_U,
            "batch pos d_model, d_model d_vocab -> batch pos d_vocab"
        )
        if b_U is not None:
            layer_logits = layer_logits + b_U
        
        # Get probability and rank of answer at last position
        prob = get_token_probability(layer_logits, answer_token_ids, position=-1)
        rank = get_token_rank(layer_logits, answer_token_ids, position=-1)
        is_top_k = in_top_k(layer_logits, answer_token_ids, k=TOP_K_PREDICTIONS, position=-1)
        
        # Get top 5 predictions for debugging
        top_tokens = torch.topk(layer_logits[0, -1], k=5)
        top_preds = [
            (model.tokenizer.decode([tid.item()]), top_tokens.values[i].item())
            for i, tid in enumerate(top_tokens.indices)
        ]
        
        results['probabilities'].append(prob)
        results['ranks'].append(rank)
        results['in_top_k'].append(is_top_k)
        results['top_predictions'].append(top_preds)
    
    # Clean up cache to free memory
    del cache
    clear_gpu_memory()
    
    return results


def find_commitment_layer(
    ranks: List[int],
    threshold_rank: int = TOP_K_PREDICTIONS,
) -> int:
    """
    Find the layer where the model first "commits" to the answer.
    
    Commitment is defined as the answer appearing in top-k predictions
    and staying there for subsequent layers.
    
    Args:
        ranks: List of answer ranks per layer
        threshold_rank: Rank threshold for commitment (default top-k)
        
    Returns:
        Layer number where commitment first occurs, or -1 if never
    """
    n_layers = len(ranks)
    
    for layer in range(n_layers):
        # Check if answer is in top-k at this layer
        if ranks[layer] < threshold_rank:
            # Verify it stays in top-k for at least 3 more layers (or to the end)
            remaining = ranks[layer:min(layer + 4, n_layers)]
            if all(r < threshold_rank for r in remaining):
                return layer
    
    return -1  # Never commits


def analyze_case(
    model,
    case,
    strategies: Dict,
) -> Dict:
    """
    Run logit lens analysis on a single medical case for all strategies.
    
    Args:
        model: HookedTransformer model
        case: MedicalCase object
        strategies: Dict of prompt strategies
        
    Returns:
        Dict with results for each strategy
    """
    print(f"\n{'='*60}")
    print(f"Analyzing case: {case.name}")
    print(f"Expected answer: {case.expected_answer}")
    print(f"{'='*60}")
    
    # Get answer token IDs
    answer_token_ids = get_answer_token_ids(model.tokenizer, case.answer_tokens)
    print(f"Answer token IDs: {answer_token_ids}")
    print(f"Tokens: {[model.tokenizer.decode([tid]) for tid in answer_token_ids]}")
    
    results = {}
    
    for strategy_name, strategy in strategies.items():
        print(f"\n--- Strategy: {strategy_name} ---")
        
        # Create prompt
        prompt = create_prompt(strategy, case)
        print(f"Prompt length: {len(model.tokenizer.encode(prompt))} tokens")
        
        # Run logit lens
        lens_results = run_logit_lens(model, prompt, answer_token_ids)
        
        # Find commitment layer
        commitment_layer = find_commitment_layer(lens_results['ranks'])
        
        results[strategy_name] = {
            'probabilities': lens_results['probabilities'],
            'ranks': lens_results['ranks'],
            'in_top_k': lens_results['in_top_k'],
            'commitment_layer': commitment_layer,
            'final_probability': lens_results['probabilities'][-1],
            'final_rank': lens_results['ranks'][-1],
        }
        
        print(f"Commitment layer: {commitment_layer}")
        print(f"Final probability: {lens_results['probabilities'][-1]:.4f}")
        print(f"Final rank: {lens_results['ranks'][-1]}")
        
        # Print probabilities at key layers
        print(f"Probabilities at key layers:")
        for layer in KEY_LAYERS:
            if layer < len(lens_results['probabilities']):
                print(f"  Layer {layer}: prob={lens_results['probabilities'][layer]:.4f}, "
                      f"rank={lens_results['ranks'][layer]}")
    
    return results


def run_full_analysis(model) -> Dict:
    """
    Run logit lens analysis on all cases and strategies.
    
    Returns:
        Dict with results for each case
    """
    all_results = {}
    
    for case in MEDICAL_CASES:
        case_results = analyze_case(model, case, PROMPT_STRATEGIES)
        all_results[case.name] = case_results
        
        # Plot layer sweep for this case
        layer_probs = {
            strategy: results['probabilities']
            for strategy, results in case_results.items()
        }
        commitment_layers = {
            strategy: results['commitment_layer']
            for strategy, results in case_results.items()
        }
        
        plot_layer_sweep(
            layer_probs,
            title=f"Answer Probability by Layer - {case.name.title()} Case",
            save_name=f"logit_lens_{case.name}",
            commitment_layers=commitment_layers,
        )
    
    return all_results


def compute_summary_statistics(all_results: Dict) -> Dict:
    """
    Compute summary statistics across all cases.
    
    Returns:
        Dict with mean commitment layers and probabilities per strategy
    """
    summary = {}
    
    for strategy in PROMPT_STRATEGIES.keys():
        commitment_layers = []
        final_probs = []
        
        for case_name, case_results in all_results.items():
            if strategy in case_results:
                cl = case_results[strategy]['commitment_layer']
                if cl >= 0:  # Only include if it committed
                    commitment_layers.append(cl)
                final_probs.append(case_results[strategy]['final_probability'])
        
        summary[strategy] = {
            'mean_commitment_layer': np.mean(commitment_layers) if commitment_layers else -1,
            'std_commitment_layer': np.std(commitment_layers) if commitment_layers else 0,
            'median_commitment_layer': np.median(commitment_layers) if commitment_layers else -1,
            'mean_final_probability': np.mean(final_probs),
            'cases_with_commitment': len(commitment_layers),
            'total_cases': len(all_results),
        }
    
    return summary


def create_combined_layer_plot(all_results: Dict):
    """Create a combined plot averaging across all cases."""
    
    # Average probabilities across cases
    avg_probs = {}
    for strategy in PROMPT_STRATEGIES.keys():
        probs_list = []
        for case_results in all_results.values():
            if strategy in case_results:
                probs_list.append(case_results[strategy]['probabilities'])
        
        if probs_list:
            avg_probs[strategy] = np.mean(probs_list, axis=0).tolist()
    
    # Average commitment layers
    avg_commitment = {}
    for strategy in PROMPT_STRATEGIES.keys():
        layers = []
        for case_results in all_results.values():
            if strategy in case_results:
                cl = case_results[strategy]['commitment_layer']
                if cl >= 0:
                    layers.append(cl)
        if layers:
            avg_commitment[strategy] = int(np.mean(layers))
    
    plot_layer_sweep(
        avg_probs,
        title="Average Answer Probability by Layer (All Cases)",
        save_name="logit_lens_combined",
        commitment_layers=avg_commitment,
    )


def main():
    """Main entry point for logit lens analysis."""
    print("=" * 70)
    print("LogitLens Analysis for MedGemma Prompt Strategies")
    print("=" * 70)
    print(f"GPU Memory: {get_gpu_memory_usage()}")
    
    # Load model
    model, tokenizer = load_model_and_tokenizer(MODEL_NAME)
    print(f"\nModel config:")
    print(f"  Layers: {model.cfg.n_layers}")
    print(f"  Heads: {model.cfg.n_heads}")
    print(f"  d_model: {model.cfg.d_model}")
    
    # Run analysis
    print("\n" + "=" * 70)
    print("Running LogitLens Analysis...")
    print("=" * 70)
    
    all_results = run_full_analysis(model)
    
    # Compute summary
    summary = compute_summary_statistics(all_results)
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    print("\nExpected vs Observed Commitment Layers:")
    print("-" * 50)
    expected = {
        'contrarian': CONTRARIAN_COMMIT_LAYER,
        'chain_of_thought': COT_COMMIT_LAYER,
        'direct_answer': DIRECT_COMMIT_LAYER,
    }
    
    for strategy, stats in summary.items():
        exp = expected.get(strategy, "N/A")
        obs = stats['mean_commitment_layer']
        print(f"{strategy:20s}: Expected L{exp}, Observed L{obs:.1f} ± {stats['std_commitment_layer']:.1f}")
        print(f"                      Final prob: {stats['mean_final_probability']:.4f}")
    
    # Create combined plot
    create_combined_layer_plot(all_results)
    
    # Save all results
    save_results(all_results, "logit_lens_full_results")
    save_results(summary, "logit_lens_summary")
    
    print("\n" + "=" * 70)
    print("Analysis complete! Results saved to contrarian_analysis/")
    print("=" * 70)
    
    return all_results, summary


if __name__ == "__main__":
    results, summary = main()
