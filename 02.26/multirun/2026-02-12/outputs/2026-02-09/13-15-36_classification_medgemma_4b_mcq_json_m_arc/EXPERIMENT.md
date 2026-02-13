# Experiment: M_arc Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-09 13:15:36  
**Duration:** 5 minutes 54 seconds

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
  prompt.answer_first=true \
  prompt.few_shot=false \
  dataset=m_arc
```

## Results

- **Accuracy:** 22.2%
- **Samples Processed:** 100
- **Correct:** 22
- **Incorrect:** 77
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.18518518518518517, 'recall': 0.35714285714285715, 'f1-score': 0.24390243902439024, 'support': 14.0}, 'B': {'precision': 0.09090909090909091, 'recall': 0.09090909090909091, 'f1-score': 0.09090909090909091, 'support': 11.0}, 'C': {'precision': 0.25, 'recall': 0.2222222222222222, 'f1-score': 0.23529411764705882, 'support': 18.0}, 'D': {'precision': 0.25, 'recall': 0.18181818181818182, 'f1-score': 0.21052631578947367, 'support': 33.0}, 'E': {'precision': 0.29411764705882354, 'recall': 0.23809523809523808, 'f1-score': 0.2631578947368421, 'support': 21.0}, 'F': {'precision': 1.0, 'recall': 0.5, 'f1-score': 0.6666666666666666, 'support': 2.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.2222222222222222, 'macro avg': {'precision': 0.25877649039413747, 'recall': 0.19877344877344877, 'f1-score': 0.2138070655966903, 'support': 99.0}, 'weighted avg': {'precision': 0.24766730485684732, 'recall': 0.2222222222222222, 'f1-score': 0.22683783644291083, 'support': 99.0}}
- **Macro Precision:** 0.259
- **Macro Recall:** 0.199
- **Macro F1:** 0.214
- **Weighted F1:** 0.227
- **Confusion Matrix:** [[5, 2, 3, 3, 1, 0, 0, 0], [1, 1, 2, 5, 1, 0, 1, 0], [8, 2, 4, 3, 1, 0, 0, 0], [9, 4, 5, 6, 9, 0, 0, 0], [3, 2, 2, 7, 5, 0, 1, 1], [1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'T', 'X']
- **Top Confused Pairs:** [('D', 'A', 9), ('D', 'E', 9), ('C', 'A', 8), ('E', 'D', 7), ('B', 'D', 5), ('D', 'C', 5), ('D', 'B', 4), ('A', 'C', 3), ('A', 'D', 3), ('C', 'D', 3)]
- **True Class Distribution:** {'E': 21, 'D': 33, 'C': 18, 'B': 11, 'A': 14, 'F': 2}
- **Pred Class Distribution:** {'E': 17, 'A': 27, 'C': 16, 'D': 24, 'X': 1, 'B': 11, 'T': 2, 'F': 1}
- **Num Classes:** 8

