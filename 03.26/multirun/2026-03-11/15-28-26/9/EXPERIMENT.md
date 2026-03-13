# Experiment: Oncology Standard

**Status:** Completed
**Started:** 2026-03-11 15:50:25  
**Duration:** 8 seconds

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
  _target_: cotlab.experiments.CompositeShiftDetectorExperiment
  name: composite_shift_detector
  description: L61 norm + L3 entropy Mahalanobis OOD detector
  norm_layer: null
  attn_layer: 3
  num_samples: null
  calibration_fraction: 0.3
  window_size: 20
  num_bins: 5
  seed: 42
  max_input_tokens: 1024
  answer_cue: '


    Answer:'
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=composite_shift_detector \
  experiment.seed=42 \
  prompt=chain_of_thought \
  dataset=oncology
```

## Results

- **Accuracy:** 0.0%
- **Samples Processed:** 2
- **Dataset:** oncology
- **Norm Layer:** 61
- **Attn Layer:** 3
- **Num Samples:** 100
- **Calibration N:** 30
- **Auroc Mahalanobis:** None
- **Spearman Rho Score Vs Acc:** None
- **Spearman P:** None
- **Mean Score Correct:** 0.000
- **Mean Score Incorrect:** 1.391
- **Accuracy By Bin:** [{'bin': 1, 'score_range': [0.1627, 0.8678], 'n': 20, 'accuracy': 0.0}, {'bin': 2, 'score_range': [0.8678, 1.2123], 'n': 20, 'accuracy': 0.0}, {'bin': 3, 'score_range': [1.2123, 1.5495], 'n': 20, 'accuracy': 0.0}, {'bin': 4, 'score_range': [1.5495, 1.8578], 'n': 20, 'accuracy': 0.0}, {'bin': 5, 'score_range': [1.8578, 3.4966], 'n': 20, 'accuracy': 0.0}]

