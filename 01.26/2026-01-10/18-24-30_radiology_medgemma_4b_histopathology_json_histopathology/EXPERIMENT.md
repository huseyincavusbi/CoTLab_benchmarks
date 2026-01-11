# Experiment: Histopathology Standard

**Status:** Completed
**Started:** 2026-01-10 18:24:30  
**Duration:** 45 seconds

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
  name: google/medgemma-4b-it
  variant: 4b
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_4b
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

- **Accuracy:** 13.5%
- **Samples Processed:** 600
- **Correct:** 81
- **Incorrect:** 519
- **True Positives:** 75
- **True Negatives:** 6
- **False Positives:** 516
- **False Negatives:** 3
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.127
- **Recall:** 0.962
- **F1:** 0.224

