# Experiment: Pubhealthbench Standard

**Status:** Completed
**Started:** 2026-02-03 10:39:36  
**Duration:** 33 minutes 8 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
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
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: true
  output_format: json
  answer_first: false
  contrarian: false
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
  prompt=mcq \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 74.4%
- **Samples Processed:** 760
- **Correct:** 564
- **Incorrect:** 194
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.6814814814814815, 'recall': 0.7666666666666667, 'f1-score': 0.7215686274509804, 'support': 120.0}, 'B': {'precision': 0.7480916030534351, 'recall': 0.8376068376068376, 'f1-score': 0.7903225806451613, 'support': 117.0}, 'C': {'precision': 0.6545454545454545, 'recall': 0.75, 'f1-score': 0.6990291262135923, 'support': 96.0}, 'D': {'precision': 0.8235294117647058, 'recall': 0.7446808510638298, 'f1-score': 0.7821229050279329, 'support': 94.0}, 'E': {'precision': 0.8202247191011236, 'recall': 0.7448979591836735, 'f1-score': 0.7807486631016043, 'support': 98.0}, 'F': {'precision': 0.7863247863247863, 'recall': 0.8, 'f1-score': 0.7931034482758621, 'support': 115.0}, 'G': {'precision': 0.7701149425287356, 'recall': 0.5677966101694916, 'f1-score': 0.6536585365853659, 'support': 118.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.7440633245382586, 'macro avg': {'precision': 0.5284312398799722, 'recall': 0.5211648924690498, 'f1-score': 0.5220553887300499, 'support': 758.0}, 'weighted avg': {'precision': 0.7536089179352599, 'recall': 0.7440633245382586, 'f1-score': 0.7447682048436498, 'support': 758.0}}
- **Macro Precision:** 0.528
- **Macro Recall:** 0.521
- **Macro F1:** 0.522
- **Weighted F1:** 0.745
- **Confusion Matrix:** [[92, 4, 7, 3, 5, 4, 5, 0, 0, 0], [3, 98, 4, 1, 1, 4, 5, 0, 0, 1], [6, 6, 72, 3, 2, 5, 1, 0, 1, 0], [5, 5, 5, 70, 5, 2, 1, 0, 0, 1], [5, 4, 7, 3, 73, 2, 3, 1, 0, 0], [5, 4, 6, 2, 1, 92, 5, 0, 0, 0], [19, 10, 9, 3, 2, 8, 67, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'P', 'T']
- **Top Confused Pairs:** [('G', 'A', 19), ('G', 'B', 10), ('G', 'C', 9), ('G', 'F', 8), ('A', 'C', 7), ('E', 'C', 7), ('C', 'A', 6), ('C', 'B', 6), ('F', 'C', 6), ('A', 'E', 5)]
- **True Class Distribution:** {'F': 115, 'A': 120, 'C': 96, 'G': 118, 'E': 98, 'B': 117, 'D': 94}
- **Pred Class Distribution:** {'F': 117, 'A': 135, 'C': 110, 'G': 87, 'E': 89, 'B': 131, 'D': 85, 'P': 1, 'T': 2, 'H': 1}
- **Num Classes:** 10

