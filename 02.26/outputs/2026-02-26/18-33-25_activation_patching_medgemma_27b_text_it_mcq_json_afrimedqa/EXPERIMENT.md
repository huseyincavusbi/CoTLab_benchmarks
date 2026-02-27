# Experiment: Afrimedqa Standard

**Status:** Completed
**Started:** 2026-02-26 18:33:26  
**Duration:** 2 minutes 2 seconds

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
  prompt=mcq \
  dataset=afrimedqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 1.7841, 2: -0.4039, 4: -0.5177, 6: -0.3012, 8: -0.6852, 10: 0.0082, 12: 0.5545, 14: -0.0628, 16: -0.8484, 18: -0.7491, 20: 1.1682, 22: -0.7878, 24: -0.7931, 26: -0.4879, 28: -0.4727, 30: 0.1839, 32: 0.5971, 34: -0.5139, 36: 0.2413, 38: 0.1398, 40: -0.026, 42: 0.1043, 44: 0.3847, 46: -0.2537, 48: -0.1201, 50: -0.0154, 52: -0.1283, 54: 0.2236, 56: 0.1709, 58: -0.2218, 60: 0.0289}
- **Top 5 Causal Layers:** [0, 20, 32, 12, 44]

