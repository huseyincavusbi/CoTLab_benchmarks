# Experiment: Tcga Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-01-24 13:30:05  
**Duration:** 2 minutes 8 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Tcga
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** No (zero-shot)
**Output Format:** JSON
**Dataset:** tcga

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
  _target_: cotlab.prompts.tcga.TCGAPromptStrategy
  name: tcga
  few_shot: false
  answer_first: true
  contrarian: false
  output_format: json
dataset:
  _target_: cotlab.datasets.loaders.TCGADataset
  name: tcga
  reports_filename: tcga/TCGA_Reports.csv
  labels_filename: tcga/tcga_patient_to_cancer_type.csv
  split: test
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
  prompt=tcga \
  prompt.answer_first=true \
  prompt.few_shot=false \
  dataset=tcga
```

## Results

- **Accuracy:** 0.0%
- **Samples Processed:** 20
- **Correct:** 0
- **Incorrect:** 0
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **True Positives:** 0
- **True Negatives:** 0
- **False Positives:** 0
- **False Negatives:** 0
- **Precision:** 0
- **Recall:** 0
- **F1:** 0

