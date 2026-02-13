# Experiment: Plab Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-12 13:30:00  
**Duration:** 18 minutes 18 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** No (zero-shot)
**Output Format:** JSON
**Dataset:** plab

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
  name: google/medgemma-27b-it
  variant: 27b
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b_it
prompt:
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: false
  output_format: json
  answer_first: true
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.PLABDataset
  name: plab
  split: main
  filename: plab/data.json
  topics_filename: plab/topics.json
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
  dataset=plab
```

## Results

- **Accuracy:** 22.6%
- **Samples Processed:** 1652
- **Correct:** 328
- **Incorrect:** 1125
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.2526997840172786, 'recall': 0.3015463917525773, 'f1-score': 0.27497062279670975, 'support': 388.0}, 'B': {'precision': 0.32083333333333336, 'recall': 0.212707182320442, 'f1-score': 0.2558139534883721, 'support': 362.0}, 'C': {'precision': 0.2894736842105263, 'recall': 0.22837370242214533, 'f1-score': 0.2553191489361702, 'support': 289.0}, 'D': {'precision': 0.1917808219178082, 'recall': 0.17142857142857143, 'f1-score': 0.1810344827586207, 'support': 245.0}, 'E': {'precision': 0.1724137931034483, 'recall': 0.16233766233766234, 'f1-score': 0.16722408026755853, 'support': 154.0}, 'F': {'precision': 0.3333333333333333, 'recall': 0.1, 'f1-score': 0.15384615384615385, 'support': 10.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 5.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'M': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'R': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'W': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.22573984858912594, 'macro avg': {'precision': 0.0780267374957864, 'recall': 0.05881967551306992, 'f1-score': 0.06441042210467926, 'support': 1453.0}, 'weighted avg': {'precision': 0.2578929362996148, 'recall': 0.22573984858912594, 'f1-score': 0.23725045080935642, 'support': 1453.0}}
- **Macro Precision:** 0.078
- **Macro Recall:** 0.059
- **Macro F1:** 0.064
- **Weighted F1:** 0.237
- **Confusion Matrix:** [[117, 72, 55, 54, 38, 1, 0, 0, 2, 5, 14, 1, 1, 1, 0, 3, 9, 2, 0, 13], [110, 77, 54, 56, 29, 0, 1, 4, 2, 4, 5, 0, 1, 3, 1, 2, 2, 0, 0, 11], [89, 34, 66, 40, 24, 1, 1, 1, 3, 3, 8, 0, 1, 1, 0, 0, 2, 4, 1, 10], [92, 36, 36, 42, 24, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 3, 0, 6], [50, 20, 16, 25, 25, 0, 0, 0, 3, 1, 4, 1, 1, 0, 0, 2, 0, 0, 0, 6], [4, 1, 1, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'W', 'X']
- **Top Confused Pairs:** [('B', 'A', 110), ('D', 'A', 92), ('C', 'A', 89), ('A', 'B', 72), ('B', 'D', 56), ('A', 'C', 55), ('A', 'D', 54), ('B', 'C', 54), ('E', 'A', 50), ('C', 'D', 40)]
- **True Class Distribution:** {'B': 362, 'C': 289, 'D': 245, 'A': 388, 'E': 154, 'G': 5, 'F': 10}
- **Pred Class Distribution:** {'B': 240, 'D': 219, 'A': 463, 'C': 228, 'E': 145, 'L': 32, 'N': 5, 'T': 14, 'X': 46, 'I': 10, 'K': 14, 'V': 9, 'W': 1, 'P': 5, 'S': 7, 'G': 3, 'R': 2, 'M': 2, 'H': 5, 'F': 3}
- **Num Classes:** 20

