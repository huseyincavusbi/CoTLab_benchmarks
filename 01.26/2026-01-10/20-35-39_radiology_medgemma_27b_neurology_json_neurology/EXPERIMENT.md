# Experiment: Neurology Answer-First

**Status:** Completed
**Started:** 2026-01-10 20:35:39  
**Duration:** 11 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Neurology
**Reasoning Mode:** Answer-First
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
  name: google/medgemma-27b-text-it
  variant: 27b
  max_new_tokens: 1024
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b
prompt:
  _target_: cotlab.prompts.NeurologyPromptStrategy
  name: neurology
  contrarian: false
  few_shot: true
  answer_first: true
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
  prompt.answer_first=true \
  dataset=neurology
```

## Results

- **Accuracy:** 94.0%
- **Samples Processed:** 100
- **Correct:** 94
- **Incorrect:** 6
- **True Positives:** 50
- **True Negatives:** 44
- **False Positives:** 6
- **False Negatives:** 0
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Precision:** 0.893
- **Recall:** 1.000
- **F1:** 0.943

