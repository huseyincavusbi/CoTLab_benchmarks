"""
Attention Pattern Analysis for MedGemma Prompt Strategies.

This script analyzes what tokens the model attends to at critical layers
(especially Layer 18) for each prompting strategy.

Key questions:
- Does contrarian attend to "devil's advocate" or "obvious" at L18?
- How do attention patterns differ between strategies at the commitment layer?
"""

import sys
sys.path.insert(0, '/home/ubuntu/TransformerLens')

import torch
import numpy as np
from typing import Dict, List, Tuple, Optional
from tqdm import tqdm

from config import (
    MODEL_NAME, N_LAYERS,
    PROMPT_STRATEGIES, MEDICAL_CASES,
    CONTRARIAN_COMMIT_LAYER, COT_COMMIT_LAYER, KEY_LAYERS
)
from utils import (
    create_prompt, get_answer_token_ids,
    save_results, load_model_and_tokenizer,
    clear_gpu_memory, get_gpu_memory_usage, 
    setup_plot_style, save_plot, plot_attention_pattern
)

import matplotlib.pyplot as plt


def extract_attention_patterns(
    model,
    prompt: str,
    layers: List[int],
) -> Tuple[Dict[int, torch.Tensor], List[str]]:
    """
    Extract attention patterns at specified layers.
    
    Args:
        model: HookedTransformer model
        prompt: Formatted prompt string
        layers: List of layer indices to extract
        
    Returns:
        Tuple of (attention patterns dict, token strings)
    """
    with torch.no_grad():
        logits, cache = model.run_with_cache(
            prompt,
            prepend_bos=True,
            return_type="logits",
        )
    
    # Get tokens for labeling
    tokens = model.to_tokens(prompt, prepend_bos=True)
    str_tokens = model.to_str_tokens(tokens[0])
    
    # Extract attention patterns
    patterns = {}
    for layer in layers:
        # Attention pattern shape: [batch, n_heads, dest_pos, src_pos]
        pattern = cache['pattern', layer]
        patterns[layer] = pattern.cpu()
    
    del cache
    clear_gpu_memory()
    
    return patterns, str_tokens


def find_key_tokens(
    str_tokens: List[str],
    keywords: List[str],
) -> Dict[str, List[int]]:
    """
    Find positions of key tokens in the sequence.
    
    Args:
        str_tokens: List of token strings
        keywords: Keywords to search for
        
    Returns:
        Dict mapping keyword to list of positions
    """
    positions = {}
    
    for keyword in keywords:
        keyword_lower = keyword.lower()
        matches = []
        for i, token in enumerate(str_tokens):
            if keyword_lower in token.lower():
                matches.append(i)
        positions[keyword] = matches
    
    return positions


def analyze_attention_to_keywords(
    patterns: Dict[int, torch.Tensor],
    keyword_positions: Dict[str, List[int]],
    query_position: int = -1,
) -> Dict:
    """
    Analyze how much attention the last position pays to keyword tokens.
    
    Args:
        patterns: Dict mapping layer to attention patterns
        keyword_positions: Dict mapping keyword to positions
        query_position: Position to analyze attention from (default last)
        
    Returns:
        Dict with attention weights to each keyword per layer
    """
    results = {}
    
    for layer, pattern in patterns.items():
        # pattern shape: [batch, n_heads, dest_pos, src_pos]
        # Get attention from query position
        attn_from_query = pattern[0, :, query_position, :]  # [n_heads, src_pos]
        
        # Average across heads
        avg_attn = attn_from_query.mean(dim=0)  # [src_pos]
        
        layer_results = {}
        for keyword, positions in keyword_positions.items():
            if positions:
                attn_to_keyword = sum(avg_attn[pos].item() for pos in positions)
                layer_results[keyword] = attn_to_keyword
            else:
                layer_results[keyword] = 0.0
        
        results[layer] = layer_results
    
    return results


def analyze_head_specialization(
    patterns: Dict[int, torch.Tensor],
    keyword_positions: Dict[str, List[int]],
    layer: int,
    query_position: int = -1,
) -> Dict:
    """
    Find which heads specialize in attending to different keywords.
    
    Args:
        patterns: Attention patterns
        keyword_positions: Keyword positions
        layer: Layer to analyze
        query_position: Position to analyze from
        
    Returns:
        Dict with per-head attention to each keyword
    """
    pattern = patterns[layer]
    attn_from_query = pattern[0, :, query_position, :]  # [n_heads, src_pos]
    n_heads = attn_from_query.shape[0]
    
    results = {}
    for keyword, positions in keyword_positions.items():
        if positions:
            head_attention = []
            for head in range(n_heads):
                attn = sum(attn_from_query[head, pos].item() for pos in positions)
                head_attention.append(attn)
            results[keyword] = head_attention
        else:
            results[keyword] = [0.0] * n_heads
    
    return results


def compare_strategy_attention(
    model,
    case,
    layer: int = CONTRARIAN_COMMIT_LAYER,
) -> Dict:
    """
    Compare attention patterns between strategies at a specific layer.
    
    Args:
        model: HookedTransformer model
        case: MedicalCase object
        layer: Layer to analyze
        
    Returns:
        Dict with attention analysis for each strategy
    """
    print(f"\n--- Attention Analysis: {case.name} at Layer {layer} ---")
    
    results = {}
    
    # Keywords to track
    contrarian_keywords = ["devil", "advocate", "obvious", "WRONG", "argue", "against"]
    general_keywords = ["diagnosis", "patient", "Question", case.expected_answer.lower()]
    all_keywords = contrarian_keywords + general_keywords
    
    for strategy_name, strategy in PROMPT_STRATEGIES.items():
        prompt = create_prompt(strategy, case)
        
        # Extract attention at this layer
        patterns, str_tokens = extract_attention_patterns(model, prompt, [layer])
        
        # Find keyword positions
        keyword_positions = find_key_tokens(str_tokens, all_keywords)
        
        # Analyze attention to keywords
        keyword_attention = analyze_attention_to_keywords(patterns, keyword_positions)
        
        # Analyze head specialization
        head_spec = analyze_head_specialization(patterns, keyword_positions, layer)
        
        results[strategy_name] = {
            'keyword_attention': keyword_attention[layer],
            'head_specialization': head_spec,
            'str_tokens': str_tokens,
            'keyword_positions': keyword_positions,
            'pattern': patterns[layer],  # Keep for visualization
        }
        
        print(f"\n{strategy_name}:")
        print(f"  Token count: {len(str_tokens)}")
        for kw, attn in keyword_attention[layer].items():
            if attn > 0.01:  # Only print significant attention
                print(f"  Attention to '{kw}': {attn:.4f}")
    
    return results


def plot_attention_comparison(
    results: Dict,
    case_name: str,
    layer: int,
):
    """Create visualization comparing attention patterns across strategies."""
    setup_plot_style()
    
    # Plot 1: Attention to contrarian-specific keywords
    fig, ax = plt.subplots(figsize=(12, 6))
    
    contrarian_keywords = ["devil", "advocate", "obvious", "WRONG", "argue"]
    strategies = list(results.keys())
    
    x = np.arange(len(contrarian_keywords))
    width = 0.25
    
    for i, strategy in enumerate(strategies):
        attn_values = [results[strategy]['keyword_attention'].get(kw, 0) for kw in contrarian_keywords]
        offset = (i - len(strategies)/2 + 0.5) * width
        ax.bar(x + offset, attn_values, width, label=strategy.replace('_', ' ').title())
    
    ax.set_xlabel('Keyword')
    ax.set_ylabel('Attention Weight')
    ax.set_title(f'Attention to Contrarian Keywords at Layer {layer} - {case_name.title()}')
    ax.set_xticks(x)
    ax.set_xticklabels(contrarian_keywords)
    ax.legend()
    
    plt.tight_layout()
    save_plot(fig, f'attention_keywords_{case_name}_L{layer}')
    plt.close()
    
    # Plot 2: Full attention patterns for each strategy
    for strategy_name, data in results.items():
        pattern = data['pattern']
        str_tokens = data['str_tokens']
        
        # Use the first 40 tokens to keep visualization manageable
        max_tokens = min(40, len(str_tokens))
        
        plot_attention_pattern(
            pattern[:, :, :max_tokens, :max_tokens],
            str_tokens[:max_tokens],
            title=f'{strategy_name.replace("_", " ").title()} - L{layer} - {case_name.title()}',
            save_name=f'attention_pattern_{case_name}_{strategy_name}_L{layer}',
        )


def plot_attention_across_layers(
    model,
    case,
    layers: List[int] = KEY_LAYERS,
):
    """
    Analyze how attention to key tokens evolves across layers.
    
    Creates a plot showing attention to "obvious" and other key tokens
    evolving across layers for the contrarian strategy.
    """
    setup_plot_style()
    
    # Focus on contrarian strategy
    strategy = PROMPT_STRATEGIES['contrarian']
    prompt = create_prompt(strategy, case)
    
    # Extract attention at all specified layers
    patterns, str_tokens = extract_attention_patterns(model, prompt, layers)
    
    # Keywords to track
    keywords = ["obvious", "devil", "advocate", "Question", case.expected_answer.lower()]
    keyword_positions = find_key_tokens(str_tokens, keywords)
    
    # Get attention evolution
    attention_evolution = analyze_attention_to_keywords(patterns, keyword_positions)
    
    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for keyword in keywords:
        if any(attention_evolution[l].get(keyword, 0) > 0 for l in layers):
            values = [attention_evolution[l].get(keyword, 0) for l in layers]
            ax.plot(layers, values, marker='o', label=keyword, linewidth=2)
    
    ax.axvline(x=CONTRARIAN_COMMIT_LAYER, color='red', linestyle='--', 
               alpha=0.7, label=f'Commitment Layer (L{CONTRARIAN_COMMIT_LAYER})')
    
    ax.set_xlabel('Layer')
    ax.set_ylabel('Attention Weight')
    ax.set_title(f'Contrarian Attention Evolution - {case.name.title()}')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    save_plot(fig, f'attention_evolution_{case.name}')
    plt.close()
    
    return attention_evolution


def main():
    """Main entry point for attention pattern analysis."""
    print("=" * 70)
    print("Attention Pattern Analysis")
    print("=" * 70)
    print(f"GPU Memory: {get_gpu_memory_usage()}")
    
    # Load model
    model, tokenizer = load_model_and_tokenizer(MODEL_NAME)
    print(f"Model has {model.cfg.n_heads} attention heads per layer")
    
    all_results = {}
    
    for case in MEDICAL_CASES:
        print(f"\n{'='*60}")
        print(f"Analyzing: {case.name}")
        print(f"{'='*60}")
        
        # Compare strategies at the commitment layer
        comparison = compare_strategy_attention(model, case, layer=CONTRARIAN_COMMIT_LAYER)
        
        # Create visualizations
        plot_attention_comparison(comparison, case.name, CONTRARIAN_COMMIT_LAYER)
        
        # Analyze attention evolution for contrarian
        evolution = plot_attention_across_layers(model, case)
        
        all_results[case.name] = {
            'comparison': {
                strategy: {
                    'keyword_attention': data['keyword_attention'],
                    'head_specialization': data['head_specialization'],
                    'keyword_positions': data['keyword_positions'],
                }
                for strategy, data in comparison.items()
            },
            'attention_evolution': evolution,
        }
    
    # Save results (excluding large tensors)
    save_results(all_results, "attention_analysis_results")
    
    # Summary
    print("\n" + "=" * 70)
    print("ATTENTION ANALYSIS SUMMARY")
    print("=" * 70)
    
    print(f"\nKey findings at Layer {CONTRARIAN_COMMIT_LAYER}:")
    
    for case_name, case_results in all_results.items():
        print(f"\n{case_name.title()}:")
        
        contrarian_attn = case_results['comparison']['contrarian']['keyword_attention']
        cot_attn = case_results['comparison']['chain_of_thought']['keyword_attention']
        
        # Check if contrarian attends more to key phrases
        obvious_contrast = contrarian_attn.get('obvious', 0)
        devil_contrast = contrarian_attn.get('devil', 0)
        
        print(f"  Contrarian attention to 'obvious': {obvious_contrast:.4f}")
        print(f"  Contrarian attention to 'devil': {devil_contrast:.4f}")
    
    print("\n" + "=" * 70)
    print("Attention analysis complete!")
    print("=" * 70)
    
    return all_results


if __name__ == "__main__":
    results = main()
