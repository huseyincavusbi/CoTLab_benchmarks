# Experiment: Histopathology Standard

**Status:** Completed
**Started:** 2026-01-10 19:44:43  
**Duration:** 2 minutes 27 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Histopathology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** histopathology

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
  _target_: cotlab.prompts.HistopathologyPromptStrategy
  name: histopathology
  output_format: json
  few_shot: true
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.HistopathologyDataset
  name: histopathology
  path: data/histopathology.tsv
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
  prompt=histopathology \
  dataset=histopathology
```

## Results

- **Accuracy:** 10.5%
- **Samples Processed:** 600
- **Correct:** 63
- **Incorrect:** 537
- **True Positives:** 57
- **True Negatives:** 6
- **False Positives:** 537
- **False Negatives:** 0
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.096
- **Recall:** 1.000
- **F1:** 0.175

