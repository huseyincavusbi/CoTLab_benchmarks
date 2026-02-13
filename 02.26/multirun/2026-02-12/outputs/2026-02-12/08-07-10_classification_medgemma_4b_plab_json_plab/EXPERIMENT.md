# Experiment: Plab Standard

**Status:** Completed
**Started:** 2026-02-12 08:07:10  
**Duration:** 4 minutes 7 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Plab
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
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
  few_shot: true
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
  dataset=plab
```

## Results

- **Accuracy:** 60.0%
- **Samples Processed:** 100
- **Correct:** 60
- **Incorrect:** 40
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.7096774193548387, 'recall': 0.7096774193548387, 'f1-score': 0.7096774193548387, 'support': 31.0}, 'B': {'precision': 0.5217391304347826, 'recall': 0.6, 'f1-score': 0.5581395348837209, 'support': 20.0}, 'C': {'precision': 0.46153846153846156, 'recall': 0.7058823529411765, 'f1-score': 0.5581395348837209, 'support': 17.0}, 'D': {'precision': 0.7272727272727273, 'recall': 0.42105263157894735, 'f1-score': 0.5333333333333333, 'support': 19.0}, 'E': {'precision': 0.6666666666666666, 'recall': 0.5, 'f1-score': 0.5714285714285714, 'support': 12.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'accuracy': 0.6, 'macro avg': {'precision': 0.5144824008779129, 'recall': 0.4894354006458271, 'f1-score': 0.48845306564736424, 'support': 100.0}, 'weighted avg': {'precision': 0.6209911827303132, 'recall': 0.6, 'f1-score': 0.5964163898117385, 'support': 100.0}}
- **Macro Precision:** 0.514
- **Macro Recall:** 0.489
- **Macro F1:** 0.488
- **Weighted F1:** 0.596
- **Confusion Matrix:** [[22, 2, 3, 2, 2, 0], [4, 12, 4, 0, 0, 0], [0, 4, 12, 0, 1, 0], [4, 3, 4, 8, 0, 0], [1, 2, 2, 1, 6, 0], [0, 0, 1, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'G']
- **Top Confused Pairs:** [('B', 'A', 4), ('B', 'C', 4), ('C', 'B', 4), ('D', 'A', 4), ('D', 'C', 4), ('A', 'C', 3), ('D', 'B', 3), ('A', 'B', 2), ('A', 'D', 2), ('A', 'E', 2)]
- **True Class Distribution:** {'B': 20, 'C': 17, 'D': 19, 'A': 31, 'E': 12, 'G': 1}
- **Pred Class Distribution:** {'A': 31, 'B': 23, 'C': 26, 'D': 11, 'E': 9}
- **Num Classes:** 6

