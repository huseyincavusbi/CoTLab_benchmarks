# Experiment: Radiology Answer-First

**Status:** Completed
**Started:** 2026-01-24 13:02:42  
**Duration:** 2 minutes 0 seconds

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
  max_model_len: 8192
  quantization: bitsandbytes
  gpu_memory_utilization: 0.7
  enforce_eager: true
  limit_mm_per_prompt:
    image: 0
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
  num_samples: 20
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=20 \
  prompt=radiology \
  prompt.answer_first=true \
  dataset=radiology
```

## Results

- **Accuracy:** 100.0%
- **Samples Processed:** 20
- **Correct:** 20
- **Incorrect:** 0
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **True Positives:** 11
- **True Negatives:** 9
- **False Positives:** 0
- **False Negatives:** 0
- **Precision:** 1.000
- **Recall:** 1.000
- **F1:** 1.000

