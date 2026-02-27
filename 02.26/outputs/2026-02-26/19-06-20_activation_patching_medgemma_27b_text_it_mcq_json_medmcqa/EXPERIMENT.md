# Experiment: Medmcqa Standard

**Status:** Completed
**Started:** 2026-02-26 19:06:20  
**Duration:** 3 minutes 23 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medmcqa

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
  name: medmcqa
  filename: medmcqa/validation.jsonl
  split: validation
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
  dataset=medmcqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 0.4033, 2: 0.0988, 4: 0.3278, 6: 0.2629, 8: 0.49, 10: 0.2024, 12: 0.0998, 14: 0.1741, 16: 0.4236, 18: 0.4599, 20: 0.26, 22: 0.3598, 24: 0.5, 26: 0.5, 28: 0.5, 30: -0.025, 32: 0.1217, 34: 0.3453, 36: 0.1498, 38: 0.3519, 40: 0.3746, 42: 0.1616, 44: 0.0609, 46: 0.3531, 48: 0.169, 50: 0.2271, 52: 0.3214, 54: 0.3306, 56: -0.0009, 58: 0.4316, 60: -0.1317}
- **Top 5 Causal Layers:** [24, 26, 28, 8, 18]

