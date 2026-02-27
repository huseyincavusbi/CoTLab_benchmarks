# Experiment: Activation Compare

**Status:** Completed
**Started:** 2026-02-26 18:28:03  
**Duration:** 1 minutes 17 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Pubmedqa
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** pubmedqa

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
  _target_: cotlab.prompts.pubmedqa.PubMedQAPromptStrategy
  name: pubmedqa
  output_format: json
  few_shot: true
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.PubMedQADataset
  name: pubmedqa
  filename: pubmedqa/test.jsonl
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
  prompt=pubmedqa \
  dataset=pubmedqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 500
- **Pooling:** last_token
- **Layer Stride:** 1
- **Activation Norms:** {0: 221.8338, 1: 25.5324, 2: 60.4564, 3: 55.0356, 4: 392.6927, 5: 90.1535, 6: 67.9135, 7: 252.7688, 8: 699.8705, 9: 916.4162, 10: 348.8218, 11: 297.5356, 12: 158.3084, 13: 365.6956, 14: 198.3274, 15: 902.0859, 16: 532.694, 17: 1321.7817, 18: 280.4713, 19: 557.3792, 20: 811.9188, 21: 1520.3816, 22: 1488.5596, 23: 1700.4962, 24: 1234.6964, 25: 3831.2227, 26: 1456.6493, 27: 4683.8804, 28: 2312.3853, 29: 4644.3975, 30: 4111.6528, 31: 2210.998, 32: 2501.3413, 33: 2724.4138, 34: 3143.4197, 35: 3966.9753, 36: 5259.0815, 37: 4293.2725, 38: 3547.1326, 39: 4987.2803, 40: 3778.9421, 41: 3892.2607, 42: 2997.7651, 43: 3907.6387, 44: 3411.5781, 45: 4234.3413, 46: 4543.377, 47: 1954.4316, 48: 4315.8091, 49: 3656.1072, 50: 3834.2551, 51: 2400.5486, 52: 9157.5156, 53: 6753.9438, 54: 5313.0596, 55: 13163.5918, 56: 12640.2549, 57: 17478.9219, 58: 20913.9824, 59: 13097.2373, 60: 11798.5303, 61: 41054.5312}
- **Activation Std:** {0: 0.002831, 1: 0.002211, 2: 0.004205, 3: 0.009722, 4: 0.005613, 5: 0.002981, 6: 0.008746, 7: 0.01102, 8: 0.02307, 9: 0.028953, 10: 0.035634, 11: 0.056458, 12: 0.038252, 13: 0.052329, 14: 0.054953, 15: 0.104259, 16: 0.101662, 17: 0.160838, 18: 0.158306, 19: 0.20662, 20: 0.310247, 21: 0.470758, 22: 0.5708, 23: 0.82204, 24: 1.329737, 25: 1.840865, 26: 2.548064, 27: 3.244885, 28: 3.408167, 29: 4.124946, 30: 3.974534, 31: 4.00393, 32: 4.16553, 33: 3.465506, 34: 4.059559, 35: 5.598209, 36: 5.842652, 37: 4.967195, 38: 4.971136, 39: 7.28619, 40: 5.918331, 41: 5.224918, 42: 5.706922, 43: 7.301332, 44: 5.998042, 45: 6.768499, 46: 7.427077, 47: 2.972178, 48: 6.179204, 49: 5.552774, 50: 5.95425, 51: 3.935899, 52: 10.284534, 53: 11.017039, 54: 7.601063, 55: 16.460077, 56: 17.947515, 57: 25.29034, 58: 30.800161, 59: 26.344273, 60: 18.904934, 61: 12.413594}

