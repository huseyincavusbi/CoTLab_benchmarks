# Experiment: Histopathology Contrarian Zero-Shot

**Status:** Completed
**Started:** 2026-01-10 18:54:50  
**Duration:** 44 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does skeptical/contrarian reasoning improve diagnostic accuracy?

## Configuration

**Prompt Strategy:** Histopathology
**Reasoning Mode:** Contrarian (skeptical)
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
  few_shot: false
  answer_first: false
  contrarian: true
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
  prompt.contrarian=true \
  prompt.few_shot=false \
  dataset=histopathology
```

## Results

- **Accuracy:** 57.8%
- **Samples Processed:** 600
- **Correct:** 347
- **Incorrect:** 253
- **True Positives:** 5
- **True Negatives:** 342
- **False Positives:** 43
- **False Negatives:** 210
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.104
- **Recall:** 0.023
- **F1:** 0.038

