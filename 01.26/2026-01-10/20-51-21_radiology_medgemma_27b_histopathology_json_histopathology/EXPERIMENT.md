# Experiment: Histopathology Contrarian

**Status:** Completed
**Started:** 2026-01-10 20:51:21  
**Duration:** 3 minutes 57 seconds

## Research Questions

1. Does skeptical/contrarian reasoning improve diagnostic accuracy?

## Configuration

**Prompt Strategy:** Histopathology
**Reasoning Mode:** Contrarian (skeptical)
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
  dataset=histopathology
```

## Results

- **Accuracy:** 47.8%
- **Samples Processed:** 600
- **Correct:** 287
- **Incorrect:** 313
- **True Positives:** 25
- **True Negatives:** 262
- **False Positives:** 187
- **False Negatives:** 126
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.118
- **Recall:** 0.166
- **F1:** 0.138

