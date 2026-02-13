# Experiment: Plab Standard

**Status:** Completed
**Started:** 2026-02-12 07:43:39  
**Duration:** 15 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Pubhealthbench
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** plab

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
  max_new_tokens: 32
  temperature: 0
  top_p: 1
  safe_name: medgemma_4b
prompt:
  _target_: cotlab.prompts.pubhealthbench.PubHealthBenchMCQPromptStrategy
  name: pubhealthbench
  output_format: json
dataset:
  _target_: cotlab.datasets.loaders.PLABDataset
  name: plab
  split: main
  filename: plab/data.json
  topics_filename: plab/topics.json
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 100
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=100 \
  prompt=pubhealthbench \
  dataset=plab
```

## Results

- **Accuracy:** 54.0%
- **Samples Processed:** 100
- **Correct:** 54
- **Incorrect:** 46
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.6923076923076923, 'recall': 0.5806451612903226, 'f1-score': 0.631578947368421, 'support': 31.0}, 'B': {'precision': 0.631578947368421, 'recall': 0.6, 'f1-score': 0.6153846153846154, 'support': 20.0}, 'C': {'precision': 0.4444444444444444, 'recall': 0.7058823529411765, 'f1-score': 0.5454545454545454, 'support': 17.0}, 'D': {'precision': 0.5714285714285714, 'recall': 0.42105263157894735, 'f1-score': 0.48484848484848486, 'support': 19.0}, 'E': {'precision': 0.3076923076923077, 'recall': 0.3333333333333333, 'f1-score': 0.32, 'support': 12.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'accuracy': 0.54, 'macro avg': {'precision': 0.4412419938735728, 'recall': 0.44015224652396334, 'f1-score': 0.43287776550934437, 'support': 100.0}, 'weighted avg': {'precision': 0.5619812351391298, 'recall': 0.54, 'f1-score': 0.5421148816096185, 'support': 100.0}}
- **Macro Precision:** 0.441
- **Macro Recall:** 0.440
- **Macro F1:** 0.433
- **Weighted F1:** 0.542
- **Confusion Matrix:** [[18, 3, 4, 1, 5, 0], [4, 12, 2, 2, 0, 0], [0, 2, 12, 1, 2, 0], [3, 1, 4, 8, 2, 1], [1, 1, 5, 1, 4, 0], [0, 0, 0, 1, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'G']
- **Top Confused Pairs:** [('A', 'E', 5), ('E', 'C', 5), ('A', 'C', 4), ('B', 'A', 4), ('D', 'C', 4), ('A', 'B', 3), ('D', 'A', 3), ('B', 'C', 2), ('B', 'D', 2), ('C', 'B', 2)]
- **True Class Distribution:** {'B': 20, 'C': 17, 'D': 19, 'A': 31, 'E': 12, 'G': 1}
- **Pred Class Distribution:** {'B': 19, 'C': 27, 'E': 13, 'A': 26, 'D': 14, 'G': 1}
- **Num Classes:** 6

