# Experiment: Medbullets Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-10 16:13:18  
**Duration:** 16 minutes 33 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
**Output Format:** JSON
**Dataset:** medbullets

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
  temperature: 1.0
  top_p: 0.9
  safe_name: medgemma_4b
prompt:
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: false
  output_format: json
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MedBulletsDataset
  name: medbullets
  split: op4_test
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 308
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=308 \
  prompt=mcq \
  prompt.few_shot=false \
  dataset=medbullets
```

## Results

- **Accuracy:** 41.5%
- **Samples Processed:** 308
- **Correct:** 127
- **Incorrect:** 179
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.39080459770114945, 'recall': 0.3953488372093023, 'f1-score': 0.3930635838150289, 'support': 86.0}, 'B': {'precision': 0.5217391304347826, 'recall': 0.47368421052631576, 'f1-score': 0.496551724137931, 'support': 76.0}, 'C': {'precision': 0.421875, 'recall': 0.35064935064935066, 'f1-score': 0.3829787234042553, 'support': 77.0}, 'D': {'precision': 0.38461538461538464, 'recall': 0.44776119402985076, 'f1-score': 0.41379310344827586, 'support': 67.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'U': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.4150326797385621, 'macro avg': {'precision': 0.21487926409391458, 'recall': 0.20843044905185243, 'f1-score': 0.21079839185068638, 'support': 306.0}, 'weighted avg': {'precision': 0.4297875002763827, 'recall': 0.4150326797385621, 'f1-score': 0.4207676433847627, 'support': 306.0}}
- **Macro Precision:** 0.215
- **Macro Recall:** 0.208
- **Macro F1:** 0.211
- **Weighted F1:** 0.421
- **Confusion Matrix:** [[34, 11, 13, 24, 1, 1, 2, 0], [15, 36, 13, 12, 0, 0, 0, 0], [21, 16, 27, 12, 0, 0, 0, 1], [17, 6, 11, 30, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'L', 'S', 'T', 'U']
- **Top Confused Pairs:** [('A', 'D', 24), ('C', 'A', 21), ('D', 'A', 17), ('C', 'B', 16), ('B', 'A', 15), ('A', 'C', 13), ('B', 'C', 13), ('B', 'D', 12), ('C', 'D', 12), ('A', 'B', 11)]
- **True Class Distribution:** {'B': 76, 'D': 67, 'C': 77, 'A': 86}
- **Pred Class Distribution:** {'B': 69, 'D': 78, 'A': 87, 'C': 64, 'T': 3, 'U': 2, 'S': 2, 'L': 1}
- **Num Classes:** 8

