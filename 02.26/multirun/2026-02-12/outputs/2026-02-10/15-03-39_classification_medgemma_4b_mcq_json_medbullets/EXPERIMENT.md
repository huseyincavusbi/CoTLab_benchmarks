# Experiment: Medbullets Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-10 15:03:39  
**Duration:** 6 minutes 26 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
**Output Format:** JSON
**Dataset:** medbullets

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
  max_new_tokens: 256
  temperature: 0
  top_p: 1
  safe_name: medgemma_4b
prompt:
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: false
  output_format: json
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MedBulletsDataset
  name: medbullets
  split: op5_test
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 308
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=308 \
  prompt=mcq \
  prompt.few_shot=false \
  dataset=medbullets
```

## Results

- **Accuracy:** 21.7%
- **Samples Processed:** 308
- **Correct:** 61
- **Incorrect:** 220
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.21674876847290642, 'recall': 0.7857142857142857, 'f1-score': 0.33976833976833976, 'support': 56.0}, 'B': {'precision': 0.2857142857142857, 'recall': 0.06060606060606061, 'f1-score': 0.1, 'support': 66.0}, 'C': {'precision': 0.13043478260869565, 'recall': 0.061224489795918366, 'f1-score': 0.08333333333333333, 'support': 49.0}, 'D': {'precision': 0.3333333333333333, 'recall': 0.06349206349206349, 'f1-score': 0.10666666666666667, 'support': 63.0}, 'E': {'precision': 0.2608695652173913, 'recall': 0.1276595744680851, 'f1-score': 0.17142857142857143, 'support': 47.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.21708185053380782, 'macro avg': {'precision': 0.13634452614962358, 'recall': 0.12207738600849037, 'f1-score': 0.08902187902187902, 'support': 281.0}, 'weighted avg': {'precision': 0.25141369325505014, 'recall': 0.21708185053380782, 'f1-score': 0.15831851678826767, 'support': 281.0}}
- **Macro Precision:** 0.136
- **Macro Recall:** 0.122
- **Macro F1:** 0.089
- **Weighted F1:** 0.158
- **Confusion Matrix:** [[44, 1, 3, 0, 8, 0, 0, 0, 0], [43, 4, 6, 6, 5, 0, 1, 0, 1], [40, 3, 3, 0, 1, 0, 1, 0, 1], [42, 4, 8, 4, 3, 1, 0, 1, 0], [34, 2, 3, 2, 6, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'I', 'V', 'X']
- **Top Confused Pairs:** [('B', 'A', 43), ('D', 'A', 42), ('C', 'A', 40), ('E', 'A', 34), ('A', 'E', 8), ('D', 'C', 8), ('B', 'C', 6), ('B', 'D', 6), ('B', 'E', 5), ('D', 'B', 4)]
- **True Class Distribution:** {'B': 66, 'E': 47, 'A': 56, 'C': 49, 'D': 63}
- **Pred Class Distribution:** {'A': 203, 'B': 14, 'C': 23, 'E': 23, 'D': 12, 'X': 2, 'V': 1, 'F': 1, 'I': 2}
- **Num Classes:** 9

