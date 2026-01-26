# Brief Analysis

- Compared residual activations between **histopathology** and **radiology** (MedGemma‑4B, 50 samples each, last‑token pooling).
- **Overall similarity is moderate** (mean cosine ~0.83), so representations are related but not identical.
- **Largest divergence appears in mid‑layers** (e.g., layers ~8–15 show the lowest cosine similarity), suggesting task‑specific features emerge mid‑stack.
- **Late layers show very large L2 gaps**, consistent with different decision dynamics for the two tasks.

**Takeaway:** Internals change meaningfully between histopathology and radiology, especially in mid/late layers.
