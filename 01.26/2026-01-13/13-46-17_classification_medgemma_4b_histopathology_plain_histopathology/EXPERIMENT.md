# Experiment: Histopathology Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-13 13:46:17  
**Duration:** 48 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Histopathology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
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
  output_format: plain
  few_shot: true
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.HistopathologyDataset
  name: histopathology
  path: data/histopathology.tsv
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
  prompt=histopathology \
  prompt.output_format=plain \
  dataset=histopathology
```

## Results

- **Accuracy:** 61.3%
- **Samples Processed:** 600
- **Correct:** 368
- **Incorrect:** 232
- **True Positives:** 15
- **True Negatives:** 353
- **False Positives:** 70
- **False Negatives:** 162
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.176
- **Recall:** 0.085
- **F1:** 0.115

