# Experiment: Neurology Standard

**Status:** Completed
**Started:** 2026-03-11 16:39:42  
**Duration:** 3 minutes 45 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** neurology

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
  _target_: cotlab.datasets.NeurologyDataset
  name: neurology
  path: data/neurology.json
experiment:
  _target_: cotlab.experiments.ActivationPatchingExperiment
  name: activation_patching
  description: Layer-wise causal activation patching (logit recovery)
  patching_mode: cot_contrast
  layer_stride: 2
  num_samples: 100
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
  experiment.num_samples=100 \
  experiment.seed=42 \
  prompt=chain_of_thought \
  dataset=neurology
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: -0.7099, 2: -0.0731, 4: -0.1618, 6: 0.2283, 8: 0.1468, 10: -0.1401, 12: -0.2812, 14: -0.0343, 16: 0.2085, 18: 0.1962, 20: 0.1362, 22: -0.3099, 24: 1.0414, 26: 0.1829, 28: 1.0761, 30: 1.4248, 32: 0.2009, 34: 1.3886, 36: 0.1122, 38: 0.0273, 40: 1.12, 42: 0.6729, 44: -0.6284, 46: -0.1383, 48: 1.2217, 50: 0.0435, 52: 0.3687, 54: 0.0208, 56: -0.5148, 58: 0.4767, 60: 0.6609}
- **Top 5 Causal Layers:** [30, 34, 48, 40, 28]

