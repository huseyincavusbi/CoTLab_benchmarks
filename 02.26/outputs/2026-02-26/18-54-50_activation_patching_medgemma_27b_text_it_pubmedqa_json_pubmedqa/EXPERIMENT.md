# Experiment: Pubmedqa Standard

**Status:** Completed
**Started:** 2026-02-26 18:54:50  
**Duration:** 2 minutes 51 seconds

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
  prompt=pubmedqa \
  dataset=pubmedqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Layer Stride:** 2
- **Mean Effect Per Layer:** {0: 0.2542, 2: -0.1122, 4: 0.0194, 6: -0.0416, 8: -0.1953, 10: 0.0848, 12: -0.1129, 14: 0.0901, 16: 0.0555, 18: -0.3918, 20: 1.4359, 22: -0.7446, 24: -0.9283, 26: -0.2937, 28: -0.0048, 30: -0.3469, 32: 0.1658, 34: 0.09, 36: 0.2026, 38: -0.0847, 40: -0.2269, 42: -0.187, 44: -0.3339, 46: -0.2473, 48: -0.2893, 50: 0.201, 52: -0.1122, 54: 0.2616, 56: 0.321, 58: 0.3727, 60: -0.0485}
- **Top 5 Causal Layers:** [20, 58, 56, 54, 0]

