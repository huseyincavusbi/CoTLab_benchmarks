# Experiment: Plab Standard

**Status:** Completed
**Started:** 2026-03-11 16:51:06  
**Duration:** 3 minutes 38 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** plab

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
  _target_: cotlab.datasets.loaders.PLABDataset
  name: plab
  split: main
  filename: plab/data.json
  topics_filename: plab/topics.json
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
  dataset=plab
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: -0.5868, 2: 0.0875, 4: 0.1799, 6: -0.0566, 8: 0.102, 10: 0.2045, 12: -0.1793, 14: 0.2922, 16: -0.2464, 18: 0.3731, 20: 0.6424, 22: -0.0671, 24: 1.08, 26: 1.177, 28: 0.2549, 30: 0.3214, 32: 0.227, 34: 0.299, 36: 0.1431, 38: -0.1019, 40: 0.376, 42: 0.4882, 44: 0.1392, 46: 0.3456, 48: 0.5879, 50: 0.1555, 52: 0.8372, 54: 0.2406, 56: 0.1447, 58: 0.4682, 60: 0.4985}
- **Top 5 Causal Layers:** [26, 24, 52, 20, 48]

