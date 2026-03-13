# Experiment: Medmcqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-03-13 09:22:38  
**Duration:** 23 minutes 55 seconds

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
  device: cuda
  dtype: bfloat16
  enable_hooks: true
  trust_remote_code: true
model:
  name: google/medgemma-27b-text-it
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
  description: CETT-based H-Neuron discovery and causal validation (arXiv:2512.01797)
  num_samples: 4183
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
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=h_neuron_analysis \
  experiment.num_samples=4183 \
  experiment.seed=42 \
  prompt=chain_of_thought \
  prompt.output_format=plain \
  dataset=medmcqa
```

## Results

- **Accuracy:** 63.1%
- **Samples Processed:** 1
- **Dataset:** medmcqa
- **N Samples:** 4183
- **N Layers:** 62
- **Intermediate Dim:** 21504
- **N Features:** 1333248
- **Probe Balanced Accuracy:** 0.713
- **Probe Auroc:** 0.778
- **N H Neurons:** 425
- **H Neuron Ratio Permille:** 0.319
- **Layer Distribution:** {28: 13, 58: 41, 54: 2, 31: 14, 30: 13, 59: 43, 32: 18, 60: 37, 35: 19, 33: 10, 36: 16, 50: 4, 52: 5, 56: 17, 57: 19, 55: 17, 61: 12, 53: 3, 34: 6, 27: 7, 26: 14, 29: 6, 11: 3, 18: 3, 48: 3, 43: 3, 21: 1, 25: 8, 40: 1, 46: 4, 37: 6, 14: 2, 12: 2, 24: 8, 41: 3, 13: 3, 23: 9, 22: 2, 19: 3, 49: 4, 39: 2, 44: 3, 51: 8, 20: 2, 47: 2, 16: 1, 45: 2, 38: 1}
- **Top H Neurons:** [{'layer': 28, 'neuron': 20090}, {'layer': 58, 'neuron': 20109}, {'layer': 54, 'neuron': 8614}, {'layer': 31, 'neuron': 1877}, {'layer': 30, 'neuron': 580}, {'layer': 59, 'neuron': 12436}, {'layer': 32, 'neuron': 16655}, {'layer': 60, 'neuron': 16541}, {'layer': 35, 'neuron': 6063}, {'layer': 31, 'neuron': 1876}, {'layer': 32, 'neuron': 18256}, {'layer': 33, 'neuron': 19010}, {'layer': 36, 'neuron': 3301}, {'layer': 50, 'neuron': 574}, {'layer': 60, 'neuron': 6552}, {'layer': 58, 'neuron': 3996}, {'layer': 60, 'neuron': 13461}, {'layer': 59, 'neuron': 13886}, {'layer': 58, 'neuron': 5211}, {'layer': 58, 'neuron': 18529}, {'layer': 52, 'neuron': 4166}, {'layer': 31, 'neuron': 18043}, {'layer': 56, 'neuron': 7647}, {'layer': 59, 'neuron': 12736}, {'layer': 35, 'neuron': 20088}, {'layer': 57, 'neuron': 18937}, {'layer': 55, 'neuron': 17226}, {'layer': 32, 'neuron': 1438}, {'layer': 60, 'neuron': 596}, {'layer': 35, 'neuron': 12129}, {'layer': 28, 'neuron': 13510}, {'layer': 59, 'neuron': 19773}, {'layer': 59, 'neuron': 13594}, {'layer': 60, 'neuron': 11880}, {'layer': 58, 'neuron': 10605}, {'layer': 59, 'neuron': 5631}, {'layer': 33, 'neuron': 6330}, {'layer': 61, 'neuron': 3520}, {'layer': 53, 'neuron': 16222}, {'layer': 34, 'neuron': 4495}, {'layer': 55, 'neuron': 7160}, {'layer': 55, 'neuron': 15655}, {'layer': 59, 'neuron': 20219}, {'layer': 59, 'neuron': 5353}, {'layer': 58, 'neuron': 72}, {'layer': 35, 'neuron': 4433}, {'layer': 35, 'neuron': 21158}, {'layer': 59, 'neuron': 9779}, {'layer': 36, 'neuron': 17691}, {'layer': 36, 'neuron': 6543}]
- **Accuracy Alpha 0.0:** 0.633
- **Accuracy Alpha 0.5:** 0.636
- **Accuracy Alpha 1.0:** 0.631
- **Accuracy Alpha 1.5:** 0.624
- **Accuracy Alpha 2.0:** 0.619

