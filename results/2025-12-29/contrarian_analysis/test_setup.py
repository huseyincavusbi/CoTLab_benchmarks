"""
Quick test to verify the TransformerLens setup works with MedGemma.

This script:
1. Loads MedGemma 27B using TransformerLens
2. Runs a simple forward pass
3. Verifies we can cache activations
4. Tests basic logit lens functionality

Run this first to ensure everything is set up correctly.
"""

import sys
sys.path.insert(0, '/home/ubuntu/TransformerLens')

import torch
import gc


def test_transformerlens_import():
    """Test that TransformerLens can be imported."""
    print("Testing TransformerLens import...")
    
    from transformer_lens import HookedTransformer
    from transformer_lens.loading_from_pretrained import OFFICIAL_MODEL_NAMES
    
    # Check that MedGemma is in the model list
    medgemma_models = [m for m in OFFICIAL_MODEL_NAMES if 'medgemma' in m.lower()]
    print(f"MedGemma models available: {medgemma_models}")
    
    assert 'google/medgemma-27b-text-it' in OFFICIAL_MODEL_NAMES, \
        "MedGemma 27B text-it not found in OFFICIAL_MODEL_NAMES"
    
    print("✓ TransformerLens imports successfully")
    print("✓ MedGemma 27B is registered")
    return True


def test_model_loading():
    """Test loading MedGemma 27B."""
    print("\nTesting model loading...")
    
    from transformer_lens import HookedTransformer
    
    # Check GPU memory
    if torch.cuda.is_available():
        gpu_mem = torch.cuda.get_device_properties(0).total_memory / 1e9
        print(f"GPU memory available: {gpu_mem:.1f} GB")
    
    print("Loading model (this may take a few minutes)...")
    
    model = HookedTransformer.from_pretrained(
        "google/medgemma-27b-text-it",
        device="cuda",
        dtype=torch.bfloat16,
        fold_ln=False,
        center_writing_weights=False,
        center_unembed=False,
    )
    
    print(f"✓ Model loaded successfully!")
    print(f"  Layers: {model.cfg.n_layers}")
    print(f"  Heads: {model.cfg.n_heads}")
    print(f"  d_model: {model.cfg.d_model}")
    print(f"  d_vocab: {model.cfg.d_vocab}")
    
    return model


def test_forward_pass(model):
    """Test a basic forward pass."""
    print("\nTesting forward pass...")
    
    test_prompt = "What is diabetes?"
    
    with torch.no_grad():
        logits = model(test_prompt, prepend_bos=True)
    
    print(f"✓ Forward pass successful!")
    print(f"  Output shape: {logits.shape}")
    
    # Get top 5 predictions for the last token
    top_tokens = torch.topk(logits[0, -1], k=5)
    print(f"  Top 5 next token predictions:")
    for i, (idx, score) in enumerate(zip(top_tokens.indices, top_tokens.values)):
        token = model.tokenizer.decode([idx.item()])
        print(f"    {i+1}. '{token}' (score: {score.item():.2f})")
    
    return True


def test_run_with_cache(model):
    """Test running with activation cache."""
    print("\nTesting run_with_cache...")
    
    test_prompt = "What is the diagnosis for a patient with polyuria and polydipsia?"
    
    with torch.no_grad():
        logits, cache = model.run_with_cache(
            test_prompt,
            prepend_bos=True,
        )
    
    print(f"✓ run_with_cache successful!")
    print(f"  Cache contains {len(cache)} activation tensors")
    
    # Test accessing residual stream
    resid_0 = cache['resid_post', 0]
    resid_mid = cache['resid_post', model.cfg.n_layers // 2]
    resid_final = cache['resid_post', model.cfg.n_layers - 1]
    
    print(f"  Layer 0 resid_post shape: {resid_0.shape}")
    print(f"  Layer {model.cfg.n_layers // 2} resid_post shape: {resid_mid.shape}")
    print(f"  Final layer resid_post shape: {resid_final.shape}")
    
    # Test accessing attention patterns
    pattern_0 = cache['pattern', 0]
    print(f"  Layer 0 attention pattern shape: {pattern_0.shape}")
    
    return cache


def test_logit_lens(model, cache):
    """Test basic logit lens functionality."""
    print("\nTesting logit lens...")
    
    import einops
    
    # Get final layer norm and unembedding
    ln_final = model.ln_final
    W_U = model.W_U
    
    # Get residual at layer 18 (expected contrarian commit layer)
    layer = 18
    resid = cache['resid_post', layer]
    
    # Apply layer norm
    resid_normed = ln_final(resid.float()).to(resid.dtype)
    
    # Project to vocabulary
    logits_at_layer = einops.einsum(
        resid_normed, W_U,
        "batch pos d_model, d_model d_vocab -> batch pos d_vocab"
    )
    
    print(f"✓ Logit lens successful!")
    print(f"  Logits at layer {layer} shape: {logits_at_layer.shape}")
    
    # Get top prediction at this layer
    top_at_layer = torch.topk(logits_at_layer[0, -1], k=3)
    print(f"  Top 3 predictions at layer {layer}:")
    for i, idx in enumerate(top_at_layer.indices):
        token = model.tokenizer.decode([idx.item()])
        print(f"    {i+1}. '{token}'")
    
    return True


def test_prompt_format():
    """Test the Gemma 3 chat format."""
    print("\nTesting prompt format...")
    
    sys.path.insert(0, '/home/ubuntu/contrarian_analysis')
    from utils import format_gemma3_chat, create_prompt
    from config import PROMPT_STRATEGIES, MEDICAL_CASES
    
    # Test formatting
    case = MEDICAL_CASES[0]
    
    for name, strategy in PROMPT_STRATEGIES.items():
        prompt = create_prompt(strategy, case)
        print(f"\n{name} prompt length: {len(prompt.split())} words")
        print(f"First 100 chars: {prompt[:100]}...")
    
    print("\n✓ Prompt formatting works!")
    return True


def main():
    """Run all tests."""
    print("=" * 70)
    print("TransformerLens + MedGemma Setup Test")
    print("=" * 70)
    
    # Test 1: Imports
    test_transformerlens_import()
    
    # Test 2: Prompt format (doesn't need model)
    test_prompt_format()
    
    # Test 3: Model loading
    model = test_model_loading()
    
    # Test 4: Forward pass
    test_forward_pass(model)
    
    # Test 5: Run with cache
    cache = test_run_with_cache(model)
    
    # Test 6: Logit lens
    test_logit_lens(model, cache)
    
    print("\n" + "=" * 70)
    print("ALL TESTS PASSED! ✓")
    print("=" * 70)
    print("\nYou can now run the full analysis with:")
    print("  cd /home/ubuntu/contrarian_analysis")
    print("  python run_all_experiments.py")
    print("\nOr run individual experiments:")
    print("  python run_all_experiments.py -e logit_lens")
    print("  python run_all_experiments.py -e patching")
    print("  etc.")
    
    # Cleanup
    del model, cache
    gc.collect()
    torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
