# Experiment: Medqa Standard

**Status:** Completed
**Started:** 2026-01-22 14:34:53  
**Duration:** 2 minutes 2 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
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
  output_format: json
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
  dataset=medqa
```

## Results

- **Accuracy:** 60.0%
- **Samples Processed:** 20
- **Correct:** 12
- **Incorrect:** 8
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.7142857142857143, 'recall': 0.625, 'f1-score': 0.6666666666666666, 'support': 8.0}, 'B': {'precision': 0.5, 'recall': 0.75, 'f1-score': 0.6, 'support': 4.0}, 'C': {'precision': 0.75, 'recall': 0.6, 'f1-score': 0.6666666666666666, 'support': 5.0}, 'D': {'precision': 0.3333333333333333, 'recall': 0.3333333333333333, 'f1-score': 0.3333333333333333, 'support': 3.0}, 'accuracy': 0.6, 'macro avg': {'precision': 0.574404761904762, 'recall': 0.5770833333333334, 'f1-score': 0.5666666666666667, 'support': 20.0}, 'weighted avg': {'precision': 0.6232142857142857, 'recall': 0.6, 'f1-score': 0.6033333333333333, 'support': 20.0}}
- **Macro Precision:** 0.574
- **Macro Recall:** 0.577
- **Macro F1:** 0.567
- **Weighted F1:** 0.603
- **Confusion Matrix:** [[5, 2, 0, 1], [0, 3, 1, 0], [1, 0, 3, 1], [1, 1, 0, 1]]
- **Class Labels:** ['A', 'B', 'C', 'D']
- **Top Confused Pairs:** [('A', 'B', 2), ('A', 'D', 1), ('B', 'C', 1), ('C', 'A', 1), ('C', 'D', 1), ('D', 'A', 1), ('D', 'B', 1)]
- **True Class Distribution:** {'A': 8, 'D': 3, 'B': 4, 'C': 5}
- **Pred Class Distribution:** {'B': 6, 'A': 7, 'D': 3, 'C': 4}
- **Num Classes:** 4

