# Experiment: Radiology Standard Zero-Shot

**Status:** Completed
**Started:** 2026-01-10 18:27:39  
**Duration:** 10 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
**Output Format:** JSON
**Dataset:** radiology

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
  _target_: cotlab.prompts.RadiologyPromptStrategy
  name: radiology
  contrarian: false
  few_shot: false
  answer_first: false
  output_format: json
dataset:
  _target_: cotlab.datasets.RadiologyDataset
  name: radiology
  path: data/radiology.json
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
  prompt=radiology \
  prompt.few_shot=false \
  dataset=radiology
```

## Results

- **Accuracy:** 53.0%
- **Samples Processed:** 100
- **Correct:** 53
- **Incorrect:** 47
- **True Positives:** 3
- **True Negatives:** 50
- **False Positives:** 0
- **False Negatives:** 47
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 1.000
- **Recall:** 0.060
- **F1:** 0.113

