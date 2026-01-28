# Experiment: Medqa Standard

**Status:** Completed
**Started:** 2026-01-27 21:22:26  
**Duration:** 0 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medqa

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
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medqa
  filename: medqa/test.jsonl
  split: test
experiment:
  _target_: cotlab.experiments.AttentionAnalysisExperiment
  name: attention_analysis
  description: Analyze attention patterns at critical layers
  all_layers: false
  force_eager_reload: false
  num_samples: 3
  target_layers:
  - 0
  - 1
  - 2
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=attention_analysis \
  experiment.num_samples=3 \
  prompt=mcq \
  dataset=medqa
```

## Results

- **Samples Processed:** 3
- **Num Samples Analyzed:** 3
- **Num Layers Analyzed:** 3
- **Num Heads:** 32
- **Overall Mean Entropy:** 2.577
- **Most Focused Layer:** 1
- **Most Focused Entropy:** 1.879

