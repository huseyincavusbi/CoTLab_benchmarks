# Experiment: Medmcqa Standard

**Status:** Completed
**Started:** 2026-01-24 14:24:45  
**Duration:** 30 seconds

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
  max_model_len: 4096
  quantization: null
  gpu_memory_utilization: 0.9
  enforce_eager: true
  limit_mm_per_prompt:
    image: 0
model:
  name: google/medgemma-4b-it
  variant: 4b
  max_new_tokens: 256
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

- **Accuracy:** 35.0%
- **Samples Processed:** 20
- **Correct:** 7
- **Incorrect:** 13
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.3333333333333333, 'recall': 0.25, 'f1-score': 0.2857142857142857, 'support': 4.0}, 'B': {'precision': 0.3333333333333333, 'recall': 0.4, 'f1-score': 0.36363636363636365, 'support': 5.0}, 'C': {'precision': 0.5, 'recall': 0.5, 'f1-score': 0.5, 'support': 8.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.35, 'macro avg': {'precision': 0.2333333333333333, 'recall': 0.22999999999999998, 'f1-score': 0.22987012987012986, 'support': 20.0}, 'weighted avg': {'precision': 0.35, 'recall': 0.35, 'f1-score': 0.34805194805194806, 'support': 20.0}}
- **Macro Precision:** 0.233
- **Macro Recall:** 0.230
- **Macro F1:** 0.230
- **Weighted F1:** 0.348
- **Confusion Matrix:** [[1, 2, 0, 0, 1], [1, 2, 2, 0, 0], [1, 1, 4, 2, 0], [0, 1, 2, 0, 0], [0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'X']
- **Top Confused Pairs:** [('A', 'B', 2), ('B', 'C', 2), ('C', 'D', 2), ('D', 'C', 2), ('A', 'X', 1), ('B', 'A', 1), ('C', 'A', 1), ('C', 'B', 1), ('D', 'B', 1)]
- **True Class Distribution:** {'A': 4, 'C': 8, 'D': 3, 'B': 5}
- **Pred Class Distribution:** {'B': 6, 'C': 8, 'A': 3, 'X': 1, 'D': 2}
- **Num Classes:** 5

