# Experiment: Histopathology Standard

**Status:** Completed
**Started:** 2026-01-28 17:35:31  
**Duration:** 13 minutes 40 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** histopathology

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
  name: google/medgemma-4b-it
  variant: 4b
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_4b
prompt:
  _target_: cotlab.prompts.ChainOfThoughtStrategy
  name: chain_of_thought
  system_role: 'You are a medical expert. Think through problems carefully and

    explain your reasoning step by step before giving your final answer.

    '
  include_examples: false
  cot_trigger: 'Let''s think through this step by step:'
  output_format: json
dataset:
  _target_: cotlab.datasets.HistopathologyDataset
  name: histopathology
  path: data/histopathology.tsv
experiment:
  _target_: cotlab.experiments.ActivationPatchingExperiment
  name: activation_patching
  description: Layer-wise causal interventions to study CoT importance
  patching:
    sweep_all_layers: true
    target_positions: null
    intervention_types:
    - patch
    - zero
  variants:
  - name: clean
    dataset:
      _target_: cotlab.datasets.HistopathologyDataset
      name: histopathology
      path: data/histopathology.tsv
    num_samples: 100
    seed: 42
  - name: corrupt
    dataset:
      _target_: cotlab.datasets.RadiologyDataset
      name: radiology
      path: data/radiology.json
    num_samples: 100
    seed: 42
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=activation_patching \
  prompt=chain_of_thought \
  dataset=histopathology
```

## Results

- **Samples Processed:** 100
- **Num Layers:** 34
- **Num Samples:** 100
- **Layer 0 Avg Effect:** 0.000
- **Layer 1 Avg Effect:** 0.060
- **Layer 2 Avg Effect:** 0.048
- **Layer 3 Avg Effect:** 0.043
- **Layer 4 Avg Effect:** 0.066
- **Layer 5 Avg Effect:** 0.032
- **Layer 6 Avg Effect:** 0.042
- **Layer 7 Avg Effect:** 0.046
- **Layer 8 Avg Effect:** 0.047
- **Layer 9 Avg Effect:** 0.049
- **Layer 10 Avg Effect:** 0.054
- **Layer 11 Avg Effect:** 0.056
- **Layer 12 Avg Effect:** 0.058
- **Layer 13 Avg Effect:** 0.059
- **Layer 14 Avg Effect:** 0.060
- **Layer 15 Avg Effect:** 0.066
- **Layer 16 Avg Effect:** 0.069
- **Layer 17 Avg Effect:** 0.067
- **Layer 18 Avg Effect:** 0.067
- **Layer 19 Avg Effect:** 0.077
- **Layer 20 Avg Effect:** 0.073
- **Layer 21 Avg Effect:** 0.102
- **Layer 22 Avg Effect:** 0.083
- **Layer 23 Avg Effect:** 0.164
- **Layer 24 Avg Effect:** 0.178
- **Layer 25 Avg Effect:** 0.213
- **Layer 26 Avg Effect:** 0.244
- **Layer 27 Avg Effect:** 0.248
- **Layer 28 Avg Effect:** 0.272
- **Layer 29 Avg Effect:** 0.298
- **Layer 30 Avg Effect:** 0.324
- **Layer 31 Avg Effect:** 0.330
- **Layer 32 Avg Effect:** 0.334
- **Layer 33 Avg Effect:** 0.350
- **Top 5 Layers:** [33, 32, 31, 30, 29]

