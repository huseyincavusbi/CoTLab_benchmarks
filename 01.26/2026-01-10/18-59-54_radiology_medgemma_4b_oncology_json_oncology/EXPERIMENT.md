# Experiment: Oncology Contrarian Zero-Shot

**Status:** Completed
**Started:** 2026-01-10 18:59:54  
**Duration:** 9 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does skeptical/contrarian reasoning improve diagnostic accuracy?

## Configuration

**Prompt Strategy:** Oncology
**Reasoning Mode:** Contrarian (skeptical)
**Few-Shot Examples:** No (zero-shot)
**Output Format:** JSON
**Dataset:** oncology

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
  _target_: cotlab.prompts.OncologyPromptStrategy
  name: oncology
  contrarian: true
  few_shot: false
  answer_first: false
  output_format: json
dataset:
  _target_: cotlab.datasets.OncologyDataset
  name: oncology
  path: data/oncology.json
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
  prompt=oncology \
  prompt.contrarian=true \
  prompt.few_shot=false \
  dataset=oncology
```

## Results

- **Accuracy:** 52.1%
- **Samples Processed:** 100
- **Correct:** 50
- **Incorrect:** 46
- **True Positives:** 0
- **True Negatives:** 50
- **False Positives:** 0
- **False Negatives:** 46
- **Parse Errors:** 4
- **Parse Error Rate:** 0.040
- **Precision:** 0
- **Recall:** 0.000
- **F1:** 0

