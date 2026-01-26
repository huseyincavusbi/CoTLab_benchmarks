# Experiment: Activation Compare: radiology vs medqa

**Status:** Completed
**Started:** 2026-01-21 12:23:07  
**Duration:** 1 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** radiology

**Variants:**
- radiology: dataset=radiology, prompt=radiology, samples=default, seed=default
- medqa: dataset=medqa, prompt=mcq, samples=default, seed=default

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
  experiment=activation_compare \
  experiment.num_samples=10 \
  experiment.seed=42 \
  prompt=radiology \
  prompt.output_format=plain \
  dataset=radiology
```

## Results

- **Num Runs:** 2
- **Num Layers:** 18
- **Comparison Mode:** pairwise
- **Pooling:** last_token
- **Pair Count:** 1

