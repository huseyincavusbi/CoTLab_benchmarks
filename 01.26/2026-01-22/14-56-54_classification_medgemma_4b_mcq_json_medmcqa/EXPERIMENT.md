# Experiment: Medmcqa Answer-First

**Status:** Completed
**Started:** 2026-01-22 14:56:54  
**Duration:** 2 minutes 1 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
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
  dataset=medmcqa
```

## Results

- **Accuracy:** 40.0%
- **Samples Processed:** 20
- **Correct:** 8
- **Incorrect:** 12
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.3333333333333333, 'recall': 0.25, 'f1-score': 0.2857142857142857, 'support': 4.0}, 'B': {'precision': 0.3333333333333333, 'recall': 0.2, 'f1-score': 0.25, 'support': 5.0}, 'C': {'precision': 0.46153846153846156, 'recall': 0.75, 'f1-score': 0.5714285714285714, 'support': 8.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'accuracy': 0.4, 'macro avg': {'precision': 0.28205128205128205, 'recall': 0.3, 'f1-score': 0.2767857142857143, 'support': 20.0}, 'weighted avg': {'precision': 0.33461538461538465, 'recall': 0.4, 'f1-score': 0.3482142857142857, 'support': 20.0}}
- **Macro Precision:** 0.282
- **Macro Recall:** 0.300
- **Macro F1:** 0.277
- **Weighted F1:** 0.348
- **Confusion Matrix:** [[1, 1, 2, 0], [1, 1, 3, 0], [1, 0, 6, 1], [0, 1, 2, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D']
- **Top Confused Pairs:** [('B', 'C', 3), ('A', 'C', 2), ('D', 'C', 2), ('A', 'B', 1), ('B', 'A', 1), ('C', 'A', 1), ('C', 'D', 1), ('D', 'B', 1)]
- **True Class Distribution:** {'A': 4, 'C': 8, 'D': 3, 'B': 5}
- **Pred Class Distribution:** {'C': 13, 'A': 3, 'B': 3, 'D': 1}
- **Num Classes:** 4

