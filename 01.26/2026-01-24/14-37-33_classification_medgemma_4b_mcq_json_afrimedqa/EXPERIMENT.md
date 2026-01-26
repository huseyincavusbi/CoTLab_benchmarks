# Experiment: Afrimedqa Standard

**Status:** Completed
**Started:** 2026-01-24 14:37:34  
**Duration:** 36 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** afrimedqa

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
  name: afrimedqa
  filename: afrimedqa/mcq.jsonl
  split: mcq
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
  dataset=afrimedqa
```

## Results

- **Accuracy:** 70.0%
- **Samples Processed:** 20
- **Correct:** 14
- **Incorrect:** 6
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.6666666666666666, 'recall': 0.5, 'f1-score': 0.5714285714285714, 'support': 4.0}, 'B': {'precision': 0.8333333333333334, 'recall': 0.8333333333333334, 'f1-score': 0.8333333333333334, 'support': 6.0}, 'C': {'precision': 0.6666666666666666, 'recall': 0.6666666666666666, 'f1-score': 0.6666666666666666, 'support': 3.0}, 'D': {'precision': 0.8, 'recall': 0.8, 'f1-score': 0.8, 'support': 5.0}, 'E': {'precision': 0.5, 'recall': 0.5, 'f1-score': 0.5, 'support': 2.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.7, 'macro avg': {'precision': 0.5777777777777778, 'recall': 0.5499999999999999, 'f1-score': 0.5619047619047618, 'support': 20.0}, 'weighted avg': {'precision': 0.7333333333333333, 'recall': 0.7, 'f1-score': 0.7142857142857142, 'support': 20.0}}
- **Macro Precision:** 0.578
- **Macro Recall:** 0.550
- **Macro F1:** 0.562
- **Weighted F1:** 0.714
- **Confusion Matrix:** [[2, 0, 0, 0, 1, 1], [1, 5, 0, 0, 0, 0], [0, 1, 2, 0, 0, 0], [0, 0, 1, 4, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'X']
- **Top Confused Pairs:** [('A', 'E', 1), ('A', 'X', 1), ('B', 'A', 1), ('C', 'B', 1), ('D', 'C', 1), ('E', 'D', 1)]
- **True Class Distribution:** {'D': 5, 'A': 4, 'B': 6, 'E': 2, 'C': 3}
- **Pred Class Distribution:** {'D': 5, 'A': 3, 'E': 2, 'B': 6, 'X': 1, 'C': 3}
- **Num Classes:** 6

