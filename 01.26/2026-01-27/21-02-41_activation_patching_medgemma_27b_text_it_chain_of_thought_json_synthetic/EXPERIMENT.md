# Experiment: Synthetic Standard

**Status:** Completed
**Started:** 2026-01-27 21:02:41  
**Duration:** 14 minutes 17 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** synthetic

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
  _target_: cotlab.prompts.ChainOfThoughtStrategy
  name: chain_of_thought
  system_role: 'You are a medical expert. Think through problems carefully and

    explain your reasoning step by step before giving your final answer.

    '
  include_examples: false
  cot_trigger: 'Let''s think through this step by step:'
  output_format: json
dataset:
  _target_: cotlab.datasets.SyntheticMedicalDataset
  name: synthetic
  path: data/Synthetic_Medical_Data.csv
  repeat: 1
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
  num_samples: 20
  seed: 42
  variants:
  - name: histopathology_clean
    dataset:
      _target_: cotlab.datasets.HistopathologyDataset
      name: histopathology
      path: data/histopathology.tsv
    prompt:
      _target_: cotlab.prompts.HistopathologyPromptStrategy
      name: histopathology
      output_format: json
      few_shot: true
      answer_first: false
      contrarian: false
    num_samples: 20
    seed: 42
  - name: radiology_corrupt
    dataset:
      _target_: cotlab.datasets.RadiologyDataset
      name: radiology
      path: data/radiology.json
    prompt:
      _target_: cotlab.prompts.RadiologyPromptStrategy
      name: radiology
      output_format: json
      few_shot: true
      answer_first: false
      contrarian: false
    num_samples: 20
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
  experiment.num_samples=20 \
  experiment.seed=42 \
  prompt=chain_of_thought \
  dataset=synthetic
```

## Results

- **Samples Processed:** 20
- **Num Layers:** 62
- **Num Samples:** 20
- **Layer 0 Avg Effect:** 0.000
- **Layer 1 Avg Effect:** 0.922
- **Layer 2 Avg Effect:** 0.906
- **Layer 3 Avg Effect:** 0.870
- **Layer 4 Avg Effect:** 0.876
- **Layer 5 Avg Effect:** 0.845
- **Layer 6 Avg Effect:** 0.856
- **Layer 7 Avg Effect:** 0.838
- **Layer 8 Avg Effect:** 0.712
- **Layer 9 Avg Effect:** 0.624
- **Layer 10 Avg Effect:** 0.701
- **Layer 11 Avg Effect:** 0.760
- **Layer 12 Avg Effect:** 0.787
- **Layer 13 Avg Effect:** 0.740
- **Layer 14 Avg Effect:** 0.682
- **Layer 15 Avg Effect:** 0.782
- **Layer 16 Avg Effect:** 0.610
- **Layer 17 Avg Effect:** 0.711
- **Layer 18 Avg Effect:** 0.667
- **Layer 19 Avg Effect:** 0.588
- **Layer 20 Avg Effect:** 0.537
- **Layer 21 Avg Effect:** 0.557
- **Layer 22 Avg Effect:** 0.554
- **Layer 23 Avg Effect:** 0.513
- **Layer 24 Avg Effect:** 0.509
- **Layer 25 Avg Effect:** 0.503
- **Layer 26 Avg Effect:** 0.473
- **Layer 27 Avg Effect:** 0.434
- **Layer 28 Avg Effect:** 0.511
- **Layer 29 Avg Effect:** 0.471
- **Layer 30 Avg Effect:** 0.485
- **Layer 31 Avg Effect:** 0.505
- **Layer 32 Avg Effect:** 0.504
- **Layer 33 Avg Effect:** 0.516
- **Layer 34 Avg Effect:** 0.503
- **Layer 35 Avg Effect:** 0.399
- **Layer 36 Avg Effect:** 0.283
- **Layer 37 Avg Effect:** 0.401
- **Layer 38 Avg Effect:** 0.375
- **Layer 39 Avg Effect:** 0.364
- **Layer 40 Avg Effect:** 0.444
- **Layer 41 Avg Effect:** 0.480
- **Layer 42 Avg Effect:** 0.481
- **Layer 43 Avg Effect:** 0.460
- **Layer 44 Avg Effect:** 0.531
- **Layer 45 Avg Effect:** 0.500
- **Layer 46 Avg Effect:** 0.443
- **Layer 47 Avg Effect:** 0.614
- **Layer 48 Avg Effect:** 0.526
- **Layer 49 Avg Effect:** 0.555
- **Layer 50 Avg Effect:** 0.686
- **Layer 51 Avg Effect:** 0.740
- **Layer 52 Avg Effect:** 0.418
- **Layer 53 Avg Effect:** 0.553
- **Layer 54 Avg Effect:** 0.632
- **Layer 55 Avg Effect:** 0.281
- **Layer 56 Avg Effect:** 0.453
- **Layer 57 Avg Effect:** 0.486
- **Layer 58 Avg Effect:** 0.405
- **Layer 59 Avg Effect:** 0.456
- **Layer 60 Avg Effect:** 0.627
- **Layer 61 Avg Effect:** 0.391
- **Top 5 Layers:** [1, 2, 4, 3, 6]

