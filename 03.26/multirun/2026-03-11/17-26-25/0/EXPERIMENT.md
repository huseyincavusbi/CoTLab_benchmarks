# Experiment: Afrimedqa Standard

**Status:** Completed
**Started:** 2026-03-11 17:26:26  
**Duration:** 2 minutes 37 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** afrimedqa

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
  _target_: cotlab.datasets.loaders.MedQADataset
  name: afrimedqa
  filename: afrimedqa/mcq.jsonl
  split: mcq
experiment:
  _target_: cotlab.experiments.SAEFeatureAnalysisExperiment
  name: sae_feature_analysis
  description: GemmaScope-2 histo feature identification and few-shot contrast
  sae_repo_id: google/gemma-scope-2-27b-it
  sae_site: resid_post_all
  sae_width: 16k
  sae_l0: small
  target_layers:
  - 50
  - 51
  - 52
  - 53
  - 54
  - 55
  - 56
  - 57
  - 58
  - 59
  - 60
  - 61
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
  dataset=afrimedqa
```

## Results

- **Samples Processed:** 2
- **Layers Analysed:** [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]
- **Sae Repo Id:** google/gemma-scope-2-27b-it
- **Top K Features:** 20
- **Layer 50 Top Feature:** 969
- **Layer 50 Top Histo Score:** 49892.041
- **Layer 50 N Significant Features:** 18
- **Layer 51 Top Feature:** 969
- **Layer 51 Top Histo Score:** 50058.120
- **Layer 51 N Significant Features:** 19
- **Layer 52 Top Feature:** 8863
- **Layer 52 Top Histo Score:** 37135.538
- **Layer 52 N Significant Features:** 20
- **Layer 53 Top Feature:** 8863
- **Layer 53 Top Histo Score:** 43880.433
- **Layer 53 N Significant Features:** 20
- **Layer 54 Top Feature:** 6616
- **Layer 54 Top Histo Score:** 51403.485
- **Layer 54 N Significant Features:** 20
- **Layer 55 Top Feature:** 15406
- **Layer 55 Top Histo Score:** 44339.757
- **Layer 55 N Significant Features:** 19
- **Layer 56 Top Feature:** 9128
- **Layer 56 Top Histo Score:** 49014.758
- **Layer 56 N Significant Features:** 18
- **Layer 57 Top Feature:** 2197
- **Layer 57 Top Histo Score:** 58026.453
- **Layer 57 N Significant Features:** 18
- **Layer 58 Top Feature:** 14047
- **Layer 58 Top Histo Score:** 54835.991
- **Layer 58 N Significant Features:** 17
- **Layer 59 Top Feature:** 10364
- **Layer 59 Top Histo Score:** 103891.670
- **Layer 59 N Significant Features:** 19
- **Layer 60 Top Feature:** 14443
- **Layer 60 Top Histo Score:** 114742.708
- **Layer 60 N Significant Features:** 16
- **Layer 61 Top Feature:** 313
- **Layer 61 Top Histo Score:** 48233.515
- **Layer 61 N Significant Features:** 20

