# Experiment: Medmcqa Standard

**Status:** Completed
**Started:** 2026-02-26 18:36:44  
**Duration:** 1 minutes 58 seconds

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
  dataset=medmcqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 1.8903, 2: -0.3845, 4: -0.4815, 6: -0.272, 8: -0.65, 10: -0.1254, 12: 0.4376, 14: -0.2308, 16: -0.9153, 18: -0.8458, 20: 1.082, 22: -0.8557, 24: -0.7849, 26: -0.6162, 28: -0.3052, 30: 0.2667, 32: 0.6458, 34: -0.6423, 36: 0.3194, 38: 0.1406, 40: -0.2024, 42: 0.1252, 44: 0.3408, 46: -0.2399, 48: -0.0488, 50: 0.0763, 52: -0.2425, 54: 0.2307, 56: -0.0235, 58: -0.2742, 60: 0.0817}
- **Top 5 Causal Layers:** [0, 20, 32, 12, 44]

