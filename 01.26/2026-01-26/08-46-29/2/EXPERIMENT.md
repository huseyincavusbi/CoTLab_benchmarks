# Experiment: Medmcqa Answer-First

**Status:** Completed
**Started:** 2026-01-26 08:59:04  
**Duration:** 5 minutes 16 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medmcqa

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
  answer_first: true
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medmcqa
  filename: medmcqa/validation.jsonl
  split: validation
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
  prompt.answer_first=true \
  dataset=medmcqa
```

## Results

- **Accuracy:** 46.4%
- **Samples Processed:** 4183
- **Correct:** 1941
- **Incorrect:** 2241
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.5423011844331641, 'recall': 0.4755192878338279, 'f1-score': 0.5067193675889328, 'support': 1348.0}, 'B': {'precision': 0.4587400177462289, 'recall': 0.47649769585253454, 'f1-score': 0.4674502712477396, 'support': 1085.0}, 'C': {'precision': 0.4728682170542636, 'recall': 0.4621212121212121, 'f1-score': 0.4674329501915709, 'support': 924.0}, 'D': {'precision': 0.4599483204134367, 'recall': 0.4315151515151515, 'f1-score': 0.4452782989368355, 'support': 825.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'M': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Y': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Z': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.46413199426111906, 'macro avg': {'precision': 0.19338577396470932, 'recall': 0.1845653347322726, 'f1-score': 0.18868808879650786, 'support': 4182.0}, 'weighted avg': {'precision': 0.48903455589904077, 'recall': 0.46413199426111906, 'f1-score': 0.47573024734901476, 'support': 4182.0}}
- **Macro Precision:** 0.193
- **Macro Recall:** 0.185
- **Macro F1:** 0.189
- **Weighted F1:** 0.476
- **Confusion Matrix:** [[641, 304, 183, 150, 1, 1, 2, 66, 0, 0], [213, 517, 161, 144, 0, 0, 1, 48, 1, 0], [165, 169, 427, 124, 0, 0, 0, 38, 0, 1], [163, 137, 132, 356, 0, 0, 0, 37, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'F', 'M', 'T', 'X', 'Y', 'Z']
- **Top Confused Pairs:** [('A', 'B', 304), ('B', 'A', 213), ('A', 'C', 183), ('C', 'B', 169), ('C', 'A', 165), ('D', 'A', 163), ('B', 'C', 161), ('A', 'D', 150), ('B', 'D', 144), ('D', 'B', 137)]
- **True Class Distribution:** {'A': 1348, 'C': 924, 'B': 1085, 'D': 825}
- **Pred Class Distribution:** {'A': 1182, 'B': 1127, 'C': 903, 'D': 774, 'X': 189, 'T': 3, 'M': 1, 'Y': 1, 'F': 1, 'Z': 1}
- **Num Classes:** 10

