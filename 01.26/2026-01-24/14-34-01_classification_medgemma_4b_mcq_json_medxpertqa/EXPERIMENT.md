# Experiment: Medxpertqa Standard

**Status:** Completed
**Started:** 2026-01-24 14:34:01  
**Duration:** 37 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medxpertqa

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
  name: medxpertqa
  filename: medxpertqa/test.jsonl
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
  dataset=medxpertqa
```

## Results

- **Accuracy:** 21.1%
- **Samples Processed:** 20
- **Correct:** 4
- **Incorrect:** 15
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.25, 'recall': 0.5, 'f1-score': 0.3333333333333333, 'support': 2.0}, 'B': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'C': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'E': {'precision': 0.3333333333333333, 'recall': 0.25, 'f1-score': 0.2857142857142857, 'support': 4.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'H': {'precision': 0.5, 'recall': 0.5, 'f1-score': 0.5, 'support': 2.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'J': {'precision': 0.2, 'recall': 0.5, 'f1-score': 0.2857142857142857, 'support': 2.0}, 'accuracy': 0.21052631578947367, 'macro avg': {'precision': 0.12833333333333333, 'recall': 0.175, 'f1-score': 0.14047619047619048, 'support': 19.0}, 'weighted avg': {'precision': 0.1701754385964912, 'recall': 0.21052631578947367, 'f1-score': 0.17794486215538843, 'support': 19.0}}
- **Macro Precision:** 0.128
- **Macro Recall:** 0.175
- **Macro F1:** 0.140
- **Weighted F1:** 0.178
- **Confusion Matrix:** [[1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 2], [0, 1, 0, 0, 0, 0, 0, 0, 0, 1]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
- **Top Confused Pairs:** [('I', 'J', 2), ('A', 'E', 1), ('C', 'A', 1), ('D', 'J', 1), ('E', 'A', 1), ('E', 'G', 1), ('E', 'I', 1), ('F', 'G', 1), ('G', 'E', 1), ('G', 'H', 1)]
- **True Class Distribution:** {'D': 1, 'G': 3, 'E': 4, 'J': 2, 'A': 2, 'F': 1, 'I': 3, 'H': 2, 'C': 1}
- **Pred Class Distribution:** {'J': 5, 'I': 1, 'E': 3, 'G': 2, 'A': 4, 'D': 1, 'H': 2, 'B': 1}
- **Num Classes:** 10

