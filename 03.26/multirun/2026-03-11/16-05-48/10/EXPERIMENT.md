# Experiment: Pediatrics Standard

**Status:** Completed
**Started:** 2026-03-11 16:47:34  
**Duration:** 3 minutes 22 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** pediatrics

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
  _target_: cotlab.datasets.PediatricsDataset
  name: pediatrics
  path: data/Pediatrics_Synthetic_Data.csv
  text_column: Scenario
  label_column: Diagnosis
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
  dataset=pediatrics
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: -0.2671, 2: 0.0106, 4: 0.0331, 6: 0.036, 8: 0.3609, 10: 0.5096, 12: 0.1987, 14: 0.2854, 16: 0.0992, 18: 0.3678, 20: 0.0299, 22: 0.2648, 24: 0.2582, 26: 0.7125, 28: 0.4412, 30: 0.1505, 32: 0.3241, 34: 0.5089, 36: 0.0427, 38: 0.2888, 40: 0.6142, 42: 0.2113, 44: 0.1485, 46: -0.0338, 48: 0.2779, 50: -0.1646, 52: -0.0623, 54: 0.3066, 56: 0.0847, 58: 0.1134, 60: 0.2965}
- **Top 5 Causal Layers:** [26, 40, 10, 34, 28]

