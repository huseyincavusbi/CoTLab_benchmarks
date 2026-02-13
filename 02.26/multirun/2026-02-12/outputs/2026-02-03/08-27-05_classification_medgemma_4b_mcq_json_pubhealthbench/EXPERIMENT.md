# Experiment: Pubhealthbench Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-03 08:27:06  
**Duration:** 2 minutes 51 seconds

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
  _target_: cotlab.datasets.loaders.PubHealthBenchDataset
  name: pubhealthbench
  split: reviewed
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 50
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=50 \
  prompt=mcq \
  prompt.answer_first=true \
  prompt.few_shot=false \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 68.0%
- **Samples Processed:** 50
- **Correct:** 34
- **Incorrect:** 16
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 1.0, 'recall': 0.6666666666666666, 'f1-score': 0.8, 'support': 9.0}, 'B': {'precision': 0.625, 'recall': 0.7142857142857143, 'f1-score': 0.6666666666666666, 'support': 7.0}, 'C': {'precision': 0.5, 'recall': 0.6666666666666666, 'f1-score': 0.5714285714285714, 'support': 9.0}, 'D': {'precision': 0.8333333333333334, 'recall': 0.625, 'f1-score': 0.7142857142857143, 'support': 8.0}, 'E': {'precision': 0.6666666666666666, 'recall': 0.5, 'f1-score': 0.5714285714285714, 'support': 4.0}, 'F': {'precision': 1.0, 'recall': 0.8, 'f1-score': 0.8888888888888888, 'support': 5.0}, 'G': {'precision': 0.5454545454545454, 'recall': 0.75, 'f1-score': 0.631578947368421, 'support': 8.0}, 'accuracy': 0.68, 'macro avg': {'precision': 0.7386363636363635, 'recall': 0.6746598639455782, 'f1-score': 0.6920396228666904, 'support': 50.0}, 'weighted avg': {'precision': 0.7314393939393941, 'recall': 0.68, 'f1-score': 0.6901319966583125, 'support': 50.0}}
- **Macro Precision:** 0.739
- **Macro Recall:** 0.675
- **Macro F1:** 0.692
- **Weighted F1:** 0.690
- **Confusion Matrix:** [[6, 0, 2, 0, 0, 0, 1], [0, 5, 1, 0, 0, 0, 1], [0, 2, 6, 0, 0, 0, 1], [0, 1, 0, 5, 1, 0, 1], [0, 0, 1, 0, 2, 0, 1], [0, 0, 0, 1, 0, 4, 0], [0, 0, 2, 0, 0, 0, 6]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Top Confused Pairs:** [('A', 'C', 2), ('C', 'B', 2), ('G', 'C', 2), ('A', 'G', 1), ('B', 'C', 1), ('B', 'G', 1), ('C', 'G', 1), ('D', 'B', 1), ('D', 'E', 1), ('D', 'G', 1)]
- **True Class Distribution:** {'B': 7, 'G': 8, 'D': 8, 'A': 9, 'E': 4, 'C': 9, 'F': 5}
- **Pred Class Distribution:** {'B': 8, 'G': 11, 'D': 6, 'C': 12, 'A': 6, 'E': 3, 'F': 4}
- **Num Classes:** 7

