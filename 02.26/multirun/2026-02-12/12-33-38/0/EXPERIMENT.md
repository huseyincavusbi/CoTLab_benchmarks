# Experiment: Plab Standard

**Status:** Completed
**Started:** 2026-02-12 12:33:38  
**Duration:** 17 minutes 3 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
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
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: true
  output_format: json
  answer_first: false
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
  prompt=mcq \
  dataset=plab
```

## Results

- **Accuracy:** 52.0%
- **Samples Processed:** 1652
- **Correct:** 733
- **Incorrect:** 676
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.5158371040723982, 'recall': 0.6015831134564644, 'f1-score': 0.5554202192448234, 'support': 379.0}, 'B': {'precision': 0.75, 'recall': 0.49572649572649574, 'f1-score': 0.5969125214408233, 'support': 351.0}, 'C': {'precision': 0.6046511627906976, 'recall': 0.47101449275362317, 'f1-score': 0.5295315682281059, 'support': 276.0}, 'D': {'precision': 0.585, 'recall': 0.4978723404255319, 'f1-score': 0.5379310344827586, 'support': 235.0}, 'E': {'precision': 0.43010752688172044, 'recall': 0.5161290322580645, 'f1-score': 0.46920821114369504, 'support': 155.0}, 'F': {'precision': 0.3, 'recall': 0.3333333333333333, 'f1-score': 0.3157894736842105, 'support': 9.0}, 'G': {'precision': 0.5, 'recall': 0.25, 'f1-score': 0.3333333333333333, 'support': 4.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'M': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'R': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.5202271114265437, 'macro avg': {'precision': 0.18427978968724082, 'recall': 0.15828294039767568, 'f1-score': 0.1669063180778875, 'support': 1409.0}, 'weighted avg': {'precision': 0.5922481547482882, 'recall': 0.5202271114265437, 'f1-score': 0.5461233324185141, 'support': 1409.0}}
- **Macro Precision:** 0.184
- **Macro Recall:** 0.158
- **Macro F1:** 0.167
- **Weighted F1:** 0.546
- **Confusion Matrix:** [[228, 29, 32, 28, 28, 2, 0, 1, 1, 4, 7, 2, 1, 0, 0, 0, 1, 2, 2, 11], [63, 174, 29, 25, 29, 1, 0, 1, 2, 2, 2, 1, 0, 4, 1, 0, 3, 2, 2, 10], [66, 10, 130, 20, 28, 2, 0, 2, 1, 2, 3, 1, 0, 1, 0, 1, 0, 0, 2, 7], [52, 7, 14, 117, 21, 2, 1, 3, 2, 0, 1, 0, 0, 1, 1, 0, 3, 0, 2, 8], [29, 12, 9, 10, 80, 0, 0, 0, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 7], [3, 0, 1, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X']
- **Top Confused Pairs:** [('C', 'A', 66), ('B', 'A', 63), ('D', 'A', 52), ('A', 'C', 32), ('A', 'B', 29), ('B', 'C', 29), ('B', 'E', 29), ('E', 'A', 29), ('A', 'D', 28), ('A', 'E', 28)]
- **True Class Distribution:** {'B': 351, 'C': 276, 'D': 235, 'A': 379, 'E': 155, 'F': 9, 'G': 4}
- **Pred Class Distribution:** {'B': 232, 'D': 200, 'A': 442, 'K': 11, 'C': 215, 'E': 186, 'H': 7, 'S': 7, 'X': 44, 'F': 10, 'M': 4, 'I': 10, 'P': 6, 'L': 15, 'V': 9, 'N': 1, 'Q': 3, 'T': 4, 'R': 1, 'G': 2}
- **Num Classes:** 20

