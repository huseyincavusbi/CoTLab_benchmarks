# Experiment: Cardiology Standard

**Status:** Completed
**Started:** 2026-03-11 16:31:31  
**Duration:** 3 minutes 51 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** cardiology

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
  _target_: cotlab.datasets.CardiologyDataset
  name: cardiology
  path: data/cardiology.json
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
  dataset=cardiology
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: -0.5117, 2: -0.1555, 4: -0.2204, 6: 0.1315, 8: 0.5946, 10: -0.2065, 12: -0.3263, 14: -0.2089, 16: 0.3616, 18: -0.0813, 20: -0.0523, 22: -0.2787, 24: 0.8358, 26: 0.0816, 28: 1.3813, 30: 1.4076, 32: 0.0799, 34: 1.3825, 36: 0.0435, 38: -0.006, 40: 1.4255, 42: 0.9202, 44: -0.5758, 46: -0.1086, 48: 1.3528, 50: 0.2135, 52: 0.2909, 54: 0.1038, 56: -0.5237, 58: 0.3884, 60: 0.8152}
- **Top 5 Causal Layers:** [40, 30, 34, 28, 48]

