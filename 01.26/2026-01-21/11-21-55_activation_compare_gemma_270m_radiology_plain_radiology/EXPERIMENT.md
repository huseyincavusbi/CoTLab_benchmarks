# Experiment: Radiology Standard (PLAIN)

**Status:** Running
**Started:** 2026-01-21 11:21:55

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** radiology

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
  name: google/gemma-3-270m
  variant: 270m
  max_new_tokens: 256
  temperature: 0.7
  top_p: 0.9
  safe_name: gemma_270m
prompt:
  _target_: cotlab.prompts.RadiologyPromptStrategy
  name: radiology
  contrarian: false
  few_shot: true
  answer_first: false
  output_format: plain
dataset:
  _target_: cotlab.datasets.RadiologyDataset
  name: radiology
  path: data/radiology.json
experiment:
  _target_: cotlab.experiments.ActivationCompareExperiment
  name: activation_compare
  description: Compare residual stream activations across runs
  num_samples: 10
  seed: 42
  pooling: last_token
  layers: null
  comparison_mode: pairwise
  store_per_layer: true
  log_samples: false
  variants:
  - name: radiology
    dataset: base
    prompt: base
  - name: medqa
    dataset:
      _target_: cotlab.datasets.loaders.MedQADataset
      name: medqa
      filename: medqa/test.jsonl
      split: test
    prompt:
      _target_: cotlab.prompts.mcq.MCQPromptStrategy
      name: mcq
      few_shot: true
      output_format: plain
      answer_first: false
      contrarian: false
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  prompt=radiology \
  prompt.output_format=plain \
  dataset=radiology
```

## Results

_Results will be added after experiment completes..._
