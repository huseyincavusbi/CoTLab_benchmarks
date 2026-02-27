# Experiment: Plab Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-26 19:36:37  
**Duration:** 1 minutes 55 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Plab
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
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
  variant: 27b-text
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b_text_it
prompt:
  _target_: cotlab.prompts.PLABPromptStrategy
  name: plab
  few_shot: false
  output_format: json
  answer_first: false
  contrarian: false
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
  prompt=plab \
  prompt.few_shot=false \
  dataset=plab
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 1.26, 2: -0.2707, 4: 0.0544, 6: 0.8131, 8: -0.0815, 10: 1.1683, 12: 0.7741, 14: 0.2513, 16: -0.1772, 18: -0.0071, 20: 1.12, 22: -0.235, 24: -0.1316, 26: -0.1266, 28: -0.1465, 30: -0.2677, 32: -0.0406, 34: -0.2677, 36: -0.0174, 38: 0.5242, 40: 0.2215, 42: 0.0823, 44: 0.2291, 46: 0.2774, 48: 0.1118, 50: -0.1423, 52: 0.0229, 54: 0.2019, 56: 0.0663, 58: -0.141, 60: -0.0471}
- **Top 5 Causal Layers:** [0, 10, 20, 6, 12]

