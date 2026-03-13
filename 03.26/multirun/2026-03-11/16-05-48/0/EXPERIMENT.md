# Experiment: Afrimedqa Standard

**Status:** Completed
**Started:** 2026-03-11 16:05:48  
**Duration:** 3 minutes 37 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** afrimedqa

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
  name: afrimedqa
  filename: afrimedqa/mcq.jsonl
  split: mcq
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
  dataset=afrimedqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: -0.8462, 2: 0.0957, 4: 0.114, 6: -0.0719, 8: -0.0349, 10: 0.0692, 12: -0.286, 14: 0.173, 16: -0.0728, 18: 0.1394, 20: 0.5044, 22: -0.0748, 24: 1.1664, 26: 0.9541, 28: 0.6187, 30: 0.9619, 32: 0.4493, 34: 0.1248, 36: -0.1261, 38: -0.2028, 40: 0.27, 42: 0.2294, 44: 0.1267, 46: 0.3403, 48: 0.5608, 50: 0.1213, 52: 0.9538, 54: -0.0456, 56: 0.3033, 58: 0.2902, 60: 0.4511}
- **Top 5 Causal Layers:** [24, 30, 26, 52, 28]

