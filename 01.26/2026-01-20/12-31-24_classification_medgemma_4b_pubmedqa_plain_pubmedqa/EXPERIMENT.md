# Experiment: Pubmedqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-20 12:31:24  
**Duration:** 2 minutes 21 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Pubmedqa
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
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
  output_format: plain
dataset:
  _target_: cotlab.datasets.loaders.PubMedQADataset
  name: pubmedqa
  filename: pubmedqa/test.jsonl
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
  prompt=pubmedqa \
  prompt.output_format=plain \
  dataset=pubmedqa
```

## Results

- **Accuracy:** 59.2%
- **Samples Processed:** 50
- **Correct:** 29
- **Incorrect:** 20
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'maybe': {'precision': 0.1111111111111111, 'recall': 0.3333333333333333, 'f1-score': 0.16666666666666666, 'support': 3.0}, 'no': {'precision': 1.0, 'recall': 0.17647058823529413, 'f1-score': 0.3, 'support': 17.0}, 'yes': {'precision': 0.6756756756756757, 'recall': 0.8620689655172413, 'f1-score': 0.7575757575757576, 'support': 29.0}, 'accuracy': 0.5918367346938775, 'macro avg': {'precision': 0.5955955955955956, 'recall': 0.45729096236195627, 'f1-score': 0.40808080808080804, 'support': 49.0}, 'weighted avg': {'precision': 0.7536311822026107, 'recall': 0.5918367346938775, 'f1-score': 0.5626468769325912, 'support': 49.0}}
- **Macro Precision:** 0.596
- **Macro Recall:** 0.457
- **Macro F1:** 0.408
- **Weighted F1:** 0.563
- **Confusion Matrix:** [[1, 0, 2], [4, 3, 10], [4, 0, 25]]
- **Class Labels:** ['maybe', 'no', 'yes']
- **Top Confused Pairs:** [('no', 'yes', 10), ('no', 'maybe', 4), ('yes', 'maybe', 4), ('maybe', 'yes', 2)]
- **True Class Distribution:** {'no': 17, 'yes': 29, 'maybe': 3}
- **Pred Class Distribution:** {'maybe': 9, 'yes': 37, 'no': 3}
- **Num Classes:** 3

