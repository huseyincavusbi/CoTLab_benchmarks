# Experiment: Cardiology Standard

**Status:** Completed
**Started:** 2026-01-28 18:03:51  
**Duration:** 20 minutes 24 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** cardiology

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
  _target_: cotlab.datasets.CardiologyDataset
  name: cardiology
  path: data/cardiology.json
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
  - name: clean_cardio
    dataset:
      _target_: cotlab.datasets.CardiologyDataset
      name: cardiology
      path: data/cardiology.json
    num_samples: 100
    seed: 42
  - name: corrupt_pubmed
    dataset:
      _target_: cotlab.datasets.loaders.PubMedQADataset
      name: pubmedqa
      filename: pubmedqa/test.jsonl
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
  dataset=cardiology
```

## Results

- **Samples Processed:** 100
- **Num Layers:** 34
- **Num Samples:** 100
- **Layer 0 Avg Effect:** 0.042
- **Layer 1 Avg Effect:** 0.761
- **Layer 2 Avg Effect:** 0.715
- **Layer 3 Avg Effect:** 0.628
- **Layer 4 Avg Effect:** 0.666
- **Layer 5 Avg Effect:** 0.550
- **Layer 6 Avg Effect:** 0.651
- **Layer 7 Avg Effect:** 0.654
- **Layer 8 Avg Effect:** 0.657
- **Layer 9 Avg Effect:** 0.718
- **Layer 10 Avg Effect:** 0.722
- **Layer 11 Avg Effect:** 0.734
- **Layer 12 Avg Effect:** 0.771
- **Layer 13 Avg Effect:** 0.768
- **Layer 14 Avg Effect:** 0.777
- **Layer 15 Avg Effect:** 0.815
- **Layer 16 Avg Effect:** 0.820
- **Layer 17 Avg Effect:** 0.842
- **Layer 18 Avg Effect:** 0.852
- **Layer 19 Avg Effect:** 0.862
- **Layer 20 Avg Effect:** 0.855
- **Layer 21 Avg Effect:** 0.857
- **Layer 22 Avg Effect:** 0.844
- **Layer 23 Avg Effect:** 0.882
- **Layer 24 Avg Effect:** 0.880
- **Layer 25 Avg Effect:** 0.899
- **Layer 26 Avg Effect:** 0.926
- **Layer 27 Avg Effect:** 0.920
- **Layer 28 Avg Effect:** 0.929
- **Layer 29 Avg Effect:** 0.951
- **Layer 30 Avg Effect:** 0.963
- **Layer 31 Avg Effect:** 0.971
- **Layer 32 Avg Effect:** 0.974
- **Layer 33 Avg Effect:** 1.000
- **Top 5 Layers:** [33, 32, 31, 30, 29]

