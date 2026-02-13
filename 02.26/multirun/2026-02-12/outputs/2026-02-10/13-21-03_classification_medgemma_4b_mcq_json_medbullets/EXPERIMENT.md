# Experiment: Medbullets Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-10 13:21:03  
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
  split: op4_test
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

- **Accuracy:** 25.4%
- **Samples Processed:** 308
- **Correct:** 72
- **Incorrect:** 212
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.2621359223300971, 'recall': 0.6835443037974683, 'f1-score': 0.37894736842105264, 'support': 79.0}, 'B': {'precision': 0.17647058823529413, 'recall': 0.04285714285714286, 'f1-score': 0.06896551724137931, 'support': 70.0}, 'C': {'precision': 0.35294117647058826, 'recall': 0.08333333333333333, 'f1-score': 0.1348314606741573, 'support': 72.0}, 'D': {'precision': 0.25, 'recall': 0.14285714285714285, 'f1-score': 0.18181818181818182, 'support': 63.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.2535211267605634, 'macro avg': {'precision': 0.11572752078177552, 'recall': 0.10584354698278747, 'f1-score': 0.08495139201719677, 'support': 284.0}, 'weighted avg': {'precision': 0.26135015403672746, 'recall': 0.2535211267605634, 'f1-score': 0.19692548920860736, 'support': 284.0}}
- **Macro Precision:** 0.116
- **Macro Recall:** 0.106
- **Macro F1:** 0.085
- **Weighted F1:** 0.197
- **Confusion Matrix:** [[54, 6, 3, 14, 0, 1, 1, 0, 0], [55, 3, 4, 8, 0, 0, 0, 0, 0], [55, 4, 6, 5, 0, 0, 0, 1, 1], [42, 4, 4, 9, 1, 2, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'I', 'L', 'N', 'Q', 'S']
- **Top Confused Pairs:** [('B', 'A', 55), ('C', 'A', 55), ('D', 'A', 42), ('A', 'D', 14), ('B', 'D', 8), ('A', 'B', 6), ('C', 'D', 5), ('B', 'C', 4), ('C', 'B', 4), ('D', 'B', 4)]
- **True Class Distribution:** {'B': 70, 'D': 63, 'C': 72, 'A': 79}
- **Pred Class Distribution:** {'A': 206, 'B': 17, 'D': 36, 'C': 17, 'L': 3, 'S': 2, 'Q': 1, 'I': 1, 'N': 1}
- **Num Classes:** 9

