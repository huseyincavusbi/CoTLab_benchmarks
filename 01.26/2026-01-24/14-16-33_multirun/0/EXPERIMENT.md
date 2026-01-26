# Experiment: Medqa Answer-First

**Status:** Completed
**Started:** 2026-01-24 14:16:34  
**Duration:** 35 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
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
  answer_first: true
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
  prompt.answer_first=true \
  dataset=medqa
```

## Results

- **Accuracy:** 40.0%
- **Samples Processed:** 20
- **Correct:** 8
- **Incorrect:** 12
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.6666666666666666, 'recall': 0.5, 'f1-score': 0.5714285714285714, 'support': 8.0}, 'B': {'precision': 0.16666666666666666, 'recall': 0.25, 'f1-score': 0.2, 'support': 4.0}, 'C': {'precision': 0.6666666666666666, 'recall': 0.4, 'f1-score': 0.5, 'support': 5.0}, 'D': {'precision': 0.2, 'recall': 0.3333333333333333, 'f1-score': 0.25, 'support': 3.0}, 'accuracy': 0.4, 'macro avg': {'precision': 0.425, 'recall': 0.3708333333333333, 'f1-score': 0.38035714285714284, 'support': 20.0}, 'weighted avg': {'precision': 0.4966666666666666, 'recall': 0.4, 'f1-score': 0.4310714285714285, 'support': 20.0}}
- **Macro Precision:** 0.425
- **Macro Recall:** 0.371
- **Macro F1:** 0.380
- **Weighted F1:** 0.431
- **Confusion Matrix:** [[4, 2, 0, 2], [1, 1, 1, 1], [0, 2, 2, 1], [1, 1, 0, 1]]
- **Class Labels:** ['A', 'B', 'C', 'D']
- **Top Confused Pairs:** [('A', 'B', 2), ('A', 'D', 2), ('C', 'B', 2), ('B', 'A', 1), ('B', 'C', 1), ('B', 'D', 1), ('C', 'D', 1), ('D', 'A', 1), ('D', 'B', 1)]
- **True Class Distribution:** {'A': 8, 'D': 3, 'B': 4, 'C': 5}
- **Pred Class Distribution:** {'B': 6, 'D': 5, 'A': 6, 'C': 3}
- **Num Classes:** 4

