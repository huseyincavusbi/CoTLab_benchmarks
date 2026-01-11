# Experiment: Cardiology Standard

**Status:** Completed
**Started:** 2026-01-09 15:32:02  
**Duration:** 21 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Cardiology
**Reasoning Mode:** Standard
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
  name: google/medgemma-27b-text-it
  variant: 27b-text
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b_text_it
  use_chat_template: true
prompt:
  _target_: cotlab.prompts.CardiologyPromptStrategy
  name: cardiology
  contrarian: false
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
  dataset=cardiology
```

## Results

- **Accuracy:** 100.0%
- **Samples Processed:** 100
- **Correct:** 56
- **Incorrect:** 0
- **True Positives:** 24
- **True Negatives:** 32
- **False Positives:** 0
- **False Negatives:** 0
- **Parse Errors:** 44
- **Parse Error Rate:** 0.440
- **Precision:** 1.000
- **Recall:** 1.000
- **F1:** 1.000

