# Experiment: Radiology Contrarian

**Status:** Completed
**Started:** 2026-01-10 19:15:10  
**Duration:** 11 seconds

## Research Questions

1. Does skeptical/contrarian reasoning improve diagnostic accuracy?

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Contrarian (skeptical)
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** radiology

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
  _target_: cotlab.prompts.RadiologyPromptStrategy
  name: radiology
  contrarian: true
  few_shot: true
  answer_first: false
  output_format: json
dataset:
  _target_: cotlab.datasets.RadiologyDataset
  name: radiology
  path: data/radiology.json
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
  prompt=radiology \
  prompt.contrarian=true \
  dataset=radiology
```

## Results

- **Accuracy:** 98.0%
- **Samples Processed:** 100
- **Correct:** 96
- **Incorrect:** 2
- **True Positives:** 46
- **True Negatives:** 50
- **False Positives:** 0
- **False Negatives:** 2
- **Parse Errors:** 2
- **Parse Error Rate:** 0.020
- **Precision:** 1.000
- **Recall:** 0.958
- **F1:** 0.979

