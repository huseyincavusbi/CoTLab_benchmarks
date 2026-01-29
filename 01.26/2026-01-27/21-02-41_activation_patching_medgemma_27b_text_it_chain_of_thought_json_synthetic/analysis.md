# Activation Patching Summary (MedGemma-27B text-it)

**Run:** 2026-01-27/21-02-41_activation_patching_medgemma_27b_text_it_chain_of_thought_json_synthetic  
**Samples:** 20  
**Variants:** clean=histopathology, corrupt=radiology (json, few_shot=true)  
**Patching:** sweep all layers, interventions = patch + zero

## Key Findings

- **Strong early-layer dominance.** Average effect is highest in layers **1–7**.  
  Top layers (avg effect): **1 (0.92), 2 (0.91), 4 (0.88), 3 (0.87), 6 (0.86)**.
- **Layer 0 has near‑zero effect** (0.00024), as expected.
- Mid/late layers show **moderate effects**, with smaller bumps (e.g., around layers 47–51).

## Interpretation (lightweight)

Patching early layers moves the output much closer to the clean (Histo) output than patching late layers. This suggests **early representations carry most of the Histo vs Radiology signal** in this setup.

## Caveats

- Only **20 samples**, so this is a noisy diagnostic.
- **Effect metric = word overlap recovery**, not logits/probabilities.
- Uses **few-shot json prompts**, which may influence the effect pattern.
