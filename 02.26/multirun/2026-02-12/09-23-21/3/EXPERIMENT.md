# Experiment: Pubhealthbench Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-12 09:53:36  
**Duration:** 8 minutes 25 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** No (zero-shot)
**Output Format:** JSON
**Dataset:** pubhealthbench

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
  few_shot: false
  output_format: json
  answer_first: true
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.PubHealthBenchDataset
  name: pubhealthbench
  split: reviewed
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
  prompt.few_shot=false \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 28.0%
- **Samples Processed:** 760
- **Correct:** 212
- **Incorrect:** 545
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.30985915492957744, 'recall': 0.18333333333333332, 'f1-score': 0.23036649214659685, 'support': 120.0}, 'B': {'precision': 0.46511627906976744, 'recall': 0.17391304347826086, 'f1-score': 0.25316455696202533, 'support': 115.0}, 'C': {'precision': 0.29508196721311475, 'recall': 0.1875, 'f1-score': 0.22929936305732485, 'support': 96.0}, 'D': {'precision': 0.32051282051282054, 'recall': 0.26595744680851063, 'f1-score': 0.29069767441860467, 'support': 94.0}, 'E': {'precision': 0.19607843137254902, 'recall': 0.20408163265306123, 'f1-score': 0.2, 'support': 98.0}, 'F': {'precision': 0.2976190476190476, 'recall': 0.43103448275862066, 'f1-score': 0.352112676056338, 'support': 116.0}, 'G': {'precision': 0.25333333333333335, 'recall': 0.4830508474576271, 'f1-score': 0.3323615160349854, 'support': 118.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'M': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.2800528401585205, 'macro avg': {'precision': 0.1644308487730931, 'recall': 0.14837467588380107, 'f1-score': 0.14523094451352886, 'support': 757.0}, 'weighted avg': {'precision': 0.3074773762178195, 'recall': 0.2800528401585205, 'f1-score': 0.27180971290850736, 'support': 757.0}}
- **Macro Precision:** 0.164
- **Macro Recall:** 0.148
- **Macro F1:** 0.145
- **Weighted F1:** 0.272
- **Confusion Matrix:** [[22, 4, 9, 12, 11, 25, 35, 2, 0, 0, 0, 0, 0], [6, 20, 10, 9, 18, 22, 28, 0, 0, 0, 1, 0, 1], [2, 6, 18, 5, 21, 21, 22, 0, 1, 0, 0, 0, 0], [13, 3, 6, 25, 11, 7, 28, 0, 0, 1, 0, 0, 0], [5, 2, 6, 10, 20, 26, 29, 0, 0, 0, 0, 0, 0], [12, 2, 7, 9, 8, 50, 26, 0, 1, 0, 0, 1, 0], [11, 6, 5, 8, 13, 17, 57, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'M', 'N', 'Q', 'S', 'X']
- **Top Confused Pairs:** [('A', 'G', 35), ('E', 'G', 29), ('B', 'G', 28), ('D', 'G', 28), ('E', 'F', 26), ('F', 'G', 26), ('A', 'F', 25), ('B', 'F', 22), ('C', 'G', 22), ('C', 'E', 21)]
- **True Class Distribution:** {'F': 116, 'A': 120, 'C': 96, 'G': 118, 'E': 98, 'B': 115, 'D': 94}
- **Pred Class Distribution:** {'F': 168, 'G': 225, 'B': 43, 'A': 71, 'E': 102, 'C': 61, 'D': 78, 'S': 2, 'Q': 1, 'I': 2, 'X': 1, 'M': 2, 'N': 1}
- **Num Classes:** 13

