# Experiment: Medbullets Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-10 07:10:15  
**Duration:** 16 minutes 42 seconds

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
  max_model_len: 8192
  quantization: bitsandbytes
  gpu_memory_utilization: 0.7
  enforce_eager: true
  limit_mm_per_prompt:
    image: 0
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
  prompt.few_shot=false \
  dataset=medbullets
```

## Results

- **Accuracy:** 39.5%
- **Samples Processed:** 308
- **Correct:** 121
- **Incorrect:** 185
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.37777777777777777, 'recall': 0.5666666666666667, 'f1-score': 0.4533333333333333, 'support': 60.0}, 'B': {'precision': 0.421875, 'recall': 0.36486486486486486, 'f1-score': 0.391304347826087, 'support': 74.0}, 'C': {'precision': 0.3181818181818182, 'recall': 0.2692307692307692, 'f1-score': 0.2916666666666667, 'support': 52.0}, 'D': {'precision': 0.5490196078431373, 'recall': 0.417910447761194, 'f1-score': 0.4745762711864407, 'support': 67.0}, 'E': {'precision': 0.34615384615384615, 'recall': 0.33962264150943394, 'f1-score': 0.34285714285714286, 'support': 53.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Y': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.3954248366013072, 'macro avg': {'precision': 0.2236675611062866, 'recall': 0.2175883766703254, 'f1-score': 0.21708197354107453, 'support': 306.0}, 'weighted avg': {'precision': 0.41033117249596485, 'recall': 0.3954248366013072, 'f1-score': 0.3963765593029974, 'support': 306.0}}
- **Macro Precision:** 0.224
- **Macro Recall:** 0.218
- **Macro F1:** 0.217
- **Weighted F1:** 0.396
- **Confusion Matrix:** [[34, 5, 5, 5, 11, 0, 0, 0, 0], [19, 27, 13, 2, 12, 0, 1, 0, 0], [13, 16, 14, 7, 1, 0, 0, 1, 0], [16, 7, 4, 28, 10, 0, 1, 0, 1], [8, 9, 8, 9, 18, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'S', 'T', 'X', 'Y']
- **Top Confused Pairs:** [('B', 'A', 19), ('C', 'B', 16), ('D', 'A', 16), ('B', 'C', 13), ('C', 'A', 13), ('B', 'E', 12), ('A', 'E', 11), ('D', 'E', 10), ('E', 'B', 9), ('E', 'D', 9)]
- **True Class Distribution:** {'B': 74, 'E': 53, 'A': 60, 'D': 67, 'C': 52}
- **Pred Class Distribution:** {'B': 64, 'A': 90, 'D': 51, 'C': 44, 'E': 52, 'Y': 1, 'X': 1, 'T': 2, 'S': 1}
- **Num Classes:** 9

