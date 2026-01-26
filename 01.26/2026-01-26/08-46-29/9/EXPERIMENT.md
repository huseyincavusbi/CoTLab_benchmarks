# Experiment: Mmlu_medical Standard

**Status:** Completed
**Started:** 2026-01-26 09:27:01  
**Duration:** 43 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** mmlu_medical

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
  dataset=mmlu_medical
```

## Results

- **Accuracy:** 68.7%
- **Samples Processed:** 644
- **Correct:** 442
- **Incorrect:** 201
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.6424581005586593, 'recall': 0.7718120805369127, 'f1-score': 0.7012195121951219, 'support': 149.0}, 'B': {'precision': 0.6753246753246753, 'recall': 0.6419753086419753, 'f1-score': 0.6582278481012658, 'support': 162.0}, 'C': {'precision': 0.7094594594594594, 'recall': 0.65625, 'f1-score': 0.6818181818181818, 'support': 160.0}, 'D': {'precision': 0.7468354430379747, 'recall': 0.686046511627907, 'f1-score': 0.7151515151515152, 'support': 172.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.687402799377916, 'macro avg': {'precision': 0.46234627973012815, 'recall': 0.45934731680113244, 'f1-score': 0.4594028428776808, 'support': 643.0}, 'weighted avg': {'precision': 0.6953313594119483, 'recall': 0.687402799377916, 'f1-score': 0.6892870737269796, 'support': 643.0}}
- **Macro Precision:** 0.462
- **Macro Recall:** 0.459
- **Macro F1:** 0.459
- **Weighted F1:** 0.689
- **Confusion Matrix:** [[115, 16, 11, 6, 0, 1], [23, 104, 15, 18, 0, 2], [23, 15, 105, 16, 1, 0], [18, 19, 17, 118, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'L', 'X']
- **Top Confused Pairs:** [('B', 'A', 23), ('C', 'A', 23), ('D', 'B', 19), ('B', 'D', 18), ('D', 'A', 18), ('D', 'C', 17), ('A', 'B', 16), ('C', 'D', 16), ('B', 'C', 15), ('C', 'B', 15)]
- **True Class Distribution:** {'A': 149, 'B': 162, 'C': 160, 'D': 172}
- **Pred Class Distribution:** {'D': 158, 'A': 179, 'B': 154, 'C': 148, 'L': 1, 'X': 3}
- **Num Classes:** 6

