# Experiment: Mmlu_medical Standard

**Status:** Completed
**Started:** 2026-02-26 19:25:05  
**Duration:** 3 minutes 27 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
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
  _target_: cotlab.datasets.loaders.MMLUMedicalDataset
  name: mmlu_medical
  filename: mmlu/medical_test.jsonl
experiment:
  _target_: cotlab.experiments.ActivationPatchingExperiment
  name: activation_patching
  description: Layer-wise causal activation patching (logit recovery)
  patching_mode: introspect_contrast
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
  dataset=mmlu_medical
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 1.12, 2: 0.0036, 4: -0.1642, 6: -0.119, 8: -0.1531, 10: 0.189, 12: 0.36, 14: -0.0118, 16: -0.137, 18: -0.1942, 20: 0.8894, 22: -0.1943, 24: -0.2, 26: -0.2, 28: -0.2, 30: 0.4248, 32: 0.5755, 34: -0.0541, 36: -0.09, 38: 0.6633, 40: -0.1949, 42: 0.0577, 44: 0.0675, 46: -0.1537, 48: -0.0754, 50: -0.0893, 52: 0.3689, 54: 0.5614, 56: 0.3964, 58: 0.1532, 60: -0.0649}
- **Top 5 Causal Layers:** [0, 20, 38, 32, 54]

