# Experiment: Mmlu_medical Answer-First

**Status:** Completed
**Started:** 2026-01-27 17:10:11  
**Duration:** 6 minutes 0 seconds

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

- **Accuracy:** 59.3%
- **Samples Processed:** 644
- **Correct:** 379
- **Incorrect:** 260
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.6137931034482759, 'recall': 0.6054421768707483, 'f1-score': 0.6095890410958904, 'support': 147.0}, 'B': {'precision': 0.7142857142857143, 'recall': 0.53125, 'f1-score': 0.6093189964157706, 'support': 160.0}, 'C': {'precision': 0.6991869918699187, 'recall': 0.5375, 'f1-score': 0.607773851590106, 'support': 160.0}, 'D': {'precision': 0.5776699029126213, 'recall': 0.6918604651162791, 'f1-score': 0.6296296296296297, 'support': 172.0}, 'E': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'O': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.593114241001565, 'macro avg': {'precision': 0.20037967019357927, 'recall': 0.1820040493836175, 'f1-score': 0.18894703990241515, 'support': 639.0}, 'weighted avg': {'precision': 0.6506141510058978, 'recall': 0.593114241001565, 'f1-score': 0.6144612535498161, 'support': 639.0}}
- **Macro Precision:** 0.200
- **Macro Recall:** 0.182
- **Macro F1:** 0.189
- **Weighted F1:** 0.614
- **Confusion Matrix:** [[89, 12, 13, 23, 0, 0, 0, 0, 1, 1, 5, 0, 3], [21, 85, 12, 32, 0, 1, 1, 0, 0, 0, 4, 0, 4], [17, 14, 86, 32, 1, 1, 2, 0, 0, 0, 6, 0, 1], [18, 8, 12, 119, 1, 0, 0, 2, 0, 0, 10, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'G', 'H', 'I', 'K', 'O', 'T', 'V', 'X']
- **Top Confused Pairs:** [('B', 'D', 32), ('C', 'D', 32), ('A', 'D', 23), ('B', 'A', 21), ('D', 'A', 18), ('C', 'A', 17), ('C', 'B', 14), ('A', 'C', 13), ('A', 'B', 12), ('B', 'C', 12)]
- **True Class Distribution:** {'A': 147, 'B': 160, 'C': 160, 'D': 172}
- **Pred Class Distribution:** {'A': 145, 'B': 119, 'C': 123, 'D': 206, 'E': 2, 'T': 25, 'X': 9, 'G': 2, 'H': 3, 'V': 1, 'I': 2, 'K': 1, 'O': 1}
- **Num Classes:** 13

