# Experiment: Cardiology Standard Zero-Shot

**Status:** Completed
**Started:** 2026-01-10 19:52:03  
**Duration:** 3 seconds

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
  name: google/medgemma-27b-text-it
  variant: 27b
  max_new_tokens: 1024
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b
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

- **Accuracy:** 86.0%
- **Samples Processed:** 100
- **Correct:** 86
- **Incorrect:** 14
- **True Positives:** 37
- **True Negatives:** 49
- **False Positives:** 1
- **False Negatives:** 13
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.974
- **Recall:** 0.740
- **F1:** 0.841

