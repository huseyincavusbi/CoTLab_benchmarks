# Experiment: Activation Compare: histopathology vs radiology

**Status:** Completed
**Started:** 2026-01-24 11:12:31  
**Duration:** 53 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Histopathology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** histopathology

**Variants:**
- histopathology: dataset=dataset, prompt=prompt, samples=default, seed=default
- radiology: dataset=dataset, prompt=prompt, samples=default, seed=default

<details>
<summary>Full Configuration (YAML)</summary>

```yaml
backend:
  _target_: cotlab.backends.TransformersBackend
  device: cuda
  dtype: bfloat16
  enable_hooks: true
  trust_remote_code: true
  load_in_4bit: true
  bnb_4bit_quant_type: nf4
  bnb_4bit_compute_dtype: bfloat16
  bnb_4bit_use_double_quant: true
model:
  name: google/medgemma-4b-it
  variant: 4b
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_4b
prompt:
  _target_: cotlab.prompts.HistopathologyPromptStrategy
  name: histopathology
  output_format: json
  few_shot: true
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.HistopathologyDataset
  name: histopathology
  path: data/histopathology.tsv
experiment:
  _target_: cotlab.experiments.ActivationCompareExperiment
  name: activation_compare
  description: Compare residual stream activations across runs
  num_samples: 50
  seed: 123
  pooling: mean
  layers: null
  comparison_mode: pairwise
  store_per_layer: true
  log_samples: false
  variants:
  - name: histopathology
    dataset:
      _target_: cotlab.datasets.HistopathologyDataset
    prompt:
      _target_: cotlab.prompts.HistopathologyPromptStrategy
  - name: radiology
    dataset:
      _target_: cotlab.datasets.RadiologyDataset
    prompt:
      _target_: cotlab.prompts.RadiologyPromptStrategy
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=activation_compare \
  experiment.num_samples=50 \
  experiment.seed=123 \
  prompt=histopathology \
  dataset=histopathology
```

## Results

- **Num Runs:** 2
- **Num Layers:** 34
- **Comparison Mode:** pairwise
- **Pooling:** mean
- **Pair Count:** 1

