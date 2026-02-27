# Experiment: Pubmedqa Standard

**Status:** Completed
**Started:** 2026-02-26 19:42:05  
**Duration:** 3 minutes 56 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Pubmedqa
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** pubmedqa

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
  _target_: cotlab.prompts.pubmedqa.PubMedQAPromptStrategy
  name: pubmedqa
  output_format: json
  few_shot: true
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.PubMedQADataset
  name: pubmedqa
  filename: pubmedqa/test.jsonl
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
  prompt=pubmedqa \
  dataset=pubmedqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 0.6859, 2: 0.179, 4: 0.1745, 6: 0.2013, 8: 0.6721, 10: 0.2475, 12: 0.1958, 14: 0.3546, 16: 0.2694, 18: 0.3848, 20: 0.28, 22: 0.6093, 24: 0.64, 26: 0.64, 28: 0.64, 30: 0.5542, 32: 0.3625, 34: 0.2617, 36: 0.6164, 38: 0.3617, 40: 0.6488, 42: 0.3288, 44: 0.292, 46: 0.5442, 48: 0.2887, 50: 0.022, 52: 0.224, 54: 0.1358, 56: 0.1964, 58: -0.0148, 60: 0.0073}
- **Top 5 Causal Layers:** [0, 8, 40, 24, 26]

