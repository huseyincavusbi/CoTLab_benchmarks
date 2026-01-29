# Experiment: Histopathology Standard

**Status:** Completed
**Started:** 2026-01-28 18:55:36  
**Duration:** 52 minutes 1 seconds

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
    head_indices:
    - 0
    - 1
    - 2
    - 3
    - 4
    - 5
    - 6
    - 7
  variants:
  - name: clean
    dataset:
      _target_: cotlab.datasets.HistopathologyDataset
      name: histopathology
      path: data/histopathology.tsv
    num_samples: 50
    seed: 42
  - name: corrupt
    dataset:
      _target_: cotlab.datasets.RadiologyDataset
      name: radiology
      path: data/radiology.json
    num_samples: 50
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

- **Samples Processed:** 50
- **Num Layers:** 34
- **Num Samples:** 50
- **Layer 0 Head 0 Avg Effect:** 0.886
- **Layer 0 Head 1 Avg Effect:** 0.879
- **Layer 0 Head 2 Avg Effect:** 0.884
- **Layer 0 Head 3 Avg Effect:** 0.886
- **Layer 0 Head 4 Avg Effect:** 0.884
- **Layer 0 Head 5 Avg Effect:** 0.882
- **Layer 0 Head 6 Avg Effect:** 0.882
- **Layer 0 Head 7 Avg Effect:** 0.882
- **Layer 1 Head 0 Avg Effect:** 0.880
- **Layer 1 Head 1 Avg Effect:** 0.883
- **Layer 1 Head 2 Avg Effect:** 0.883
- **Layer 1 Head 3 Avg Effect:** 0.885
- **Layer 1 Head 4 Avg Effect:** 0.885
- **Layer 1 Head 5 Avg Effect:** 0.881
- **Layer 1 Head 6 Avg Effect:** 0.881
- **Layer 1 Head 7 Avg Effect:** 0.884
- **Layer 2 Head 0 Avg Effect:** 0.883
- **Layer 2 Head 1 Avg Effect:** 0.885
- **Layer 2 Head 2 Avg Effect:** 0.884
- **Layer 2 Head 3 Avg Effect:** 0.884
- **Layer 2 Head 4 Avg Effect:** 0.885
- **Layer 2 Head 5 Avg Effect:** 0.886
- **Layer 2 Head 6 Avg Effect:** 0.885
- **Layer 2 Head 7 Avg Effect:** 0.886
- **Layer 3 Head 0 Avg Effect:** 0.881
- **Layer 3 Head 1 Avg Effect:** 0.881
- **Layer 3 Head 2 Avg Effect:** 0.884
- **Layer 3 Head 3 Avg Effect:** 0.885
- **Layer 3 Head 4 Avg Effect:** 0.884
- **Layer 3 Head 5 Avg Effect:** 0.883
- **Layer 3 Head 6 Avg Effect:** 0.883
- **Layer 3 Head 7 Avg Effect:** 0.882
- **Layer 4 Head 0 Avg Effect:** 0.882
- **Layer 4 Head 1 Avg Effect:** 0.887
- **Layer 4 Head 2 Avg Effect:** 0.881
- **Layer 4 Head 3 Avg Effect:** 0.886
- **Layer 4 Head 4 Avg Effect:** 0.885
- **Layer 4 Head 5 Avg Effect:** 0.886
- **Layer 4 Head 6 Avg Effect:** 0.884
- **Layer 4 Head 7 Avg Effect:** 0.884
- **Layer 5 Head 0 Avg Effect:** 0.882
- **Layer 5 Head 1 Avg Effect:** 0.884
- **Layer 5 Head 2 Avg Effect:** 0.885
- **Layer 5 Head 3 Avg Effect:** 0.886
- **Layer 5 Head 4 Avg Effect:** 0.885
- **Layer 5 Head 5 Avg Effect:** 0.883
- **Layer 5 Head 6 Avg Effect:** 0.883
- **Layer 5 Head 7 Avg Effect:** 0.881
- **Layer 6 Head 0 Avg Effect:** 0.885
- **Layer 6 Head 1 Avg Effect:** 0.884
- **Layer 6 Head 2 Avg Effect:** 0.883
- **Layer 6 Head 3 Avg Effect:** 0.882
- **Layer 6 Head 4 Avg Effect:** 0.884
- **Layer 6 Head 5 Avg Effect:** 0.884
- **Layer 6 Head 6 Avg Effect:** 0.887
- **Layer 6 Head 7 Avg Effect:** 0.884
- **Layer 7 Head 0 Avg Effect:** 0.885
- **Layer 7 Head 1 Avg Effect:** 0.884
- **Layer 7 Head 2 Avg Effect:** 0.888
- **Layer 7 Head 3 Avg Effect:** 0.890
- **Layer 7 Head 4 Avg Effect:** 0.884
- **Layer 7 Head 5 Avg Effect:** 0.886
- **Layer 7 Head 6 Avg Effect:** 0.889
- **Layer 7 Head 7 Avg Effect:** 0.886
- **Layer 8 Head 0 Avg Effect:** 0.880
- **Layer 8 Head 1 Avg Effect:** 0.885
- **Layer 8 Head 2 Avg Effect:** 0.880
- **Layer 8 Head 3 Avg Effect:** 0.884
- **Layer 8 Head 4 Avg Effect:** 0.883
- **Layer 8 Head 5 Avg Effect:** 0.884
- **Layer 8 Head 6 Avg Effect:** 0.880
- **Layer 8 Head 7 Avg Effect:** 0.881
- **Layer 9 Head 0 Avg Effect:** 0.885
- **Layer 9 Head 1 Avg Effect:** 0.887
- **Layer 9 Head 2 Avg Effect:** 0.883
- **Layer 9 Head 3 Avg Effect:** 0.886
- **Layer 9 Head 4 Avg Effect:** 0.884
- **Layer 9 Head 5 Avg Effect:** 0.884
- **Layer 9 Head 6 Avg Effect:** 0.886
- **Layer 9 Head 7 Avg Effect:** 0.885
- **Layer 10 Head 0 Avg Effect:** 0.878
- **Layer 10 Head 1 Avg Effect:** 0.874
- **Layer 10 Head 2 Avg Effect:** 0.878
- **Layer 10 Head 3 Avg Effect:** 0.879
- **Layer 10 Head 4 Avg Effect:** 0.875
- **Layer 10 Head 5 Avg Effect:** 0.873
- **Layer 10 Head 6 Avg Effect:** 0.878
- **Layer 10 Head 7 Avg Effect:** 0.878
- **Layer 11 Head 0 Avg Effect:** 0.880
- **Layer 11 Head 1 Avg Effect:** 0.882
- **Layer 11 Head 2 Avg Effect:** 0.878
- **Layer 11 Head 3 Avg Effect:** 0.883
- **Layer 11 Head 4 Avg Effect:** 0.881
- **Layer 11 Head 5 Avg Effect:** 0.879
- **Layer 11 Head 6 Avg Effect:** 0.880
- **Layer 11 Head 7 Avg Effect:** 0.883
- **Layer 12 Head 0 Avg Effect:** 0.875
- **Layer 12 Head 1 Avg Effect:** 0.875
- **Layer 12 Head 2 Avg Effect:** 0.874
- **Layer 12 Head 3 Avg Effect:** 0.875
- **Layer 12 Head 4 Avg Effect:** 0.880
- **Layer 12 Head 5 Avg Effect:** 0.879
- **Layer 12 Head 6 Avg Effect:** 0.882
- **Layer 12 Head 7 Avg Effect:** 0.879
- **Layer 13 Head 0 Avg Effect:** 0.883
- **Layer 13 Head 1 Avg Effect:** 0.880
- **Layer 13 Head 2 Avg Effect:** 0.878
- **Layer 13 Head 3 Avg Effect:** 0.879
- **Layer 13 Head 4 Avg Effect:** 0.877
- **Layer 13 Head 5 Avg Effect:** 0.877
- **Layer 13 Head 6 Avg Effect:** 0.881
- **Layer 13 Head 7 Avg Effect:** 0.883
- **Layer 14 Head 0 Avg Effect:** 0.874
- **Layer 14 Head 1 Avg Effect:** 0.879
- **Layer 14 Head 2 Avg Effect:** 0.880
- **Layer 14 Head 3 Avg Effect:** 0.874
- **Layer 14 Head 4 Avg Effect:** 0.881
- **Layer 14 Head 5 Avg Effect:** 0.877
- **Layer 14 Head 6 Avg Effect:** 0.877
- **Layer 14 Head 7 Avg Effect:** 0.881
- **Layer 15 Head 0 Avg Effect:** 0.872
- **Layer 15 Head 1 Avg Effect:** 0.874
- **Layer 15 Head 2 Avg Effect:** 0.872
- **Layer 15 Head 3 Avg Effect:** 0.869
- **Layer 15 Head 4 Avg Effect:** 0.862
- **Layer 15 Head 5 Avg Effect:** 0.871
- **Layer 15 Head 6 Avg Effect:** 0.874
- **Layer 15 Head 7 Avg Effect:** 0.874
- **Layer 16 Head 0 Avg Effect:** 0.870
- **Layer 16 Head 1 Avg Effect:** 0.874
- **Layer 16 Head 2 Avg Effect:** 0.869
- **Layer 16 Head 3 Avg Effect:** 0.878
- **Layer 16 Head 4 Avg Effect:** 0.870
- **Layer 16 Head 5 Avg Effect:** 0.880
- **Layer 16 Head 6 Avg Effect:** 0.880
- **Layer 16 Head 7 Avg Effect:** 0.874
- **Layer 17 Head 0 Avg Effect:** 0.889
- **Layer 17 Head 1 Avg Effect:** 0.879
- **Layer 17 Head 2 Avg Effect:** 0.886
- **Layer 17 Head 3 Avg Effect:** 0.887
- **Layer 17 Head 4 Avg Effect:** 0.875
- **Layer 17 Head 5 Avg Effect:** 0.882
- **Layer 17 Head 6 Avg Effect:** 0.886
- **Layer 17 Head 7 Avg Effect:** 0.881
- **Layer 18 Head 0 Avg Effect:** 0.885
- **Layer 18 Head 1 Avg Effect:** 0.879
- **Layer 18 Head 2 Avg Effect:** 0.887
- **Layer 18 Head 3 Avg Effect:** 0.885
- **Layer 18 Head 4 Avg Effect:** 0.884
- **Layer 18 Head 5 Avg Effect:** 0.886
- **Layer 18 Head 6 Avg Effect:** 0.889
- **Layer 18 Head 7 Avg Effect:** 0.891
- **Layer 19 Head 0 Avg Effect:** 0.882
- **Layer 19 Head 1 Avg Effect:** 0.887
- **Layer 19 Head 2 Avg Effect:** 0.888
- **Layer 19 Head 3 Avg Effect:** 0.886
- **Layer 19 Head 4 Avg Effect:** 0.886
- **Layer 19 Head 5 Avg Effect:** 0.887
- **Layer 19 Head 6 Avg Effect:** 0.889
- **Layer 19 Head 7 Avg Effect:** 0.883
- **Layer 20 Head 0 Avg Effect:** 0.889
- **Layer 20 Head 1 Avg Effect:** 0.894
- **Layer 20 Head 2 Avg Effect:** 0.893
- **Layer 20 Head 3 Avg Effect:** 0.895
- **Layer 20 Head 4 Avg Effect:** 0.889
- **Layer 20 Head 5 Avg Effect:** 0.894
- **Layer 20 Head 6 Avg Effect:** 0.893
- **Layer 20 Head 7 Avg Effect:** 0.895
- **Layer 21 Head 0 Avg Effect:** 0.892
- **Layer 21 Head 1 Avg Effect:** 0.888
- **Layer 21 Head 2 Avg Effect:** 0.887
- **Layer 21 Head 3 Avg Effect:** 0.894
- **Layer 21 Head 4 Avg Effect:** 0.890
- **Layer 21 Head 5 Avg Effect:** 0.887
- **Layer 21 Head 6 Avg Effect:** 0.891
- **Layer 21 Head 7 Avg Effect:** 0.888
- **Layer 22 Head 0 Avg Effect:** 0.902
- **Layer 22 Head 1 Avg Effect:** 0.900
- **Layer 22 Head 2 Avg Effect:** 0.901
- **Layer 22 Head 3 Avg Effect:** 0.906
- **Layer 22 Head 4 Avg Effect:** 0.906
- **Layer 22 Head 5 Avg Effect:** 0.903
- **Layer 22 Head 6 Avg Effect:** 0.906
- **Layer 22 Head 7 Avg Effect:** 0.902
- **Layer 23 Head 0 Avg Effect:** 0.876
- **Layer 23 Head 1 Avg Effect:** 0.874
- **Layer 23 Head 2 Avg Effect:** 0.860
- **Layer 23 Head 3 Avg Effect:** 0.868
- **Layer 23 Head 4 Avg Effect:** 0.869
- **Layer 23 Head 5 Avg Effect:** 0.880
- **Layer 23 Head 6 Avg Effect:** 0.868
- **Layer 23 Head 7 Avg Effect:** 0.874
- **Layer 24 Head 0 Avg Effect:** 0.932
- **Layer 24 Head 1 Avg Effect:** 0.932
- **Layer 24 Head 2 Avg Effect:** 0.931
- **Layer 24 Head 3 Avg Effect:** 0.932
- **Layer 24 Head 4 Avg Effect:** 0.933
- **Layer 24 Head 5 Avg Effect:** 0.932
- **Layer 24 Head 6 Avg Effect:** 0.932
- **Layer 24 Head 7 Avg Effect:** 0.933
- **Layer 25 Head 0 Avg Effect:** 0.903
- **Layer 25 Head 1 Avg Effect:** 0.906
- **Layer 25 Head 2 Avg Effect:** 0.904
- **Layer 25 Head 3 Avg Effect:** 0.906
- **Layer 25 Head 4 Avg Effect:** 0.905
- **Layer 25 Head 5 Avg Effect:** 0.902
- **Layer 25 Head 6 Avg Effect:** 0.903
- **Layer 25 Head 7 Avg Effect:** 0.903
- **Layer 26 Head 0 Avg Effect:** 0.896
- **Layer 26 Head 1 Avg Effect:** 0.898
- **Layer 26 Head 2 Avg Effect:** 0.890
- **Layer 26 Head 3 Avg Effect:** 0.890
- **Layer 26 Head 4 Avg Effect:** 0.892
- **Layer 26 Head 5 Avg Effect:** 0.894
- **Layer 26 Head 6 Avg Effect:** 0.893
- **Layer 26 Head 7 Avg Effect:** 0.894
- **Layer 27 Head 0 Avg Effect:** 0.928
- **Layer 27 Head 1 Avg Effect:** 0.922
- **Layer 27 Head 2 Avg Effect:** 0.927
- **Layer 27 Head 3 Avg Effect:** 0.929
- **Layer 27 Head 4 Avg Effect:** 0.927
- **Layer 27 Head 5 Avg Effect:** 0.925
- **Layer 27 Head 6 Avg Effect:** 0.924
- **Layer 27 Head 7 Avg Effect:** 0.924
- **Layer 28 Head 0 Avg Effect:** 0.910
- **Layer 28 Head 1 Avg Effect:** 0.909
- **Layer 28 Head 2 Avg Effect:** 0.909
- **Layer 28 Head 3 Avg Effect:** 0.909
- **Layer 28 Head 4 Avg Effect:** 0.908
- **Layer 28 Head 5 Avg Effect:** 0.906
- **Layer 28 Head 6 Avg Effect:** 0.905
- **Layer 28 Head 7 Avg Effect:** 0.906
- **Layer 29 Head 0 Avg Effect:** 0.917
- **Layer 29 Head 1 Avg Effect:** 0.918
- **Layer 29 Head 2 Avg Effect:** 0.917
- **Layer 29 Head 3 Avg Effect:** 0.917
- **Layer 29 Head 4 Avg Effect:** 0.916
- **Layer 29 Head 5 Avg Effect:** 0.916
- **Layer 29 Head 6 Avg Effect:** 0.917
- **Layer 29 Head 7 Avg Effect:** 0.918
- **Layer 30 Head 0 Avg Effect:** 0.932
- **Layer 30 Head 1 Avg Effect:** 0.934
- **Layer 30 Head 2 Avg Effect:** 0.935
- **Layer 30 Head 3 Avg Effect:** 0.936
- **Layer 30 Head 4 Avg Effect:** 0.935
- **Layer 30 Head 5 Avg Effect:** 0.935
- **Layer 30 Head 6 Avg Effect:** 0.937
- **Layer 30 Head 7 Avg Effect:** 0.933
- **Layer 31 Head 0 Avg Effect:** 0.905
- **Layer 31 Head 1 Avg Effect:** 0.904
- **Layer 31 Head 2 Avg Effect:** 0.907
- **Layer 31 Head 3 Avg Effect:** 0.906
- **Layer 31 Head 4 Avg Effect:** 0.908
- **Layer 31 Head 5 Avg Effect:** 0.901
- **Layer 31 Head 6 Avg Effect:** 0.907
- **Layer 31 Head 7 Avg Effect:** 0.904
- **Layer 32 Head 0 Avg Effect:** 0.933
- **Layer 32 Head 1 Avg Effect:** 0.933
- **Layer 32 Head 2 Avg Effect:** 0.930
- **Layer 32 Head 3 Avg Effect:** 0.928
- **Layer 32 Head 4 Avg Effect:** 0.929
- **Layer 32 Head 5 Avg Effect:** 0.928
- **Layer 32 Head 6 Avg Effect:** 0.926
- **Layer 32 Head 7 Avg Effect:** 0.931
- **Layer 33 Head 0 Avg Effect:** 0.916
- **Layer 33 Head 1 Avg Effect:** 0.916
- **Layer 33 Head 2 Avg Effect:** 0.927
- **Layer 33 Head 3 Avg Effect:** 0.931
- **Layer 33 Head 4 Avg Effect:** 0.933
- **Layer 33 Head 5 Avg Effect:** 0.891
- **Layer 33 Head 6 Avg Effect:** 0.923
- **Layer 33 Head 7 Avg Effect:** 0.927
- **Top 10 Heads:** ['30:6', '30:3', '30:2', '30:4', '30:5', '30:1', '33:4', '30:7', '24:4', '32:0']

