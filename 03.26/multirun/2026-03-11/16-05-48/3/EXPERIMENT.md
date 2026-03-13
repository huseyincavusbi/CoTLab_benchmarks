# Experiment: Medqa Standard

**Status:** Completed
**Started:** 2026-03-11 16:17:59  
**Duration:** 4 minutes 14 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
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
  name: medqa
  filename: medqa/test.jsonl
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
  dataset=medqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 0.0049, 2: 0.2032, 4: 0.1993, 6: -0.0566, 8: -0.0341, 10: 0.2525, 12: -0.0846, 14: 0.4613, 16: 0.0148, 18: 0.442, 20: 0.5607, 22: 0.0775, 24: 0.8396, 26: 0.9571, 28: 0.4486, 30: 0.8505, 32: 0.403, 34: 0.0633, 36: 0.1102, 38: 0.0275, 40: 0.1624, 42: 0.2808, 44: -0.0073, 46: 0.2923, 48: 0.4171, 50: 0.1186, 52: 0.7805, 54: 0.0316, 56: 0.2144, 58: 0.2869, 60: 0.5038}
- **Top 5 Causal Layers:** [26, 30, 24, 52, 20]

