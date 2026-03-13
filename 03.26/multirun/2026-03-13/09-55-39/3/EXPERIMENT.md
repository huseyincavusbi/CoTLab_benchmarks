# Experiment: Histopathology Standard (PLAIN)

**Status:** Completed
**Started:** 2026-03-13 10:08:54  
**Duration:** 4 minutes 19 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
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
  _target_: cotlab.datasets.HistopathologyDataset
  name: histopathology
  path: data/histopathology.tsv
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
  dataset=histopathology
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 500
- **Mask Layer:** 3
- **Mean Importance Per Group:** {'delimiter': 0.4281, 'choice': 0.0006, 'content': 0.1541}
- **Dominant Group:** delimiter
- **Accuracy When Dominant:** {'delimiter': 0.0, 'choice': 0.0, 'content': 0.0}
- **Point Biserial Correlations:** {'choice': {'r': 0.0, 'p_value': 1.0, 'n': 500, 'mean_importance_correct': None, 'mean_importance_incorrect': 0.0006}, 'content': {'r': 0.0, 'p_value': 1.0, 'n': 500, 'mean_importance_correct': None, 'mean_importance_incorrect': 0.1541}, 'delimiter': {'r': 0.0, 'p_value': 1.0, 'n': 500, 'mean_importance_correct': None, 'mean_importance_incorrect': 0.4281}}

