# Experiment: Activation Compare

**Status:** Completed
**Started:** 2026-02-26 18:14:32  
**Duration:** 8 minutes 0 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medxpertqa

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
  name: medxpertqa
  filename: medxpertqa/test.jsonl
  split: test
experiment:
  _target_: cotlab.experiments.ActivationCompareExperiment
  name: activation_compare
  description: Collect mean layer activations for representational comparison
  layer_stride: 1
  num_samples: null
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
  experiment.seed=42 \
  prompt=mcq \
  dataset=medxpertqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 2450
- **Pooling:** last_token
- **Layer Stride:** 1
- **Activation Norms:** {0: 197.1005, 1: 26.4199, 2: 60.1224, 3: 51.2749, 4: 388.5116, 5: 89.3451, 6: 64.1234, 7: 246.6735, 8: 710.797, 9: 857.3578, 10: 343.3477, 11: 261.9283, 12: 150.9323, 13: 288.0218, 14: 281.3865, 15: 623.9142, 16: 509.5196, 17: 1359.6558, 18: 493.5876, 19: 363.6562, 20: 468.7053, 21: 1206.2958, 22: 884.9802, 23: 908.0634, 24: 842.6752, 25: 2414.1157, 26: 1502.8914, 27: 3701.4622, 28: 3124.2395, 29: 3812.0671, 30: 5499.8149, 31: 2071.2241, 32: 2295.6604, 33: 2598.6301, 34: 3732.925, 35: 2933.0093, 36: 4993.9355, 37: 3309.2832, 38: 2990.9631, 39: 3923.6489, 40: 3669.5911, 41: 3272.9426, 42: 2677.8455, 43: 3376.8838, 44: 2962.0305, 45: 3624.2166, 46: 4492.8086, 47: 1939.7748, 48: 3638.5588, 49: 3329.0225, 50: 3184.3528, 51: 2251.5195, 52: 6865.9321, 53: 5066.6431, 54: 4741.5562, 55: 10911.9473, 56: 10551.4775, 57: 15274.7305, 58: 19810.2891, 59: 10118.2773, 60: 9440.665, 61: 34672.8164}
- **Activation Std:** {0: 0.381134, 1: 0.073705, 2: 0.084948, 3: 0.164943, 4: 0.145566, 5: 0.1244, 6: 0.182994, 7: 0.20159, 8: 0.468796, 9: 0.609655, 10: 0.449572, 11: 0.360645, 12: 0.40794, 13: 0.517143, 14: 0.677372, 15: 0.777436, 16: 0.954286, 17: 1.181807, 18: 1.426857, 19: 1.710568, 20: 2.286241, 21: 2.906271, 22: 3.439556, 23: 4.524239, 24: 5.770439, 25: 6.81294, 26: 8.61696, 27: 10.03122, 28: 10.553805, 29: 13.127478, 30: 13.337081, 31: 12.484767, 32: 13.414426, 33: 12.043925, 34: 14.995661, 35: 19.962275, 36: 23.990761, 37: 20.27104, 38: 21.10931, 39: 25.524385, 40: 21.877121, 41: 21.90559, 42: 21.071201, 43: 23.938278, 44: 22.250921, 45: 26.44487, 46: 32.624607, 47: 20.28326, 48: 28.822697, 49: 27.59252, 50: 24.758089, 51: 17.041122, 52: 41.306141, 53: 35.535145, 54: 29.082897, 55: 71.626465, 56: 65.146927, 57: 65.518097, 58: 86.083046, 59: 77.027847, 60: 58.723778, 61: 50.281757}

