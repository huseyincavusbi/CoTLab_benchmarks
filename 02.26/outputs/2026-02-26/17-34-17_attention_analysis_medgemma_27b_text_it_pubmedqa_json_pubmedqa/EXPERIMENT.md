# Experiment: Pubmedqa Standard

**Status:** Running
**Started:** 2026-02-26 17:34:17

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
  _target_: cotlab.backends.TransformersBackend
  device: cuda
  dtype: bfloat16
  enable_hooks: true
  trust_remote_code: true
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
  _target_: cotlab.experiments.AttentionAnalysisExperiment
  name: attention_analysis
  description: Analyze attention patterns at critical layers
  all_layers: true
  target_layers: null
  layer_stride: 1
  force_eager_reload: false
  num_samples: null
  last_k_tokens: 16
  max_input_tokens: 1024
  analyze_generated_tokens: false
  generated_max_new_tokens: 16
  generated_do_sample: false
  generated_temperature: 0.7
  generated_top_p: 0.9
  question: Patient presents with chest pain, sweating, and shortness of breath. What
    is the diagnosis?
  batch_size: 8
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=attention_analysis \
  prompt=pubmedqa \
  dataset=pubmedqa
```

## Results

_Results will be added after experiment completes..._
