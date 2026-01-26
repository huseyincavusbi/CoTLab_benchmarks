# Experiment: Mmlu_medical Answer-First

**Status:** Completed
**Started:** 2026-01-26 09:25:26  
**Duration:** 46 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
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
  dataset=mmlu_medical
```

## Results

- **Accuracy:** 59.0%
- **Samples Processed:** 644
- **Correct:** 380
- **Incorrect:** 264
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.5621301775147929, 'recall': 0.6375838926174496, 'f1-score': 0.5974842767295597, 'support': 149.0}, 'B': {'precision': 0.5755813953488372, 'recall': 0.6073619631901841, 'f1-score': 0.591044776119403, 'support': 163.0}, 'C': {'precision': 0.6351351351351351, 'recall': 0.5875, 'f1-score': 0.6103896103896104, 'support': 160.0}, 'D': {'precision': 0.7022900763358778, 'recall': 0.5348837209302325, 'f1-score': 0.6072607260726073, 'support': 172.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.5900621118012422, 'macro avg': {'precision': 0.3093920980418304, 'recall': 0.29591619709223327, 'f1-score': 0.30077242366389756, 'support': 644.0}, 'weighted avg': {'precision': 0.6211066438555236, 'recall': 0.5900621118012422, 'f1-score': 0.6016717985822876, 'support': 644.0}}
- **Macro Precision:** 0.309
- **Macro Recall:** 0.296
- **Macro F1:** 0.301
- **Weighted F1:** 0.602
- **Confusion Matrix:** [[95, 21, 15, 7, 1, 0, 1, 9], [24, 99, 18, 18, 0, 0, 0, 4], [28, 20, 94, 14, 0, 1, 0, 3], [22, 32, 21, 92, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'H', 'L', 'T', 'X']
- **Top Confused Pairs:** [('D', 'B', 32), ('C', 'A', 28), ('B', 'A', 24), ('D', 'A', 22), ('A', 'B', 21), ('D', 'C', 21), ('C', 'B', 20), ('B', 'C', 18), ('B', 'D', 18), ('A', 'C', 15)]
- **True Class Distribution:** {'A': 149, 'B': 163, 'C': 160, 'D': 172}
- **Pred Class Distribution:** {'T': 1, 'B': 172, 'C': 148, 'A': 169, 'X': 21, 'D': 131, 'H': 1, 'L': 1}
- **Num Classes:** 8

