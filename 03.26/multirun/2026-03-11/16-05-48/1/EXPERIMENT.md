# Experiment: Medbullets Standard

**Status:** Completed
**Started:** 2026-03-11 16:09:38  
**Duration:** 4 minutes 33 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
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
  _target_: cotlab.datasets.loaders.MedBulletsDataset
  name: medbullets
  split: op5_test
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
  dataset=medbullets
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 0.1265, 2: 0.1799, 4: 0.2648, 6: 0.2438, 8: 0.168, 10: 0.2837, 12: 0.0544, 14: 0.5099, 16: 0.1909, 18: 0.4757, 20: 0.5855, 22: 0.147, 24: 0.7718, 26: 0.5682, 28: 0.505, 30: 0.3626, 32: 0.2176, 34: 0.3432, 36: 0.1601, 38: 0.1365, 40: 0.1815, 42: 0.1745, 44: 0.1464, 46: 0.0959, 48: 0.4552, 50: 0.0868, 52: 0.5217, 54: 0.169, 56: -0.0056, 58: 0.2945, 60: 0.3662}
- **Top 5 Causal Layers:** [24, 20, 26, 52, 14]

