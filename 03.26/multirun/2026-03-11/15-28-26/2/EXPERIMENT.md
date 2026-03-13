# Experiment: Medmcqa Standard

**Status:** Completed
**Started:** 2026-03-11 15:34:46  
**Duration:** 5 minutes 46 seconds

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
  dataset=medmcqa
```

## Results

- **Accuracy:** 63.9%
- **Samples Processed:** 2
- **Dataset:** medmcqa
- **Norm Layer:** 61
- **Attn Layer:** 3
- **Num Samples:** 4183
- **Calibration N:** 1254
- **Auroc Mahalanobis:** 0.496
- **Spearman Rho Score Vs Acc:** 0.020
- **Spearman P:** 0.189
- **Mean Score Correct:** 1.221
- **Mean Score Incorrect:** 1.204
- **Accuracy By Bin:** [{'bin': 1, 'score_range': [0.0195, 0.6717], 'n': 837, 'accuracy': 0.6069}, {'bin': 2, 'score_range': [0.6717, 1.01], 'n': 836, 'accuracy': 0.6543}, {'bin': 3, 'score_range': [1.01, 1.3204], 'n': 837, 'accuracy': 0.6655}, {'bin': 4, 'score_range': [1.3204, 1.6905], 'n': 836, 'accuracy': 0.6411}, {'bin': 5, 'score_range': [1.6905, 13.5016], 'n': 837, 'accuracy': 0.626}]

