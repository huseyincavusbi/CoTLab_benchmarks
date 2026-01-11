# Experiment: Neurology Contrarian

**Status:** Completed
**Started:** 2026-01-10 19:18:29  
**Duration:** 10 seconds

## Research Questions

1. Does skeptical/contrarian reasoning improve diagnostic accuracy?

## Configuration

**Prompt Strategy:** Neurology
**Reasoning Mode:** Contrarian (skeptical)
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** neurology

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
  _target_: cotlab.prompts.NeurologyPromptStrategy
  name: neurology
  contrarian: true
  few_shot: true
  answer_first: false
  output_format: json
dataset:
  _target_: cotlab.datasets.NeurologyDataset
  name: neurology
  path: data/neurology.json
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
  prompt=neurology \
  prompt.contrarian=true \
  dataset=neurology
```

## Results

- **Accuracy:** 92.9%
- **Samples Processed:** 100
- **Correct:** 92
- **Incorrect:** 7
- **True Positives:** 49
- **True Negatives:** 43
- **False Positives:** 7
- **False Negatives:** 0
- **Parse Errors:** 1
- **Parse Error Rate:** 0.010
- **Precision:** 0.875
- **Recall:** 1.000
- **F1:** 0.933

