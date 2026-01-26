# Experiment: Mmlu_medical Answer-First

**Status:** Completed
**Started:** 2026-01-24 12:41:21  
**Duration:** 2 minutes 0 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** mmlu_medical

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
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: true
  output_format: json
  answer_first: true
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MMLUMedicalDataset
  name: mmlu_medical
  filename: mmlu/medical_test.jsonl
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
  prompt=mcq \
  prompt.answer_first=true \
  dataset=mmlu_medical
```

## Results

- **Accuracy:** 65.0%
- **Samples Processed:** 20
- **Correct:** 13
- **Incorrect:** 7
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.625, 'recall': 0.8333333333333334, 'f1-score': 0.7142857142857143, 'support': 6.0}, 'B': {'precision': 0.6666666666666666, 'recall': 0.4, 'f1-score': 0.5, 'support': 5.0}, 'C': {'precision': 0.6, 'recall': 0.6, 'f1-score': 0.6, 'support': 5.0}, 'D': {'precision': 0.75, 'recall': 0.75, 'f1-score': 0.75, 'support': 4.0}, 'accuracy': 0.65, 'macro avg': {'precision': 0.6604166666666667, 'recall': 0.6458333333333334, 'f1-score': 0.6410714285714286, 'support': 20.0}, 'weighted avg': {'precision': 0.6541666666666666, 'recall': 0.65, 'f1-score': 0.6392857142857142, 'support': 20.0}}
- **Macro Precision:** 0.660
- **Macro Recall:** 0.646
- **Macro F1:** 0.641
- **Weighted F1:** 0.639
- **Confusion Matrix:** [[5, 1, 0, 0], [2, 2, 1, 0], [1, 0, 3, 1], [0, 0, 1, 3]]
- **Class Labels:** ['A', 'B', 'C', 'D']
- **Top Confused Pairs:** [('B', 'A', 2), ('A', 'B', 1), ('B', 'C', 1), ('C', 'A', 1), ('C', 'D', 1), ('D', 'C', 1)]
- **True Class Distribution:** {'A': 6, 'C': 5, 'B': 5, 'D': 4}
- **Pred Class Distribution:** {'A': 8, 'D': 4, 'B': 3, 'C': 5}
- **Num Classes:** 4

