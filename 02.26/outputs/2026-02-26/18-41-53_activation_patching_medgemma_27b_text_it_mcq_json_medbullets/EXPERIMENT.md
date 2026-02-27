# Experiment: Medbullets Standard

**Status:** Completed
**Started:** 2026-02-26 18:41:53  
**Duration:** 2 minutes 33 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medbullets

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
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: true
  output_format: json
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MedBulletsDataset
  name: medbullets
  split: op5_test
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
  prompt=mcq \
  dataset=medbullets
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 1.6557, 2: -0.3761, 4: -0.4346, 6: -0.2009, 8: -0.7058, 10: 0.0041, 12: 0.3576, 14: 0.0818, 16: -0.7715, 18: -0.695, 20: 0.917, 22: -0.8966, 24: -0.7699, 26: -0.5258, 28: -0.3328, 30: 0.2963, 32: 0.5128, 34: -0.2234, 36: 0.2796, 38: 0.4066, 40: -0.1656, 42: 0.0956, 44: 0.2739, 46: -0.1912, 48: 0.0916, 50: 0.023, 52: -0.124, 54: 0.0135, 56: 0.2139, 58: -0.3574, 60: -0.2625}
- **Top 5 Causal Layers:** [0, 20, 32, 38, 12]

