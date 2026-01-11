# Experiment: Cardiology Contrarian

**Status:** Completed
**Started:** 2026-01-10 19:17:06  
**Duration:** 11 seconds

## Research Questions

1. Does skeptical/contrarian reasoning improve diagnostic accuracy?

## Configuration

**Prompt Strategy:** Cardiology
**Reasoning Mode:** Contrarian (skeptical)
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** cardiology

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
  _target_: cotlab.prompts.CardiologyPromptStrategy
  name: cardiology
  contrarian: true
  few_shot: true
  answer_first: false
  output_format: json
dataset:
  _target_: cotlab.datasets.CardiologyDataset
  name: cardiology
  path: data/cardiology.json
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
  prompt=cardiology \
  prompt.contrarian=true \
  dataset=cardiology
```

## Results

- **Accuracy:** 100.0%
- **Samples Processed:** 100
- **Correct:** 94
- **Incorrect:** 0
- **True Positives:** 46
- **True Negatives:** 48
- **False Positives:** 0
- **False Negatives:** 0
- **Parse Errors:** 6
- **Parse Error Rate:** 0.060
- **Precision:** 1.000
- **Recall:** 1.000
- **F1:** 1.000

