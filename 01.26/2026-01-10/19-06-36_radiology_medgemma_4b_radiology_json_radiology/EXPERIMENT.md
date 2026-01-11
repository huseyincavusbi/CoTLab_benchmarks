# Experiment: Radiology Answer-First

**Status:** Completed
**Started:** 2026-01-10 19:06:36  
**Duration:** 11 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
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
  few_shot: true
  answer_first: true
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
  prompt.answer_first=true \
  dataset=radiology
```

## Results

- **Accuracy:** 98.0%
- **Samples Processed:** 100
- **Correct:** 98
- **Incorrect:** 2
- **True Positives:** 49
- **True Negatives:** 49
- **False Positives:** 1
- **False Negatives:** 1
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.980
- **Recall:** 0.980
- **F1:** 0.980

