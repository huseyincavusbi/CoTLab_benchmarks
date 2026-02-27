# Experiment: Medqa Standard

**Status:** Completed
**Started:** 2026-02-26 19:19:44  
**Duration:** 4 minutes 3 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medqa

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
  name: medqa
  filename: medqa/test.jsonl
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
  dataset=medqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: -0.3367, 2: 0.1016, 4: 1.0137, 6: 0.9175, 8: 1.2134, 10: 0.603, 12: -0.2354, 14: 0.6423, 16: 1.1124, 18: 1.2534, 20: -0.2016, 22: 1.2731, 24: 1.2802, 26: 1.2809, 28: 1.2531, 30: 0.429, 32: -0.1937, 34: 0.3531, 36: 1.1084, 38: -0.2598, 40: 0.9509, 42: 0.7251, 44: 0.3023, 46: 1.0595, 48: 0.3147, 50: 0.2341, 52: 0.0453, 54: -0.1197, 56: -0.1884, 58: 0.1975, 60: 0.1337}
- **Top 5 Causal Layers:** [26, 24, 22, 18, 28]

