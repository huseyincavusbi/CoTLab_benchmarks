# Experiment: Oncology Contrarian Zero-Shot

**Status:** Completed
**Started:** 2026-01-10 20:22:08  
**Duration:** 57 seconds

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
  name: google/medgemma-27b-text-it
  variant: 27b
  max_new_tokens: 1024
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b
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

- **Accuracy:** 78.6%
- **Samples Processed:** 100
- **Correct:** 44
- **Incorrect:** 12
- **True Positives:** 0
- **True Negatives:** 44
- **False Positives:** 0
- **False Negatives:** 12
- **Parse Errors:** 44
- **Parse Error Rate:** 0.440
- **Precision:** 0
- **Recall:** 0.000
- **F1:** 0

