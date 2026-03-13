# Experiment: Histopathology Standard

**Status:** Completed
**Started:** 2026-03-11 16:35:31  
**Duration:** 4 minutes 1 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** histopathology

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
  _target_: cotlab.datasets.HistopathologyDataset
  name: histopathology
  path: data/histopathology.tsv
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
  dataset=histopathology
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: -0.1865, 2: 0.0689, 4: 0.2529, 6: 0.0892, 8: -0.4046, 10: 0.5029, 12: 0.3895, 14: 0.22, 16: -0.3872, 18: 0.381, 20: -0.3119, 22: -0.0439, 24: -0.4055, 26: -0.6059, 28: -0.4338, 30: 0.1955, 32: -0.1236, 34: 0.351, 36: 0.0628, 38: 1.2043, 40: 0.6154, 42: 0.2919, 44: 0.153, 46: 0.356, 48: 0.4079, 50: -0.6022, 52: 0.6639, 54: 0.1954, 56: -0.2486, 58: -0.0762, 60: -0.5783}
- **Top 5 Causal Layers:** [38, 52, 40, 10, 48]

