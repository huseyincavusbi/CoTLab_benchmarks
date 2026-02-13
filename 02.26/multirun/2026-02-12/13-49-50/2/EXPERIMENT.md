# Experiment: Plab Answer-First

**Status:** Completed
**Started:** 2026-02-12 14:04:48  
**Duration:** 4 minutes 9 seconds

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
  prompt=plab \
  prompt.answer_first=true \
  dataset=plab
```

## Results

- **Accuracy:** 69.5%
- **Samples Processed:** 1652
- **Correct:** 1106
- **Incorrect:** 485
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.7160194174757282, 'recall': 0.7007125890736342, 'f1-score': 0.7082833133253301, 'support': 421.0}, 'B': {'precision': 0.6758104738154613, 'recall': 0.7002583979328165, 'f1-score': 0.6878172588832487, 'support': 387.0}, 'C': {'precision': 0.6828571428571428, 'recall': 0.739938080495356, 'f1-score': 0.7102526002971769, 'support': 323.0}, 'D': {'precision': 0.7172131147540983, 'recall': 0.6529850746268657, 'f1-score': 0.68359375, 'support': 268.0}, 'E': {'precision': 0.6666666666666666, 'recall': 0.6477272727272727, 'f1-score': 0.6570605187319885, 'support': 176.0}, 'F': {'precision': 0.875, 'recall': 0.6363636363636364, 'f1-score': 0.7368421052631579, 'support': 11.0}, 'G': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 5.0}, 'accuracy': 0.6951602765556254, 'macro avg': {'precision': 0.761938116509871, 'recall': 0.7254264358885117, 'f1-score': 0.7405499352144146, 'support': 1591.0}, 'weighted avg': {'precision': 0.6962395558479911, 'recall': 0.6951602765556254, 'f1-score': 0.6949938299487707, 'support': 1591.0}}
- **Macro Precision:** 0.762
- **Macro Recall:** 0.725
- **Macro F1:** 0.741
- **Weighted F1:** 0.695
- **Confusion Matrix:** [[295, 55, 29, 21, 21, 0, 0], [34, 271, 46, 22, 14, 0, 0], [34, 25, 239, 13, 12, 0, 0], [31, 28, 25, 175, 9, 0, 0], [17, 21, 10, 13, 114, 1, 0], [1, 1, 1, 0, 1, 7, 0], [0, 0, 0, 0, 0, 0, 5]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Top Confused Pairs:** [('A', 'B', 55), ('B', 'C', 46), ('B', 'A', 34), ('C', 'A', 34), ('D', 'A', 31), ('A', 'C', 29), ('D', 'B', 28), ('C', 'B', 25), ('D', 'C', 25), ('B', 'D', 22)]
- **True Class Distribution:** {'B': 387, 'C': 323, 'D': 268, 'A': 421, 'E': 176, 'G': 5, 'F': 11}
- **Pred Class Distribution:** {'B': 401, 'C': 350, 'A': 412, 'D': 244, 'E': 171, 'F': 8, 'G': 5}
- **Num Classes:** 7

