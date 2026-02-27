# Experiment: Histopathology Standard

**Status:** Completed
**Started:** 2026-02-26 19:50:05  
**Duration:** 3 minutes 47 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Histopathology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** histopathology

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
  _target_: cotlab.prompts.HistopathologyPromptStrategy
  name: histopathology
  output_format: json
  few_shot: true
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.HistopathologyDataset
  name: histopathology
  path: data/histopathology.tsv
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
  prompt=histopathology \
  dataset=histopathology
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 0.5809, 2: -0.2627, 4: -0.1479, 6: -0.1956, 8: 0.678, 10: 0.8856, 12: 0.0251, 14: 0.2696, 16: 0.291, 18: -0.4916, 20: 1.864, 22: 1.8211, 24: 1.4307, 26: 1.9354, 28: 1.9202, 30: 1.2023, 32: 1.4004, 34: 1.8498, 36: -0.6309, 38: -0.8205, 40: -0.4712, 42: -0.052, 44: 1.5862, 46: 1.1899, 48: 0.7042, 50: 1.4661, 52: 0.6416, 54: -0.1123, 56: -0.4108, 58: 1.4878, 60: 1.1077}
- **Top 5 Causal Layers:** [26, 28, 20, 34, 22]

