# Experiment: Medmcqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-03-18 10:46:28  
**Duration:** 31 minutes 8 seconds

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
  num_samples: 2000
  validation_split: 0.2
  l1_C: 0.01
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
  experiment.num_samples=2000 \
  experiment.seed=42 \
  prompt=chain_of_thought \
  prompt.output_format=plain \
  dataset=medmcqa
```

## Results

- **Accuracy:** 51.1%
- **Samples Processed:** 1
- **Dataset:** medmcqa
- **N Samples:** 2000
- **N Training Rows:** 4000
- **N Layers:** 34
- **Intermediate Dim:** 10240
- **N Features:** 348160
- **Probe Balanced Accuracy:** 0.838
- **Probe Auroc:** 0.894
- **Random Baseline Balanced Accuracy:** 0.831
- **Random Baseline Auroc:** 0.822
- **N H Neurons:** 17
- **H Neuron Ratio Permille:** 0.049
- **Layer Distribution:** {21: 1, 14: 2, 10: 1, 15: 4, 5: 1, 16: 2, 11: 2, 23: 1, 20: 1, 8: 1, 13: 1}
- **Contrastive Labeling:** True
- **Top H Neurons:** [{'layer': 21, 'neuron': 5230}, {'layer': 14, 'neuron': 9737}, {'layer': 10, 'neuron': 7494}, {'layer': 15, 'neuron': 3150}, {'layer': 5, 'neuron': 243}, {'layer': 16, 'neuron': 169}, {'layer': 11, 'neuron': 866}, {'layer': 15, 'neuron': 5142}, {'layer': 11, 'neuron': 3495}, {'layer': 15, 'neuron': 3287}, {'layer': 14, 'neuron': 7516}, {'layer': 16, 'neuron': 8850}, {'layer': 23, 'neuron': 7109}, {'layer': 15, 'neuron': 9967}, {'layer': 20, 'neuron': 3380}, {'layer': 8, 'neuron': 1571}, {'layer': 13, 'neuron': 9318}]
- **Accuracy Alpha 0.0:** 0.507
- **Accuracy Alpha 0.5:** 0.505
- **Accuracy Alpha 1.0:** 0.512
- **Accuracy Alpha 1.5:** 0.510
- **Accuracy Alpha 2.0:** 0.507

