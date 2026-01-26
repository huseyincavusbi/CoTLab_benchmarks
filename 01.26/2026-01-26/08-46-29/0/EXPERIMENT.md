# Experiment: Afrimedqa Answer-First

**Status:** Completed
**Started:** 2026-01-26 08:46:29  
**Duration:** 5 minutes 9 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** afrimedqa

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
  _target_: cotlab.datasets.loaders.MedQADataset
  name: afrimedqa
  filename: afrimedqa/mcq.jsonl
  split: mcq
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
  dataset=afrimedqa
```

## Results

- **Accuracy:** 52.1%
- **Samples Processed:** 3958
- **Correct:** 2061
- **Incorrect:** 1894
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.5585392051557465, 'recall': 0.48552754435107376, 'f1-score': 0.5194805194805194, 'support': 1071.0}, 'B': {'precision': 0.4845814977973568, 'recall': 0.5438813349814586, 'f1-score': 0.512521840419336, 'support': 809.0}, 'C': {'precision': 0.5649038461538461, 'recall': 0.5471478463329453, 'f1-score': 0.5558840922531046, 'support': 859.0}, 'D': {'precision': 0.5485933503836317, 'recall': 0.5423514538558787, 'f1-score': 0.5454545454545454, 'support': 791.0}, 'E': {'precision': 0.47086247086247085, 'recall': 0.4752941176470588, 'f1-score': 0.47306791569086654, 'support': 425.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.5211125158027813, 'macro avg': {'precision': 0.218956697529421, 'recall': 0.21618352476403457, 'f1-score': 0.21720074277486434, 'support': 3955.0}, 'weighted avg': {'precision': 0.5333826079787668, 'recall': 0.5211125158027813, 'f1-score': 0.5261710872645916, 'support': 3955.0}}
- **Macro Precision:** 0.219
- **Macro Recall:** 0.216
- **Macro F1:** 0.217
- **Weighted F1:** 0.526
- **Confusion Matrix:** [[520, 182, 147, 124, 75, 0, 0, 0, 0, 0, 0, 23], [137, 440, 83, 79, 53, 1, 1, 1, 0, 0, 0, 14], [126, 109, 470, 92, 45, 0, 1, 0, 1, 1, 0, 14], [96, 114, 88, 429, 54, 0, 0, 0, 0, 1, 0, 9], [52, 63, 44, 58, 202, 0, 0, 0, 0, 0, 1, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'I', 'L', 'P', 'T', 'V', 'X']
- **Top Confused Pairs:** [('A', 'B', 182), ('A', 'C', 147), ('B', 'A', 137), ('C', 'A', 126), ('A', 'D', 124), ('D', 'B', 114), ('C', 'B', 109), ('D', 'A', 96), ('C', 'D', 92), ('D', 'C', 88)]
- **True Class Distribution:** {'B': 809, 'E': 425, 'C': 859, 'D': 791, 'A': 1071}
- **Pred Class Distribution:** {'B': 908, 'E': 429, 'C': 832, 'D': 782, 'A': 931, 'X': 65, 'L': 1, 'F': 1, 'P': 1, 'I': 2, 'V': 1, 'T': 2}
- **Num Classes:** 12

