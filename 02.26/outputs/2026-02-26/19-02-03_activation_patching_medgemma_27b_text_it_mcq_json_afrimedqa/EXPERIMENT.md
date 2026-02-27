# Experiment: Afrimedqa Standard

**Status:** Completed
**Started:** 2026-02-26 19:02:03  
**Duration:** 3 minutes 30 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** afrimedqa

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
  _target_: cotlab.datasets.loaders.MedQADataset
  name: afrimedqa
  filename: afrimedqa/mcq.jsonl
  split: mcq
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
  dataset=afrimedqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 0.8, 2: 0.2581, 4: 0.1087, 6: 0.0921, 8: 0.1404, 10: 0.2528, 12: 0.5622, 14: 0.1099, 16: 0.1327, 18: 0.152, 20: 0.6686, 22: 0.1792, 24: 0.1552, 26: 0.14, 28: 0.148, 30: 0.4225, 32: 0.5627, 34: 0.0963, 36: 0.1201, 38: 0.4276, 40: 0.0931, 42: 0.1043, 44: 0.1668, 46: 0.0831, 48: 0.0471, 50: 0.1177, 52: 0.1633, 54: 0.466, 56: 0.4848, 58: 0.2415, 60: -0.0276}
- **Top 5 Causal Layers:** [0, 20, 32, 12, 56]

