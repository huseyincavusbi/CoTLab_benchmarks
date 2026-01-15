# Experiment: Histopathology Standard Zero-Shot

**Status:** Completed
**Started:** 2026-01-15 13:45:22  
**Duration:** 3 minutes 37 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Histopathology
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
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
  variant: 27b-text
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b_text_it
prompt:
  _target_: cotlab.prompts.HistopathologyPromptStrategy
  name: histopathology
  output_format: json
  few_shot: false
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
  prompt.few_shot=false \
  dataset=histopathology
```

## Results

- **Accuracy:** 30.1%
- **Samples Processed:** 600
- **Correct:** 178
- **Incorrect:** 413
- **True Positives:** 50
- **True Negatives:** 128
- **False Positives:** 345
- **False Negatives:** 68
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.127
- **Recall:** 0.424
- **F1:** 0.195

