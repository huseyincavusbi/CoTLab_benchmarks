# Experiment: M_arc Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-12 10:07:49  
**Duration:** 1 minutes 23 seconds

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
  prompt.few_shot=false \
  dataset=m_arc
```

## Results

- **Accuracy:** 22.0%
- **Samples Processed:** 100
- **Correct:** 18
- **Incorrect:** 64
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.12903225806451613, 'recall': 0.2857142857142857, 'f1-score': 0.17777777777777778, 'support': 14.0}, 'B': {'precision': 0.3333333333333333, 'recall': 0.2727272727272727, 'f1-score': 0.3, 'support': 11.0}, 'C': {'precision': 0.3125, 'recall': 0.4166666666666667, 'f1-score': 0.35714285714285715, 'support': 12.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 23.0}, 'E': {'precision': 0.5555555555555556, 'recall': 0.25, 'f1-score': 0.3448275862068966, 'support': 20.0}, 'F': {'precision': 0.5, 'recall': 0.5, 'f1-score': 0.5, 'support': 2.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'O': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.21951219512195122, 'macro avg': {'precision': 0.16640192245030955, 'recall': 0.1568280204643841, 'f1-score': 0.1527043837388665, 'support': 82.0}, 'weighted avg': {'precision': 0.26017352915464637, 'recall': 0.21951219512195122, 'f1-score': 0.2191604255944037, 'support': 82.0}}
- **Macro Precision:** 0.166
- **Macro Recall:** 0.157
- **Macro F1:** 0.153
- **Weighted F1:** 0.219
- **Confusion Matrix:** [[4, 2, 2, 1, 1, 1, 0, 0, 1, 0, 2], [4, 3, 3, 0, 0, 0, 1, 0, 0, 0, 0], [5, 0, 5, 2, 0, 0, 0, 0, 0, 0, 0], [13, 2, 4, 0, 3, 0, 0, 1, 0, 0, 0], [4, 2, 2, 2, 5, 0, 0, 1, 0, 2, 2], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'I', 'K', 'O', 'Q', 'X']
- **Top Confused Pairs:** [('D', 'A', 13), ('C', 'A', 5), ('B', 'A', 4), ('D', 'C', 4), ('E', 'A', 4), ('B', 'C', 3), ('D', 'E', 3), ('A', 'B', 2), ('A', 'C', 2), ('A', 'X', 2)]
- **True Class Distribution:** {'E': 20, 'D': 23, 'C': 12, 'B': 11, 'A': 14, 'F': 2}
- **Pred Class Distribution:** {'E': 9, 'K': 2, 'A': 31, 'C': 16, 'B': 9, 'D': 5, 'I': 1, 'O': 1, 'Q': 2, 'X': 4, 'F': 2}
- **Num Classes:** 11

