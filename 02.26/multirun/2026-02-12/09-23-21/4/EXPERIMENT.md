# Experiment: M_arc Standard

**Status:** Completed
**Started:** 2026-02-12 10:03:04  
**Duration:** 1 minutes 21 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** m_arc

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
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: true
  output_format: json
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MARCDataset
  name: m_arc
  filename: m_arc/test-00000-of-00001.parquet
  split: test
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
  prompt=mcq \
  dataset=m_arc
```

## Results

- **Accuracy:** 25.6%
- **Samples Processed:** 100
- **Correct:** 23
- **Incorrect:** 67
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.2, 'recall': 0.35714285714285715, 'f1-score': 0.2564102564102564, 'support': 14.0}, 'B': {'precision': 0.16666666666666666, 'recall': 0.2, 'f1-score': 0.18181818181818182, 'support': 10.0}, 'C': {'precision': 0.18181818181818182, 'recall': 0.13333333333333333, 'f1-score': 0.15384615384615385, 'support': 15.0}, 'D': {'precision': 0.42105263157894735, 'recall': 0.27586206896551724, 'f1-score': 0.3333333333333333, 'support': 29.0}, 'E': {'precision': 0.3333333333333333, 'recall': 0.25, 'f1-score': 0.2857142857142857, 'support': 20.0}, 'F': {'precision': 1.0, 'recall': 0.5, 'f1-score': 0.6666666666666666, 'support': 2.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.25555555555555554, 'macro avg': {'precision': 0.23028708133971293, 'recall': 0.17163382594417076, 'f1-score': 0.1877788877788878, 'support': 90.0}, 'weighted avg': {'precision': 0.31190147084883924, 'recall': 0.25555555555555554, 'f1-score': 0.27144337144337144, 'support': 90.0}}
- **Macro Precision:** 0.230
- **Macro Recall:** 0.172
- **Macro F1:** 0.188
- **Weighted F1:** 0.271
- **Confusion Matrix:** [[5, 1, 3, 2, 2, 0, 0, 0, 0, 1], [1, 2, 2, 3, 1, 0, 1, 0, 0, 0], [5, 1, 2, 2, 4, 0, 0, 1, 0, 0], [10, 4, 3, 8, 3, 0, 0, 0, 1, 0], [3, 4, 1, 4, 5, 0, 2, 1, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'I', 'K', 'V', 'X']
- **Top Confused Pairs:** [('D', 'A', 10), ('C', 'A', 5), ('C', 'E', 4), ('D', 'B', 4), ('E', 'B', 4), ('E', 'D', 4), ('A', 'C', 3), ('B', 'D', 3), ('D', 'C', 3), ('D', 'E', 3)]
- **True Class Distribution:** {'E': 20, 'D': 29, 'C': 15, 'B': 10, 'A': 14, 'F': 2}
- **Pred Class Distribution:** {'E': 15, 'A': 25, 'K': 2, 'V': 1, 'D': 19, 'C': 11, 'B': 12, 'I': 3, 'F': 1, 'X': 1}
- **Num Classes:** 10

