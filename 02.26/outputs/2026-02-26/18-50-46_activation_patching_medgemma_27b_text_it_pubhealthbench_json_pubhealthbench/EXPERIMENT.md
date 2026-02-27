# Experiment: Pubhealthbench Standard

**Status:** Completed
**Started:** 2026-02-26 18:50:46  
**Duration:** 2 minutes 8 seconds

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
  patching_mode: few_shot_contrast
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
- **Mean Effect Per Layer:** {0: 0.0, 2: 0.0, 4: 0.0, 6: 0.0, 8: 0.0, 10: 0.0, 12: 0.0, 14: 0.0, 16: 0.0, 18: 0.0, 20: 0.0, 22: 0.0, 24: 0.0, 26: 0.0, 28: 0.0, 30: 0.0, 32: 0.0, 34: 0.0, 36: 0.0, 38: 0.0, 40: 0.0, 42: 0.0, 44: 0.0, 46: 0.0, 48: 0.0, 50: 0.0, 52: 0.0, 54: 0.0, 56: 0.0, 58: 0.0, 60: 0.0}
- **Top 5 Causal Layers:** [0, 2, 4, 6, 8]

