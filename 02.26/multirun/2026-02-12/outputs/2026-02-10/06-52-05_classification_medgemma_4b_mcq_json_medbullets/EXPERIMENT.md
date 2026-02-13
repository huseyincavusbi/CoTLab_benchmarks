# Experiment: Medbullets Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-10 06:52:05  
**Duration:** 16 minutes 37 seconds

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
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
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
  prompt.answer_first=true \
  prompt.few_shot=false \
  dataset=medbullets
```

## Results

- **Accuracy:** 42.5%
- **Samples Processed:** 308
- **Correct:** 131
- **Incorrect:** 177
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.38636363636363635, 'recall': 0.5573770491803278, 'f1-score': 0.4563758389261745, 'support': 61.0}, 'B': {'precision': 0.5882352941176471, 'recall': 0.40540540540540543, 'f1-score': 0.48, 'support': 74.0}, 'C': {'precision': 0.3333333333333333, 'recall': 0.37735849056603776, 'f1-score': 0.35398230088495575, 'support': 53.0}, 'D': {'precision': 0.4727272727272727, 'recall': 0.3880597014925373, 'f1-score': 0.4262295081967213, 'support': 67.0}, 'E': {'precision': 0.44680851063829785, 'recall': 0.39622641509433965, 'f1-score': 0.42, 'support': 53.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.4253246753246753, 'macro avg': {'precision': 0.2784335058975234, 'recall': 0.26555338271733103, 'f1-score': 0.2670734560009814, 'support': 308.0}, 'weighted avg': {'precision': 0.4549280473575046, 'recall': 0.4253246753246753, 'f1-score': 0.43161482198240136, 'support': 308.0}}
- **Macro Precision:** 0.278
- **Macro Recall:** 0.266
- **Macro F1:** 0.267
- **Weighted F1:** 0.432
- **Confusion Matrix:** [[34, 5, 10, 5, 5, 0, 2, 0], [16, 30, 13, 7, 5, 1, 2, 0], [16, 3, 20, 7, 6, 0, 0, 1], [14, 9, 8, 26, 10, 0, 0, 0], [8, 4, 9, 10, 21, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'L', 'T', 'X']
- **Top Confused Pairs:** [('B', 'A', 16), ('C', 'A', 16), ('D', 'A', 14), ('B', 'C', 13), ('A', 'C', 10), ('D', 'E', 10), ('E', 'D', 10), ('D', 'B', 9), ('E', 'C', 9), ('D', 'C', 8)]
- **True Class Distribution:** {'B': 74, 'E': 53, 'A': 61, 'D': 67, 'C': 53}
- **Pred Class Distribution:** {'A': 88, 'B': 51, 'D': 55, 'C': 60, 'E': 47, 'L': 1, 'T': 5, 'X': 1}
- **Num Classes:** 8

