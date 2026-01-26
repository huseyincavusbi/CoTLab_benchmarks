# Experiment: Medqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-21 08:19:14  
**Duration:** 1 minutes 57 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
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
  prompt.output_format=plain \
  dataset=medqa
```

## Results

- **Accuracy:** 50.0%
- **Samples Processed:** 10
- **Correct:** 5
- **Incorrect:** 5
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.75, 'recall': 0.6, 'f1-score': 0.6666666666666666, 'support': 5.0}, 'B': {'precision': 0.5, 'recall': 1.0, 'f1-score': 0.6666666666666666, 'support': 1.0}, 'C': {'precision': 1.0, 'recall': 0.5, 'f1-score': 0.6666666666666666, 'support': 2.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 2.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.5, 'macro avg': {'precision': 0.45, 'recall': 0.42000000000000004, 'f1-score': 0.4, 'support': 10.0}, 'weighted avg': {'precision': 0.625, 'recall': 0.5, 'f1-score': 0.5333333333333333, 'support': 10.0}}
- **Macro Precision:** 0.450
- **Macro Recall:** 0.420
- **Macro F1:** 0.400
- **Weighted F1:** 0.533
- **Confusion Matrix:** [[3, 0, 0, 0, 2], [0, 1, 0, 0, 0], [0, 0, 1, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'I']
- **Top Confused Pairs:** [('A', 'I', 2), ('C', 'D', 1), ('D', 'A', 1), ('D', 'B', 1)]
- **True Class Distribution:** {'A': 5, 'D': 2, 'B': 1, 'C': 2}
- **Pred Class Distribution:** {'A': 4, 'B': 2, 'D': 1, 'I': 2, 'C': 1}
- **Num Classes:** 5

