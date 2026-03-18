# Experiment: Medmcqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-03-18 09:19:30  
**Duration:** 1 minutes 41 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Chain_of_thought
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** medmcqa

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
  name: google/medgemma-4b-it
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
  name: medmcqa
  filename: medmcqa/validation.jsonl
  split: validation
experiment:
  _target_: cotlab.experiments.HNeuronAnalysisExperiment
  name: h_neuron_analysis
  description: CETT-based H-Neuron discovery and causal validation
  num_samples: 100
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
  experiment.num_samples=100 \
  experiment.seed=42 \
  prompt=chain_of_thought \
  prompt.output_format=plain \
  dataset=medmcqa
```

## Results

- **Accuracy:** 47.0%
- **Samples Processed:** 1
- **Dataset:** medmcqa
- **N Samples:** 100
- **N Training Rows:** 200
- **N Layers:** 34
- **Intermediate Dim:** 10240
- **N Features:** 348160
- **Probe Balanced Accuracy:** 0.862
- **Probe Auroc:** 0.931
- **Random Baseline Balanced Accuracy:** 0.845
- **Random Baseline Auroc:** 0.959
- **N H Neurons:** 11
- **H Neuron Ratio Permille:** 0.032
- **Layer Distribution:** {18: 1, 24: 1, 12: 4, 11: 1, 14: 2, 15: 1, 13: 1}
- **Contrastive Labeling:** True
- **Top H Neurons:** [{'layer': 18, 'neuron': 3185}, {'layer': 24, 'neuron': 1464}, {'layer': 12, 'neuron': 4914}, {'layer': 11, 'neuron': 4962}, {'layer': 14, 'neuron': 3397}, {'layer': 15, 'neuron': 3150}, {'layer': 12, 'neuron': 8585}, {'layer': 12, 'neuron': 90}, {'layer': 12, 'neuron': 5034}, {'layer': 13, 'neuron': 6373}, {'layer': 14, 'neuron': 2870}]
- **Accuracy Alpha 0.0:** 0.450
- **Accuracy Alpha 0.5:** 0.450
- **Accuracy Alpha 1.0:** 0.450
- **Accuracy Alpha 1.5:** 0.450
- **Accuracy Alpha 2.0:** 0.450

