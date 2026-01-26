# Experiment: Afrimedqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-20 12:14:26  
**Duration:** 2 minutes 39 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
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
  output_format: plain
  answer_first: false
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: afrimedqa
  filename: afrimedqa/mcq.jsonl
  split: mcq
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
  dataset=afrimedqa
```

## Results

- **Accuracy:** 54.0%
- **Samples Processed:** 50
- **Correct:** 27
- **Incorrect:** 23
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'A': {'precision': 0.39285714285714285, 'recall': 0.8461538461538461, 'f1-score': 0.5365853658536586, 'support': 13.0}, 'B': {'precision': 1.0, 'recall': 0.45454545454545453, 'f1-score': 0.625, 'support': 11.0}, 'C': {'precision': 0.6666666666666666, 'recall': 0.2857142857142857, 'f1-score': 0.4, 'support': 7.0}, 'D': {'precision': 0.6923076923076923, 'recall': 0.5625, 'f1-score': 0.6206896551724138, 'support': 16.0}, 'E': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'accuracy': 0.54, 'macro avg': {'precision': 0.4586385836385836, 'recall': 0.3581522644022644, 'f1-score': 0.36371250350434536, 'support': 50.0}, 'weighted avg': {'precision': 0.637014652014652, 'recall': 0.54, 'f1-score': 0.5316328847771237, 'support': 50.0}}
- **Macro Precision:** 0.459
- **Macro Recall:** 0.358
- **Macro F1:** 0.364
- **Weighted F1:** 0.532
- **Confusion Matrix:** [[0, 0, 0, 0, 0, 0], [1, 11, 0, 1, 0, 0], [0, 5, 5, 0, 1, 0], [0, 3, 0, 2, 2, 0], [0, 7, 0, 0, 9, 0], [0, 2, 0, 0, 1, 0]]
- **Class Labels:** ['', 'A', 'B', 'C', 'D', 'E']
- **Top Confused Pairs:** [('D', 'A', 7), ('B', 'A', 5), ('C', 'A', 3), ('C', 'D', 2), ('E', 'A', 2), ('A', '', 1), ('A', 'C', 1), ('B', 'D', 1), ('E', 'D', 1)]
- **True Class Distribution:** {'D': 16, 'A': 13, 'B': 11, 'E': 3, 'C': 7}
- **Pred Class Distribution:** {'A': 28, 'B': 5, 'D': 13, 'C': 3, '': 1}
- **Num Classes:** 6

