# Experiment: Medbullets Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-12 10:23:16  
**Duration:** 4 minutes 18 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
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
  prompt.few_shot=false \
  dataset=medbullets
```

## Results

- **Accuracy:** 21.2%
- **Samples Processed:** 308
- **Correct:** 58
- **Incorrect:** 216
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.22727272727272727, 'recall': 0.46296296296296297, 'f1-score': 0.3048780487804878, 'support': 54.0}, 'B': {'precision': 0.3333333333333333, 'recall': 0.17142857142857143, 'f1-score': 0.22641509433962265, 'support': 70.0}, 'C': {'precision': 0.2926829268292683, 'recall': 0.2608695652173913, 'f1-score': 0.27586206896551724, 'support': 46.0}, 'D': {'precision': 0.18181818181818182, 'recall': 0.06896551724137931, 'f1-score': 0.1, 'support': 58.0}, 'E': {'precision': 0.38461538461538464, 'recall': 0.10869565217391304, 'f1-score': 0.1694915254237288, 'support': 46.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'R': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'U': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.2116788321167883, 'macro avg': {'precision': 0.08351309140405266, 'recall': 0.06311307464848341, 'f1-score': 0.06333216102996214, 'support': 274.0}, 'weighted avg': {'precision': 0.2821432024743401, 'recall': 0.2116788321167883, 'f1-score': 0.21386400211615056, 'support': 274.0}}
- **Macro Precision:** 0.084
- **Macro Recall:** 0.063
- **Macro F1:** 0.063
- **Weighted F1:** 0.214
- **Confusion Matrix:** [[25, 8, 4, 8, 3, 1, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 1], [29, 12, 11, 2, 1, 0, 0, 1, 1, 4, 3, 0, 1, 1, 2, 1, 1], [11, 6, 12, 5, 1, 1, 1, 0, 2, 2, 0, 0, 0, 0, 1, 1, 3], [26, 4, 7, 4, 3, 3, 0, 0, 3, 2, 0, 0, 1, 0, 2, 0, 3], [19, 6, 7, 3, 5, 0, 1, 0, 3, 1, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'K', 'L', 'P', 'Q', 'R', 'S', 'T', 'U', 'X']
- **Top Confused Pairs:** [('B', 'A', 29), ('D', 'A', 26), ('E', 'A', 19), ('B', 'C', 11), ('C', 'A', 11), ('A', 'B', 8), ('A', 'D', 8), ('D', 'C', 7), ('E', 'C', 7), ('C', 'B', 6)]
- **True Class Distribution:** {'B': 70, 'E': 46, 'A': 54, 'D': 58, 'C': 46}
- **Pred Class Distribution:** {'A': 110, 'X': 9, 'B': 36, 'D': 22, 'E': 13, 'C': 41, 'S': 1, 'L': 9, 'H': 2, 'F': 5, 'P': 5, 'K': 9, 'T': 5, 'R': 3, 'U': 2, 'I': 1, 'Q': 1}
- **Num Classes:** 17

