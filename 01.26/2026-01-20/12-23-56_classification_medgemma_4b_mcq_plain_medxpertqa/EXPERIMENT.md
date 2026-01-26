# Experiment: Medxpertqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-20 12:23:56  
**Duration:** 3 minutes 50 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
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
  output_format: plain
  answer_first: false
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medxpertqa
  filename: medxpertqa/test.jsonl
  split: test
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
  dataset=medxpertqa
```

## Results

- **Accuracy:** 14.0%
- **Samples Processed:** 50
- **Correct:** 7
- **Incorrect:** 43
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 4.0}, 'B': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'C': {'precision': 0.2222222222222222, 'recall': 0.4, 'f1-score': 0.2857142857142857, 'support': 5.0}, 'D': {'precision': 0.6666666666666666, 'recall': 0.2857142857142857, 'f1-score': 0.4, 'support': 7.0}, 'E': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 8.0}, 'F': {'precision': 0.16666666666666666, 'recall': 0.3333333333333333, 'f1-score': 0.2222222222222222, 'support': 3.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 5.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 4.0}, 'I': {'precision': 0.2857142857142857, 'recall': 0.3333333333333333, 'f1-score': 0.3076923076923077, 'support': 6.0}, 'J': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 7.0}, 'M': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'W': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.14, 'macro avg': {'precision': 0.10317460317460318, 'recall': 0.10402930402930402, 'f1-score': 0.09350990889452429, 'support': 50.0}, 'weighted avg': {'precision': 0.1598412698412698, 'recall': 0.14, 'f1-score': 0.13482783882783886, 'support': 50.0}}
- **Macro Precision:** 0.103
- **Macro Recall:** 0.104
- **Macro F1:** 0.094
- **Weighted F1:** 0.135
- **Confusion Matrix:** [[0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 2, 0, 3, 0, 1, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 1, 1, 0, 0, 2, 1, 0, 0], [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0], [0, 0, 2, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0], [1, 1, 2, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'M', 'T', 'W']
- **Top Confused Pairs:** [('D', 'F', 3), ('E', 'A', 3), ('H', 'I', 3), ('E', 'J', 2), ('I', 'C', 2), ('J', 'C', 2), ('A', 'C', 1), ('A', 'D', 1), ('A', 'E', 1), ('A', 'I', 1)]
- **True Class Distribution:** {'D': 7, 'G': 5, 'E': 8, 'J': 7, 'A': 4, 'F': 3, 'I': 6, 'H': 4, 'C': 5, 'B': 1}
- **Pred Class Distribution:** {'D': 3, 'C': 9, 'F': 6, 'J': 5, 'A': 7, 'E': 3, 'I': 7, 'G': 3, 'H': 3, 'B': 1, 'W': 1, 'M': 1, 'T': 1}
- **Num Classes:** 13

