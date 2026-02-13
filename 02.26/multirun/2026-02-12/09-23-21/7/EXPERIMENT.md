# Experiment: M_arc Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-12 10:10:09  
**Duration:** 1 minutes 23 seconds

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
  prompt.few_shot=false \
  dataset=m_arc
```

## Results

- **Accuracy:** 17.9%
- **Samples Processed:** 100
- **Correct:** 15
- **Incorrect:** 69
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.13043478260869565, 'recall': 0.21428571428571427, 'f1-score': 0.16216216216216217, 'support': 14.0}, 'B': {'precision': 0.09523809523809523, 'recall': 0.18181818181818182, 'f1-score': 0.125, 'support': 11.0}, 'C': {'precision': 0.35714285714285715, 'recall': 0.38461538461538464, 'f1-score': 0.37037037037037035, 'support': 13.0}, 'D': {'precision': 0.2857142857142857, 'recall': 0.08695652173913043, 'f1-score': 0.13333333333333333, 'support': 23.0}, 'E': {'precision': 0.3333333333333333, 'recall': 0.09523809523809523, 'f1-score': 0.14814814814814814, 'support': 21.0}, 'F': {'precision': 1.0, 'recall': 0.5, 'f1-score': 0.6666666666666666, 'support': 2.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.17857142857142858, 'macro avg': {'precision': 0.20016939582156973, 'recall': 0.13299217251786422, 'f1-score': 0.14597097097097098, 'support': 84.0}, 'weighted avg': {'precision': 0.27485704426698215, 'recall': 0.17857142857142858, 'f1-score': 0.19013328804995472, 'support': 84.0}}
- **Macro Precision:** 0.200
- **Macro Recall:** 0.133
- **Macro F1:** 0.146
- **Weighted F1:** 0.190
- **Confusion Matrix:** [[3, 6, 2, 1, 0, 0, 0, 0, 0, 0, 2], [2, 2, 3, 0, 2, 0, 2, 0, 0, 0, 0], [5, 0, 5, 2, 0, 0, 0, 0, 1, 0, 0], [7, 10, 1, 2, 2, 0, 0, 0, 0, 0, 1], [5, 3, 3, 2, 2, 0, 1, 2, 0, 2, 1], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'I', 'Q', 'S', 'T', 'X']
- **Top Confused Pairs:** [('D', 'B', 10), ('D', 'A', 7), ('A', 'B', 6), ('C', 'A', 5), ('E', 'A', 5), ('B', 'C', 3), ('E', 'B', 3), ('E', 'C', 3), ('A', 'C', 2), ('A', 'X', 2)]
- **True Class Distribution:** {'E': 21, 'D': 23, 'C': 13, 'B': 11, 'A': 14, 'F': 2}
- **Pred Class Distribution:** {'D': 7, 'B': 21, 'A': 23, 'C': 14, 'S': 1, 'X': 4, 'E': 6, 'I': 3, 'T': 2, 'Q': 2, 'F': 1}
- **Num Classes:** 11

