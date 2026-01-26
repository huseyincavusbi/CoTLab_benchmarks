# Experiment: Afrimedqa Answer-First

**Status:** Completed
**Started:** 2026-01-22 15:14:48  
**Duration:** 2 minutes 1 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** afrimedqa

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
  name: afrimedqa
  filename: afrimedqa/mcq.jsonl
  split: mcq
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
  dataset=afrimedqa
```

## Results

- **Accuracy:** 55.0%
- **Samples Processed:** 20
- **Correct:** 11
- **Incorrect:** 9
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.6666666666666666, 'recall': 0.5, 'f1-score': 0.5714285714285714, 'support': 4.0}, 'B': {'precision': 0.7142857142857143, 'recall': 0.8333333333333334, 'f1-score': 0.7692307692307693, 'support': 6.0}, 'C': {'precision': 0.5, 'recall': 0.3333333333333333, 'f1-score': 0.4, 'support': 3.0}, 'D': {'precision': 0.5, 'recall': 0.4, 'f1-score': 0.4444444444444444, 'support': 5.0}, 'E': {'precision': 0.3333333333333333, 'recall': 0.5, 'f1-score': 0.4, 'support': 2.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.55, 'macro avg': {'precision': 0.4523809523809524, 'recall': 0.4277777777777778, 'f1-score': 0.43085063085063086, 'support': 20.0}, 'weighted avg': {'precision': 0.5809523809523809, 'recall': 0.55, 'f1-score': 0.5561660561660562, 'support': 20.0}}
- **Macro Precision:** 0.452
- **Macro Recall:** 0.428
- **Macro F1:** 0.431
- **Weighted F1:** 0.556
- **Confusion Matrix:** [[2, 0, 0, 1, 1, 0], [1, 5, 0, 0, 0, 0], [0, 2, 1, 0, 0, 0], [0, 0, 1, 2, 1, 1], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'I']
- **Top Confused Pairs:** [('C', 'B', 2), ('A', 'D', 1), ('A', 'E', 1), ('B', 'A', 1), ('D', 'C', 1), ('D', 'E', 1), ('D', 'I', 1), ('E', 'D', 1)]
- **True Class Distribution:** {'D': 5, 'A': 4, 'B': 6, 'E': 2, 'C': 3}
- **Pred Class Distribution:** {'E': 3, 'A': 3, 'D': 4, 'B': 7, 'C': 2, 'I': 1}
- **Num Classes:** 6

