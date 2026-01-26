# Experiment: Medmcqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-20 11:50:47  
**Duration:** 2 minutes 34 seconds

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
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medmcqa
  filename: medmcqa/validation.jsonl
  split: validation
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 50
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  prompt=mcq \
  prompt.output_format=plain \
  dataset=medmcqa
```

## Results

- **Accuracy:** 26.0%
- **Samples Processed:** 50
- **Correct:** 13
- **Incorrect:** 37
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.28125, 'recall': 0.6, 'f1-score': 0.3829787234042553, 'support': 15.0}, 'B': {'precision': 0.3333333333333333, 'recall': 0.08333333333333333, 'f1-score': 0.13333333333333333, 'support': 12.0}, 'C': {'precision': 0.2222222222222222, 'recall': 0.14285714285714285, 'f1-score': 0.17391304347826086, 'support': 14.0}, 'D': {'precision': 0.16666666666666666, 'recall': 0.1111111111111111, 'f1-score': 0.13333333333333333, 'support': 9.0}, 'accuracy': 0.26, 'macro avg': {'precision': 0.2508680555555555, 'recall': 0.23432539682539683, 'f1-score': 0.2058896083872957, 'support': 50.0}, 'weighted avg': {'precision': 0.2565972222222222, 'recall': 0.26, 'f1-score': 0.21958926919518962, 'support': 50.0}}
- **Macro Precision:** 0.251
- **Macro Recall:** 0.234
- **Macro F1:** 0.206
- **Weighted F1:** 0.220
- **Confusion Matrix:** [[9, 2, 2, 2], [9, 1, 1, 1], [10, 0, 2, 2], [4, 0, 4, 1]]
- **Class Labels:** ['A', 'B', 'C', 'D']
- **Top Confused Pairs:** [('C', 'A', 10), ('B', 'A', 9), ('D', 'A', 4), ('D', 'C', 4), ('A', 'B', 2), ('A', 'C', 2), ('A', 'D', 2), ('C', 'D', 2), ('B', 'C', 1), ('B', 'D', 1)]
- **True Class Distribution:** {'A': 15, 'C': 14, 'D': 9, 'B': 12}
- **Pred Class Distribution:** {'A': 32, 'C': 9, 'D': 6, 'B': 3}
- **Num Classes:** 4

