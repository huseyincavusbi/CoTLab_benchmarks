# Experiment: Radiology Standard Zero-Shot (YAML)

**Status:** Completed
**Started:** 2026-01-13 13:21:15  
**Duration:** 21 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. How does YAML output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
**Output Format:** YAML
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
  name: google/medgemma-27b-text-it
  variant: 27b-text
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b_text_it
prompt:
  _target_: cotlab.prompts.RadiologyPromptStrategy
  name: radiology
  contrarian: false
  few_shot: false
  answer_first: false
  output_format: yaml
dataset:
  _target_: cotlab.datasets.RadiologyDataset
  name: radiology
  path: data/radiology.json
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
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
  prompt.output_format=yaml \
  dataset=radiology
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

