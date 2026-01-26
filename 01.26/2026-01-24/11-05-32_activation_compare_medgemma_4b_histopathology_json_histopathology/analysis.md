# Brief Analysis

- Compared residual activations between **histopathology** and **radiology** (MedGemma‑4B, 50 samples each) using **mean pooling**.
- **Overall similarity is high** (mean cosine ~0.93), higher than last‑token pooling, indicating averaging smooths differences.
- **Divergence shifts later**: the largest cosine drops appear in **layers ~23–25 and 33**.
- **Late layers still show large L2 gaps**, suggesting task‑specific decision dynamics persist even with mean pooling.

**Takeaway:** Mean pooling makes runs look more similar overall, but **late‑layer divergence remains**, consistent with different task demands.
