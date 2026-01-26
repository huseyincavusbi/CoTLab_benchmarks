# Experiment: Medqa Answer-First Zero-Shot (PLAIN)

**Status:** Completed
**Started:** 2026-01-21 09:59:57  
**Duration:** 1 minutes 56 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does "answer first, then justify" reasoning order affect performance?
3. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** No (zero-shot)
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
  few_shot: false
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
  prompt.answer_first=true \
  prompt.few_shot=false \
  prompt.output_format=plain \
  dataset=medqa
```

## Results

- **Accuracy:** 30.0%
- **Samples Processed:** 10
- **Correct:** 3
- **Incorrect:** 7
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 1.0, 'recall': 0.4, 'f1-score': 0.5714285714285714, 'support': 5.0}, 'B': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'C': {'precision': 0.5, 'recall': 0.5, 'f1-score': 0.5, 'support': 2.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 2.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.3, 'macro avg': {'precision': 0.3, 'recall': 0.18, 'f1-score': 0.21428571428571427, 'support': 10.0}, 'weighted avg': {'precision': 0.6, 'recall': 0.3, 'f1-score': 0.3857142857142857, 'support': 10.0}}
- **Macro Precision:** 0.300
- **Macro Recall:** 0.180
- **Macro F1:** 0.214
- **Weighted F1:** 0.386
- **Confusion Matrix:** [[2, 1, 1, 0, 1], [0, 0, 0, 0, 1], [0, 0, 1, 1, 0], [0, 0, 0, 0, 2], [0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'I']
- **Top Confused Pairs:** [('D', 'I', 2), ('A', 'B', 1), ('A', 'C', 1), ('A', 'I', 1), ('B', 'I', 1), ('C', 'D', 1)]
- **True Class Distribution:** {'A': 5, 'D': 2, 'B': 1, 'C': 2}
- **Pred Class Distribution:** {'B': 1, 'A': 2, 'C': 2, 'I': 4, 'D': 1}
- **Num Classes:** 5

