# Experiment: M_arc Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-09 13:23:23  
**Duration:** 5 minutes 51 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
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
  few_shot: false
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
  num_samples: 100
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=100 \
  prompt=mcq \
  prompt.few_shot=false \
  dataset=m_arc
```

## Results

- **Accuracy:** 22.4%
- **Samples Processed:** 100
- **Correct:** 22
- **Incorrect:** 76
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.08333333333333333, 'recall': 0.14285714285714285, 'f1-score': 0.10526315789473684, 'support': 14.0}, 'B': {'precision': 0.09090909090909091, 'recall': 0.1, 'f1-score': 0.09523809523809523, 'support': 10.0}, 'C': {'precision': 0.2777777777777778, 'recall': 0.2777777777777778, 'f1-score': 0.2777777777777778, 'support': 18.0}, 'D': {'precision': 0.32, 'recall': 0.24242424242424243, 'f1-score': 0.27586206896551724, 'support': 33.0}, 'E': {'precision': 0.375, 'recall': 0.2857142857142857, 'f1-score': 0.32432432432432434, 'support': 21.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 2.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.22448979591836735, 'macro avg': {'precision': 0.14337752525252526, 'recall': 0.1310966810966811, 'f1-score': 0.13480817802505643, 'support': 98.0}, 'weighted avg': {'precision': 0.26031385281385283, 'recall': 0.22448979591836735, 'f1-score': 0.23816657397530763, 'support': 98.0}}
- **Macro Precision:** 0.143
- **Macro Recall:** 0.131
- **Macro F1:** 0.135
- **Weighted F1:** 0.238
- **Confusion Matrix:** [[2, 1, 3, 4, 1, 1, 2, 0], [2, 1, 3, 4, 0, 0, 0, 0], [7, 3, 5, 2, 1, 0, 0, 0], [8, 5, 3, 8, 8, 0, 0, 1], [3, 1, 4, 7, 6, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'K']
- **Top Confused Pairs:** [('D', 'A', 8), ('D', 'E', 8), ('C', 'A', 7), ('E', 'D', 7), ('D', 'B', 5), ('A', 'D', 4), ('B', 'D', 4), ('E', 'C', 4), ('A', 'C', 3), ('B', 'C', 3)]
- **True Class Distribution:** {'E': 21, 'D': 33, 'C': 18, 'B': 10, 'A': 14, 'F': 2}
- **Pred Class Distribution:** {'E': 16, 'C': 18, 'K': 1, 'D': 25, 'A': 24, 'B': 11, 'G': 2, 'F': 1}
- **Num Classes:** 8

