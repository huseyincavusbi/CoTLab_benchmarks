# Experiment: Medbullets Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-12 10:28:32  
**Duration:** 4 minutes 18 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
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
  _target_: cotlab.datasets.loaders.MedBulletsDataset
  name: medbullets
  split: op5_test
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
  dataset=medbullets
```

## Results

- **Accuracy:** 17.6%
- **Samples Processed:** 308
- **Correct:** 47
- **Incorrect:** 220
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.24210526315789474, 'recall': 0.4423076923076923, 'f1-score': 0.3129251700680272, 'support': 52.0}, 'B': {'precision': 0.3225806451612903, 'recall': 0.15151515151515152, 'f1-score': 0.20618556701030927, 'support': 66.0}, 'C': {'precision': 0.21428571428571427, 'recall': 0.2, 'f1-score': 0.20689655172413793, 'support': 45.0}, 'D': {'precision': 0.25, 'recall': 0.08620689655172414, 'f1-score': 0.1282051282051282, 'support': 58.0}, 'E': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 46.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'R': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'U': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.1760299625468165, 'macro avg': {'precision': 0.05415640118973155, 'recall': 0.046317354756556205, 'f1-score': 0.04495854826355803, 'support': 267.0}, 'weighted avg': {'precision': 0.21731330864311918, 'recall': 0.1760299625468165, 'f1-score': 0.17463145516742123, 'support': 267.0}}
- **Macro Precision:** 0.054
- **Macro Recall:** 0.046
- **Macro F1:** 0.045
- **Weighted F1:** 0.175
- **Confusion Matrix:** [[23, 5, 4, 3, 5, 2, 0, 1, 0, 2, 0, 2, 1, 1, 0, 0, 1, 0, 2], [19, 10, 10, 5, 2, 2, 0, 1, 2, 4, 1, 6, 1, 0, 0, 2, 0, 0, 1], [15, 6, 9, 4, 0, 3, 1, 0, 1, 3, 0, 1, 0, 0, 0, 1, 0, 0, 1], [23, 3, 8, 5, 2, 3, 2, 1, 1, 2, 1, 2, 0, 0, 0, 1, 0, 1, 3], [15, 7, 11, 3, 0, 0, 2, 0, 1, 3, 0, 2, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'K', 'L', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X']
- **Top Confused Pairs:** [('D', 'A', 23), ('B', 'A', 19), ('C', 'A', 15), ('E', 'A', 15), ('E', 'C', 11), ('B', 'C', 10), ('D', 'C', 8), ('E', 'B', 7), ('B', 'P', 6), ('C', 'B', 6)]
- **True Class Distribution:** {'B': 66, 'E': 46, 'A': 52, 'D': 58, 'C': 45}
- **Pred Class Distribution:** {'C': 42, 'X': 8, 'B': 31, 'A': 95, 'D': 20, 'F': 10, 'N': 2, 'H': 5, 'L': 14, 'P': 13, 'S': 1, 'R': 1, 'E': 9, 'V': 1, 'T': 4, 'K': 5, 'U': 1, 'I': 3, 'Q': 2}
- **Num Classes:** 19

