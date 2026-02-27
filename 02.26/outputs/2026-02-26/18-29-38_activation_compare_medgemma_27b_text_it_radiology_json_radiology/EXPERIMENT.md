# Experiment: Activation Compare

**Status:** Completed
**Started:** 2026-02-26 18:29:38  
**Duration:** 12 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** radiology

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
  _target_: cotlab.prompts.RadiologyPromptStrategy
  name: radiology
  contrarian: false
  few_shot: true
  answer_first: false
  output_format: json
dataset:
  _target_: cotlab.datasets.RadiologyDataset
  name: radiology
  path: data/radiology.json
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
  prompt=radiology \
  dataset=radiology
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Pooling:** last_token
- **Layer Stride:** 1
- **Activation Norms:** {0: 225.0859, 1: 26.5045, 2: 57.7213, 3: 56.4238, 4: 396.828, 5: 89.6335, 6: 66.1444, 7: 219.5573, 8: 760.144, 9: 757.2498, 10: 366.4254, 11: 359.6165, 12: 158.849, 13: 452.0739, 14: 303.1702, 15: 842.9147, 16: 782.2743, 17: 1358.6407, 18: 234.6549, 19: 331.3759, 20: 494.1383, 21: 1186.801, 22: 786.4156, 23: 959.845, 24: 2938.8752, 25: 1594.6996, 26: 1503.0941, 27: 6993.0625, 28: 4586.8135, 29: 5688.3887, 30: 5953.8774, 31: 2452.3706, 32: 2327.0745, 33: 2661.8052, 34: 3557.8098, 35: 3529.9729, 36: 4805.9487, 37: 3876.5955, 38: 3491.3213, 39: 4783.3052, 40: 4708.8623, 41: 3990.4246, 42: 3329.8103, 43: 4424.0557, 44: 4450.1182, 45: 4705.2041, 46: 5673.5215, 47: 2345.8044, 48: 4621.5259, 49: 4348.9941, 50: 3606.9229, 51: 2497.689, 52: 8244.0801, 53: 6723.1426, 54: 5168.0654, 55: 11655.3604, 56: 10859.0, 57: 16987.1621, 58: 20477.3301, 59: 13116.1523, 60: 10391.8164, 61: 28629.2383}
- **Activation Std:** {0: 0.002895, 1: 0.002711, 2: 0.003666, 3: 0.008555, 4: 0.005133, 5: 0.00328, 6: 0.0115, 7: 0.016065, 8: 0.028297, 9: 0.04393, 10: 0.051636, 11: 0.07258, 12: 0.060314, 13: 0.067729, 14: 0.080479, 15: 0.123529, 16: 0.135533, 17: 0.220552, 18: 0.233802, 19: 0.28205, 20: 0.419445, 21: 0.490922, 22: 0.626818, 23: 0.845392, 24: 1.205902, 25: 1.84001, 26: 2.25268, 27: 2.487252, 28: 2.67652, 29: 2.765786, 30: 2.601294, 31: 2.519135, 32: 2.466705, 33: 2.386914, 34: 2.704957, 35: 3.691401, 36: 4.368117, 37: 3.761679, 38: 4.081671, 39: 6.24492, 40: 5.43704, 41: 4.485096, 42: 5.951858, 43: 7.522135, 44: 7.723064, 45: 8.014783, 46: 9.6998, 47: 4.077605, 48: 7.586985, 49: 7.27651, 50: 6.707305, 51: 4.661885, 52: 12.378921, 53: 13.192141, 54: 9.152438, 55: 17.795965, 56: 18.954334, 57: 32.613853, 58: 40.919182, 59: 33.030384, 60: 23.921875, 61: 15.716264}

