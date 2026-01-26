# Experiment: Pubmedqa Answer-First

**Status:** Completed
**Started:** 2026-01-26 09:29:35  
**Duration:** 45 seconds

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

- **Accuracy:** 45.4%
- **Samples Processed:** 500
- **Correct:** 227
- **Incorrect:** 273
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'maybe': {'precision': 0.09259259259259259, 'recall': 0.2727272727272727, 'f1-score': 0.1382488479262673, 'support': 55.0}, 'no': {'precision': 0.4896551724137931, 'recall': 0.42011834319526625, 'f1-score': 0.45222929936305734, 'support': 169.0}, 'yes': {'precision': 0.7305699481865285, 'recall': 0.5108695652173914, 'f1-score': 0.6012793176972282, 'support': 276.0}, 'accuracy': 0.454, 'macro avg': {'precision': 0.4376059043976381, 'recall': 0.4012383937133101, 'f1-score': 0.3972524883288509, 'support': 500.0}, 'weighted avg': {'precision': 0.578963244860011, 'recall': 0.454, 'f1-score': 0.49996705982547274, 'support': 500.0}}
- **Macro Precision:** 0.438
- **Macro Recall:** 0.401
- **Macro F1:** 0.397
- **Weighted F1:** 0.500
- **Confusion Matrix:** [[15, 19, 21], [67, 71, 31], [80, 55, 141]]
- **Class Labels:** ['maybe', 'no', 'yes']
- **Top Confused Pairs:** [('yes', 'maybe', 80), ('no', 'maybe', 67), ('yes', 'no', 55), ('no', 'yes', 31), ('maybe', 'yes', 21), ('maybe', 'no', 19)]
- **True Class Distribution:** {'yes': 276, 'no': 169, 'maybe': 55}
- **Pred Class Distribution:** {'maybe': 162, 'yes': 193, 'no': 145}
- **Num Classes:** 3

