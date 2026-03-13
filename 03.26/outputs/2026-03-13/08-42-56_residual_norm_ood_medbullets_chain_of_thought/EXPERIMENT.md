# Experiment: Medbullets Standard (PLAIN)

**Status:** Completed
**Started:** 2026-03-13 08:42:56  
**Duration:** 42 seconds

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
  _target_: cotlab.experiments.ResidualNormOODExperiment
  name: residual_norm_ood
  description: L2 residual norm OOD flag vs logit entropy baseline
  target_layer: null
  num_samples: null
  seed: 42
  max_input_tokens: 1024
  answer_cue: '


    Answer:'
  threshold_percentile_step: 5
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=residual_norm_ood \
  experiment.seed=42 \
  prompt=chain_of_thought \
  prompt.output_format=plain \
  dataset=medbullets
```

## Results

- **Accuracy:** 55.2%
- **Samples Processed:** 1
- **Dataset:** medbullets
- **Target Layer:** 61
- **Num Samples:** 308
- **Auroc L2 Norm:** 0.606
- **Auroc Logit Entropy:** 0.648
- **Norm Threshold Tau:** 11040.778
- **Balanced Acc At Tau:** 0.598
- **Mean Norm Correct:** 12395.556
- **Mean Norm Incorrect:** 11494.931
- **Mean Entropy Correct:** 0.380
- **Mean Entropy Incorrect:** 0.582

