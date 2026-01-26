# Experiment: Medqa Answer-First (PLAIN)

**Status:** Completed
**Started:** 2026-01-22 13:08:44  
**Duration:** 2 minutes 1 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?
2. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
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
  prompt.output_format=plain \
  dataset=medqa
```

## Results

- **Accuracy:** 40.0%
- **Samples Processed:** 20
- **Correct:** 8
- **Incorrect:** 12
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.75, 'recall': 0.375, 'f1-score': 0.5, 'support': 8.0}, 'B': {'precision': 0.3333333333333333, 'recall': 0.25, 'f1-score': 0.2857142857142857, 'support': 4.0}, 'C': {'precision': 0.6, 'recall': 0.6, 'f1-score': 0.6, 'support': 5.0}, 'D': {'precision': 0.25, 'recall': 0.3333333333333333, 'f1-score': 0.2857142857142857, 'support': 3.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.4, 'macro avg': {'precision': 0.3866666666666666, 'recall': 0.31166666666666665, 'f1-score': 0.33428571428571424, 'support': 20.0}, 'weighted avg': {'precision': 0.5541666666666666, 'recall': 0.4, 'f1-score': 0.45, 'support': 20.0}}
- **Macro Precision:** 0.387
- **Macro Recall:** 0.312
- **Macro F1:** 0.334
- **Weighted F1:** 0.450
- **Confusion Matrix:** [[3, 1, 0, 2, 2], [0, 1, 1, 0, 2], [1, 0, 3, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'I']
- **Top Confused Pairs:** [('A', 'D', 2), ('A', 'I', 2), ('B', 'I', 2), ('A', 'B', 1), ('B', 'C', 1), ('C', 'A', 1), ('C', 'D', 1), ('D', 'B', 1), ('D', 'C', 1)]
- **True Class Distribution:** {'A': 8, 'D': 3, 'B': 4, 'C': 5}
- **Pred Class Distribution:** {'B': 3, 'D': 4, 'I': 4, 'A': 4, 'C': 5}
- **Num Classes:** 5

