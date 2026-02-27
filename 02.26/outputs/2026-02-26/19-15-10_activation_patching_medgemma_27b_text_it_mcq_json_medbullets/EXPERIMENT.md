# Experiment: Medbullets Standard

**Status:** Completed
**Started:** 2026-02-26 19:15:10  
**Duration:** 4 minutes 17 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medbullets

<details>
<summary>Full Configuration (YAML)</summary>

```yaml
backend:
  _target_: cotlab.backends.TransformersBackend
  device: cuda
  dtype: bfloat16
  enable_hooks: true
  trust_remote_code: true
model:
  name: google/medgemma-27b-text-it
  variant: 27b-text
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b_text_it
prompt:
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: true
  output_format: json
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MedBulletsDataset
  name: medbullets
  split: op5_test
experiment:
  _target_: cotlab.experiments.ActivationPatchingExperiment
  name: activation_patching
  description: Layer-wise causal activation patching (logit recovery)
  patching_mode: introspect_contrast
  layer_stride: 2
  num_samples: 50
  max_input_tokens: 1024
  seed: 42
  answer_cue: '


    Answer:'
  introspect_instruction: Think deeply about this problem. Carefully reason through
    the underlying mechanisms and consider all relevant factors before committing
    to your answer.
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=activation_patching \
  experiment.num_samples=50 \
  experiment.seed=42 \
  prompt=mcq \
  dataset=medbullets
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: -0.2, 2: -0.0538, 4: 0.8224, 6: 0.9426, 8: 1.1114, 10: 0.4937, 12: -0.1047, 14: 0.3976, 16: 0.9714, 18: 1.0861, 20: -0.2951, 22: 1.1708, 24: 1.18, 26: 1.18, 28: 1.0924, 30: 0.3002, 32: -0.1495, 34: 0.374, 36: 0.7992, 38: -0.2078, 40: 0.4461, 42: 0.4136, 44: -0.1017, 46: 0.8887, 48: 0.019, 50: 0.2545, 52: -0.1792, 54: -0.388, 56: -0.2971, 58: -0.0, 60: 0.1503}
- **Top 5 Causal Layers:** [24, 26, 22, 8, 28]

