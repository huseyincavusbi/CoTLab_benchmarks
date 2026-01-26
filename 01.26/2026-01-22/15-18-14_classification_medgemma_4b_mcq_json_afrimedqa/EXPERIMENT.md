# Experiment: Afrimedqa Standard

**Status:** Completed
**Started:** 2026-01-22 15:18:14  
**Duration:** 2 minutes 1 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
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
  answer_first: false
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
  dataset=afrimedqa
```

## Results

- **Accuracy:** 55.0%
- **Samples Processed:** 20
- **Correct:** 11
- **Incorrect:** 9
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.25, 'recall': 0.25, 'f1-score': 0.25, 'support': 4.0}, 'B': {'precision': 0.5714285714285714, 'recall': 0.6666666666666666, 'f1-score': 0.6153846153846154, 'support': 6.0}, 'C': {'precision': 0.6666666666666666, 'recall': 0.6666666666666666, 'f1-score': 0.6666666666666666, 'support': 3.0}, 'D': {'precision': 0.6, 'recall': 0.6, 'f1-score': 0.6, 'support': 5.0}, 'E': {'precision': 1.0, 'recall': 0.5, 'f1-score': 0.6666666666666666, 'support': 2.0}, 'accuracy': 0.55, 'macro avg': {'precision': 0.6176190476190476, 'recall': 0.5366666666666666, 'f1-score': 0.5597435897435897, 'support': 20.0}, 'weighted avg': {'precision': 0.5714285714285714, 'recall': 0.55, 'f1-score': 0.5512820512820513, 'support': 20.0}}
- **Macro Precision:** 0.618
- **Macro Recall:** 0.537
- **Macro F1:** 0.560
- **Weighted F1:** 0.551
- **Confusion Matrix:** [[1, 1, 1, 1, 0], [2, 4, 0, 0, 0], [0, 1, 2, 0, 0], [1, 1, 0, 3, 0], [0, 0, 0, 1, 1]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E']
- **Top Confused Pairs:** [('B', 'A', 2), ('A', 'B', 1), ('A', 'C', 1), ('A', 'D', 1), ('C', 'B', 1), ('D', 'A', 1), ('D', 'B', 1), ('E', 'D', 1)]
- **True Class Distribution:** {'D': 5, 'A': 4, 'B': 6, 'E': 2, 'C': 3}
- **Pred Class Distribution:** {'D': 5, 'A': 4, 'B': 7, 'C': 3, 'E': 1}
- **Num Classes:** 5

