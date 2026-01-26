# Experiment: Medqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-22 13:15:28  
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
  experiment=classification \
  experiment.num_samples=20 \
  prompt=mcq \
  prompt.output_format=plain \
  dataset=medqa
```

## Results

- **Accuracy:** 45.0%
- **Samples Processed:** 20
- **Correct:** 9
- **Incorrect:** 11
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.625, 'recall': 0.625, 'f1-score': 0.625, 'support': 8.0}, 'B': {'precision': 0.6666666666666666, 'recall': 0.5, 'f1-score': 0.5714285714285714, 'support': 4.0}, 'C': {'precision': 0.3333333333333333, 'recall': 0.2, 'f1-score': 0.25, 'support': 5.0}, 'D': {'precision': 0.3333333333333333, 'recall': 0.3333333333333333, 'f1-score': 0.3333333333333333, 'support': 3.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.45, 'macro avg': {'precision': 0.3916666666666666, 'recall': 0.33166666666666667, 'f1-score': 0.3559523809523809, 'support': 20.0}, 'weighted avg': {'precision': 0.5166666666666666, 'recall': 0.45, 'f1-score': 0.47678571428571426, 'support': 20.0}}
- **Macro Precision:** 0.392
- **Macro Recall:** 0.332
- **Macro F1:** 0.356
- **Weighted F1:** 0.477
- **Confusion Matrix:** [[5, 1, 0, 1, 1], [1, 2, 1, 0, 0], [1, 0, 1, 1, 2], [1, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'I']
- **Top Confused Pairs:** [('C', 'I', 2), ('A', 'B', 1), ('A', 'D', 1), ('A', 'I', 1), ('B', 'A', 1), ('B', 'C', 1), ('C', 'A', 1), ('C', 'D', 1), ('D', 'A', 1), ('D', 'C', 1)]
- **True Class Distribution:** {'A': 8, 'D': 3, 'B': 4, 'C': 5}
- **Pred Class Distribution:** {'B': 3, 'D': 3, 'A': 8, 'C': 3, 'I': 3}
- **Num Classes:** 5

