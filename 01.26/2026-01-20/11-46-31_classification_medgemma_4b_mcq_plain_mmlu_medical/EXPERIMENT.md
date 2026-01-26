# Experiment: Mmlu_medical Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-20 11:46:31  
**Duration:** 2 minutes 38 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** mmlu_medical

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
  _target_: cotlab.datasets.loaders.MMLUMedicalDataset
  name: mmlu_medical
  filename: mmlu/medical_test.jsonl
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
  dataset=mmlu_medical
```

## Results

- **Accuracy:** 55.1%
- **Samples Processed:** 50
- **Correct:** 27
- **Incorrect:** 22
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.5454545454545454, 'recall': 0.8, 'f1-score': 0.6486486486486487, 'support': 15.0}, 'B': {'precision': 0.5, 'recall': 0.45454545454545453, 'f1-score': 0.47619047619047616, 'support': 11.0}, 'C': {'precision': 0.4444444444444444, 'recall': 0.4, 'f1-score': 0.42105263157894735, 'support': 10.0}, 'D': {'precision': 0.75, 'recall': 0.46153846153846156, 'f1-score': 0.5714285714285714, 'support': 13.0}, 'accuracy': 0.5510204081632653, 'macro avg': {'precision': 0.5599747474747474, 'recall': 0.5290209790209791, 'f1-score': 0.5293300819616609, 'support': 49.0}, 'weighted avg': {'precision': 0.5689033189033189, 'recall': 0.5510204081632653, 'f1-score': 0.5429984226976707, 'support': 49.0}}
- **Macro Precision:** 0.560
- **Macro Recall:** 0.529
- **Macro F1:** 0.529
- **Weighted F1:** 0.543
- **Confusion Matrix:** [[12, 2, 1, 0], [2, 5, 3, 1], [3, 2, 4, 1], [5, 1, 1, 6]]
- **Class Labels:** ['A', 'B', 'C', 'D']
- **Top Confused Pairs:** [('D', 'A', 5), ('B', 'C', 3), ('C', 'A', 3), ('A', 'B', 2), ('B', 'A', 2), ('C', 'B', 2), ('A', 'C', 1), ('B', 'D', 1), ('C', 'D', 1), ('D', 'B', 1)]
- **True Class Distribution:** {'C': 10, 'B': 11, 'A': 15, 'D': 13}
- **Pred Class Distribution:** {'A': 22, 'D': 8, 'B': 10, 'C': 9}
- **Num Classes:** 4

