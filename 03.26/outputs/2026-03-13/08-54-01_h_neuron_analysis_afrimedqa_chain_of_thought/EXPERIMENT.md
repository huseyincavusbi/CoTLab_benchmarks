# Experiment: Afrimedqa Standard (PLAIN)

**Status:** Completed
**Started:** 2026-03-13 08:54:01  
**Duration:** 2 minutes 18 seconds

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
  num_samples: 500
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
  experiment.num_samples=500 \
  experiment.seed=42 \
  prompt=chain_of_thought \
  prompt.output_format=plain \
  dataset=afrimedqa
```

## Results

- **Accuracy:** 72.4%
- **Samples Processed:** 1
- **Dataset:** afrimedqa
- **N Samples:** 500
- **N Layers:** 62
- **Intermediate Dim:** 21504
- **N Features:** 1333248
- **Probe Balanced Accuracy:** 0.698
- **Probe Auroc:** 0.704
- **N H Neurons:** 48
- **H Neuron Ratio Permille:** 0.036
- **Layer Distribution:** {29: 3, 30: 1, 57: 1, 26: 2, 46: 1, 36: 3, 44: 1, 59: 6, 60: 4, 32: 4, 31: 1, 23: 1, 55: 4, 58: 6, 35: 2, 27: 1, 22: 1, 50: 1, 51: 1, 20: 1, 43: 2, 33: 1}
- **Top H Neurons:** [{'layer': 29, 'neuron': 13578}, {'layer': 30, 'neuron': 19805}, {'layer': 57, 'neuron': 19946}, {'layer': 26, 'neuron': 13241}, {'layer': 46, 'neuron': 21113}, {'layer': 36, 'neuron': 11383}, {'layer': 44, 'neuron': 20359}, {'layer': 59, 'neuron': 14328}, {'layer': 60, 'neuron': 2032}, {'layer': 32, 'neuron': 2358}, {'layer': 31, 'neuron': 18392}, {'layer': 23, 'neuron': 17425}, {'layer': 55, 'neuron': 1484}, {'layer': 58, 'neuron': 15990}, {'layer': 55, 'neuron': 19955}, {'layer': 60, 'neuron': 21365}, {'layer': 60, 'neuron': 3622}, {'layer': 59, 'neuron': 20901}, {'layer': 58, 'neuron': 13512}, {'layer': 59, 'neuron': 13081}, {'layer': 35, 'neuron': 11808}, {'layer': 58, 'neuron': 18767}, {'layer': 27, 'neuron': 1622}, {'layer': 22, 'neuron': 14692}, {'layer': 60, 'neuron': 1339}, {'layer': 55, 'neuron': 15272}, {'layer': 36, 'neuron': 19503}, {'layer': 29, 'neuron': 17912}, {'layer': 26, 'neuron': 11293}, {'layer': 29, 'neuron': 9767}, {'layer': 58, 'neuron': 7825}, {'layer': 50, 'neuron': 20904}, {'layer': 51, 'neuron': 9122}, {'layer': 32, 'neuron': 20818}, {'layer': 59, 'neuron': 5929}, {'layer': 58, 'neuron': 4039}, {'layer': 59, 'neuron': 2487}, {'layer': 58, 'neuron': 3844}, {'layer': 55, 'neuron': 7600}, {'layer': 32, 'neuron': 10535}, {'layer': 59, 'neuron': 2381}, {'layer': 20, 'neuron': 13018}, {'layer': 35, 'neuron': 16343}, {'layer': 43, 'neuron': 16542}, {'layer': 32, 'neuron': 16983}, {'layer': 43, 'neuron': 14341}, {'layer': 33, 'neuron': 13706}, {'layer': 36, 'neuron': 6101}]
- **Accuracy Alpha 0.0:** 0.730
- **Accuracy Alpha 0.5:** 0.720
- **Accuracy Alpha 1.5:** 0.700
- **Accuracy Alpha 2.0:** 0.730

