# Experiment: Pubmedqa Standard

**Status:** Completed
**Started:** 2026-01-24 12:59:18  
**Duration:** 2 minutes 5 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Pubmedqa
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** pubmedqa

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
  _target_: cotlab.prompts.pubmedqa.PubMedQAPromptStrategy
  name: pubmedqa
  output_format: json
  few_shot: true
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.PubMedQADataset
  name: pubmedqa
  filename: pubmedqa/test.jsonl
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 20
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=20 \
  prompt=pubmedqa \
  dataset=pubmedqa
```

## Results

- **Accuracy:** 70.0%
- **Samples Processed:** 20
- **Correct:** 14
- **Incorrect:** 6
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'maybe': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'no': {'precision': 1.0, 'recall': 0.5, 'f1-score': 0.6666666666666666, 'support': 6.0}, 'yes': {'precision': 0.7333333333333333, 'recall': 0.8461538461538461, 'f1-score': 0.7857142857142857, 'support': 13.0}, 'accuracy': 0.7, 'macro avg': {'precision': 0.5777777777777778, 'recall': 0.44871794871794873, 'f1-score': 0.48412698412698413, 'support': 20.0}, 'weighted avg': {'precision': 0.7766666666666666, 'recall': 0.7, 'f1-score': 0.7107142857142856, 'support': 20.0}}
- **Macro Precision:** 0.578
- **Macro Recall:** 0.449
- **Macro F1:** 0.484
- **Weighted F1:** 0.711
- **Confusion Matrix:** [[0, 0, 1], [0, 3, 3], [2, 0, 11]]
- **Class Labels:** ['maybe', 'no', 'yes']
- **Top Confused Pairs:** [('no', 'yes', 3), ('yes', 'maybe', 2), ('maybe', 'yes', 1)]
- **True Class Distribution:** {'no': 6, 'yes': 13, 'maybe': 1}
- **Pred Class Distribution:** {'no': 3, 'yes': 15, 'maybe': 2}
- **Num Classes:** 3

