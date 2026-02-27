# Experiment: Pubhealthbench Standard

**Status:** Completed
**Started:** 2026-02-26 19:39:32  
**Duration:** 2 minutes 6 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Pubhealthbench
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** pubhealthbench

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
  _target_: cotlab.prompts.pubhealthbench.PubHealthBenchMCQPromptStrategy
  name: pubhealthbench
  output_format: json
dataset:
  _target_: cotlab.datasets.loaders.PubHealthBenchDataset
  name: pubhealthbench
  split: reviewed
experiment:
  _target_: cotlab.experiments.ActivationPatchingExperiment
  name: activation_patching
  description: Layer-wise causal activation patching (logit recovery)
  patching_mode: introspect_contrast
  layer_stride: 2
  num_samples: 50
  max_input_tokens: 1024
  seed: 42
  answer_cue: '


    Answer:'
  introspect_instruction: Think deeply about this problem. Carefully reason through
    the underlying mechanisms and consider all relevant factors before committing
    to your answer.
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=activation_patching \
  experiment.num_samples=50 \
  experiment.seed=42 \
  prompt=pubhealthbench \
  dataset=pubhealthbench
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 0.4073, 2: 0.1554, 4: 0.1009, 6: 0.2547, 8: 0.4185, 10: 0.1768, 12: 0.1031, 14: 0.2104, 16: 0.3638, 18: 0.4066, 20: 0.3214, 22: 0.66, 24: 0.6967, 26: 0.3161, 28: 0.1457, 30: 0.2779, 32: 0.421, 34: 0.4788, 36: -0.0222, 38: 0.2734, 40: 0.1136, 42: -0.0072, 44: 0.1245, 46: -0.0113, 48: 0.0329, 50: -0.0525, 52: 0.1144, 54: 0.0096, 56: 0.2615, 58: -0.1547, 60: -0.0637}
- **Top 5 Causal Layers:** [24, 22, 34, 32, 8]

