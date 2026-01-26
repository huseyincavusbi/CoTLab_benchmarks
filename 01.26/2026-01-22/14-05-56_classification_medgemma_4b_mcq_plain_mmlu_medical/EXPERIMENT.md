# Experiment: Mmlu_medical Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-22 14:05:56  
**Duration:** 2 minutes 0 seconds

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
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MMLUMedicalDataset
  name: mmlu_medical
  filename: mmlu/medical_test.jsonl
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
  prompt.output_format=plain \
  dataset=mmlu_medical
```

## Results

- **Accuracy:** 20.0%
- **Samples Processed:** 20
- **Correct:** 4
- **Incorrect:** 16
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'A': {'precision': 0.25, 'recall': 0.16666666666666666, 'f1-score': 0.2, 'support': 6.0}, 'B': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 5.0}, 'C': {'precision': 0.6666666666666666, 'recall': 0.4, 'f1-score': 0.5, 'support': 5.0}, 'D': {'precision': 0.5, 'recall': 0.25, 'f1-score': 0.3333333333333333, 'support': 4.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'M': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.2, 'macro avg': {'precision': 0.20238095238095236, 'recall': 0.11666666666666667, 'f1-score': 0.1476190476190476, 'support': 20.0}, 'weighted avg': {'precision': 0.3416666666666667, 'recall': 0.2, 'f1-score': 0.25166666666666665, 'support': 20.0}}
- **Macro Precision:** 0.202
- **Macro Recall:** 0.117
- **Macro F1:** 0.148
- **Weighted F1:** 0.252
- **Confusion Matrix:** [[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 4, 1], [1, 1, 0, 1, 0, 2, 0], [0, 2, 0, 2, 1, 0, 0], [0, 0, 1, 0, 1, 2, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['', 'A', 'B', 'C', 'D', 'I', 'M']
- **Top Confused Pairs:** [('A', 'I', 4), ('B', 'I', 2), ('C', 'A', 2), ('D', 'I', 2), ('A', 'M', 1), ('B', '', 1), ('B', 'A', 1), ('B', 'C', 1), ('C', 'D', 1), ('D', 'B', 1)]
- **True Class Distribution:** {'A': 6, 'C': 5, 'B': 5, 'D': 4}
- **Pred Class Distribution:** {'A': 4, 'I': 8, 'D': 2, 'M': 1, 'B': 1, '': 1, 'C': 3}
- **Num Classes:** 7

