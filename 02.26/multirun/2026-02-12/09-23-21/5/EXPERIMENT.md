# Experiment: M_arc Answer-First

**Status:** Completed
**Started:** 2026-02-12 10:05:24  
**Duration:** 1 minutes 27 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
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
  prompt.answer_first=true \
  dataset=m_arc
```

## Results

- **Accuracy:** 21.1%
- **Samples Processed:** 100
- **Correct:** 19
- **Incorrect:** 71
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.19047619047619047, 'recall': 0.2857142857142857, 'f1-score': 0.22857142857142856, 'support': 14.0}, 'B': {'precision': 0.10526315789473684, 'recall': 0.18181818181818182, 'f1-score': 0.13333333333333333, 'support': 11.0}, 'C': {'precision': 0.29411764705882354, 'recall': 0.38461538461538464, 'f1-score': 0.3333333333333333, 'support': 13.0}, 'D': {'precision': 0.38461538461538464, 'recall': 0.17857142857142858, 'f1-score': 0.24390243902439024, 'support': 28.0}, 'E': {'precision': 0.2727272727272727, 'recall': 0.13636363636363635, 'f1-score': 0.18181818181818182, 'support': 22.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 2.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.2111111111111111, 'macro avg': {'precision': 0.11338178661567348, 'recall': 0.1060984470075379, 'f1-score': 0.10190533782551521, 'support': 90.0}, 'weighted avg': {'precision': 0.2713035731611583, 'recall': 0.2111111111111111, 'f1-score': 0.2203252032520325, 'support': 90.0}}
- **Macro Precision:** 0.113
- **Macro Recall:** 0.106
- **Macro F1:** 0.102
- **Weighted F1:** 0.220
- **Confusion Matrix:** [[4, 2, 6, 2, 0, 0, 0, 0, 0, 0, 0], [2, 2, 1, 1, 1, 0, 3, 0, 1, 0, 0], [1, 4, 5, 3, 0, 0, 0, 0, 0, 0, 0], [6, 6, 2, 5, 7, 0, 0, 2, 0, 0, 0], [6, 5, 3, 2, 3, 0, 0, 1, 0, 1, 1], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'I', 'K', 'L', 'Q', 'X']
- **Top Confused Pairs:** [('D', 'E', 7), ('A', 'C', 6), ('D', 'A', 6), ('D', 'B', 6), ('E', 'A', 6), ('E', 'B', 5), ('C', 'B', 4), ('B', 'I', 3), ('C', 'D', 3), ('E', 'C', 3)]
- **True Class Distribution:** {'E': 22, 'D': 28, 'C': 13, 'B': 11, 'A': 14, 'F': 2}
- **Pred Class Distribution:** {'E': 11, 'A': 21, 'D': 13, 'K': 3, 'B': 19, 'C': 17, 'X': 1, 'I': 3, 'L': 1, 'Q': 1}
- **Num Classes:** 11

