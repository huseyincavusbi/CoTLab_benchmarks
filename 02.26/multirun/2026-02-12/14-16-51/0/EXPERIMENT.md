# Experiment: Pubhealthbench Standard

**Status:** Completed
**Started:** 2026-02-12 14:16:51  
**Duration:** 41 seconds

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
  max_model_len: null
  quantization: null
  gpu_memory_utilization: 0.9
  enforce_eager: false
  limit_mm_per_prompt: null
model:
  name: google/medgemma-27b-it
  variant: 27b
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b_it
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
  num_samples: -1
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=-1 \
  prompt=pubhealthbench \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 86.0%
- **Samples Processed:** 760
- **Correct:** 650
- **Incorrect:** 106
- **Parse Errors:** 4
- **Parse Error Rate:** 0.005
- **Classification Report:** {'A': {'precision': 0.856, 'recall': 0.8916666666666667, 'f1-score': 0.8734693877551021, 'support': 120.0}, 'B': {'precision': 0.8956521739130435, 'recall': 0.8803418803418803, 'f1-score': 0.8879310344827587, 'support': 117.0}, 'C': {'precision': 0.7368421052631579, 'recall': 0.8842105263157894, 'f1-score': 0.8038277511961722, 'support': 95.0}, 'D': {'precision': 0.8137254901960784, 'recall': 0.8829787234042553, 'f1-score': 0.8469387755102041, 'support': 94.0}, 'E': {'precision': 0.851063829787234, 'recall': 0.8163265306122449, 'f1-score': 0.8333333333333334, 'support': 98.0}, 'F': {'precision': 0.9444444444444444, 'recall': 0.8869565217391304, 'f1-score': 0.9147982062780269, 'support': 115.0}, 'G': {'precision': 0.9285714285714286, 'recall': 0.7777777777777778, 'f1-score': 0.8465116279069768, 'support': 117.0}, 'accuracy': 0.8597883597883598, 'macro avg': {'precision': 0.8608999245964839, 'recall': 0.8600369466939635, 'f1-score': 0.8581157309232248, 'support': 756.0}, 'weighted avg': {'precision': 0.8659520158721887, 'recall': 0.8597883597883598, 'f1-score': 0.8605693911117019, 'support': 756.0}}
- **Macro Precision:** 0.861
- **Macro Recall:** 0.860
- **Macro F1:** 0.858
- **Weighted F1:** 0.861
- **Confusion Matrix:** [[107, 1, 4, 2, 2, 3, 1], [3, 103, 2, 4, 2, 1, 2], [1, 2, 84, 4, 2, 2, 0], [4, 2, 1, 83, 3, 0, 1], [1, 2, 11, 4, 80, 0, 0], [1, 0, 4, 4, 1, 102, 3], [8, 5, 8, 1, 4, 0, 91]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Top Confused Pairs:** [('E', 'C', 11), ('G', 'A', 8), ('G', 'C', 8), ('G', 'B', 5), ('A', 'C', 4), ('B', 'D', 4), ('C', 'D', 4), ('D', 'A', 4), ('E', 'D', 4), ('F', 'C', 4)]
- **True Class Distribution:** {'F': 115, 'A': 120, 'C': 95, 'G': 117, 'E': 98, 'B': 117, 'D': 94}
- **Pred Class Distribution:** {'F': 108, 'A': 125, 'C': 114, 'G': 98, 'E': 94, 'B': 115, 'D': 102}
- **Num Classes:** 7

