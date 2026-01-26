# Experiment: Pubmedqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-20 11:54:52  
**Duration:** 3 minutes 40 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** pubmedqa

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
  _target_: cotlab.datasets.loaders.PubMedQADataset
  name: pubmedqa
  filename: pubmedqa/test.jsonl
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
  dataset=pubmedqa
```

## Results

- **Accuracy:** 0.0%
- **Samples Processed:** 50
- **Correct:** 0
- **Incorrect:** 46
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'B': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'C': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'maybe': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'no': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 13.0}, 'yes': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 30.0}, 'accuracy': 0.0, 'macro avg': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 46.0}, 'weighted avg': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 46.0}}
- **Macro Precision:** 0.000
- **Macro Recall:** 0.000
- **Macro F1:** 0.000
- **Weighted F1:** 0.000
- **Confusion Matrix:** [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 0, 1, 0, 0, 0, 0], [3, 7, 1, 2, 0, 0, 0], [18, 8, 2, 2, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'maybe', 'no', 'yes']
- **Top Confused Pairs:** [('yes', 'A', 18), ('yes', 'B', 8), ('no', 'B', 7), ('no', 'A', 3), ('maybe', 'A', 2), ('no', 'D', 2), ('yes', 'C', 2), ('yes', 'D', 2), ('maybe', 'C', 1), ('no', 'C', 1)]
- **True Class Distribution:** {'no': 13, 'yes': 30, 'maybe': 3}
- **Pred Class Distribution:** {'A': 23, 'B': 15, 'D': 4, 'C': 4}
- **Num Classes:** 7

