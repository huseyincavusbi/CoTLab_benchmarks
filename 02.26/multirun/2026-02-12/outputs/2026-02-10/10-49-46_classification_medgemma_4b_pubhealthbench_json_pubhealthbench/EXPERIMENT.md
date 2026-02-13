# Experiment: Pubhealthbench Standard

**Status:** Completed
**Started:** 2026-02-10 10:49:46  
**Duration:** 25 minutes 57 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Pubhealthbench
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
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
  _target_: cotlab.prompts.pubhealthbench.PubHealthBenchMCQPromptStrategy
  name: pubhealthbench
  output_format: json
dataset:
  _target_: cotlab.datasets.loaders.PubHealthBenchDataset
  name: pubhealthbench
  split: reviewed
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 760
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=760 \
  prompt=pubhealthbench \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 90.4%
- **Samples Processed:** 760
- **Correct:** 113
- **Incorrect:** 12
- **Parse Errors:** 635
- **Parse Error Rate:** 0.836
- **Classification Report:** {'A': {'precision': 0.8571428571428571, 'recall': 0.9, 'f1-score': 0.8780487804878049, 'support': 20.0}, 'B': {'precision': 0.9411764705882353, 'recall': 1.0, 'f1-score': 0.9696969696969697, 'support': 16.0}, 'C': {'precision': 0.8666666666666667, 'recall': 0.8125, 'f1-score': 0.8387096774193549, 'support': 16.0}, 'D': {'precision': 0.9166666666666666, 'recall': 0.9166666666666666, 'f1-score': 0.9166666666666666, 'support': 12.0}, 'E': {'precision': 0.95, 'recall': 0.9047619047619048, 'f1-score': 0.926829268292683, 'support': 21.0}, 'F': {'precision': 0.8846153846153846, 'recall': 0.9583333333333334, 'f1-score': 0.92, 'support': 24.0}, 'G': {'precision': 0.9285714285714286, 'recall': 0.8125, 'f1-score': 0.8666666666666667, 'support': 16.0}, 'accuracy': 0.904, 'macro avg': {'precision': 0.9064056391787485, 'recall': 0.9006802721088435, 'f1-score': 0.9023740041757351, 'support': 125.0}, 'weighted avg': {'precision': 0.9048500754147812, 'recall': 0.904, 'f1-score': 0.9032445061154424, 'support': 125.0}}
- **Macro Precision:** 0.906
- **Macro Recall:** 0.901
- **Macro F1:** 0.902
- **Weighted F1:** 0.903
- **Confusion Matrix:** [[18, 0, 1, 0, 1, 0, 0], [0, 16, 0, 0, 0, 0, 0], [0, 1, 13, 0, 0, 1, 1], [0, 0, 0, 11, 0, 1, 0], [0, 0, 0, 1, 19, 1, 0], [0, 0, 1, 0, 0, 23, 0], [3, 0, 0, 0, 0, 0, 13]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Top Confused Pairs:** [('G', 'A', 3), ('A', 'C', 1), ('A', 'E', 1), ('C', 'B', 1), ('C', 'F', 1), ('C', 'G', 1), ('D', 'F', 1), ('E', 'D', 1), ('E', 'F', 1), ('F', 'C', 1)]
- **True Class Distribution:** {'F': 24, 'A': 20, 'C': 16, 'G': 16, 'E': 21, 'B': 16, 'D': 12}
- **Pred Class Distribution:** {'F': 26, 'A': 21, 'C': 15, 'G': 14, 'E': 20, 'D': 12, 'B': 17}
- **Num Classes:** 7

