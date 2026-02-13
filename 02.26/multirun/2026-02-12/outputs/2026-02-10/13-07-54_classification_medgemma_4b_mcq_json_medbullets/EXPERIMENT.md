# Experiment: Medbullets Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-10 13:07:54  
**Duration:** 6 minutes 27 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
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
  max_new_tokens: 256
  temperature: 0
  top_p: 1
  safe_name: medgemma_4b
prompt:
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: false
  output_format: json
  answer_first: true
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
  prompt.answer_first=true \
  prompt.few_shot=false \
  dataset=medbullets
```

## Results

- **Accuracy:** 26.2%
- **Samples Processed:** 308
- **Correct:** 76
- **Incorrect:** 214
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.25, 'recall': 0.5802469135802469, 'f1-score': 0.34944237918215615, 'support': 81.0}, 'B': {'precision': 0.30434782608695654, 'recall': 0.09722222222222222, 'f1-score': 0.14736842105263157, 'support': 72.0}, 'C': {'precision': 0.3333333333333333, 'recall': 0.11842105263157894, 'f1-score': 0.17475728155339806, 'support': 76.0}, 'D': {'precision': 0.3170731707317073, 'recall': 0.21311475409836064, 'f1-score': 0.2549019607843137, 'support': 61.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'U': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.2620689655172414, 'macro avg': {'precision': 0.12047543301519972, 'recall': 0.10090049425324088, 'f1-score': 0.09264700425724995, 'support': 290.0}, 'weighted avg': {'precision': 0.29944082836630465, 'recall': 0.2620689655172414, 'f1-score': 0.2336066621911914, 'support': 290.0}}
- **Macro Precision:** 0.120
- **Macro Recall:** 0.101
- **Macro F1:** 0.093
- **Weighted F1:** 0.234
- **Confusion Matrix:** [[47, 8, 6, 15, 0, 0, 2, 2, 0, 1], [50, 7, 6, 6, 0, 2, 0, 1, 0, 0], [54, 6, 9, 7, 0, 0, 0, 0, 0, 0], [37, 2, 6, 13, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'I', 'K', 'L', 'T', 'U', 'V']
- **Top Confused Pairs:** [('C', 'A', 54), ('B', 'A', 50), ('D', 'A', 37), ('A', 'D', 15), ('A', 'B', 8), ('C', 'D', 7), ('A', 'C', 6), ('B', 'C', 6), ('B', 'D', 6), ('C', 'B', 6)]
- **True Class Distribution:** {'B': 72, 'D': 61, 'C': 76, 'A': 81}
- **Pred Class Distribution:** {'A': 188, 'D': 41, 'T': 3, 'B': 23, 'C': 27, 'U': 1, 'L': 3, 'V': 1, 'K': 2, 'I': 1}
- **Num Classes:** 10

