# Experiment: M_arc Standard

**Status:** Completed
**Started:** 2026-02-26 16:10:00  
**Duration:** 43 seconds

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
  _target_: cotlab.experiments.AttentionAnalysisExperiment
  name: attention_analysis
  description: Analyze attention patterns at critical layers
  all_layers: true
  target_layers: null
  layer_stride: 1
  force_eager_reload: false
  num_samples: null
  last_k_tokens: 16
  max_input_tokens: 1024
  analyze_generated_tokens: false
  generated_max_new_tokens: 16
  generated_do_sample: false
  generated_temperature: 0.7
  generated_top_p: 0.9
  question: Patient presents with chest pain, sweating, and shortness of breath. What
    is the diagnosis?
  batch_size: 16
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=attention_analysis \
  prompt=mcq \
  dataset=m_arc
```

## Results

- **Samples Processed:** 62
- **Num Samples Analyzed:** 100
- **Num Layers Analyzed:** 62
- **Num Heads:** 32
- **Overall Mean Entropy:** 1.609
- **Overall Mean Entropy All Tokens:** 1.609
- **Overall Mean Entropy Last Token:** 2.237
- **Overall Mean Entropy Last K Tokens:** 2.132
- **Last K Tokens:** 16
- **Most Focused Layer:** 3
- **Most Focused Entropy:** 0.283
- **Most Focused Layer All Tokens:** 3
- **Most Focused Entropy All Tokens:** 0.283
- **Most Focused Layer Last Token:** 3
- **Most Focused Entropy Last Token:** 0.540
- **Analyze Generated Tokens:** False

