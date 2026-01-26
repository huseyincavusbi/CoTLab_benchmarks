# Experiment: Medmcqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-22 13:39:24  
**Duration:** 2 minutes 0 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
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
  output_format: plain
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
  prompt.output_format=plain \
  dataset=medmcqa
```

## Results

- **Accuracy:** 25.0%
- **Samples Processed:** 20
- **Correct:** 5
- **Incorrect:** 15
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.3333333333333333, 'recall': 0.5, 'f1-score': 0.4, 'support': 4.0}, 'B': {'precision': 0.3333333333333333, 'recall': 0.2, 'f1-score': 0.25, 'support': 5.0}, 'C': {'precision': 0.3333333333333333, 'recall': 0.25, 'f1-score': 0.2857142857142857, 'support': 8.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'W': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.25, 'macro avg': {'precision': 0.16666666666666666, 'recall': 0.15833333333333333, 'f1-score': 0.15595238095238095, 'support': 20.0}, 'weighted avg': {'precision': 0.2833333333333333, 'recall': 0.25, 'f1-score': 0.2567857142857143, 'support': 20.0}}
- **Macro Precision:** 0.167
- **Macro Recall:** 0.158
- **Macro F1:** 0.156
- **Weighted F1:** 0.257
- **Confusion Matrix:** [[2, 0, 2, 0, 0, 0], [2, 1, 2, 0, 0, 0], [2, 1, 2, 1, 1, 1], [0, 1, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'I', 'W']
- **Top Confused Pairs:** [('A', 'C', 2), ('B', 'A', 2), ('B', 'C', 2), ('C', 'A', 2), ('D', 'I', 2), ('C', 'B', 1), ('C', 'D', 1), ('C', 'I', 1), ('C', 'W', 1), ('D', 'B', 1)]
- **True Class Distribution:** {'A': 4, 'C': 8, 'D': 3, 'B': 5}
- **Pred Class Distribution:** {'C': 6, 'I': 3, 'A': 6, 'B': 3, 'W': 1, 'D': 1}
- **Num Classes:** 6

