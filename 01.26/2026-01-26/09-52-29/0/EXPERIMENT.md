# Experiment: Radiology Answer-First

**Status:** Completed
**Started:** 2026-01-26 09:52:29  
**Duration:** 15 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Answer-First
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
  max_model_len: null
  quantization: null
  gpu_memory_utilization: 0.9
  enforce_eager: false
  limit_mm_per_prompt: null
model:
  name: google/medgemma-27b-text-it
  variant: 27b-text
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b_text_it
prompt:
  _target_: cotlab.prompts.RadiologyPromptStrategy
  name: radiology
  contrarian: false
  few_shot: true
  answer_first: true
  output_format: json
dataset:
  _target_: cotlab.datasets.RadiologyDataset
  name: radiology
  path: data/radiology.json
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: -1
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=-1 \
  prompt=radiology \
  prompt.answer_first=true \
  dataset=radiology
```

## Results

- **Accuracy:** 99.0%
- **Samples Processed:** 100
- **Correct:** 99
- **Incorrect:** 1
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **True Positives:** 49
- **True Negatives:** 50
- **False Positives:** 0
- **False Negatives:** 1
- **Precision:** 1.000
- **Recall:** 0.980
- **F1:** 0.990

