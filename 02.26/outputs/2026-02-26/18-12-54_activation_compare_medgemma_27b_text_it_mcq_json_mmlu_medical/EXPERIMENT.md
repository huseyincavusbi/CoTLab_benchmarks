# Experiment: Activation Compare

**Status:** Completed
**Started:** 2026-02-26 18:12:55  
**Duration:** 1 minutes 20 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** mmlu_medical

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
  _target_: cotlab.datasets.loaders.MMLUMedicalDataset
  name: mmlu_medical
  filename: mmlu/medical_test.jsonl
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
  dataset=mmlu_medical
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 644
- **Pooling:** last_token
- **Layer Stride:** 1
- **Activation Norms:** {0: 221.9772, 1: 26.4282, 2: 62.5688, 3: 54.0906, 4: 391.83, 5: 89.6358, 6: 68.4954, 7: 262.7596, 8: 729.4463, 9: 878.3091, 10: 316.3015, 11: 255.0805, 12: 157.8052, 13: 278.6972, 14: 238.025, 15: 679.9179, 16: 535.6683, 17: 1396.3947, 18: 420.4955, 19: 345.2946, 20: 635.3533, 21: 943.8547, 22: 820.7686, 23: 1082.1581, 24: 1462.4454, 25: 2278.5208, 26: 1483.4495, 27: 3392.5146, 28: 3512.5964, 29: 4668.6831, 30: 5475.481, 31: 2566.7185, 32: 2488.469, 33: 2762.0161, 34: 3825.7844, 35: 3237.6353, 36: 5653.0522, 37: 3633.5098, 38: 3252.1196, 39: 4361.3564, 40: 3553.6802, 41: 3532.3408, 42: 2534.3582, 43: 3331.1082, 44: 3021.0132, 45: 3756.4512, 46: 4427.5176, 47: 1875.1166, 48: 3497.3042, 49: 3173.9043, 50: 3753.4319, 51: 2343.2678, 52: 7330.7412, 53: 5272.2739, 54: 5035.5664, 55: 11854.1357, 56: 11595.3701, 57: 15501.2656, 58: 21155.6543, 59: 11148.0742, 60: 11056.6895, 61: 39747.2617}
- **Activation Std:** {0: 0.002107, 1: 0.001594, 2: 0.003516, 3: 0.006132, 4: 0.003678, 5: 0.002028, 6: 0.009012, 7: 0.00906, 8: 0.013123, 9: 0.02104, 10: 0.027205, 11: 0.049535, 12: 0.034698, 13: 0.043171, 14: 0.042992, 15: 0.112877, 16: 0.104752, 17: 0.192211, 18: 0.214212, 19: 0.262576, 20: 0.420333, 21: 0.587851, 22: 0.632068, 23: 0.828724, 24: 1.195795, 25: 1.564846, 26: 2.268261, 27: 2.96919, 28: 3.289594, 29: 3.879722, 30: 4.432607, 31: 4.095591, 32: 4.31735, 33: 3.786563, 34: 4.409841, 35: 6.066629, 36: 7.169632, 37: 6.278211, 38: 6.192122, 39: 8.290927, 40: 7.225432, 41: 6.037049, 42: 6.780017, 43: 8.014882, 44: 7.355244, 45: 8.424267, 46: 9.722685, 47: 4.380184, 48: 8.032448, 49: 6.551005, 50: 7.740646, 51: 5.206974, 52: 12.893408, 53: 13.490951, 54: 10.227351, 55: 25.336803, 56: 25.042547, 57: 29.966331, 58: 44.346672, 59: 38.567997, 60: 27.368364, 61: 20.359476}

