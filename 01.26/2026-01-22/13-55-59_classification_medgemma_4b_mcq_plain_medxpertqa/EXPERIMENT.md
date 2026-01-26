# Experiment: Medxpertqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-22 13:55:59  
**Duration:** 2 minutes 2 seconds

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
  prompt.output_format=plain \
  dataset=medxpertqa
```

## Results

- **Accuracy:** 10.0%
- **Samples Processed:** 20
- **Correct:** 2
- **Incorrect:** 18
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.3333333333333333, 'recall': 0.5, 'f1-score': 0.4, 'support': 2.0}, 'B': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'C': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 2.0}, 'E': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 4.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 2.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'J': {'precision': 0.25, 'recall': 0.5, 'f1-score': 0.3333333333333333, 'support': 2.0}, 'accuracy': 0.1, 'macro avg': {'precision': 0.05833333333333333, 'recall': 0.1, 'f1-score': 0.07333333333333333, 'support': 20.0}, 'weighted avg': {'precision': 0.05833333333333333, 'recall': 0.1, 'f1-score': 0.07333333333333333, 'support': 20.0}}
- **Macro Precision:** 0.058
- **Macro Recall:** 0.100
- **Macro F1:** 0.073
- **Weighted F1:** 0.073
- **Confusion Matrix:** [[1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
- **Top Confused Pairs:** [('D', 'C', 2), ('A', 'E', 1), ('C', 'A', 1), ('E', 'B', 1), ('E', 'G', 1), ('E', 'I', 1), ('E', 'J', 1), ('F', 'G', 1), ('G', 'C', 1), ('G', 'E', 1)]
- **True Class Distribution:** {'D': 2, 'G': 3, 'E': 4, 'J': 2, 'A': 2, 'F': 1, 'I': 3, 'H': 2, 'C': 1}
- **Pred Class Distribution:** {'C': 4, 'I': 2, 'F': 1, 'B': 1, 'E': 2, 'G': 2, 'J': 4, 'D': 1, 'A': 3}
- **Num Classes:** 10

