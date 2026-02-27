# Experiment: Activation Compare

**Status:** Completed
**Started:** 2026-02-26 17:57:38  
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
**Dataset:** medmcqa

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
  name: medmcqa
  filename: medmcqa/validation.jsonl
  split: validation
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
  dataset=medmcqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 4183
- **Pooling:** last_token
- **Layer Stride:** 1
- **Activation Norms:** {0: 221.9909, 1: 26.418, 2: 62.7655, 3: 54.1258, 4: 392.055, 5: 89.7808, 6: 68.5852, 7: 264.0935, 8: 730.5853, 9: 878.1671, 10: 315.2672, 11: 252.7674, 12: 157.7471, 13: 280.4865, 14: 236.892, 15: 679.4726, 16: 540.9509, 17: 1396.5725, 18: 430.0983, 19: 350.0084, 20: 632.0403, 21: 932.7051, 22: 818.4661, 23: 1092.9707, 24: 1360.4565, 25: 2229.0378, 26: 1493.7314, 27: 3572.4238, 28: 3584.1353, 29: 4748.3696, 30: 5485.2925, 31: 2537.7244, 32: 2525.3713, 33: 2769.0354, 34: 3883.8772, 35: 3200.4675, 36: 5530.1484, 37: 3547.4277, 38: 3247.9397, 39: 4286.1729, 40: 3572.4456, 41: 3512.0569, 42: 2564.572, 43: 3290.7644, 44: 3027.0535, 45: 3716.9705, 46: 4541.6479, 47: 1914.3401, 48: 3543.0735, 49: 3181.8379, 50: 3717.8037, 51: 2331.9229, 52: 7283.1421, 53: 5134.6147, 54: 5050.1235, 55: 11783.5342, 56: 11474.9082, 57: 15578.0371, 58: 21124.6445, 59: 11087.5576, 60: 10935.4355, 61: 38673.918}
- **Activation Std:** {0: 0.001125, 1: 0.001348, 2: 0.003274, 3: 0.005372, 4: 0.003047, 5: 0.001578, 6: 0.007488, 7: 0.007912, 8: 0.012257, 9: 0.018883, 10: 0.025324, 11: 0.046052, 12: 0.032319, 13: 0.041678, 14: 0.042041, 15: 0.113336, 16: 0.10405, 17: 0.195391, 18: 0.22162, 19: 0.273486, 20: 0.416204, 21: 0.590149, 22: 0.650055, 23: 0.860023, 24: 1.278557, 25: 1.662084, 26: 2.397241, 27: 3.146803, 28: 3.485561, 29: 4.074157, 30: 4.518541, 31: 4.204267, 32: 4.521211, 33: 4.009152, 34: 4.639013, 35: 6.336872, 36: 7.571981, 37: 6.577568, 38: 6.528341, 39: 8.716426, 40: 7.607183, 41: 6.474402, 42: 7.279544, 43: 8.545063, 44: 8.150431, 45: 9.081507, 46: 10.641901, 47: 4.956387, 48: 8.942163, 49: 7.327731, 50: 8.680159, 51: 5.764601, 52: 14.307725, 53: 15.295737, 54: 11.586792, 55: 28.240574, 56: 28.316813, 57: 33.457851, 58: 47.816628, 59: 43.307575, 60: 30.660284, 61: 22.943661}

