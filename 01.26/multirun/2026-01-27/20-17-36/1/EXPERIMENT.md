# Experiment: Pubmedqa Standard

**Status:** Completed
**Started:** 2026-01-27 20:20:34  
**Duration:** 2 minutes 24 seconds

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

- **Accuracy:** 65.0%
- **Samples Processed:** 500
- **Correct:** 307
- **Incorrect:** 165
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'maybe': {'precision': 0.1440677966101695, 'recall': 0.32075471698113206, 'f1-score': 0.19883040935672514, 'support': 53.0}, 'no': {'precision': 0.8225806451612904, 'recall': 0.6296296296296297, 'f1-score': 0.7132867132867133, 'support': 162.0}, 'yes': {'precision': 0.8173913043478261, 'recall': 0.7315175097276264, 'f1-score': 0.7720739219712526, 'support': 257.0}, 'accuracy': 0.6504237288135594, 'macro avg': {'precision': 0.5946799153730953, 'recall': 0.560633952112796, 'f1-score': 0.5613970148715637, 'support': 472.0}, 'weighted avg': {'precision': 0.7435661503259733, 'recall': 0.6504237288135594, 'f1-score': 0.6875285110062836, 'support': 472.0}}
- **Macro Precision:** 0.595
- **Macro Recall:** 0.561
- **Macro F1:** 0.561
- **Weighted F1:** 0.688
- **Confusion Matrix:** [[17, 11, 25], [43, 102, 17], [58, 11, 188]]
- **Class Labels:** ['maybe', 'no', 'yes']
- **Top Confused Pairs:** [('yes', 'maybe', 58), ('no', 'maybe', 43), ('maybe', 'yes', 25), ('no', 'yes', 17), ('maybe', 'no', 11), ('yes', 'no', 11)]
- **True Class Distribution:** {'yes': 257, 'no': 162, 'maybe': 53}
- **Pred Class Distribution:** {'yes': 230, 'maybe': 118, 'no': 124}
- **Num Classes:** 3

