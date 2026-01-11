# Experiment: Histopathology Answer-First

**Status:** Completed
**Started:** 2026-01-10 20:39:36  
**Duration:** 1 minutes 24 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Histopathology
**Reasoning Mode:** Answer-First
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
  answer_first: true
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
  prompt.answer_first=true \
  dataset=histopathology
```

## Results

- **Accuracy:** 19.5%
- **Samples Processed:** 600
- **Correct:** 117
- **Incorrect:** 483
- **True Positives:** 91
- **True Negatives:** 26
- **False Positives:** 482
- **False Negatives:** 1
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.159
- **Recall:** 0.989
- **F1:** 0.274

