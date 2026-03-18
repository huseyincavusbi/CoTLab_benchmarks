# Experiment: Afrimedqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-03-18 09:11:54  
**Duration:** 1 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** afrimedqa

<details>
<summary>Full Configuration (YAML)</summary>

```yaml
backend:
  _target_: cotlab.backends.TransformersBackend
  device: mps
  dtype: bfloat16
  enable_hooks: true
  trust_remote_code: true
model:
  name: google/gemma-3-270m-it
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
prompt:
  _target_: cotlab.prompts.ChainOfThoughtStrategy
  name: chain_of_thought
  system_role: 'You are a medical expert. Think through problems carefully and

    explain your reasoning step by step before giving your final answer.

    '
  include_examples: false
  cot_trigger: 'Let''s think through this step by step:'
  output_format: plain
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: afrimedqa
  filename: afrimedqa/mcq.jsonl
  split: mcq
experiment:
  _target_: cotlab.experiments.HNeuronAnalysisExperiment
  name: h_neuron_analysis
  description: CETT-based H-Neuron discovery and causal validation
  num_samples: 10
  validation_split: 0.2
  l1_C: 0.1
  alpha_values:
  - 0.0
  - 0.5
  - 1.0
  - 1.5
  - 2.0
  layer_stride: 1
  seed: 42
  max_input_tokens: 1024
  answer_cue: '


    Answer:'
  contrastive_labeling: true
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=h_neuron_analysis \
  experiment.num_samples=10 \
  experiment.seed=42 \
  prompt=chain_of_thought \
  prompt.output_format=plain \
  dataset=afrimedqa
```

## Results

- **Accuracy:** 20.0%
- **Samples Processed:** 1
- **Dataset:** afrimedqa
- **N Samples:** 10
- **N Training Rows:** 20
- **N Layers:** 18
- **Intermediate Dim:** 2048
- **N Features:** 36864
- **Probe Balanced Accuracy:** 0.500
- **Probe Auroc:** 0.500
- **Random Baseline Balanced Accuracy:** None
- **Random Baseline Auroc:** None
- **N H Neurons:** 0
- **H Neuron Ratio Permille:** 0.000
- **Layer Distribution:** {}
- **Contrastive Labeling:** True
- **Top H Neurons:** []

