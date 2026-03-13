# Experiment: Mmlu_medical Standard

**Status:** Completed
**Started:** 2026-03-11 17:19:19  
**Duration:** 1 minutes 15 seconds

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
  _target_: cotlab.datasets.loaders.MMLUMedicalDataset
  name: mmlu_medical
  filename: mmlu/medical_test.jsonl
experiment:
  _target_: cotlab.experiments.SAEFeatureAnalysisExperiment
  name: sae_feature_analysis
  description: GemmaScope-2 histo feature identification and few-shot contrast
  sae_repo_id: google/gemma-scope-2-27b-it
  sae_site: resid_post_all
  sae_width: 16k
  sae_l0: small
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
  dataset=mmlu_medical
```

## Results

- **Samples Processed:** 2
- **Layers Analysed:** [24, 25, 26, 27, 28]
- **Sae Repo Id:** google/gemma-scope-2-27b-it
- **Top K Features:** 20
- **Layer 24 Top Feature:** 11930
- **Layer 24 Top Histo Score:** 5651.781
- **Layer 24 N Significant Features:** 20
- **Layer 25 Top Feature:** 15071
- **Layer 25 Top Histo Score:** 9861.222
- **Layer 25 N Significant Features:** 19
- **Layer 26 Top Feature:** 12445
- **Layer 26 Top Histo Score:** 13528.949
- **Layer 26 N Significant Features:** 11
- **Layer 27 Top Feature:** 17
- **Layer 27 Top Histo Score:** 7332.122
- **Layer 27 N Significant Features:** 20
- **Layer 28 Top Feature:** 528
- **Layer 28 Top Histo Score:** 7831.899
- **Layer 28 N Significant Features:** 20

