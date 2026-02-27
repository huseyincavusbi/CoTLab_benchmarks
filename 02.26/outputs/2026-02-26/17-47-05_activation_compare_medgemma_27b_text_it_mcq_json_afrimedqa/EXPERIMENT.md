# Experiment: Activation Compare

**Status:** Completed
**Started:** 2026-02-26 17:47:05  
**Duration:** 7 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
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
  variant: 27b-text
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b_text_it
prompt:
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: true
  output_format: json
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: afrimedqa
  filename: afrimedqa/mcq.jsonl
  split: mcq
experiment:
  _target_: cotlab.experiments.ActivationCompareExperiment
  name: activation_compare
  description: Collect mean layer activations for representational comparison
  layer_stride: 2
  num_samples: 50
  pooling: last_token
  max_input_tokens: 1024
  seed: 42
  answer_cue: '


    Answer:'
  batch_size: 4
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=activation_compare \
  experiment.num_samples=50 \
  experiment.seed=42 \
  prompt=mcq \
  dataset=afrimedqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 50
- **Pooling:** last_token
- **Layer Stride:** 2
- **Activation Norms:** {0: 222.3593, 2: 62.4792, 4: 392.238, 6: 68.5351, 8: 729.7928, 10: 315.5555, 12: 157.0611, 14: 243.1941, 16: 531.9236, 18: 430.055, 20: 638.1853, 22: 793.1257, 24: 1297.5115, 26: 1532.0486, 28: 3584.6692, 30: 5531.9087, 32: 2540.3545, 34: 3953.179, 36: 5464.7959, 38: 3217.8726, 40: 3541.5239, 42: 2571.1543, 44: 3026.6489, 46: 4669.7378, 48: 3583.6101, 50: 3666.092, 52: 7256.5225, 54: 5072.3862, 56: 11410.5176, 58: 20930.9316, 60: 11107.6621}
- **Activation Std:** {0: 0.002299, 2: 0.004181, 4: 0.004292, 6: 0.009473, 8: 0.01451, 10: 0.028422, 12: 0.037518, 14: 0.045174, 16: 0.099966, 18: 0.223865, 20: 0.437625, 22: 0.689949, 24: 1.414239, 26: 2.614858, 28: 3.697366, 30: 4.689953, 32: 4.516093, 34: 4.71444, 36: 7.738883, 38: 6.831052, 40: 7.971083, 42: 7.872389, 44: 9.006795, 46: 11.842677, 48: 10.239943, 50: 9.885745, 52: 16.128292, 54: 13.819777, 56: 30.813351, 58: 49.508331, 60: 32.391521}

