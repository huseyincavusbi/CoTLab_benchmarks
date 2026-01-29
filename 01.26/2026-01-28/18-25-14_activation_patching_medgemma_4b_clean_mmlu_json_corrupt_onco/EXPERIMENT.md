# Experiment: Mmlu_medical Standard

**Status:** Completed
**Started:** 2026-01-28 18:25:14  
**Duration:** 11 minutes 58 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** mmlu_medical

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
  _target_: cotlab.datasets.loaders.MMLUMedicalDataset
  name: mmlu_medical
  filename: mmlu/medical_test.jsonl
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
  - name: clean_mmlu
    dataset:
      _target_: cotlab.datasets.loaders.MMLUMedicalDataset
      name: mmlu_medical
      filename: mmlu/medical_test.jsonl
    num_samples: 100
    seed: 42
  - name: corrupt_onco
    dataset:
      _target_: cotlab.datasets.OncologyDataset
      name: oncology
      path: data/oncology.json
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
  dataset=mmlu_medical
```

## Results

- **Samples Processed:** 100
- **Num Layers:** 34
- **Num Samples:** 100
- **Layer 0 Avg Effect:** 0.086
- **Layer 1 Avg Effect:** 0.659
- **Layer 2 Avg Effect:** 0.538
- **Layer 3 Avg Effect:** 0.497
- **Layer 4 Avg Effect:** 0.604
- **Layer 5 Avg Effect:** 0.361
- **Layer 6 Avg Effect:** 0.492
- **Layer 7 Avg Effect:** 0.588
- **Layer 8 Avg Effect:** 0.547
- **Layer 9 Avg Effect:** 0.596
- **Layer 10 Avg Effect:** 0.632
- **Layer 11 Avg Effect:** 0.624
- **Layer 12 Avg Effect:** 0.643
- **Layer 13 Avg Effect:** 0.651
- **Layer 14 Avg Effect:** 0.637
- **Layer 15 Avg Effect:** 0.730
- **Layer 16 Avg Effect:** 0.743
- **Layer 17 Avg Effect:** 0.747
- **Layer 18 Avg Effect:** 0.746
- **Layer 19 Avg Effect:** 0.775
- **Layer 20 Avg Effect:** 0.741
- **Layer 21 Avg Effect:** 0.798
- **Layer 22 Avg Effect:** 0.775
- **Layer 23 Avg Effect:** 0.831
- **Layer 24 Avg Effect:** 0.852
- **Layer 25 Avg Effect:** 0.865
- **Layer 26 Avg Effect:** 0.890
- **Layer 27 Avg Effect:** 0.896
- **Layer 28 Avg Effect:** 0.915
- **Layer 29 Avg Effect:** 0.930
- **Layer 30 Avg Effect:** 0.947
- **Layer 31 Avg Effect:** 0.955
- **Layer 32 Avg Effect:** 0.957
- **Layer 33 Avg Effect:** 0.981
- **Top 5 Layers:** [33, 32, 31, 30, 29]

