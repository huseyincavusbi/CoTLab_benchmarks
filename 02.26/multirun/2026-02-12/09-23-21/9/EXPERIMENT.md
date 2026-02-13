# Experiment: Medbullets Answer-First

**Status:** Completed
**Started:** 2026-02-12 10:17:52  
**Duration:** 4 minutes 27 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
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
  _target_: cotlab.datasets.loaders.MedBulletsDataset
  name: medbullets
  split: op5_test
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
  dataset=medbullets
```

## Results

- **Accuracy:** 26.5%
- **Samples Processed:** 308
- **Correct:** 75
- **Incorrect:** 208
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.25, 'recall': 0.4107142857142857, 'f1-score': 0.3108108108108108, 'support': 56.0}, 'B': {'precision': 0.4782608695652174, 'recall': 0.3142857142857143, 'f1-score': 0.3793103448275862, 'support': 70.0}, 'C': {'precision': 0.27450980392156865, 'recall': 0.30434782608695654, 'f1-score': 0.28865979381443296, 'support': 46.0}, 'D': {'precision': 0.3235294117647059, 'recall': 0.1774193548387097, 'f1-score': 0.22916666666666666, 'support': 62.0}, 'E': {'precision': 0.23809523809523808, 'recall': 0.10204081632653061, 'f1-score': 0.14285714285714285, 'support': 49.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'R': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'U': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.26501766784452296, 'macro avg': {'precision': 0.09777470770917063, 'recall': 0.08180049982826229, 'f1-score': 0.08442529743603996, 'support': 283.0}, 'weighted avg': {'precision': 0.32449188002132795, 'recall': 0.26501766784452296, 'f1-score': 0.27718661976018966, 'support': 283.0}}
- **Macro Precision:** 0.098
- **Macro Recall:** 0.082
- **Macro F1:** 0.084
- **Weighted F1:** 0.277
- **Confusion Matrix:** [[23, 7, 7, 7, 6, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [21, 22, 12, 5, 4, 1, 0, 0, 3, 1, 0, 0, 0, 1, 0, 0], [11, 3, 14, 5, 4, 1, 1, 0, 2, 0, 0, 0, 2, 0, 0, 3], [19, 9, 11, 11, 2, 0, 0, 0, 3, 0, 2, 0, 1, 0, 1, 3], [18, 5, 7, 6, 5, 0, 0, 0, 4, 2, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'L', 'P', 'Q', 'R', 'T', 'U', 'V', 'X']
- **Top Confused Pairs:** [('B', 'A', 21), ('D', 'A', 19), ('E', 'A', 18), ('B', 'C', 12), ('C', 'A', 11), ('D', 'C', 11), ('D', 'B', 9), ('A', 'B', 7), ('A', 'C', 7), ('A', 'D', 7)]
- **True Class Distribution:** {'B': 70, 'E': 49, 'A': 56, 'D': 62, 'C': 46}
- **Pred Class Distribution:** {'C': 51, 'X': 8, 'B': 46, 'A': 92, 'D': 34, 'E': 21, 'P': 3, 'F': 3, 'L': 13, 'H': 1, 'R': 1, 'V': 2, 'Q': 2, 'I': 1, 'U': 1, 'T': 4}
- **Num Classes:** 16

