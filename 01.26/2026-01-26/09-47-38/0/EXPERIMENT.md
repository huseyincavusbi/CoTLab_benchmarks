# Experiment: Histopathology Answer-First

**Status:** Completed
**Started:** 2026-01-26 09:47:38  
**Duration:** 1 minutes 17 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Histopathology
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** histopathology

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
  _target_: cotlab.prompts.HistopathologyPromptStrategy
  name: histopathology
  output_format: json
  few_shot: true
  answer_first: true
  contrarian: false
dataset:
  _target_: cotlab.datasets.HistopathologyDataset
  name: histopathology
  path: data/histopathology.tsv
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
  prompt=histopathology \
  prompt.answer_first=true \
  dataset=histopathology
```

## Results

- **Accuracy:** 60.8%
- **Samples Processed:** 600
- **Correct:** 365
- **Incorrect:** 235
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **True Positives:** 94
- **True Negatives:** 362
- **False Positives:** 7
- **False Negatives:** 137
- **Precision:** 0.931
- **Recall:** 0.407
- **F1:** 0.566

