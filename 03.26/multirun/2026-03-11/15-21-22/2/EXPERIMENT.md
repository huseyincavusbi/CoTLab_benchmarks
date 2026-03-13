# Experiment: Oncology Standard

**Status:** Completed
**Started:** 2026-03-11 15:22:38  
**Duration:** 7 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** oncology

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
  _target_: cotlab.datasets.OncologyDataset
  name: oncology
  path: data/oncology.json
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
  dataset=oncology
```

## Results

- **Accuracy:** 0.0%
- **Samples Processed:** 1
- **Dataset:** oncology
- **Target Layer:** 61
- **Num Samples:** 100
- **Auroc L2 Norm:** None
- **Auroc Logit Entropy:** None
- **Norm Threshold Tau:** 30812.132
- **Balanced Acc At Tau:** 0.000
- **Mean Norm Correct:** 0.000
- **Mean Norm Incorrect:** 30812.132
- **Mean Entropy Correct:** 0.000
- **Mean Entropy Incorrect:** 0.761

