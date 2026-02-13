# Experiment: M_arc Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-09 11:56:51  
**Duration:** 3 minutes 23 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
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
  answer_first: true
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
  num_samples: 50
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=50 \
  prompt=mcq \
  prompt.answer_first=true \
  prompt.few_shot=false \
  dataset=m_arc
```

## Results

- **Accuracy:** 26.0%
- **Samples Processed:** 50
- **Correct:** 13
- **Incorrect:** 37
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.2, 'recall': 0.25, 'f1-score': 0.2222222222222222, 'support': 8.0}, 'B': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 5.0}, 'C': {'precision': 0.4, 'recall': 0.2857142857142857, 'f1-score': 0.3333333333333333, 'support': 7.0}, 'D': {'precision': 0.2727272727272727, 'recall': 0.15789473684210525, 'f1-score': 0.2, 'support': 19.0}, 'E': {'precision': 0.375, 'recall': 0.5454545454545454, 'f1-score': 0.4444444444444444, 'support': 11.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.26, 'macro avg': {'precision': 0.17824675324675326, 'recall': 0.17700908114441946, 'f1-score': 0.17142857142857143, 'support': 50.0}, 'weighted avg': {'precision': 0.2741363636363636, 'recall': 0.26, 'f1-score': 0.256, 'support': 50.0}}
- **Macro Precision:** 0.178
- **Macro Recall:** 0.177
- **Macro F1:** 0.171
- **Weighted F1:** 0.256
- **Confusion Matrix:** [[2, 2, 0, 1, 2, 0, 1], [1, 0, 1, 3, 0, 0, 0], [0, 0, 2, 3, 2, 0, 0], [4, 2, 2, 3, 6, 2, 0], [3, 1, 0, 1, 6, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'T', 'X']
- **Top Confused Pairs:** [('D', 'E', 6), ('D', 'A', 4), ('B', 'D', 3), ('C', 'D', 3), ('E', 'A', 3), ('A', 'B', 2), ('A', 'E', 2), ('C', 'E', 2), ('D', 'B', 2), ('D', 'C', 2)]
- **True Class Distribution:** {'E': 11, 'C': 7, 'D': 19, 'A': 8, 'B': 5}
- **Pred Class Distribution:** {'A': 10, 'C': 5, 'E': 16, 'D': 11, 'B': 5, 'T': 2, 'X': 1}
- **Num Classes:** 7

