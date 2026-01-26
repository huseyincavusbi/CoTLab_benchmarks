# Experiment: Medmcqa Standard

**Status:** Completed
**Started:** 2026-01-22 15:00:20  
**Duration:** 2 minutes 1 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
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
  output_format: json
  answer_first: false
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
  dataset=medmcqa
```

## Results

- **Accuracy:** 20.0%
- **Samples Processed:** 20
- **Correct:** 4
- **Incorrect:** 16
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.16666666666666666, 'recall': 0.25, 'f1-score': 0.2, 'support': 4.0}, 'B': {'precision': 0.2, 'recall': 0.2, 'f1-score': 0.2, 'support': 5.0}, 'C': {'precision': 0.4, 'recall': 0.25, 'f1-score': 0.3076923076923077, 'support': 8.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'accuracy': 0.2, 'macro avg': {'precision': 0.19166666666666668, 'recall': 0.175, 'f1-score': 0.17692307692307693, 'support': 20.0}, 'weighted avg': {'precision': 0.24333333333333335, 'recall': 0.2, 'f1-score': 0.21307692307692308, 'support': 20.0}}
- **Macro Precision:** 0.192
- **Macro Recall:** 0.175
- **Macro F1:** 0.177
- **Weighted F1:** 0.213
- **Confusion Matrix:** [[1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 2, 2], [0, 2, 1, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D']
- **Top Confused Pairs:** [('C', 'A', 3), ('B', 'A', 2), ('C', 'D', 2), ('D', 'B', 2), ('A', 'B', 1), ('A', 'C', 1), ('A', 'D', 1), ('B', 'C', 1), ('B', 'D', 1), ('C', 'B', 1)]
- **True Class Distribution:** {'A': 4, 'C': 8, 'D': 3, 'B': 5}
- **Pred Class Distribution:** {'B': 5, 'C': 5, 'A': 6, 'D': 4}
- **Num Classes:** 4

