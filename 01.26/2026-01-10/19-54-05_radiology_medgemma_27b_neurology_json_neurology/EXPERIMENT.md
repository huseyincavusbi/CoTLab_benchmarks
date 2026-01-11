# Experiment: Neurology Standard Zero-Shot

**Status:** Completed
**Started:** 2026-01-10 19:54:05  
**Duration:** 4 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Neurology
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
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
  name: google/medgemma-27b-text-it
  variant: 27b
  max_new_tokens: 1024
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b
prompt:
  _target_: cotlab.prompts.NeurologyPromptStrategy
  name: neurology
  contrarian: false
  few_shot: false
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
  prompt.few_shot=false \
  dataset=neurology
```

## Results

- **Accuracy:** 50.0%
- **Samples Processed:** 100
- **Correct:** 50
- **Incorrect:** 50
- **True Positives:** 0
- **True Negatives:** 50
- **False Positives:** 0
- **False Negatives:** 50
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0
- **Recall:** 0.000
- **F1:** 0

