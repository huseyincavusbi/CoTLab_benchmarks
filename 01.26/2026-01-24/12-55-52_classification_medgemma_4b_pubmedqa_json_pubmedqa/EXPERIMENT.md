# Experiment: Pubmedqa Answer-First

**Status:** Completed
**Started:** 2026-01-24 12:55:53  
**Duration:** 2 minutes 5 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Pubmedqa
**Reasoning Mode:** Answer-First
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
  answer_first: true
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
  prompt.answer_first=true \
  dataset=pubmedqa
```

## Results

- **Accuracy:** 55.0%
- **Samples Processed:** 20
- **Correct:** 11
- **Incorrect:** 9
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'maybe': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'no': {'precision': 0.5, 'recall': 1.0, 'f1-score': 0.6666666666666666, 'support': 6.0}, 'yes': {'precision': 0.8333333333333334, 'recall': 0.38461538461538464, 'f1-score': 0.5263157894736842, 'support': 13.0}, 'accuracy': 0.55, 'macro avg': {'precision': 0.4444444444444445, 'recall': 0.4615384615384615, 'f1-score': 0.39766081871345027, 'support': 20.0}, 'weighted avg': {'precision': 0.6916666666666667, 'recall': 0.55, 'f1-score': 0.5421052631578946, 'support': 20.0}}
- **Macro Precision:** 0.444
- **Macro Recall:** 0.462
- **Macro F1:** 0.398
- **Weighted F1:** 0.542
- **Confusion Matrix:** [[0, 0, 1], [0, 6, 0], [2, 6, 5]]
- **Class Labels:** ['maybe', 'no', 'yes']
- **Top Confused Pairs:** [('yes', 'no', 6), ('yes', 'maybe', 2), ('maybe', 'yes', 1)]
- **True Class Distribution:** {'no': 6, 'yes': 13, 'maybe': 1}
- **Pred Class Distribution:** {'no': 12, 'yes': 6, 'maybe': 2}
- **Num Classes:** 3

