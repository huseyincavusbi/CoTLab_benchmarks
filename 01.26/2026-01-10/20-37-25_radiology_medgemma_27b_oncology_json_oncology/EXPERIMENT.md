# Experiment: Oncology Answer-First

**Status:** Completed
**Started:** 2026-01-10 20:37:26  
**Duration:** 12 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Oncology
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** oncology

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
  _target_: cotlab.prompts.OncologyPromptStrategy
  name: oncology
  contrarian: false
  few_shot: true
  answer_first: true
  output_format: json
dataset:
  _target_: cotlab.datasets.OncologyDataset
  name: oncology
  path: data/oncology.json
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
  prompt=oncology \
  prompt.answer_first=true \
  dataset=oncology
```

## Results

- **Accuracy:** 100.0%
- **Samples Processed:** 100
- **Correct:** 100
- **Incorrect:** 0
- **True Positives:** 50
- **True Negatives:** 50
- **False Positives:** 0
- **False Negatives:** 0
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 1.000
- **Recall:** 1.000
- **F1:** 1.000

