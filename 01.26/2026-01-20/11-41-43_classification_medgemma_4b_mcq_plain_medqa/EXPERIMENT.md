# Experiment: Medqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-20 11:41:43  
**Duration:** 3 minutes 13 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** medqa

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
  output_format: plain
  answer_first: false
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medqa
  filename: medqa/test.jsonl
  split: test
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
  prompt=mcq \
  prompt.output_format=plain \
  dataset=medqa
```

## Results

- **Accuracy:** 52.0%
- **Samples Processed:** 50
- **Correct:** 26
- **Incorrect:** 24
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.47619047619047616, 'recall': 0.6666666666666666, 'f1-score': 0.5555555555555556, 'support': 15.0}, 'B': {'precision': 0.6666666666666666, 'recall': 0.4444444444444444, 'f1-score': 0.5333333333333333, 'support': 9.0}, 'C': {'precision': 0.5, 'recall': 0.5384615384615384, 'f1-score': 0.5185185185185185, 'support': 13.0}, 'D': {'precision': 0.5555555555555556, 'recall': 0.38461538461538464, 'f1-score': 0.45454545454545453, 'support': 13.0}, 'accuracy': 0.52, 'macro avg': {'precision': 0.5496031746031746, 'recall': 0.5085470085470085, 'f1-score': 0.5154882154882156, 'support': 50.0}, 'weighted avg': {'precision': 0.5373015873015873, 'recall': 0.52, 'f1-score': 0.5156632996632997, 'support': 50.0}}
- **Macro Precision:** 0.550
- **Macro Recall:** 0.509
- **Macro F1:** 0.515
- **Weighted F1:** 0.516
- **Confusion Matrix:** [[10, 1, 2, 2], [1, 4, 4, 0], [4, 0, 7, 2], [6, 1, 1, 5]]
- **Class Labels:** ['A', 'B', 'C', 'D']
- **Top Confused Pairs:** [('D', 'A', 6), ('B', 'C', 4), ('C', 'A', 4), ('A', 'C', 2), ('A', 'D', 2), ('C', 'D', 2), ('A', 'B', 1), ('B', 'A', 1), ('D', 'B', 1), ('D', 'C', 1)]
- **True Class Distribution:** {'A': 15, 'D': 13, 'B': 9, 'C': 13}
- **Pred Class Distribution:** {'A': 21, 'D': 9, 'C': 14, 'B': 6}
- **Num Classes:** 4

