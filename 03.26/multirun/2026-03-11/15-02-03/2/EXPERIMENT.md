# Experiment: Medmcqa Standard

**Status:** Completed
**Started:** 2026-03-11 15:07:58  
**Duration:** 4 minutes 32 seconds

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
  dataset=medmcqa
```

## Results

- **Accuracy:** 63.6%
- **Samples Processed:** 1
- **Dataset:** medmcqa
- **Target Layer:** 61
- **Num Samples:** 4183
- **Auroc L2 Norm:** 0.594
- **Auroc Logit Entropy:** 0.728
- **Norm Threshold Tau:** 30825.034
- **Balanced Acc At Tau:** 0.574
- **Mean Norm Correct:** 29801.968
- **Mean Norm Incorrect:** 28324.361
- **Mean Entropy Correct:** 0.554
- **Mean Entropy Incorrect:** 0.826

