# Experiment: Afrimedqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-03-13 09:04:42  
**Duration:** 9 minutes 39 seconds

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
  name: afrimedqa
  filename: afrimedqa/mcq.jsonl
  split: mcq
experiment:
  _target_: cotlab.experiments.HNeuronAnalysisExperiment
  name: h_neuron_analysis
  description: CETT-based H-Neuron discovery and causal validation (arXiv:2512.01797)
  num_samples: 2000
  validation_split: 0.2
  l1_C: 0.1
  alpha_values:
  - 0.0
  - 0.5
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
  experiment.num_samples=2000 \
  experiment.seed=42 \
  prompt=chain_of_thought \
  prompt.output_format=plain \
  dataset=afrimedqa
```

## Results

- **Accuracy:** 69.5%
- **Samples Processed:** 1
- **Dataset:** afrimedqa
- **N Samples:** 2000
- **N Layers:** 62
- **Intermediate Dim:** 21504
- **N Features:** 1333248
- **Probe Balanced Accuracy:** 0.709
- **Probe Auroc:** 0.773
- **N H Neurons:** 213
- **H Neuron Ratio Permille:** 0.160
- **Layer Distribution:** {58: 25, 35: 6, 19: 2, 32: 12, 31: 7, 49: 3, 57: 10, 29: 5, 23: 3, 59: 23, 30: 10, 55: 6, 46: 4, 56: 9, 27: 5, 60: 18, 61: 12, 44: 1, 36: 4, 16: 1, 51: 2, 26: 3, 41: 3, 18: 1, 40: 3, 28: 1, 53: 2, 25: 2, 34: 5, 48: 2, 52: 3, 37: 1, 39: 1, 11: 4, 17: 1, 50: 2, 47: 1, 24: 1, 42: 2, 43: 2, 38: 1, 13: 1, 45: 1, 4: 1, 9: 1}
- **Top H Neurons:** [{'layer': 58, 'neuron': 397}, {'layer': 35, 'neuron': 12129}, {'layer': 19, 'neuron': 17394}, {'layer': 32, 'neuron': 9886}, {'layer': 31, 'neuron': 18643}, {'layer': 49, 'neuron': 17977}, {'layer': 57, 'neuron': 5926}, {'layer': 29, 'neuron': 16466}, {'layer': 23, 'neuron': 5038}, {'layer': 58, 'neuron': 4308}, {'layer': 59, 'neuron': 441}, {'layer': 30, 'neuron': 15886}, {'layer': 55, 'neuron': 12110}, {'layer': 46, 'neuron': 2352}, {'layer': 29, 'neuron': 16082}, {'layer': 57, 'neuron': 20571}, {'layer': 56, 'neuron': 13423}, {'layer': 27, 'neuron': 20386}, {'layer': 60, 'neuron': 2076}, {'layer': 60, 'neuron': 21280}, {'layer': 61, 'neuron': 17834}, {'layer': 30, 'neuron': 9432}, {'layer': 59, 'neuron': 8976}, {'layer': 56, 'neuron': 14242}, {'layer': 61, 'neuron': 4877}, {'layer': 46, 'neuron': 9949}, {'layer': 58, 'neuron': 6770}, {'layer': 27, 'neuron': 4895}, {'layer': 60, 'neuron': 2032}, {'layer': 59, 'neuron': 5350}, {'layer': 61, 'neuron': 2355}, {'layer': 59, 'neuron': 21377}, {'layer': 29, 'neuron': 11942}, {'layer': 59, 'neuron': 15906}, {'layer': 35, 'neuron': 8232}, {'layer': 44, 'neuron': 20359}, {'layer': 19, 'neuron': 17929}, {'layer': 58, 'neuron': 13998}, {'layer': 60, 'neuron': 13539}, {'layer': 36, 'neuron': 10855}, {'layer': 57, 'neuron': 8565}, {'layer': 30, 'neuron': 20897}, {'layer': 16, 'neuron': 14546}, {'layer': 55, 'neuron': 1484}, {'layer': 59, 'neuron': 19635}, {'layer': 55, 'neuron': 16639}, {'layer': 60, 'neuron': 633}, {'layer': 61, 'neuron': 15607}, {'layer': 60, 'neuron': 15560}, {'layer': 58, 'neuron': 20109}]
- **Accuracy Alpha 0.0:** 0.710
- **Accuracy Alpha 0.5:** 0.700
- **Accuracy Alpha 1.5:** 0.695
- **Accuracy Alpha 2.0:** 0.690

