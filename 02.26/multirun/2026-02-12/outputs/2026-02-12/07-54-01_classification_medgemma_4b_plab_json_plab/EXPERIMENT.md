# Experiment: Plab Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-12 07:54:01  
**Duration:** 4 minutes 5 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Plab
**Reasoning Mode:** Standard
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
  _target_: cotlab.prompts.PLABPromptStrategy
  name: plab
  few_shot: false
  output_format: json
  answer_first: false
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
  prompt=plab \
  prompt.few_shot=false \
  dataset=plab
```

## Results

- **Accuracy:** 62.0%
- **Samples Processed:** 100
- **Correct:** 62
- **Incorrect:** 38
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.7241379310344828, 'recall': 0.6774193548387096, 'f1-score': 0.7, 'support': 31.0}, 'B': {'precision': 0.6086956521739131, 'recall': 0.7, 'f1-score': 0.6511627906976745, 'support': 20.0}, 'C': {'precision': 0.5416666666666666, 'recall': 0.7647058823529411, 'f1-score': 0.6341463414634146, 'support': 17.0}, 'D': {'precision': 0.5384615384615384, 'recall': 0.3684210526315789, 'f1-score': 0.4375, 'support': 19.0}, 'E': {'precision': 0.6363636363636364, 'recall': 0.5833333333333334, 'f1-score': 0.6086956521739131, 'support': 12.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'accuracy': 0.62, 'macro avg': {'precision': 0.5082209041167062, 'recall': 0.5156466038594272, 'f1-score': 0.505250797389167, 'support': 100.0}, 'weighted avg': {'precision': 0.6169765510601343, 'recall': 0.62, 'f1-score': 0.6112059144491849, 'support': 100.0}}
- **Macro Precision:** 0.508
- **Macro Recall:** 0.516
- **Macro F1:** 0.505
- **Weighted F1:** 0.611
- **Confusion Matrix:** [[21, 2, 3, 2, 3, 0], [3, 14, 2, 1, 0, 0], [1, 3, 13, 0, 0, 0], [3, 3, 5, 7, 1, 0], [1, 1, 1, 2, 7, 0], [0, 0, 0, 1, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'G']
- **Top Confused Pairs:** [('D', 'C', 5), ('A', 'C', 3), ('A', 'E', 3), ('B', 'A', 3), ('C', 'B', 3), ('D', 'A', 3), ('D', 'B', 3), ('A', 'B', 2), ('A', 'D', 2), ('B', 'C', 2)]
- **True Class Distribution:** {'B': 20, 'C': 17, 'D': 19, 'A': 31, 'E': 12, 'G': 1}
- **Pred Class Distribution:** {'B': 23, 'C': 24, 'D': 13, 'A': 29, 'E': 11}
- **Num Classes:** 6

