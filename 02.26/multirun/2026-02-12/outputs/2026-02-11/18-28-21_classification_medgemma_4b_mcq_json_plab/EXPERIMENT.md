# Experiment: Plab Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-11 18:28:21  
**Duration:** 4 minutes 11 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** No (zero-shot)
**Output Format:** JSON
**Dataset:** plab

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
  _target_: cotlab.datasets.loaders.PLABDataset
  name: plab
  split: main
  filename: plab/data.json
  topics_filename: plab/topics.json
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 100
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=100 \
  prompt=mcq \
  prompt.answer_first=true \
  prompt.few_shot=false \
  dataset=plab
```

## Results

- **Accuracy:** 65.0%
- **Samples Processed:** 100
- **Correct:** 65
- **Incorrect:** 35
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.6857142857142857, 'recall': 0.7741935483870968, 'f1-score': 0.7272727272727273, 'support': 31.0}, 'B': {'precision': 0.5217391304347826, 'recall': 0.6, 'f1-score': 0.5581395348837209, 'support': 20.0}, 'C': {'precision': 0.6363636363636364, 'recall': 0.8235294117647058, 'f1-score': 0.717948717948718, 'support': 17.0}, 'D': {'precision': 0.7272727272727273, 'recall': 0.42105263157894735, 'f1-score': 0.5333333333333333, 'support': 19.0}, 'E': {'precision': 0.75, 'recall': 0.5, 'f1-score': 0.6, 'support': 12.0}, 'G': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 1.0}, 'accuracy': 0.65, 'macro avg': {'precision': 0.7201816299642386, 'recall': 0.6864625986217915, 'f1-score': 0.68944905223975, 'support': 100.0}, 'weighted avg': {'precision': 0.6632828910220215, 'recall': 0.65, 'f1-score': 0.642467067815905, 'support': 100.0}}
- **Macro Precision:** 0.720
- **Macro Recall:** 0.686
- **Macro F1:** 0.689
- **Weighted F1:** 0.642
- **Confusion Matrix:** [[24, 2, 2, 2, 1, 0], [4, 12, 3, 1, 0, 0], [1, 2, 14, 0, 0, 0], [4, 3, 3, 8, 1, 0], [2, 4, 0, 0, 6, 0], [0, 0, 0, 0, 0, 1]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'G']
- **Top Confused Pairs:** [('B', 'A', 4), ('D', 'A', 4), ('E', 'B', 4), ('B', 'C', 3), ('D', 'B', 3), ('D', 'C', 3), ('A', 'B', 2), ('A', 'C', 2), ('A', 'D', 2), ('C', 'B', 2)]
- **True Class Distribution:** {'B': 20, 'C': 17, 'D': 19, 'A': 31, 'E': 12, 'G': 1}
- **Pred Class Distribution:** {'B': 23, 'C': 22, 'D': 11, 'A': 35, 'E': 8, 'G': 1}
- **Num Classes:** 6

