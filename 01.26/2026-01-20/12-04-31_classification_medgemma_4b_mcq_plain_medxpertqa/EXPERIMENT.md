# Experiment: Medxpertqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-20 12:04:31  
**Duration:** 3 minutes 54 seconds

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

- **Accuracy:** 8.9%
- **Samples Processed:** 50
- **Correct:** 4
- **Incorrect:** 41
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'B': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'C': {'precision': 0.1, 'recall': 0.4, 'f1-score': 0.16, 'support': 5.0}, 'D': {'precision': 0.25, 'recall': 0.3333333333333333, 'f1-score': 0.2857142857142857, 'support': 6.0}, 'E': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 7.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 5.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 4.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 5.0}, 'J': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 6.0}, 'accuracy': 0.08888888888888889, 'macro avg': {'precision': 0.034999999999999996, 'recall': 0.07333333333333333, 'f1-score': 0.044571428571428574, 'support': 45.0}, 'weighted avg': {'precision': 0.044444444444444446, 'recall': 0.08888888888888889, 'f1-score': 0.05587301587301587, 'support': 45.0}}
- **Macro Precision:** 0.035
- **Macro Recall:** 0.073
- **Macro F1:** 0.045
- **Weighted F1:** 0.056
- **Confusion Matrix:** [[0, 0, 3, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [2, 0, 2, 1, 0, 0, 0, 0, 0, 0], [3, 0, 1, 2, 0, 0, 0, 0, 0, 0], [5, 0, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 4, 0, 0, 0, 0, 0, 0, 0], [3, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 3, 1, 0, 0, 0, 0, 0, 0], [1, 0, 4, 1, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
- **Top Confused Pairs:** [('E', 'A', 5), ('G', 'C', 4), ('J', 'C', 4), ('A', 'C', 3), ('D', 'A', 3), ('H', 'A', 3), ('I', 'C', 3), ('C', 'A', 2), ('B', 'D', 1), ('C', 'D', 1)]
- **True Class Distribution:** {'D': 6, 'G': 5, 'E': 7, 'J': 6, 'A': 3, 'F': 3, 'I': 5, 'H': 4, 'C': 5, 'B': 1}
- **Pred Class Distribution:** {'D': 8, 'C': 20, 'A': 17}
- **Num Classes:** 10

