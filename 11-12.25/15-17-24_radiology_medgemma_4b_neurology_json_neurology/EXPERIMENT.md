# Experiment: Neurology Standard

**Status:** Completed
**Started:** 2026-01-09 15:17:24  
**Duration:** 10 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Neurology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** neurology

<details>
<summary>Full Configuration (YAML)</summary>

```yaml
backend:
  _target_: cotlab.backends.VLLMBackend
  tensor_parallel_size: 1
  dtype: bfloat16
  trust_remote_code: true
  max_model_len: 4096
model:
  name: google/medgemma-4b-it
  variant: 4b
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_4b
prompt:
  _target_: cotlab.prompts.NeurologyPromptStrategy
  name: neurology
  contrarian: false
  few_shot: true
  answer_first: false
  output_format: json
dataset:
  _target_: cotlab.datasets.NeurologyDataset
  name: neurology
  path: data/neurology.json
experiment:
  _target_: cotlab.experiments.RadiologyExperiment
  name: radiology
  description: Pathological fracture detection from radiology reports
  num_samples: -1
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  prompt=neurology \
  dataset=neurology
```

## Results

- **Accuracy:** 87.0%
- **Samples Processed:** 100
- **Correct:** 87
- **Incorrect:** 13
- **True Positives:** 50
- **True Negatives:** 37
- **False Positives:** 13
- **False Negatives:** 0
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.794
- **Recall:** 1.000
- **F1:** 0.885

