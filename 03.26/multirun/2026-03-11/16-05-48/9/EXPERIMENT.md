# Experiment: Oncology Standard

**Status:** Completed
**Started:** 2026-03-11 16:43:36  
**Duration:** 3 minutes 48 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** oncology

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
  _target_: cotlab.datasets.OncologyDataset
  name: oncology
  path: data/oncology.json
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
  dataset=oncology
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: -0.3872, 2: -0.0578, 4: -0.1687, 6: 0.1105, 8: 0.2991, 10: 0.0554, 12: -0.0832, 14: 0.0163, 16: 0.1955, 18: 0.2978, 20: 0.3208, 22: -0.1684, 24: 1.091, 26: 0.2743, 28: 1.1241, 30: 1.4003, 32: 0.1401, 34: 1.3771, 36: 0.6409, 38: 0.3722, 40: 1.2285, 42: 0.8737, 44: -0.5197, 46: -0.0185, 48: 1.1667, 50: 0.1097, 52: 0.4588, 54: 0.0297, 56: -0.3504, 58: 0.5031, 60: 0.5017}
- **Top 5 Causal Layers:** [30, 34, 40, 48, 28]

