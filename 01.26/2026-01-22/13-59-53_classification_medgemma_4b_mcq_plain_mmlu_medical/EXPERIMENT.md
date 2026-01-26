# Experiment: Mmlu_medical Answer-First (PLAIN)

**Status:** Completed
**Started:** 2026-01-22 13:59:53  
**Duration:** 2 minutes 0 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?
2. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
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
  answer_first: true
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
  prompt.answer_first=true \
  prompt.output_format=plain \
  dataset=mmlu_medical
```

## Results

- **Accuracy:** 55.0%
- **Samples Processed:** 20
- **Correct:** 11
- **Incorrect:** 9
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.75, 'recall': 0.5, 'f1-score': 0.6, 'support': 6.0}, 'B': {'precision': 1.0, 'recall': 0.2, 'f1-score': 0.3333333333333333, 'support': 5.0}, 'C': {'precision': 0.5, 'recall': 0.6, 'f1-score': 0.5454545454545454, 'support': 5.0}, 'D': {'precision': 0.8, 'recall': 1.0, 'f1-score': 0.8888888888888888, 'support': 4.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.55, 'macro avg': {'precision': 0.61, 'recall': 0.45999999999999996, 'f1-score': 0.4735353535353536, 'support': 20.0}, 'weighted avg': {'precision': 0.76, 'recall': 0.55, 'f1-score': 0.5774747474747474, 'support': 20.0}}
- **Macro Precision:** 0.610
- **Macro Recall:** 0.460
- **Macro F1:** 0.474
- **Weighted F1:** 0.577
- **Confusion Matrix:** [[3, 0, 0, 0, 3], [0, 1, 3, 0, 1], [1, 0, 3, 1, 0], [0, 0, 0, 4, 0], [0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'I']
- **Top Confused Pairs:** [('A', 'I', 3), ('B', 'C', 3), ('B', 'I', 1), ('C', 'A', 1), ('C', 'D', 1)]
- **True Class Distribution:** {'A': 6, 'C': 5, 'B': 5, 'D': 4}
- **Pred Class Distribution:** {'A': 4, 'C': 6, 'I': 4, 'D': 5, 'B': 1}
- **Num Classes:** 5

