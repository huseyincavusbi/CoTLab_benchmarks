# Experiment: Medxpertqa Standard

**Status:** Completed
**Started:** 2026-03-11 16:22:23  
**Duration:** 5 minutes 17 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
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
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medxpertqa
  filename: medxpertqa/test.jsonl
  split: test
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
  dataset=medxpertqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 0.7533, 2: -0.0385, 4: 0.3384, 6: 0.2992, 8: 0.1624, 10: 0.6065, 12: 0.6283, 14: 0.2868, 16: 0.3302, 18: -0.0449, 20: 0.1915, 22: 0.7244, 24: 0.5474, 26: 0.3059, 28: 0.0242, 30: 0.3079, 32: 0.1336, 34: 0.1991, 36: 0.2059, 38: 0.1499, 40: 0.1769, 42: 0.1544, 44: 0.3536, 46: 0.1128, 48: 0.318, 50: 0.0493, 52: 0.099, 54: 0.1629, 56: 0.1355, 58: 0.2136, 60: 0.175}
- **Top 5 Causal Layers:** [0, 22, 12, 10, 24]

