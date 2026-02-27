# Experiment: Activation Compare

**Status:** Completed
**Started:** 2026-02-26 18:07:08  
**Duration:** 53 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medbullets

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
  _target_: cotlab.datasets.loaders.MedBulletsDataset
  name: medbullets
  split: op5_test
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
  dataset=medbullets
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 308
- **Pooling:** last_token
- **Layer Stride:** 1
- **Activation Norms:** {0: 221.3981, 1: 26.4028, 2: 62.5729, 3: 54.8277, 4: 394.7964, 5: 89.6838, 6: 68.8073, 7: 254.0382, 8: 728.9638, 9: 873.7281, 10: 317.8902, 11: 265.8304, 12: 155.3901, 13: 289.9635, 14: 261.7685, 15: 661.7365, 16: 508.6946, 17: 1370.3169, 18: 422.3201, 19: 430.3761, 20: 535.214, 21: 1216.8104, 22: 800.4551, 23: 1134.212, 24: 1210.0735, 25: 2564.762, 26: 1746.9326, 27: 3432.2021, 28: 3397.8821, 29: 4349.1758, 30: 5294.7788, 31: 2582.6807, 32: 2562.0142, 33: 2715.2122, 34: 3765.5046, 35: 3326.2427, 36: 5401.3306, 37: 3742.6868, 38: 3442.7998, 39: 4506.2798, 40: 4005.7168, 41: 3720.2815, 42: 3097.4753, 43: 3862.4756, 44: 3489.1064, 45: 4292.4404, 46: 5192.4834, 47: 2178.71, 48: 4196.6694, 49: 3848.6294, 50: 3926.4153, 51: 2516.0566, 52: 8137.3438, 53: 6541.0083, 54: 5092.3438, 55: 12589.5986, 56: 12174.6504, 57: 16112.6299, 58: 21164.668, 59: 12149.7959, 60: 10973.3604, 61: 40065.2031}
- **Activation Std:** {0: 0.052145, 1: 0.012017, 2: 0.012296, 3: 0.028451, 4: 0.019182, 5: 0.012881, 6: 0.025205, 7: 0.032138, 8: 0.058275, 9: 0.073322, 10: 0.075101, 11: 0.059027, 12: 0.042262, 13: 0.067938, 14: 0.097845, 15: 0.12761, 16: 0.151569, 17: 0.218351, 18: 0.247419, 19: 0.316778, 20: 0.453701, 21: 0.632238, 22: 0.763651, 23: 0.937485, 24: 1.341202, 25: 1.705934, 26: 2.264229, 27: 2.657964, 28: 2.959502, 29: 3.546172, 30: 3.729598, 31: 3.409832, 32: 3.770102, 33: 3.246706, 34: 3.811115, 35: 5.278333, 36: 6.604999, 37: 5.308605, 38: 5.761787, 39: 7.53025, 40: 6.572669, 41: 5.513095, 42: 6.681477, 43: 8.012096, 44: 7.630662, 45: 9.060596, 46: 10.419409, 47: 5.035975, 48: 9.634584, 49: 8.051735, 50: 8.481786, 51: 6.858174, 52: 14.483772, 53: 14.87425, 54: 11.070693, 55: 24.579067, 56: 24.495195, 57: 29.302589, 58: 38.819191, 59: 34.32415, 60: 23.961346, 61: 17.765326}

