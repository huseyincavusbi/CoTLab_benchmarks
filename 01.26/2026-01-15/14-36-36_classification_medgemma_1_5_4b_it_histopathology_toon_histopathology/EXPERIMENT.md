# Experiment: Histopathology Standard Zero-Shot (TOON)

**Status:** Completed
**Started:** 2026-01-15 14:36:36  
**Duration:** 36 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. How does TOON output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Histopathology
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
**Output Format:** TOON
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
  name: google/medgemma-1.5-4b-it
  variant: 4b
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_1_5_4b_it
prompt:
  _target_: cotlab.prompts.HistopathologyPromptStrategy
  name: histopathology
  output_format: toon
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
  prompt.output_format=toon \
  dataset=histopathology
```

## Results

- **Accuracy:** 16.7%
- **Samples Processed:** 600
- **Correct:** 93
- **Incorrect:** 464
- **True Positives:** 73
- **True Negatives:** 20
- **False Positives:** 450
- **False Negatives:** 14
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.140
- **Recall:** 0.839
- **F1:** 0.239

