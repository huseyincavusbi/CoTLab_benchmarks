# Brief Analysis

- Mean pooling, seed=42, 50 samples each (histopathology vs radiology).
- **Mean cosine similarity ~0.9285**, **mean L2 ~631.8** → runs are highly similar overall.
- **Lowest cosine layers:** 24, 25, 33, 7, 23 (largest directional divergence).
- **Highest L2 layers:** 33, 32, 26, 28, 27 (largest magnitude shifts).

**Takeaway:** With mean pooling, the divergence pattern is stable and concentrated in late layers.
