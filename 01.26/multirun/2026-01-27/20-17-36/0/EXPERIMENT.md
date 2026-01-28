# Experiment: Pubmedqa Answer-First

**Status:** Completed
**Started:** 2026-01-27 20:17:37  
**Duration:** 1 minutes 52 seconds

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
  max_model_len: null
  quantization: null
  gpu_memory_utilization: 0.9
  enforce_eager: false
  limit_mm_per_prompt: null
model:
  name: google/medgemma-27b-text-it
  variant: 27b-text
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b_text_it
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
  prompt.answer_first=true \
  dataset=pubmedqa
```

## Results

- **Accuracy:** 67.3%
- **Samples Processed:** 500
- **Correct:** 325
- **Incorrect:** 158
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'maybe': {'precision': 0.17142857142857143, 'recall': 0.3333333333333333, 'f1-score': 0.22641509433962265, 'support': 54.0}, 'no': {'precision': 0.7697841726618705, 'recall': 0.6645962732919255, 'f1-score': 0.7133333333333334, 'support': 161.0}, 'yes': {'precision': 0.8368200836820083, 'recall': 0.746268656716418, 'f1-score': 0.7889546351084813, 'support': 268.0}, 'accuracy': 0.6728778467908902, 'macro avg': {'precision': 0.5926776092574834, 'recall': 0.5813994211138923, 'f1-score': 0.5762343542604791, 'support': 483.0}, 'weighted avg': {'precision': 0.7400831823653876, 'recall': 0.6728778467908902, 'f1-score': 0.7008549150519241, 'support': 483.0}}
- **Macro Precision:** 0.593
- **Macro Recall:** 0.581
- **Macro F1:** 0.576
- **Weighted F1:** 0.701
- **Confusion Matrix:** [[18, 16, 20], [35, 107, 19], [52, 16, 200]]
- **Class Labels:** ['maybe', 'no', 'yes']
- **Top Confused Pairs:** [('yes', 'maybe', 52), ('no', 'maybe', 35), ('maybe', 'yes', 20), ('no', 'yes', 19), ('maybe', 'no', 16), ('yes', 'no', 16)]
- **True Class Distribution:** {'yes': 268, 'no': 161, 'maybe': 54}
- **Pred Class Distribution:** {'yes': 239, 'maybe': 105, 'no': 139}
- **Num Classes:** 3

