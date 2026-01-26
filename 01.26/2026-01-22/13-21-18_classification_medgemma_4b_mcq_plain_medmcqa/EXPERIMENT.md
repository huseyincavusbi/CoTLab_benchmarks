# Experiment: Medmcqa Answer-First (PLAIN)

**Status:** Completed
**Started:** 2026-01-22 13:21:18  
**Duration:** 2 minutes 0 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?
2. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** medmcqa

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
  few_shot: true
  output_format: plain
  answer_first: true
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medmcqa
  filename: medmcqa/validation.jsonl
  split: validation
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 20
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=20 \
  prompt=mcq \
  prompt.answer_first=true \
  prompt.output_format=plain \
  dataset=medmcqa
```

## Results

- **Accuracy:** 15.0%
- **Samples Processed:** 20
- **Correct:** 3
- **Incorrect:** 17
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.5, 'recall': 0.25, 'f1-score': 0.3333333333333333, 'support': 4.0}, 'B': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 5.0}, 'C': {'precision': 0.3333333333333333, 'recall': 0.25, 'f1-score': 0.2857142857142857, 'support': 8.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'O': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.15, 'macro avg': {'precision': 0.13888888888888887, 'recall': 0.08333333333333333, 'f1-score': 0.10317460317460318, 'support': 20.0}, 'weighted avg': {'precision': 0.2333333333333333, 'recall': 0.15, 'f1-score': 0.18095238095238092, 'support': 20.0}}
- **Macro Precision:** 0.139
- **Macro Recall:** 0.083
- **Macro F1:** 0.103
- **Weighted F1:** 0.181
- **Confusion Matrix:** [[1, 0, 1, 0, 2, 0], [1, 0, 2, 2, 0, 0], [0, 0, 2, 2, 3, 1], [0, 0, 1, 0, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'I', 'O']
- **Top Confused Pairs:** [('C', 'I', 3), ('A', 'I', 2), ('B', 'C', 2), ('B', 'D', 2), ('C', 'D', 2), ('D', 'I', 2), ('A', 'C', 1), ('B', 'A', 1), ('C', 'O', 1), ('D', 'C', 1)]
- **True Class Distribution:** {'A': 4, 'C': 8, 'D': 3, 'B': 5}
- **Pred Class Distribution:** {'I': 7, 'C': 6, 'D': 4, 'O': 1, 'A': 2}
- **Num Classes:** 6

