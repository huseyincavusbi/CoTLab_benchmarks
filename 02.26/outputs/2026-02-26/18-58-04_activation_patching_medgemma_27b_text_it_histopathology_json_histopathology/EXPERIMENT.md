# Experiment: Histopathology Standard

**Status:** Completed
**Started:** 2026-02-26 18:58:04  
**Duration:** 2 minutes 50 seconds

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
  patching_mode: few_shot_contrast
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
- **Mean Effect Per Layer:** {0: 0.6142, 2: 0.1561, 4: 0.5579, 6: 0.0038, 8: 0.9632, 10: 1.1586, 12: 0.6651, 14: 1.0812, 16: 0.8031, 18: 0.943, 20: 1.1964, 22: 1.1709, 24: 1.1097, 26: 1.2, 28: 1.2, 30: 0.566, 32: 0.3968, 34: 1.1475, 36: 0.4636, 38: -0.2921, 40: -0.2908, 42: 0.0523, 44: 1.0237, 46: 0.7639, 48: 0.6263, 50: 0.4231, 52: 0.9064, 54: -0.1076, 56: 0.7806, 58: 0.9197, 60: 0.7237}
- **Top 5 Causal Layers:** [26, 28, 20, 22, 10]

