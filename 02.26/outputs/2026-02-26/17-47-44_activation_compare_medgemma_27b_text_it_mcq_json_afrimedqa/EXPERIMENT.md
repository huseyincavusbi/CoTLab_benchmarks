# Experiment: Activation Compare

**Status:** Completed
**Started:** 2026-02-26 17:47:44  
**Duration:** 8 minutes 32 seconds

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
  dataset=afrimedqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 3958
- **Pooling:** last_token
- **Layer Stride:** 1
- **Activation Norms:** {0: 222.284, 1: 26.3884, 2: 62.4234, 3: 54.1307, 4: 392.1647, 5: 89.7237, 6: 68.5133, 7: 261.7638, 8: 729.2377, 9: 871.1774, 10: 314.9332, 11: 258.1636, 12: 156.9751, 13: 283.23, 14: 243.9408, 15: 665.1416, 16: 529.0502, 17: 1381.3687, 18: 427.4858, 19: 356.4809, 20: 633.7704, 21: 984.1268, 22: 799.8218, 23: 1070.6836, 24: 1310.6121, 25: 2105.5933, 26: 1528.444, 27: 3598.7163, 28: 3572.8396, 29: 4857.7485, 30: 5535.4648, 31: 2496.9343, 32: 2526.72, 33: 2787.7295, 34: 3960.2605, 35: 3176.2405, 36: 5487.0449, 37: 3463.8279, 38: 3195.4565, 39: 4219.2119, 40: 3488.4531, 41: 3428.0308, 42: 2529.0857, 43: 3232.2859, 44: 2971.6426, 45: 3627.3823, 46: 4617.5166, 47: 1942.8899, 48: 3562.5525, 49: 3170.377, 50: 3620.8418, 51: 2296.4734, 52: 7208.2339, 53: 4833.4512, 54: 5065.8462, 55: 11629.2666, 56: 11334.8291, 57: 15595.3447, 58: 20938.6777, 59: 10953.5146, 60: 11003.7412, 61: 38984.0234}
- **Activation Std:** {0: 0.001289, 1: 0.001516, 2: 0.003727, 3: 0.005997, 4: 0.003529, 5: 0.001811, 6: 0.008805, 7: 0.01064, 8: 0.013675, 9: 0.023575, 10: 0.028893, 11: 0.047332, 12: 0.039192, 13: 0.044284, 14: 0.04479, 15: 0.108139, 16: 0.10303, 17: 0.199561, 18: 0.228445, 19: 0.296343, 20: 0.45332, 21: 0.658826, 22: 0.70763, 23: 0.971582, 24: 1.455592, 25: 1.883443, 26: 2.70324, 27: 3.523019, 28: 3.840655, 29: 4.516501, 30: 4.896974, 31: 4.452526, 32: 4.800146, 33: 4.398348, 34: 5.040649, 35: 7.015175, 36: 8.292543, 37: 7.546241, 38: 7.3054, 39: 9.804049, 40: 8.510365, 41: 7.461379, 42: 8.374496, 43: 9.941493, 44: 9.632344, 45: 10.605272, 46: 12.51592, 47: 6.018708, 48: 10.86372, 49: 8.922794, 50: 10.639402, 51: 6.941918, 52: 17.085506, 53: 18.587717, 54: 14.43029, 55: 32.275166, 56: 31.992409, 57: 37.489491, 58: 50.963268, 59: 47.328396, 60: 34.079346, 61: 25.258341}

