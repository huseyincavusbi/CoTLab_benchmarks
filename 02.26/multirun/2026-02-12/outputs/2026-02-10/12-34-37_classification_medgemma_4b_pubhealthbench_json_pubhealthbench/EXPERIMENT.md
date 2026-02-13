# Experiment: Pubhealthbench Standard

**Status:** Completed
**Started:** 2026-02-10 12:34:38  
**Duration:** 1 minutes 25 seconds

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
  max_new_tokens: 32
  temperature: 0
  top_p: 1
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
  num_samples: 760
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=760 \
  prompt=pubhealthbench \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 78.5%
- **Samples Processed:** 760
- **Correct:** 596
- **Incorrect:** 163
- **Parse Errors:** 1
- **Parse Error Rate:** 0.001
- **Classification Report:** {'A': {'precision': 0.7401574803149606, 'recall': 0.7833333333333333, 'f1-score': 0.7611336032388664, 'support': 120.0}, 'B': {'precision': 0.8828828828828829, 'recall': 0.8376068376068376, 'f1-score': 0.8596491228070176, 'support': 117.0}, 'C': {'precision': 0.6666666666666666, 'recall': 0.8125, 'f1-score': 0.7323943661971831, 'support': 96.0}, 'D': {'precision': 0.7934782608695652, 'recall': 0.776595744680851, 'f1-score': 0.7849462365591398, 'support': 94.0}, 'E': {'precision': 0.7647058823529411, 'recall': 0.7959183673469388, 'f1-score': 0.78, 'support': 98.0}, 'F': {'precision': 0.792, 'recall': 0.853448275862069, 'f1-score': 0.8215767634854771, 'support': 116.0}, 'G': {'precision': 0.8941176470588236, 'recall': 0.6440677966101694, 'f1-score': 0.7487684729064039, 'support': 118.0}, 'accuracy': 0.7852437417654808, 'macro avg': {'precision': 0.7905726885922629, 'recall': 0.7862100507771714, 'f1-score': 0.7840669378848697, 'support': 759.0}, 'weighted avg': {'precision': 0.7944956657185259, 'recall': 0.7852437417654808, 'f1-score': 0.7853852035781881, 'support': 759.0}}
- **Macro Precision:** 0.791
- **Macro Recall:** 0.786
- **Macro F1:** 0.784
- **Weighted F1:** 0.785
- **Confusion Matrix:** [[94, 2, 7, 4, 6, 6, 1], [4, 98, 3, 1, 4, 4, 3], [3, 2, 78, 3, 3, 5, 2], [5, 2, 3, 73, 5, 4, 2], [4, 3, 8, 4, 78, 1, 0], [3, 2, 5, 4, 2, 99, 1], [14, 2, 13, 3, 4, 6, 76]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Top Confused Pairs:** [('G', 'A', 14), ('G', 'C', 13), ('E', 'C', 8), ('A', 'C', 7), ('A', 'E', 6), ('A', 'F', 6), ('G', 'F', 6), ('C', 'F', 5), ('D', 'A', 5), ('D', 'E', 5)]
- **True Class Distribution:** {'F': 116, 'A': 120, 'C': 96, 'G': 118, 'E': 98, 'B': 117, 'D': 94}
- **Pred Class Distribution:** {'F': 125, 'A': 127, 'C': 117, 'G': 85, 'E': 102, 'D': 92, 'B': 111}
- **Num Classes:** 7

