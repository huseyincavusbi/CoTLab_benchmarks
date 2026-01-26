# Experiment: Tcga Answer-First

**Status:** Running
**Started:** 2026-01-24 13:15:37

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Tcga
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
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
  few_shot: true
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
  dataset=tcga
```

## Results

_Results will be added after experiment completes..._
