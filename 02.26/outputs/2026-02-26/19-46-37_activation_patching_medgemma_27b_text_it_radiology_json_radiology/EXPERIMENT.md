# Experiment: Radiology Standard

**Status:** Completed
**Started:** 2026-02-26 19:46:37  
**Duration:** 3 minutes 7 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** radiology

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
  _target_: cotlab.prompts.RadiologyPromptStrategy
  name: radiology
  contrarian: false
  few_shot: true
  answer_first: false
  output_format: json
dataset:
  _target_: cotlab.datasets.RadiologyDataset
  name: radiology
  path: data/radiology.json
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
  prompt=radiology \
  dataset=radiology
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 1.626, 2: 0.4122, 4: -0.2615, 6: -0.3312, 8: 0.3132, 10: 0.2229, 12: -0.0522, 14: 0.3153, 16: 0.7181, 18: 0.3686, 20: 0.6079, 22: 0.8566, 24: 0.9353, 26: 0.34, 28: 0.7799, 30: 0.4784, 32: 0.4311, 34: 0.4154, 36: -0.2438, 38: 0.3652, 40: 0.4872, 42: 0.3696, 44: 0.6771, 46: 0.34, 48: 0.4742, 50: 0.7659, 52: -0.2953, 54: 0.3297, 56: 0.3761, 58: 0.4914, 60: 0.2446}
- **Top 5 Causal Layers:** [0, 24, 22, 28, 50]

