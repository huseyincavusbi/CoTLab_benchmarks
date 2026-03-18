# Experiment: Medmcqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-03-18 09:48:21  
**Duration:** 32 minutes 40 seconds

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
- **Probe Balanced Accuracy:** 0.832
- **Probe Auroc:** 0.896
- **Random Baseline Balanced Accuracy:** 0.847
- **Random Baseline Auroc:** 0.893
- **N H Neurons:** 155
- **H Neuron Ratio Permille:** 0.445
- **Layer Distribution:** {17: 6, 23: 8, 11: 14, 16: 12, 14: 19, 13: 9, 33: 4, 24: 6, 9: 1, 21: 4, 19: 6, 27: 3, 10: 3, 15: 13, 20: 3, 18: 5, 12: 11, 26: 4, 32: 4, 25: 3, 22: 4, 31: 1, 8: 2, 7: 1, 5: 1, 30: 3, 28: 3, 29: 2}
- **Contrastive Labeling:** True
- **Top H Neurons:** [{'layer': 17, 'neuron': 9228}, {'layer': 23, 'neuron': 9320}, {'layer': 11, 'neuron': 3135}, {'layer': 16, 'neuron': 2974}, {'layer': 14, 'neuron': 7040}, {'layer': 13, 'neuron': 7995}, {'layer': 14, 'neuron': 7735}, {'layer': 33, 'neuron': 2104}, {'layer': 16, 'neuron': 6366}, {'layer': 24, 'neuron': 9638}, {'layer': 16, 'neuron': 3653}, {'layer': 14, 'neuron': 441}, {'layer': 17, 'neuron': 3913}, {'layer': 9, 'neuron': 9804}, {'layer': 11, 'neuron': 9375}, {'layer': 21, 'neuron': 8740}, {'layer': 19, 'neuron': 20}, {'layer': 21, 'neuron': 9296}, {'layer': 19, 'neuron': 3197}, {'layer': 27, 'neuron': 5676}, {'layer': 10, 'neuron': 6784}, {'layer': 15, 'neuron': 4754}, {'layer': 33, 'neuron': 4725}, {'layer': 14, 'neuron': 584}, {'layer': 14, 'neuron': 3158}, {'layer': 24, 'neuron': 3791}, {'layer': 11, 'neuron': 1237}, {'layer': 16, 'neuron': 8261}, {'layer': 20, 'neuron': 5980}, {'layer': 27, 'neuron': 7825}, {'layer': 11, 'neuron': 7217}, {'layer': 18, 'neuron': 5021}, {'layer': 14, 'neuron': 8025}, {'layer': 16, 'neuron': 3597}, {'layer': 12, 'neuron': 6755}, {'layer': 21, 'neuron': 9852}, {'layer': 26, 'neuron': 30}, {'layer': 32, 'neuron': 5127}, {'layer': 32, 'neuron': 8074}, {'layer': 25, 'neuron': 8248}, {'layer': 22, 'neuron': 4930}, {'layer': 12, 'neuron': 9396}, {'layer': 13, 'neuron': 7001}, {'layer': 15, 'neuron': 3150}, {'layer': 18, 'neuron': 1919}, {'layer': 20, 'neuron': 3812}, {'layer': 13, 'neuron': 8669}, {'layer': 32, 'neuron': 8119}, {'layer': 27, 'neuron': 9466}, {'layer': 31, 'neuron': 7177}]
- **Accuracy Alpha 0.0:** 0.510
- **Accuracy Alpha 0.5:** 0.507
- **Accuracy Alpha 1.0:** 0.512
- **Accuracy Alpha 1.5:** 0.500
- **Accuracy Alpha 2.0:** 0.500

