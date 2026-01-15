# Experiment: Radiology Standard (TOON)

**Status:** Completed
**Started:** 2026-01-13 13:16:13  
**Duration:** 5 seconds

## Research Questions

1. How does TOON output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** TOON
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
  few_shot: true
  answer_first: false
  output_format: toon
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
  prompt.output_format=toon \
  dataset=radiology
```

## Results

- **Accuracy:** 99.0%
- **Samples Processed:** 100
- **Correct:** 99
- **Incorrect:** 1
- **True Positives:** 49
- **True Negatives:** 50
- **False Positives:** 0
- **False Negatives:** 1
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 1.000
- **Recall:** 0.980
- **F1:** 0.990

