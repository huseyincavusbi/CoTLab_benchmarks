# Experiment: Medqa Answer-First

**Status:** Completed
**Started:** 2026-01-22 14:53:24  
**Duration:** 2 minutes 2 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
**Output Format:** JSON
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
  output_format: json
  answer_first: true
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medqa
  filename: medqa/test.jsonl
  split: test
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 20
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=20 \
  prompt=mcq \
  prompt.answer_first=true \
  dataset=medqa
```

## Results

- **Accuracy:** 55.0%
- **Samples Processed:** 20
- **Correct:** 11
- **Incorrect:** 9
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.75, 'recall': 0.375, 'f1-score': 0.5, 'support': 8.0}, 'B': {'precision': 0.42857142857142855, 'recall': 0.75, 'f1-score': 0.5454545454545454, 'support': 4.0}, 'C': {'precision': 1.0, 'recall': 0.8, 'f1-score': 0.8888888888888888, 'support': 5.0}, 'D': {'precision': 0.25, 'recall': 0.3333333333333333, 'f1-score': 0.2857142857142857, 'support': 3.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.55, 'macro avg': {'precision': 0.48571428571428577, 'recall': 0.45166666666666666, 'f1-score': 0.44401154401154397, 'support': 20.0}, 'weighted avg': {'precision': 0.6732142857142858, 'recall': 0.55, 'f1-score': 0.5741702741702742, 'support': 20.0}}
- **Macro Precision:** 0.486
- **Macro Recall:** 0.452
- **Macro F1:** 0.444
- **Weighted F1:** 0.574
- **Confusion Matrix:** [[3, 2, 0, 3, 0], [0, 3, 0, 0, 1], [0, 1, 4, 0, 0], [1, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'T']
- **Top Confused Pairs:** [('A', 'D', 3), ('A', 'B', 2), ('B', 'T', 1), ('C', 'B', 1), ('D', 'A', 1), ('D', 'B', 1)]
- **True Class Distribution:** {'A': 8, 'D': 3, 'B': 4, 'C': 5}
- **Pred Class Distribution:** {'B': 7, 'D': 4, 'C': 4, 'A': 4, 'T': 1}
- **Num Classes:** 5

