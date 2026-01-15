# Experiment: Histopathology Standard (MARKDOWN)

**Status:** Completed
**Started:** 2026-01-13 13:53:45  
**Duration:** 48 seconds

## Research Questions

1. How does MARKDOWN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Histopathology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** MARKDOWN
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
  output_format: markdown
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
  prompt.output_format=markdown \
  dataset=histopathology
```

## Results

- **Accuracy:** 61.8%
- **Samples Processed:** 600
- **Correct:** 371
- **Incorrect:** 229
- **True Positives:** 17
- **True Negatives:** 354
- **False Positives:** 79
- **False Negatives:** 150
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.177
- **Recall:** 0.102
- **F1:** 0.129

