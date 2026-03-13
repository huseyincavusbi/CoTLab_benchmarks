# Experiment: Histopathology Standard

**Status:** Running
**Started:** 2026-03-11 17:00:19

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
  name: google/medgemma-27b-text-it
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: google_medgemma_27b_text_it
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
  _target_: cotlab.experiments.SAEFeatureAnalysisExperiment
  name: sae_feature_analysis
  description: GemmaScope-2 histo feature identification and few-shot contrast
  sae_repo_id: google/gemma-scope-2-27b-it
  sae_site: resid_post_all
  sae_width: 64k
  sae_l0: medium
  target_layers:
  - 24
  - 25
  - 26
  - 27
  - 28
  top_k_features: 20
  few_shot_contrast: true
  num_samples: 500
  seed: 42
  max_input_tokens: 1024
  answer_cue: '


    Answer:'
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=sae_feature_analysis \
  experiment.num_samples=500 \
  experiment.seed=42 \
  prompt=chain_of_thought \
  dataset=histopathology
```

## Results

_Results will be added after experiment completes..._
