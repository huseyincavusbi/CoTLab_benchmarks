# Experiment: Medqa Contrarian (PLAIN)

**Status:** Completed
**Started:** 2026-01-21 08:43:51  
**Duration:** 1 minutes 57 seconds

## Research Questions

1. Does skeptical/contrarian reasoning improve diagnostic accuracy?
2. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Contrarian (skeptical)
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** medqa

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
  contrarian: true
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medqa
  filename: medqa/test.jsonl
  split: test
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 10
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  prompt=mcq \
  prompt.contrarian=true \
  prompt.output_format=plain \
  dataset=medqa
```

## Results

- **Accuracy:** 20.0%
- **Samples Processed:** 10
- **Correct:** 2
- **Incorrect:** 8
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.5, 'recall': 0.2, 'f1-score': 0.2857142857142857, 'support': 5.0}, 'B': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'C': {'precision': 0.2, 'recall': 0.5, 'f1-score': 0.2857142857142857, 'support': 2.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 2.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.2, 'macro avg': {'precision': 0.13999999999999999, 'recall': 0.13999999999999999, 'f1-score': 0.11428571428571428, 'support': 10.0}, 'weighted avg': {'precision': 0.29, 'recall': 0.2, 'f1-score': 0.19999999999999998, 'support': 10.0}}
- **Macro Precision:** 0.140
- **Macro Recall:** 0.140
- **Macro F1:** 0.114
- **Weighted F1:** 0.200
- **Confusion Matrix:** [[1, 0, 3, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'I']
- **Top Confused Pairs:** [('A', 'C', 3), ('A', 'I', 1), ('B', 'C', 1), ('C', 'I', 1), ('D', 'A', 1), ('D', 'B', 1)]
- **True Class Distribution:** {'A': 5, 'D': 2, 'B': 1, 'C': 2}
- **Pred Class Distribution:** {'C': 5, 'B': 1, 'I': 2, 'A': 2}
- **Num Classes:** 5

