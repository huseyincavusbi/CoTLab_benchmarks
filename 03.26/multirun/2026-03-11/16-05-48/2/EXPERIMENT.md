# Experiment: Medmcqa Standard

**Status:** Completed
**Started:** 2026-03-11 16:14:21  
**Duration:** 3 minutes 29 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
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
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: google_medgemma_27b_text_it
prompt:
  _target_: cotlab.prompts.ChainOfThoughtStrategy
  name: chain_of_thought
  system_role: 'You are a medical expert. Think through problems carefully and

    explain your reasoning step by step before giving your final answer.

    '
  include_examples: false
  cot_trigger: 'Let''s think through this step by step:'
  output_format: json
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medmcqa
  filename: medmcqa/validation.jsonl
  split: validation
experiment:
  _target_: cotlab.experiments.ActivationPatchingExperiment
  name: activation_patching
  description: Layer-wise causal activation patching (logit recovery)
  patching_mode: cot_contrast
  layer_stride: 2
  num_samples: 100
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
  experiment.num_samples=100 \
  experiment.seed=42 \
  prompt=chain_of_thought \
  dataset=medmcqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: -0.5196, 2: 0.0928, 4: 0.2186, 6: 0.1399, 8: 0.1943, 10: 0.3466, 12: -0.1927, 14: 0.296, 16: -0.0906, 18: 0.2764, 20: 0.6835, 22: 0.1987, 24: 1.3637, 26: 1.1152, 28: 0.7087, 30: 1.1448, 32: 0.3826, 34: 0.2185, 36: 0.1507, 38: 0.0006, 40: 0.3121, 42: 0.4504, 44: 0.3729, 46: 0.5839, 48: 0.6558, 50: 0.3105, 52: 0.9785, 54: -0.0571, 56: 0.5152, 58: 0.2808, 60: 0.513}
- **Top 5 Causal Layers:** [24, 30, 26, 52, 28]

