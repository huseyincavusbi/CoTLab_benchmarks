# Experiment: Pubhealthbench Standard

**Status:** Completed
**Started:** 2026-02-03 11:14:11  
**Duration:** 2 minutes 47 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Pubhealthbench
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** pubhealthbench

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
  _target_: cotlab.prompts.pubhealthbench.PubHealthBenchMCQPromptStrategy
  name: pubhealthbench
  output_format: json
dataset:
  _target_: cotlab.datasets.loaders.PubHealthBenchDataset
  name: pubhealthbench
  split: reviewed
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
  experiment=classification \
  experiment.num_samples=50 \
  prompt=pubhealthbench \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 68.0%
- **Samples Processed:** 50
- **Correct:** 34
- **Incorrect:** 16
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.875, 'recall': 0.7777777777777778, 'f1-score': 0.8235294117647058, 'support': 9.0}, 'B': {'precision': 0.7142857142857143, 'recall': 0.7142857142857143, 'f1-score': 0.7142857142857143, 'support': 7.0}, 'C': {'precision': 0.5, 'recall': 0.5555555555555556, 'f1-score': 0.5263157894736842, 'support': 9.0}, 'D': {'precision': 0.8333333333333334, 'recall': 0.625, 'f1-score': 0.7142857142857143, 'support': 8.0}, 'E': {'precision': 0.6, 'recall': 0.75, 'f1-score': 0.6666666666666666, 'support': 4.0}, 'F': {'precision': 0.6666666666666666, 'recall': 0.8, 'f1-score': 0.7272727272727273, 'support': 5.0}, 'G': {'precision': 0.625, 'recall': 0.625, 'f1-score': 0.625, 'support': 8.0}, 'accuracy': 0.68, 'macro avg': {'precision': 0.6877551020408165, 'recall': 0.692517006802721, 'f1-score': 0.685336574821316, 'support': 50.0}, 'weighted avg': {'precision': 0.6955, 'recall': 0.68, 'f1-score': 0.6833184565692306, 'support': 50.0}}
- **Macro Precision:** 0.688
- **Macro Recall:** 0.693
- **Macro F1:** 0.685
- **Weighted F1:** 0.683
- **Confusion Matrix:** [[7, 0, 1, 0, 0, 0, 1], [0, 5, 0, 0, 1, 1, 0], [0, 2, 5, 0, 0, 1, 1], [1, 0, 0, 5, 1, 0, 1], [0, 0, 1, 0, 3, 0, 0], [0, 0, 0, 1, 0, 4, 0], [0, 0, 3, 0, 0, 0, 5]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Top Confused Pairs:** [('G', 'C', 3), ('C', 'B', 2), ('A', 'C', 1), ('A', 'G', 1), ('B', 'E', 1), ('B', 'F', 1), ('C', 'F', 1), ('C', 'G', 1), ('D', 'A', 1), ('D', 'E', 1)]
- **True Class Distribution:** {'B': 7, 'G': 8, 'D': 8, 'A': 9, 'E': 4, 'C': 9, 'F': 5}
- **Pred Class Distribution:** {'B': 7, 'G': 8, 'D': 6, 'A': 8, 'E': 5, 'F': 6, 'C': 10}
- **Num Classes:** 7

