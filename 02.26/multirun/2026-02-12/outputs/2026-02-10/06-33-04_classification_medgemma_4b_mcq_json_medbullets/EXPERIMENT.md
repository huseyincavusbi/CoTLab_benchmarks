# Experiment: Medbullets Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-10 06:33:05  
**Duration:** 16 minutes 31 seconds

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
  prompt.few_shot=false \
  dataset=medbullets
```

## Results

- **Accuracy:** 49.2%
- **Samples Processed:** 308
- **Correct:** 151
- **Incorrect:** 156
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.5054945054945055, 'recall': 0.5348837209302325, 'f1-score': 0.519774011299435, 'support': 86.0}, 'B': {'precision': 0.5789473684210527, 'recall': 0.5789473684210527, 'f1-score': 0.5789473684210527, 'support': 76.0}, 'C': {'precision': 0.4927536231884058, 'recall': 0.44155844155844154, 'f1-score': 0.4657534246575342, 'support': 77.0}, 'D': {'precision': 0.4090909090909091, 'recall': 0.39705882352941174, 'f1-score': 0.40298507462686567, 'support': 68.0}, 'M': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.49185667752442996, 'macro avg': {'precision': 0.28375520088498185, 'recall': 0.2789211934913055, 'f1-score': 0.2810656970006983, 'support': 307.0}, 'weighted avg': {'precision': 0.49912944063914183, 'recall': 0.49185667752442996, 'f1-score': 0.4950050936319492, 'support': 307.0}}
- **Macro Precision:** 0.284
- **Macro Recall:** 0.279
- **Macro F1:** 0.281
- **Weighted F1:** 0.495
- **Confusion Matrix:** [[46, 13, 11, 15, 0, 1, 0], [8, 44, 12, 12, 0, 0, 0], [23, 7, 34, 12, 0, 1, 0], [14, 12, 12, 27, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'M', 'T', 'X']
- **Top Confused Pairs:** [('C', 'A', 23), ('A', 'D', 15), ('D', 'A', 14), ('A', 'B', 13), ('B', 'C', 12), ('B', 'D', 12), ('C', 'D', 12), ('D', 'B', 12), ('D', 'C', 12), ('A', 'C', 11)]
- **True Class Distribution:** {'B': 76, 'D': 68, 'C': 77, 'A': 86}
- **Pred Class Distribution:** {'B': 76, 'X': 1, 'D': 66, 'C': 69, 'A': 91, 'T': 3, 'M': 1}
- **Num Classes:** 7

