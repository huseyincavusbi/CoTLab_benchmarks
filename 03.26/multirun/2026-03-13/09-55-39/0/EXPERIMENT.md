# Experiment: Afrimedqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-03-13 09:55:40  
**Duration:** 3 minutes 58 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
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
  _target_: cotlab.datasets.loaders.MedQADataset
  name: afrimedqa
  filename: afrimedqa/mcq.jsonl
  split: mcq
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
  dataset=afrimedqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 500
- **Mask Layer:** 3
- **Mean Importance Per Group:** {'delimiter': 0.173, 'choice': 0.2258, 'content': 0.1653}
- **Dominant Group:** choice
- **Accuracy When Dominant:** {'delimiter': 0.7915, 'choice': 0.7299, 'content': 0.6484}
- **Point Biserial Correlations:** {'choice': {'r': -0.1045, 'p_value': 0.0194, 'n': 500, 'mean_importance_correct': 0.2063, 'mean_importance_incorrect': 0.2822}, 'content': {'r': -0.1351, 'p_value': 0.0025, 'n': 500, 'mean_importance_correct': 0.1512, 'mean_importance_incorrect': 0.2061}, 'delimiter': {'r': 0.0115, 'p_value': 0.797, 'n': 500, 'mean_importance_correct': 0.1741, 'mean_importance_incorrect': 0.1699}}

