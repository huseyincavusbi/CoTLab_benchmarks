# Experiment: Tcga Answer-First

**Status:** Completed
**Started:** 2026-01-24 13:26:27  
**Duration:** 2 minutes 9 seconds

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

- **Accuracy:** 30.0%
- **Samples Processed:** 20
- **Correct:** 6
- **Incorrect:** 14
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'BLCA': {'precision': 1.0, 'recall': 0.3333333333333333, 'f1-score': 0.5, 'support': 3.0}, 'BRCA': {'precision': 1.0, 'recall': 0.3333333333333333, 'f1-score': 0.5, 'support': 3.0}, 'CCRC': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'CESC': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'COAD': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'HNSC': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'KICH': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'KIRC': {'precision': 0.5, 'recall': 1.0, 'f1-score': 0.6666666666666666, 'support': 1.0}, 'LUAD': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'LUSC': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'PCPG': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'PRAD': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'SARC': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'SCC': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'STAD': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'THCA': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 1.0}, 'THYM': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 1.0}, 'UCEC': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 1.0}, 'UROS': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.3, 'macro avg': {'precision': 0.2894736842105263, 'recall': 0.24561403508771926, 'f1-score': 0.24561403508771926, 'support': 20.0}, 'weighted avg': {'precision': 0.475, 'recall': 0.3, 'f1-score': 0.3333333333333333, 'support': 20.0}}
- **Macro Precision:** 0.289
- **Macro Recall:** 0.246
- **Macro F1:** 0.246
- **Weighted F1:** 0.333
- **Confusion Matrix:** [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['BLCA', 'BRCA', 'CCRC', 'CESC', 'COAD', 'HNSC', 'KICH', 'KIRC', 'LUAD', 'LUSC', 'PCPG', 'PRAD', 'SARC', 'SCC', 'STAD', 'THCA', 'THYM', 'UCEC', 'UROS']
- **Top Confused Pairs:** [('BLCA', 'UROS', 2), ('BRCA', 'LUAD', 2), ('HNSC', 'LUAD', 2), ('CESC', 'CCRC', 1), ('COAD', 'LUAD', 1), ('HNSC', 'SCC', 1), ('KICH', 'KIRC', 1), ('LUSC', 'LUAD', 1), ('PRAD', 'PCPG', 1), ('SARC', 'PRAD', 1)]
- **True Class Distribution:** {'THYM': 1, 'CESC': 1, 'BLCA': 3, 'KIRC': 1, 'KICH': 1, 'HNSC': 3, 'COAD': 1, 'BRCA': 3, 'UCEC': 1, 'SARC': 1, 'STAD': 1, 'LUSC': 1, 'PRAD': 1, 'THCA': 1}
- **Pred Class Distribution:** {'THYM': 1, 'CCRC': 1, 'UROS': 2, 'KIRC': 2, 'SCC': 1, 'LUAD': 7, 'BRCA': 1, 'UCEC': 1, 'PRAD': 1, 'BLCA': 1, 'PCPG': 1, 'THCA': 1}
- **Num Classes:** 19

