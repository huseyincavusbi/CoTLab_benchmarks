# Experiment: M_arc Standard

**Status:** Completed
**Started:** 2026-02-26 18:39:01  
**Duration:** 2 minutes 35 seconds

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
  patching_mode: few_shot_contrast
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
- **Mean Effect Per Layer:** {0: 1.3501, 2: -0.1638, 4: -0.1728, 6: 0.1253, 8: -0.355, 10: -0.1099, 12: 0.3044, 14: -0.0394, 16: -0.3921, 18: -0.4844, 20: 0.9177, 22: -0.4198, 24: -0.1812, 26: 0.2617, 28: -0.1077, 30: 0.164, 32: 0.6129, 34: -0.3084, 36: 0.3547, 38: 0.2144, 40: -0.0654, 42: 0.2342, 44: 0.2595, 46: -0.3118, 48: -0.0855, 50: -0.0002, 52: -0.257, 54: 0.1381, 56: 0.2053, 58: -0.1956, 60: -0.1528}
- **Top 5 Causal Layers:** [0, 20, 32, 36, 12]

