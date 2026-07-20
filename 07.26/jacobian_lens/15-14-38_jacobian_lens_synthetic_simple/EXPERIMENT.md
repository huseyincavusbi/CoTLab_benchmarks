# Experiment: Synthetic Standard (PLAIN)

**Status:** Running
**Started:** 2026-07-18 15:14:38

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Simple
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** synthetic

<details>
<summary>Full Configuration (YAML)</summary>

```yaml
backend:
  _target_: cotlab.backends.VLLMBackend
  tensor_parallel_size: 1
  dtype: bfloat16
  trust_remote_code: true
  max_model_len: null
  quantization: null
  gpu_memory_utilization: 0.9
  enforce_eager: false
  limit_mm_per_prompt: null
model:
  name: openai-community/gpt2
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
prompt:
  _target_: cotlab.prompts.SimplePromptStrategy
  name: simple
  system_role: null
  include_instructions: false
  output_format: plain
dataset:
  _target_: cotlab.datasets.SyntheticMedicalDataset
  name: synthetic
  path: data/Synthetic_Medical_Data.csv
  repeat: 1
experiment:
  _target_: cotlab.experiments.JacobianLensExperiment
  name: jacobian_lens
  description: Jacobian lens for causal concept readout from residuals
  mode: apply
  lens_path: null
  corpus_path: null
  n_corpus_prompts: 100
  source_layers: null
  target_layer: null
  layer_stride: 1
  dim_batch: 8
  skip_first_n: 16
  top_k: 10
  num_samples: 100
  max_input_tokens: 512
  answer_cue: '


    Answer:'
  seed: 42
seed: 42
verbose: true
dry_run: false
mode: fit
n_corpus_prompts: 5
max_input_tokens: 64
dim_batch: 4
source_layers:
- 2
- 6
- 10

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=jacobian_lens \
  experiment.num_samples=100 \
  experiment.seed=42 \
  prompt=simple \
  prompt.output_format=plain \
  dataset=synthetic
```

## Results

_Results will be added after experiment completes..._
