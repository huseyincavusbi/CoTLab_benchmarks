# Experiment: Afrimedqa Standard

**Status:** Completed
**Started:** 2026-03-11 15:28:27  
**Duration:** 5 minutes 26 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
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
  name: afrimedqa
  filename: afrimedqa/mcq.jsonl
  split: mcq
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
  dataset=afrimedqa
```

## Results

- **Accuracy:** 70.0%
- **Samples Processed:** 2
- **Dataset:** afrimedqa
- **Norm Layer:** 61
- **Attn Layer:** 3
- **Num Samples:** 3958
- **Calibration N:** 1187
- **Auroc Mahalanobis:** 0.501
- **Spearman Rho Score Vs Acc:** 0.013
- **Spearman P:** 0.434
- **Mean Score Correct:** 1.277
- **Mean Score Incorrect:** 1.280
- **Accuracy By Bin:** [{'bin': 1, 'score_range': [0.0121, 0.703], 'n': 792, 'accuracy': 0.7071}, {'bin': 2, 'score_range': [0.703, 1.0728], 'n': 791, 'accuracy': 0.7105}, {'bin': 3, 'score_range': [1.0728, 1.4094], 'n': 792, 'accuracy': 0.6881}, {'bin': 4, 'score_range': [1.4094, 1.7887], 'n': 791, 'accuracy': 0.6928}, {'bin': 5, 'score_range': [1.7887, 8.4306], 'n': 792, 'accuracy': 0.7008}]

