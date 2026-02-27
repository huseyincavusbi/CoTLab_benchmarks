# Experiment: M_arc Standard

**Status:** Completed
**Started:** 2026-02-26 19:10:36  
**Duration:** 4 minutes 17 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** m_arc

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
  _target_: cotlab.datasets.loaders.MARCDataset
  name: m_arc
  filename: m_arc/test-00000-of-00001.parquet
  split: test
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
  dataset=m_arc
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 0.2506, 2: -0.028, 4: 0.4309, 6: 0.2033, 8: 0.6089, 10: 0.6103, 12: -0.0583, 14: 0.2769, 16: 0.6264, 18: 0.7292, 20: 0.1648, 22: 0.6539, 24: 0.4005, 26: 0.5813, 28: 0.469, 30: 0.2601, 32: -0.0241, 34: 0.3325, 36: 0.6439, 38: 0.066, 40: 0.5909, 42: 0.2657, 44: 0.3111, 46: 0.3427, 48: 0.2192, 50: 0.0435, 52: 0.0503, 54: -0.0319, 56: -0.0577, 58: -0.0899, 60: 0.0448}
- **Top 5 Causal Layers:** [18, 22, 36, 16, 10]

