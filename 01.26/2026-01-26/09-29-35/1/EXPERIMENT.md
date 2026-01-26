# Experiment: Pubmedqa Standard

**Status:** Completed
**Started:** 2026-01-26 09:31:17  
**Duration:** 45 seconds

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
  max_model_len: null
  quantization: null
  gpu_memory_utilization: 0.9
  enforce_eager: false
  limit_mm_per_prompt: null
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
  num_samples: -1
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=-1 \
  prompt=pubmedqa \
  dataset=pubmedqa
```

## Results

- **Accuracy:** 60.6%
- **Samples Processed:** 500
- **Correct:** 301
- **Incorrect:** 196
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'maybe': {'precision': 0.10638297872340426, 'recall': 0.18181818181818182, 'f1-score': 0.1342281879194631, 'support': 55.0}, 'no': {'precision': 0.7564102564102564, 'recall': 0.35119047619047616, 'f1-score': 0.4796747967479675, 'support': 168.0}, 'yes': {'precision': 0.7138461538461538, 'recall': 0.8467153284671532, 'f1-score': 0.7746243739565943, 'support': 274.0}, 'accuracy': 0.6056338028169014, 'macro avg': {'precision': 0.5255464629932715, 'recall': 0.459907995491937, 'f1-score': 0.462842452874675, 'support': 497.0}, 'weighted avg': {'precision': 0.6610097244679204, 'recall': 0.6056338028169014, 'f1-score': 0.6040543151978589, 'support': 497.0}}
- **Macro Precision:** 0.526
- **Macro Recall:** 0.460
- **Macro F1:** 0.463
- **Weighted F1:** 0.604
- **Confusion Matrix:** [[10, 11, 34], [50, 59, 59], [34, 8, 232]]
- **Class Labels:** ['maybe', 'no', 'yes']
- **Top Confused Pairs:** [('no', 'yes', 59), ('no', 'maybe', 50), ('maybe', 'yes', 34), ('yes', 'maybe', 34), ('maybe', 'no', 11), ('yes', 'no', 8)]
- **True Class Distribution:** {'yes': 274, 'no': 168, 'maybe': 55}
- **Pred Class Distribution:** {'yes': 325, 'maybe': 94, 'no': 78}
- **Num Classes:** 3

