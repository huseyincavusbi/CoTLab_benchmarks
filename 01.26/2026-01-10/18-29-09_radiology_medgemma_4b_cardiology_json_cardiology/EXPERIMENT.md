# Experiment: Cardiology Standard Zero-Shot

**Status:** Completed
**Started:** 2026-01-10 18:29:09  
**Duration:** 9 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Cardiology
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
**Output Format:** JSON
**Dataset:** cardiology

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
  _target_: cotlab.prompts.CardiologyPromptStrategy
  name: cardiology
  contrarian: false
  few_shot: false
  answer_first: false
  output_format: json
dataset:
  _target_: cotlab.datasets.CardiologyDataset
  name: cardiology
  path: data/cardiology.json
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
  prompt=cardiology \
  prompt.few_shot=false \
  dataset=cardiology
```

## Results

- **Accuracy:** 54.0%
- **Samples Processed:** 100
- **Correct:** 54
- **Incorrect:** 46
- **True Positives:** 20
- **True Negatives:** 34
- **False Positives:** 17
- **False Negatives:** 29
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.541
- **Recall:** 0.408
- **F1:** 0.465

