# Experiment: Radiology Contrarian Zero-Shot

**Status:** Completed
**Started:** 2026-01-10 18:49:41  
**Duration:** 10 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does skeptical/contrarian reasoning improve diagnostic accuracy?

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Contrarian (skeptical)
**Few-Shot Examples:** No (zero-shot)
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
  few_shot: false
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
  prompt.few_shot=false \
  dataset=radiology
```

## Results

- **Accuracy:** 64.6%
- **Samples Processed:** 100
- **Correct:** 64
- **Incorrect:** 35
- **True Positives:** 16
- **True Negatives:** 48
- **False Positives:** 2
- **False Negatives:** 33
- **Parse Errors:** 1
- **Parse Error Rate:** 0.010
- **Precision:** 0.889
- **Recall:** 0.327
- **F1:** 0.478

