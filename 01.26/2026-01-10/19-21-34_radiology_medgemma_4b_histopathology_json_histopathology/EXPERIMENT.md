# Experiment: Histopathology Contrarian

**Status:** Completed
**Started:** 2026-01-10 19:21:34  
**Duration:** 44 seconds

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

- **Accuracy:** 58.7%
- **Samples Processed:** 600
- **Correct:** 352
- **Incorrect:** 248
- **True Positives:** 6
- **True Negatives:** 346
- **False Positives:** 34
- **False Negatives:** 214
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.150
- **Recall:** 0.027
- **F1:** 0.046

