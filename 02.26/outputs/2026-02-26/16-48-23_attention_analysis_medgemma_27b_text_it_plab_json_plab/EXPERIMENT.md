# Experiment: Plab Standard Zero-Shot

**Status:** Running
**Started:** 2026-02-26 16:48:23

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Plab
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
**Output Format:** JSON
**Dataset:** plab

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
  _target_: cotlab.prompts.PLABPromptStrategy
  name: plab
  few_shot: false
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
  batch_size: 16
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=attention_analysis \
  prompt=plab \
  prompt.few_shot=false \
  dataset=plab
```

## Results

_Results will be added after experiment completes..._
