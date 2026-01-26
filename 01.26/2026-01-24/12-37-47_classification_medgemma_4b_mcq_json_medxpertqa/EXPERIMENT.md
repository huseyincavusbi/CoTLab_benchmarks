# Experiment: Medxpertqa Standard

**Status:** Completed
**Started:** 2026-01-24 12:37:47  
**Duration:** 2 minutes 5 seconds

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

- **Accuracy:** 10.5%
- **Samples Processed:** 20
- **Correct:** 2
- **Incorrect:** 17
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.5, 'recall': 0.5, 'f1-score': 0.5, 'support': 2.0}, 'B': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'C': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'E': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 4.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 2.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'J': {'precision': 0.16666666666666666, 'recall': 0.5, 'f1-score': 0.25, 'support': 2.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.10526315789473684, 'macro avg': {'precision': 0.0606060606060606, 'recall': 0.09090909090909091, 'f1-score': 0.06818181818181818, 'support': 19.0}, 'weighted avg': {'precision': 0.07017543859649122, 'recall': 0.10526315789473684, 'f1-score': 0.07894736842105263, 'support': 19.0}}
- **Macro Precision:** 0.061
- **Macro Recall:** 0.091
- **Macro F1:** 0.068
- **Weighted F1:** 0.079
- **Confusion Matrix:** [[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'T']
- **Top Confused Pairs:** [('G', 'H', 2), ('I', 'J', 2), ('A', 'E', 1), ('C', 'I', 1), ('D', 'J', 1), ('E', 'G', 1), ('E', 'H', 1), ('E', 'J', 1), ('E', 'T', 1), ('F', 'A', 1)]
- **True Class Distribution:** {'D': 1, 'G': 3, 'E': 4, 'J': 2, 'A': 2, 'F': 1, 'I': 3, 'H': 2, 'C': 1}
- **Pred Class Distribution:** {'J': 6, 'H': 3, 'T': 1, 'E': 2, 'A': 2, 'G': 1, 'D': 1, 'I': 1, 'F': 1, 'B': 1}
- **Num Classes:** 11

