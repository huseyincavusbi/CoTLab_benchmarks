# Experiment: Activation Compare

**Status:** Completed
**Started:** 2026-02-26 18:09:02  
**Duration:** 3 minutes 31 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medqa

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
  name: medqa
  filename: medqa/test.jsonl
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
  dataset=medqa
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 1273
- **Pooling:** last_token
- **Layer Stride:** 1
- **Activation Norms:** {0: 220.8073, 1: 26.4027, 2: 62.3953, 3: 54.511, 4: 394.1129, 5: 89.4895, 6: 68.583, 7: 255.2367, 8: 726.7537, 9: 870.572, 10: 314.4339, 11: 261.9007, 12: 156.0947, 13: 288.3417, 14: 255.9404, 15: 659.15, 16: 520.1393, 17: 1363.7609, 18: 405.46, 19: 428.1653, 20: 544.0883, 21: 1169.2939, 22: 780.8428, 23: 1140.5006, 24: 1218.1528, 25: 2457.1558, 26: 1556.2256, 27: 3531.4597, 28: 3466.3921, 29: 4439.9692, 30: 5263.0991, 31: 2599.0713, 32: 2557.3491, 33: 2710.843, 34: 3769.7153, 35: 3306.9727, 36: 5399.0615, 37: 3738.022, 38: 3398.5852, 39: 4477.0391, 40: 3900.5967, 41: 3704.1472, 42: 2974.5803, 43: 3746.9409, 44: 3391.0828, 45: 4186.4668, 46: 4977.5913, 47: 2091.0525, 48: 4055.147, 49: 3716.9971, 50: 3939.2026, 51: 2494.8367, 52: 8119.2949, 53: 6407.0078, 54: 5081.2451, 55: 12521.25, 56: 12112.1865, 57: 15995.1807, 58: 21049.7402, 59: 12003.667, 60: 10989.916, 61: 40466.0312}
- **Activation Std:** {0: 0.070746, 1: 0.01105, 2: 0.016069, 3: 0.037095, 4: 0.033062, 5: 0.019075, 6: 0.043766, 7: 0.041495, 8: 0.092483, 9: 0.115836, 10: 0.098376, 11: 0.07905, 12: 0.077336, 13: 0.098392, 14: 0.142498, 15: 0.189616, 16: 0.241868, 17: 0.329741, 18: 0.35249, 19: 0.457973, 20: 0.644031, 21: 0.853174, 22: 1.019475, 23: 1.334108, 24: 1.79383, 25: 2.179407, 26: 2.924388, 27: 3.493304, 28: 3.778229, 29: 4.444754, 30: 4.649373, 31: 4.217947, 32: 4.512364, 33: 3.985612, 34: 4.808893, 35: 6.405169, 36: 7.784925, 37: 6.73603, 38: 6.583323, 39: 8.64503, 40: 7.669759, 41: 6.930421, 42: 7.463029, 43: 8.686658, 44: 8.202929, 45: 9.788796, 46: 11.736609, 47: 5.5891, 48: 9.990831, 49: 9.064146, 50: 9.062017, 51: 5.936728, 52: 15.426663, 53: 15.991019, 54: 10.810181, 55: 27.104208, 56: 26.328398, 57: 29.461819, 58: 40.621658, 59: 35.456715, 60: 24.491394, 61: 18.748476}

