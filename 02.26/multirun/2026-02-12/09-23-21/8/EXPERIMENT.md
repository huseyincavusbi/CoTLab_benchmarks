# Experiment: Medbullets Standard

**Status:** Completed
**Started:** 2026-02-12 10:12:30  
**Duration:** 4 minutes 23 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
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
  answer_first: false
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
  dataset=medbullets
```

## Results

- **Accuracy:** 27.7%
- **Samples Processed:** 308
- **Correct:** 78
- **Incorrect:** 204
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.26595744680851063, 'recall': 0.45454545454545453, 'f1-score': 0.33557046979865773, 'support': 55.0}, 'B': {'precision': 0.45454545454545453, 'recall': 0.28169014084507044, 'f1-score': 0.34782608695652173, 'support': 71.0}, 'C': {'precision': 0.2647058823529412, 'recall': 0.19148936170212766, 'f1-score': 0.2222222222222222, 'support': 47.0}, 'D': {'precision': 0.3333333333333333, 'recall': 0.22950819672131148, 'f1-score': 0.27184466019417475, 'support': 61.0}, 'E': {'precision': 0.2564102564102564, 'recall': 0.20833333333333334, 'f1-score': 0.22988505747126436, 'support': 48.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'R': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'U': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.2765957446808511, 'macro avg': {'precision': 0.08749735408058311, 'recall': 0.07586480484151652, 'f1-score': 0.07818602759126893, 'support': 282.0}, 'weighted avg': {'precision': 0.3261793934709547, 'recall': 0.2765957446808511, 'f1-score': 0.28799106201329444, 'support': 282.0}}
- **Macro Precision:** 0.087
- **Macro Recall:** 0.076
- **Macro F1:** 0.078
- **Weighted F1:** 0.288
- **Confusion Matrix:** [[25, 3, 5, 7, 8, 2, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2], [26, 20, 4, 6, 7, 0, 0, 1, 1, 2, 0, 1, 0, 0, 0, 2, 0, 1], [16, 4, 9, 6, 7, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1], [19, 9, 9, 14, 7, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], [8, 8, 7, 9, 10, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'K', 'L', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'X']
- **Top Confused Pairs:** [('B', 'A', 26), ('D', 'A', 19), ('C', 'A', 16), ('D', 'B', 9), ('D', 'C', 9), ('E', 'D', 9), ('A', 'E', 8), ('E', 'A', 8), ('E', 'B', 8), ('A', 'D', 7)]
- **True Class Distribution:** {'B': 71, 'E': 48, 'A': 55, 'D': 61, 'C': 47}
- **Pred Class Distribution:** {'A': 94, 'C': 34, 'X': 5, 'B': 44, 'I': 3, 'D': 42, 'E': 39, 'L': 4, 'F': 3, 'H': 1, 'U': 1, 'S': 1, 'P': 4, 'T': 2, 'R': 2, 'N': 1, 'Q': 1, 'K': 1}
- **Num Classes:** 18

