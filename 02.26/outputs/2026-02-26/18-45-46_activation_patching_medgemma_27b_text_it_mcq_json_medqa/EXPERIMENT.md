# Experiment: Medqa Standard

**Status:** Completed
**Started:** 2026-02-26 18:45:46  
**Duration:** 2 minutes 20 seconds

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
  dataset=medqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 1.4071, 2: -0.3863, 4: -0.4211, 6: -0.2044, 8: -0.7768, 10: -0.0575, 12: 0.3696, 14: -0.1725, 16: -0.8733, 18: -0.8849, 20: 0.7563, 22: -0.9452, 24: -0.8289, 26: -0.5639, 28: -0.3379, 30: 0.1548, 32: 0.3848, 34: -0.4107, 36: 0.4226, 38: 0.2455, 40: -0.1425, 42: 0.1654, 44: 0.2731, 46: -0.2475, 48: -0.0402, 50: 0.0243, 52: -0.1416, 54: 0.0783, 56: 0.0608, 58: -0.2392, 60: -0.1507}
- **Top 5 Causal Layers:** [0, 20, 36, 32, 12]

