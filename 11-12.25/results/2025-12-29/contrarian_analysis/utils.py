"""
Utility functions for MedGemma Mechanistic Analysis.

Provides helper functions for prompt formatting, token handling,
result saving/loading, and plotting.
"""

import json
import os
import pickle
from typing import Dict, List, Optional, Tuple, Union

import numpy as np
import torch
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from pathlib import Path

from config import (
    OUTPUT_DIR, PLOTS_DIR, RESULTS_DIR,
    PromptStrategy, MedicalCase, N_LAYERS
)


# ============================================================================
# Prompt Formatting
# ============================================================================

def format_gemma3_chat(
    system_message: str,
    user_message: str,
) -> str:
    """
    Format a prompt using Gemma 3 chat template.
    
    Gemma 3 uses a specific format for chat:
    <bos><start_of_turn>user
    {system_message}
    
    {user_message}<end_of_turn>
    <start_of_turn>model
    
    Note: We don't include <bos> as TransformerLens handles that.
    """
    # Gemma 3 chat format
    formatted = (
        f"<start_of_turn>user\n"
        f"{system_message}\n\n"
        f"{user_message}<end_of_turn>\n"
        f"<start_of_turn>model\n"
    )
    return formatted


def create_prompt(
    strategy: PromptStrategy,
    case: MedicalCase,
) -> str:
    """Create a fully formatted prompt for a given strategy and case."""
    user_content = strategy.format(case.question)
    return format_gemma3_chat(strategy.system_message, user_content)


# ============================================================================
# Token Handling
# ============================================================================

def get_answer_token_ids(
    tokenizer,
    answer_tokens: List[str],
) -> List[int]:
    """
    Get token IDs for all variations of an answer.
    
    Args:
        tokenizer: HuggingFace tokenizer
        answer_tokens: List of possible answer strings
        
    Returns:
        List of unique token IDs that match any answer variation
    """
    token_ids = set()
    for answer in answer_tokens:
        # Encode without special tokens
        ids = tokenizer.encode(answer, add_special_tokens=False)
        # We want the first token if the answer becomes multiple tokens
        if ids:
            token_ids.add(ids[0])
    return list(token_ids)


def get_token_probability(
    logits: torch.Tensor,
    token_ids: List[int],
    position: int = -1,
) -> float:
    """
    Get the probability of any of the target tokens at a position.
    
    Args:
        logits: Logits tensor of shape [batch, pos, vocab]
        token_ids: List of token IDs to sum probability for
        position: Position to get probability at (default -1 for last)
        
    Returns:
        Sum of probabilities for all target tokens
    """
    probs = torch.softmax(logits[0, position], dim=-1)
    total_prob = sum(probs[tid].item() for tid in token_ids)
    return total_prob


def get_token_rank(
    logits: torch.Tensor,
    token_ids: List[int],
    position: int = -1,
) -> int:
    """
    Get the best rank of any target token at a position.
    
    Args:
        logits: Logits tensor of shape [batch, pos, vocab]
        token_ids: List of token IDs to check rank for
        position: Position to check (default -1 for last)
        
    Returns:
        Best (lowest) rank among all target tokens
    """
    # Get ranks for all tokens
    logits_at_pos = logits[0, position]
    sorted_indices = torch.argsort(logits_at_pos, descending=True)
    ranks = torch.argsort(sorted_indices)
    
    best_rank = float('inf')
    for tid in token_ids:
        rank = ranks[tid].item()
        if rank < best_rank:
            best_rank = rank
    
    return best_rank


def in_top_k(
    logits: torch.Tensor,
    token_ids: List[int],
    k: int = 10,
    position: int = -1,
) -> bool:
    """Check if any target token is in top-k predictions."""
    return get_token_rank(logits, token_ids, position) < k


# ============================================================================
# Result Saving/Loading
# ============================================================================

def save_results(data: Dict, name: str, subdir: Optional[str] = None):
    """Save results to JSON file."""
    if subdir:
        path = os.path.join(RESULTS_DIR, subdir)
        os.makedirs(path, exist_ok=True)
    else:
        path = RESULTS_DIR
    
    filepath = os.path.join(path, f"{name}.json")
    
    # Convert numpy/torch types to Python types
    def convert(obj):
        if isinstance(obj, (np.integer, np.floating)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, torch.Tensor):
            return obj.cpu().numpy().tolist()
        elif isinstance(obj, dict):
            return {k: convert(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert(v) for v in obj]
        return obj
    
    with open(filepath, 'w') as f:
        json.dump(convert(data), f, indent=2)
    
    print(f"Saved results to {filepath}")


def load_results(name: str, subdir: Optional[str] = None) -> Dict:
    """Load results from JSON file."""
    if subdir:
        path = os.path.join(RESULTS_DIR, subdir)
    else:
        path = RESULTS_DIR
    
    filepath = os.path.join(path, f"{name}.json")
    with open(filepath, 'r') as f:
        return json.load(f)


def save_cache(data, name: str):
    """Save data to pickle for caching expensive computations."""
    filepath = os.path.join(RESULTS_DIR, f"{name}.pkl")
    with open(filepath, 'wb') as f:
        pickle.dump(data, f)
    print(f"Saved cache to {filepath}")


def load_cache(name: str):
    """Load data from pickle cache."""
    filepath = os.path.join(RESULTS_DIR, f"{name}.pkl")
    with open(filepath, 'rb') as f:
        return pickle.load(f)


# ============================================================================
# Plotting Helpers
# ============================================================================

def setup_plot_style():
    """Set up consistent plot styling."""
    plt.style.use('default')
    plt.rcParams.update({
        'figure.figsize': (12, 8),
        'font.size': 12,
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 10,
        'figure.dpi': 150,
    })


def save_plot(fig, name: str, subdir: Optional[str] = None):
    """Save a matplotlib figure to the plots directory."""
    if subdir:
        path = os.path.join(PLOTS_DIR, subdir)
        os.makedirs(path, exist_ok=True)
    else:
        path = PLOTS_DIR
    
    filepath = os.path.join(path, f"{name}.png")
    fig.savefig(filepath, bbox_inches='tight', dpi=150)
    print(f"Saved plot to {filepath}")
    
    # Also save as SVG for high quality
    svg_path = os.path.join(path, f"{name}.svg")
    fig.savefig(svg_path, bbox_inches='tight', format='svg')


def plot_layer_sweep(
    layer_probs: Dict[str, List[float]],
    title: str,
    save_name: str,
    commitment_layers: Optional[Dict[str, int]] = None,
):
    """
    Plot answer probability across layers for different strategies.
    
    Args:
        layer_probs: Dict mapping strategy name to list of probabilities per layer
        title: Plot title
        save_name: Filename for saving
        commitment_layers: Optional dict mapping strategy to layer where it commits
    """
    setup_plot_style()
    fig, ax = plt.subplots(figsize=(14, 8))
    
    colors = {
        'contrarian': '#2ecc71',      # Green
        'chain_of_thought': '#3498db', # Blue
        'direct_answer': '#e74c3c',    # Red
    }
    
    for strategy, probs in layer_probs.items():
        color = colors.get(strategy, '#95a5a6')
        ax.plot(range(len(probs)), probs, 
                label=strategy.replace('_', ' ').title(),
                color=color, linewidth=2, marker='o', markersize=3)
        
        # Mark commitment layer if provided
        if commitment_layers and strategy in commitment_layers:
            layer = commitment_layers[strategy]
            if layer < len(probs):
                ax.axvline(x=layer, color=color, linestyle='--', alpha=0.5)
                ax.scatter([layer], [probs[layer]], s=100, color=color, 
                          zorder=5, edgecolors='black')
    
    ax.set_xlabel('Layer')
    ax.set_ylabel('Answer Probability')
    ax.set_title(title)
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, N_LAYERS - 1)
    ax.set_ylim(0, 1)
    
    save_plot(fig, save_name)
    plt.close(fig)
    return fig


def plot_attention_pattern(
    attention: torch.Tensor,
    tokens: List[str],
    title: str,
    save_name: str,
    head_idx: Optional[int] = None,
):
    """
    Plot attention pattern heatmap.
    
    Args:
        attention: Attention weights [batch, heads, dest, src] or [dest, src]
        tokens: List of token strings
        title: Plot title
        save_name: Filename for saving
        head_idx: If provided, select this head from multi-head attention
    """
    setup_plot_style()
    
    # Handle different attention shapes
    attn = attention
    if attn.dim() == 4:  # [batch, heads, dest, src]
        attn = attn[0]  # Remove batch
        if head_idx is not None:
            attn = attn[head_idx]  # Select head
        else:
            attn = attn.mean(dim=0)  # Average over heads
    elif attn.dim() == 3:  # [heads, dest, src]
        if head_idx is not None:
            attn = attn[head_idx]
        else:
            attn = attn.mean(dim=0)
    
    attn = attn.cpu().numpy()
    
    # Truncate if too many tokens
    max_tokens = 50
    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]
        attn = attn[:max_tokens, :max_tokens]
    
    fig, ax = plt.subplots(figsize=(12, 10))
    im = ax.imshow(attn, cmap='Blues')
    
    ax.set_xticks(range(len(tokens)))
    ax.set_yticks(range(len(tokens)))
    ax.set_xticklabels(tokens, rotation=45, ha='right', fontsize=8)
    ax.set_yticklabels(tokens, fontsize=8)
    
    ax.set_xlabel('Source Token')
    ax.set_ylabel('Destination Token')
    ax.set_title(title)
    
    plt.colorbar(im, ax=ax, label='Attention Weight')
    
    save_plot(fig, save_name)
    plt.close(fig)
    return fig


def plot_head_contributions(
    contributions: Dict[str, np.ndarray],
    title: str,
    save_name: str,
):
    """
    Plot head contribution heatmap comparing strategies.
    
    Args:
        contributions: Dict mapping strategy to [n_layers, n_heads] array
        title: Plot title
        save_name: Filename for saving
    """
    setup_plot_style()
    
    n_strategies = len(contributions)
    fig, axes = plt.subplots(1, n_strategies, figsize=(6 * n_strategies, 10))
    
    if n_strategies == 1:
        axes = [axes]
    
    for ax, (strategy, contrib) in zip(axes, contributions.items()):
        im = ax.imshow(contrib, cmap='RdBu_r', aspect='auto',
                       norm=mcolors.TwoSlopeNorm(vcenter=0))
        ax.set_xlabel('Head')
        ax.set_ylabel('Layer')
        ax.set_title(strategy.replace('_', ' ').title())
        plt.colorbar(im, ax=ax, label='Contribution')
    
    fig.suptitle(title, fontsize=14)
    plt.tight_layout()
    
    save_plot(fig, save_name)
    plt.close(fig)
    return fig


# ============================================================================
# Model Loading Helper
# ============================================================================

def load_model_and_tokenizer(
    model_name: str = "google/medgemma-27b-text-it",
    device: str = "cuda",
    dtype: str = "bfloat16",
):
    """
    Load MedGemma model using TransformerLens.
    
    Returns:
        Tuple of (model, tokenizer)
    """
    import sys
    sys.path.insert(0, '/home/ubuntu/TransformerLens')
    
    from transformer_lens import HookedTransformer
    
    print(f"Loading {model_name}...")
    print(f"Device: {device}, Dtype: {dtype}")
    
    # Load with TransformerLens
    model = HookedTransformer.from_pretrained(
        model_name,
        device=device,
        dtype=getattr(torch, dtype),
        fold_ln=False,  # Keep layer norms for accurate logit lens
        center_writing_weights=False,
        center_unembed=False,
    )
    
    print(f"Model loaded. Layers: {model.cfg.n_layers}, Heads: {model.cfg.n_heads}")
    
    return model, model.tokenizer


# ============================================================================
# Memory Management
# ============================================================================

def clear_gpu_memory():
    """Clear GPU memory cache."""
    import gc
    gc.collect()
    torch.cuda.empty_cache()
    if torch.cuda.is_available():
        torch.cuda.synchronize()


def get_gpu_memory_usage() -> str:
    """Get current GPU memory usage as a string."""
    if not torch.cuda.is_available():
        return "No GPU available"
    
    allocated = torch.cuda.memory_allocated() / 1e9
    reserved = torch.cuda.memory_reserved() / 1e9
    total = torch.cuda.get_device_properties(0).total_memory / 1e9
    
    return f"Allocated: {allocated:.2f}GB, Reserved: {reserved:.2f}GB, Total: {total:.2f}GB"
