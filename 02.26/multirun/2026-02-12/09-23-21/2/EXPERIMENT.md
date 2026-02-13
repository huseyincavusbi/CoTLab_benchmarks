# Experiment: Pubhealthbench Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-12 09:44:13  
**Duration:** 8 minutes 25 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
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
  answer_first: false
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
  prompt.few_shot=false \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 24.8%
- **Samples Processed:** 760
- **Correct:** 188
- **Incorrect:** 569
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.18571428571428572, 'recall': 0.1092436974789916, 'f1-score': 0.13756613756613756, 'support': 119.0}, 'B': {'precision': 0.5135135135135135, 'recall': 0.16379310344827586, 'f1-score': 0.24836601307189543, 'support': 116.0}, 'C': {'precision': 0.3392857142857143, 'recall': 0.2, 'f1-score': 0.25165562913907286, 'support': 95.0}, 'D': {'precision': 0.2112676056338028, 'recall': 0.1595744680851064, 'f1-score': 0.18181818181818182, 'support': 94.0}, 'E': {'precision': 0.21978021978021978, 'recall': 0.20408163265306123, 'f1-score': 0.21164021164021163, 'support': 98.0}, 'F': {'precision': 0.26744186046511625, 'recall': 0.39655172413793105, 'f1-score': 0.3194444444444444, 'support': 116.0}, 'G': {'precision': 0.2222222222222222, 'recall': 0.47058823529411764, 'f1-score': 0.3018867924528302, 'support': 119.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Z': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.24834874504623514, 'macro avg': {'precision': 0.15070964781652882, 'recall': 0.131064066238268, 'f1-score': 0.12710595462559798, 'support': 757.0}, 'weighted avg': {'precision': 0.28106344405699785, 'recall': 0.24834874504623514, 'f1-score': 0.23764840996567282, 'support': 757.0}}
- **Macro Precision:** 0.151
- **Macro Recall:** 0.131
- **Macro F1:** 0.127
- **Weighted F1:** 0.238
- **Confusion Matrix:** [[13, 2, 3, 16, 10, 24, 49, 0, 0, 0, 1, 0, 1], [11, 19, 9, 8, 11, 29, 27, 0, 0, 1, 0, 1, 0], [6, 3, 19, 9, 13, 19, 26, 0, 0, 0, 0, 0, 0], [13, 2, 6, 15, 14, 11, 31, 1, 1, 0, 0, 0, 0], [10, 6, 4, 3, 20, 24, 31, 0, 0, 0, 0, 0, 0], [8, 2, 10, 9, 8, 46, 32, 0, 0, 0, 1, 0, 0], [9, 3, 5, 11, 15, 19, 56, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'N', 'Q', 'S', 'X', 'Z']
- **Top Confused Pairs:** [('A', 'G', 49), ('F', 'G', 32), ('D', 'G', 31), ('E', 'G', 31), ('B', 'F', 29), ('B', 'G', 27), ('C', 'G', 26), ('A', 'F', 24), ('E', 'F', 24), ('C', 'F', 19)]
- **True Class Distribution:** {'F': 116, 'A': 119, 'C': 95, 'G': 119, 'E': 98, 'B': 116, 'D': 94}
- **Pred Class Distribution:** {'F': 172, 'G': 252, 'C': 56, 'A': 70, 'E': 91, 'D': 71, 'B': 37, 'S': 3, 'Q': 1, 'X': 1, 'H': 1, 'N': 1, 'Z': 1}
- **Num Classes:** 13

