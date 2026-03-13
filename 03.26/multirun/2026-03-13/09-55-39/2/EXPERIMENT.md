# Experiment: Medbullets Standard (PLAIN)

**Status:** Completed
**Started:** 2026-03-13 10:05:50  
**Duration:** 2 minutes 48 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
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
prompt:
  _target_: cotlab.prompts.ChainOfThoughtStrategy
  name: chain_of_thought
  system_role: 'You are a medical expert. Think through problems carefully and

    explain your reasoning step by step before giving your final answer.

    '
  include_examples: false
  cot_trigger: 'Let''s think through this step by step:'
  output_format: plain
dataset:
  _target_: cotlab.datasets.loaders.MedBulletsDataset
  name: medbullets
  split: op5_test
experiment:
  _target_: cotlab.experiments.ActivationPatchingExperiment
  name: activation_patching
  description: Layer-wise causal activation patching (logit recovery)
  patching_mode: token_group_contrast
  layer_stride: 1
  num_samples: 500
  max_input_tokens: 1024
  seed: 42
  answer_cue: '


    Answer:'
  introspect_instruction: Think deeply about this problem. Carefully reason through
    the underlying mechanisms and consider all relevant factors before committing
    to your answer.
  token_group_contrast_layer: 3
  token_group_mode: all
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=activation_patching \
  experiment.num_samples=500 \
  experiment.seed=42 \
  prompt=chain_of_thought \
  prompt.output_format=plain \
  dataset=medbullets
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 308
- **Mask Layer:** 3
- **Mean Importance Per Group:** {'delimiter': 0.2161, 'choice': 0.2815, 'content': 0.2131}
- **Dominant Group:** choice
- **Accuracy When Dominant:** {'delimiter': 0.6383, 'choice': 0.4636, 'content': 0.5088}
- **Point Biserial Correlations:** {'choice': {'r': -0.1562, 'p_value': 0.006, 'n': 308, 'mean_importance_correct': 0.2246, 'mean_importance_incorrect': 0.3514}, 'content': {'r': -0.1746, 'p_value': 0.0021, 'n': 308, 'mean_importance_correct': 0.1765, 'mean_importance_incorrect': 0.2582}, 'delimiter': {'r': 0.1023, 'p_value': 0.0729, 'n': 308, 'mean_importance_correct': 0.2331, 'mean_importance_incorrect': 0.1952}}

