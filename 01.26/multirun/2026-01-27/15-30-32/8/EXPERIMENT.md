# Experiment: Mmlu_medical Standard

**Status:** Completed
**Started:** 2026-01-27 19:30:52  
**Duration:** 5 minutes 17 seconds

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
  name: google/medgemma-27b-text-it
  variant: 27b-text
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b_text_it
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

- **Accuracy:** 62.2%
- **Samples Processed:** 644
- **Correct:** 395
- **Incorrect:** 240
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.6258503401360545, 'recall': 0.6258503401360545, 'f1-score': 0.6258503401360545, 'support': 147.0}, 'B': {'precision': 0.7678571428571429, 'recall': 0.5408805031446541, 'f1-score': 0.6346863468634686, 'support': 159.0}, 'C': {'precision': 0.75, 'recall': 0.5660377358490566, 'f1-score': 0.6451612903225806, 'support': 159.0}, 'D': {'precision': 0.5247933884297521, 'recall': 0.7470588235294118, 'f1-score': 0.616504854368932, 'support': 170.0}, 'E': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'W': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.6220472440944882, 'macro avg': {'precision': 0.22237507261857914, 'recall': 0.2066522835549314, 'f1-score': 0.2101835693075863, 'support': 635.0}, 'weighted avg': {'precision': 0.6654396247989662, 'recall': 0.6220472440944882, 'f1-score': 0.6303962197721265, 'support': 635.0}}
- **Macro Precision:** 0.222
- **Macro Recall:** 0.207
- **Macro F1:** 0.210
- **Weighted F1:** 0.630
- **Confusion Matrix:** [[92, 6, 6, 42, 0, 0, 0, 0, 0, 0, 0, 1], [20, 86, 14, 35, 0, 0, 1, 1, 0, 0, 0, 2], [17, 10, 90, 38, 1, 1, 0, 1, 0, 0, 0, 1], [18, 10, 10, 127, 0, 0, 0, 0, 1, 1, 1, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'K', 'T', 'V', 'W', 'X']
- **Top Confused Pairs:** [('A', 'D', 42), ('C', 'D', 38), ('B', 'D', 35), ('B', 'A', 20), ('D', 'A', 18), ('C', 'A', 17), ('B', 'C', 14), ('C', 'B', 10), ('D', 'B', 10), ('D', 'C', 10)]
- **True Class Distribution:** {'B': 159, 'A': 147, 'C': 159, 'D': 170}
- **Pred Class Distribution:** {'B': 112, 'A': 147, 'C': 120, 'D': 242, 'T': 1, 'V': 1, 'K': 2, 'E': 1, 'G': 1, 'X': 6, 'F': 1, 'W': 1}
- **Num Classes:** 12

