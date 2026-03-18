# Experiment: Medmcqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-03-18 09:14:29  
**Duration:** 1 minutes 5 seconds

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
  contrastive_labeling: false
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
- **N Training Rows:** 100
- **N Layers:** 34
- **Intermediate Dim:** 10240
- **N Features:** 348160
- **Probe Balanced Accuracy:** 0.641
- **Probe Auroc:** 0.576
- **Random Baseline Balanced Accuracy:** 0.515
- **Random Baseline Auroc:** 0.535
- **N H Neurons:** 6
- **H Neuron Ratio Permille:** 0.017
- **Layer Distribution:** {32: 1, 21: 2, 17: 1, 27: 1, 16: 1}
- **Contrastive Labeling:** False
- **Top H Neurons:** [{'layer': 32, 'neuron': 1559}, {'layer': 21, 'neuron': 6800}, {'layer': 17, 'neuron': 8998}, {'layer': 27, 'neuron': 6629}, {'layer': 16, 'neuron': 2232}, {'layer': 21, 'neuron': 7665}]
- **Accuracy Alpha 0.0:** 0.450
- **Accuracy Alpha 0.5:** 0.450
- **Accuracy Alpha 1.0:** 0.450
- **Accuracy Alpha 1.5:** 0.450
- **Accuracy Alpha 2.0:** 0.450

