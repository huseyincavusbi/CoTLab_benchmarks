# Experiment: Plab Answer-First

**Status:** Completed
**Started:** 2026-02-12 08:15:09  
**Duration:** 4 minutes 7 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Plab
**Reasoning Mode:** Answer-First
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
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_4b
prompt:
  _target_: cotlab.prompts.PLABPromptStrategy
  name: plab
  few_shot: true
  output_format: json
  answer_first: true
  contrarian: false
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
  prompt=plab \
  prompt.answer_first=true \
  dataset=plab
```

## Results

- **Accuracy:** 55.0%
- **Samples Processed:** 100
- **Correct:** 55
- **Incorrect:** 45
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.6785714285714286, 'recall': 0.6129032258064516, 'f1-score': 0.6440677966101694, 'support': 31.0}, 'B': {'precision': 0.39285714285714285, 'recall': 0.55, 'f1-score': 0.4583333333333333, 'support': 20.0}, 'C': {'precision': 0.5416666666666666, 'recall': 0.7647058823529411, 'f1-score': 0.6341463414634146, 'support': 17.0}, 'D': {'precision': 0.7272727272727273, 'recall': 0.42105263157894735, 'f1-score': 0.5333333333333333, 'support': 19.0}, 'E': {'precision': 0.4444444444444444, 'recall': 0.3333333333333333, 'f1-score': 0.38095238095238093, 'support': 12.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'accuracy': 0.55, 'macro avg': {'precision': 0.46413540163540173, 'recall': 0.44699917884527895, 'f1-score': 0.4418055309487719, 'support': 100.0}, 'weighted avg': {'precision': 0.5725270562770564, 'recall': 0.55, 'f1-score': 0.5461801807122186, 'support': 100.0}}
- **Macro Precision:** 0.464
- **Macro Recall:** 0.447
- **Macro F1:** 0.442
- **Weighted F1:** 0.546
- **Confusion Matrix:** [[19, 5, 3, 1, 3, 0], [5, 11, 3, 0, 1, 0], [0, 3, 13, 0, 1, 0], [3, 6, 2, 8, 0, 0], [1, 3, 3, 1, 4, 0], [0, 0, 0, 1, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'G']
- **Top Confused Pairs:** [('D', 'B', 6), ('A', 'B', 5), ('B', 'A', 5), ('A', 'C', 3), ('A', 'E', 3), ('B', 'C', 3), ('C', 'B', 3), ('D', 'A', 3), ('E', 'B', 3), ('E', 'C', 3)]
- **True Class Distribution:** {'B': 20, 'C': 17, 'D': 19, 'A': 31, 'E': 12, 'G': 1}
- **Pred Class Distribution:** {'A': 28, 'B': 28, 'C': 24, 'E': 9, 'D': 11}
- **Num Classes:** 6

