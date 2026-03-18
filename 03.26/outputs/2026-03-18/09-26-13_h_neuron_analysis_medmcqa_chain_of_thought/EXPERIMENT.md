# Experiment: Medmcqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-03-18 09:26:13  
**Duration:** 21 minutes 35 seconds

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
- **N Training Rows:** 2000
- **N Layers:** 34
- **Intermediate Dim:** 10240
- **N Features:** 348160
- **Probe Balanced Accuracy:** 0.630
- **Probe Auroc:** 0.671
- **Random Baseline Balanced Accuracy:** 0.669
- **Random Baseline Auroc:** 0.706
- **N H Neurons:** 218
- **H Neuron Ratio Permille:** 0.626
- **Layer Distribution:** {33: 13, 23: 6, 20: 17, 16: 18, 17: 19, 14: 5, 22: 9, 19: 15, 15: 8, 13: 8, 24: 2, 12: 7, 21: 22, 31: 10, 18: 9, 30: 4, 10: 2, 1: 1, 11: 10, 28: 6, 32: 5, 25: 4, 8: 2, 27: 3, 26: 5, 5: 3, 7: 1, 9: 1, 6: 1, 29: 2}
- **Contrastive Labeling:** False
- **Top H Neurons:** [{'layer': 33, 'neuron': 2966}, {'layer': 23, 'neuron': 5777}, {'layer': 20, 'neuron': 8816}, {'layer': 16, 'neuron': 6572}, {'layer': 17, 'neuron': 5505}, {'layer': 33, 'neuron': 535}, {'layer': 33, 'neuron': 8320}, {'layer': 16, 'neuron': 5709}, {'layer': 14, 'neuron': 6984}, {'layer': 22, 'neuron': 3534}, {'layer': 19, 'neuron': 3463}, {'layer': 15, 'neuron': 3125}, {'layer': 17, 'neuron': 8673}, {'layer': 16, 'neuron': 6738}, {'layer': 13, 'neuron': 1035}, {'layer': 22, 'neuron': 1501}, {'layer': 24, 'neuron': 5680}, {'layer': 12, 'neuron': 3258}, {'layer': 16, 'neuron': 7358}, {'layer': 20, 'neuron': 5361}, {'layer': 21, 'neuron': 6724}, {'layer': 21, 'neuron': 4748}, {'layer': 19, 'neuron': 2071}, {'layer': 31, 'neuron': 4455}, {'layer': 18, 'neuron': 4450}, {'layer': 31, 'neuron': 268}, {'layer': 21, 'neuron': 491}, {'layer': 13, 'neuron': 2179}, {'layer': 33, 'neuron': 253}, {'layer': 19, 'neuron': 4001}, {'layer': 16, 'neuron': 9250}, {'layer': 21, 'neuron': 7636}, {'layer': 33, 'neuron': 735}, {'layer': 16, 'neuron': 4346}, {'layer': 31, 'neuron': 9398}, {'layer': 19, 'neuron': 6778}, {'layer': 21, 'neuron': 6672}, {'layer': 33, 'neuron': 3426}, {'layer': 30, 'neuron': 1400}, {'layer': 21, 'neuron': 1012}, {'layer': 31, 'neuron': 5990}, {'layer': 30, 'neuron': 5657}, {'layer': 22, 'neuron': 1443}, {'layer': 21, 'neuron': 2836}, {'layer': 18, 'neuron': 7561}, {'layer': 10, 'neuron': 7204}, {'layer': 1, 'neuron': 3744}, {'layer': 13, 'neuron': 10119}, {'layer': 20, 'neuron': 6880}, {'layer': 17, 'neuron': 3341}]
- **Accuracy Alpha 0.0:** 0.497
- **Accuracy Alpha 0.5:** 0.495
- **Accuracy Alpha 1.0:** 0.512
- **Accuracy Alpha 1.5:** 0.510
- **Accuracy Alpha 2.0:** 0.515

