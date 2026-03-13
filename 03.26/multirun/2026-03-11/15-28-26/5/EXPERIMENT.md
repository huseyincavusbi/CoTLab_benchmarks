# Experiment: Mmlu_medical Standard

**Status:** Completed
**Started:** 2026-03-11 15:47:45  
**Duration:** 53 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** mmlu_medical

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
  _target_: cotlab.datasets.loaders.MMLUMedicalDataset
  name: mmlu_medical
  filename: mmlu/medical_test.jsonl
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
  dataset=mmlu_medical
```

## Results

- **Accuracy:** 82.3%
- **Samples Processed:** 2
- **Dataset:** mmlu_medical
- **Norm Layer:** 61
- **Attn Layer:** 3
- **Num Samples:** 644
- **Calibration N:** 193
- **Auroc Mahalanobis:** 0.560
- **Spearman Rho Score Vs Acc:** -0.265
- **Spearman P:** 0.000
- **Mean Score Correct:** 1.254
- **Mean Score Incorrect:** 1.407
- **Accuracy By Bin:** [{'bin': 1, 'score_range': [0.0638, 0.7445], 'n': 129, 'accuracy': 0.845}, {'bin': 2, 'score_range': [0.7445, 1.0292], 'n': 129, 'accuracy': 0.8372}, {'bin': 3, 'score_range': [1.0292, 1.3793], 'n': 128, 'accuracy': 0.8828}, {'bin': 4, 'score_range': [1.3793, 1.8359], 'n': 129, 'accuracy': 0.7597}, {'bin': 5, 'score_range': [1.8359, 3.2007], 'n': 129, 'accuracy': 0.7907}]

