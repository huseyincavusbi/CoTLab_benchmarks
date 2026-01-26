# Experiment: Medqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-21 07:25:42  
**Duration:** 2 minutes 1 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** medqa

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
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medqa
  filename: medqa/test.jsonl
  split: test
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
  prompt=mcq \
  prompt.output_format=plain \
  dataset=medqa
```

## Results

- **Accuracy:** 35.0%
- **Samples Processed:** 20
- **Correct:** 7
- **Incorrect:** 13
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.6, 'recall': 0.375, 'f1-score': 0.46153846153846156, 'support': 8.0}, 'B': {'precision': 0.25, 'recall': 0.25, 'f1-score': 0.25, 'support': 4.0}, 'C': {'precision': 1.0, 'recall': 0.4, 'f1-score': 0.5714285714285714, 'support': 5.0}, 'D': {'precision': 1.0, 'recall': 0.3333333333333333, 'f1-score': 0.5, 'support': 3.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.35, 'macro avg': {'precision': 0.35625, 'recall': 0.16979166666666667, 'f1-score': 0.2228708791208791, 'support': 20.0}, 'weighted avg': {'precision': 0.6900000000000001, 'recall': 0.35, 'f1-score': 0.4524725274725275, 'support': 20.0}}
- **Macro Precision:** 0.356
- **Macro Recall:** 0.170
- **Macro F1:** 0.223
- **Weighted F1:** 0.452
- **Confusion Matrix:** [[3, 1, 0, 0, 1, 2, 0, 1], [0, 1, 0, 0, 1, 1, 1, 0], [1, 1, 2, 0, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'F', 'I', 'Q', 'T']
- **Top Confused Pairs:** [('A', 'I', 2), ('A', 'B', 1), ('A', 'F', 1), ('A', 'T', 1), ('B', 'F', 1), ('B', 'I', 1), ('B', 'Q', 1), ('C', 'A', 1), ('C', 'B', 1), ('C', 'F', 1)]
- **True Class Distribution:** {'A': 8, 'D': 3, 'B': 4, 'C': 5}
- **Pred Class Distribution:** {'B': 4, 'A': 5, 'I': 3, 'F': 3, 'C': 2, 'D': 1, 'Q': 1, 'T': 1}
- **Num Classes:** 8

