# Experiment: Medxpertqa Standard

**Status:** Completed
**Started:** 2026-02-26 19:29:09  
**Duration:** 4 minutes 51 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medxpertqa

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
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medxpertqa
  filename: medxpertqa/test.jsonl
  split: test
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
  prompt=mcq \
  dataset=medxpertqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 1.0639, 2: 0.2338, 4: -0.2795, 6: -0.1071, 8: 0.3687, 10: 0.2562, 12: 0.6895, 14: 0.2241, 16: 0.0771, 18: -0.1032, 20: 0.8169, 22: -0.1886, 24: -0.2362, 26: -0.36, 28: -0.0043, 30: 0.4572, 32: 0.3774, 34: 0.0751, 36: -0.099, 38: 0.4914, 40: -0.4097, 42: -0.3334, 44: -0.1307, 46: -0.2291, 48: -0.2644, 50: -0.1557, 52: 0.5377, 54: 0.2225, 56: 0.2965, 58: 0.1567, 60: 0.0741}
- **Top 5 Causal Layers:** [0, 20, 12, 52, 38]

