# Experiment: Mmlu_medical Standard

**Status:** Completed
**Started:** 2026-03-11 16:27:50  
**Duration:** 3 minutes 31 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** mmlu_medical

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
  _target_: cotlab.datasets.loaders.MMLUMedicalDataset
  name: mmlu_medical
  filename: mmlu/medical_test.jsonl
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
  dataset=mmlu_medical
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: -0.7091, 2: 0.0265, 4: 0.1541, 6: -0.1616, 8: 0.0291, 10: 0.1231, 12: -0.27, 14: 0.1019, 16: -0.2464, 18: 0.1356, 20: 0.5155, 22: -0.0403, 24: 1.416, 26: 0.9058, 28: 0.822, 30: 1.0645, 32: 0.3986, 34: 0.0222, 36: -0.0204, 38: -0.0468, 40: 0.2434, 42: 0.2686, 44: 0.3755, 46: 0.5231, 48: 0.6132, 50: 0.195, 52: 0.8593, 54: 0.035, 56: 0.4285, 58: 0.2553, 60: 0.415}
- **Top 5 Causal Layers:** [24, 30, 26, 52, 28]

