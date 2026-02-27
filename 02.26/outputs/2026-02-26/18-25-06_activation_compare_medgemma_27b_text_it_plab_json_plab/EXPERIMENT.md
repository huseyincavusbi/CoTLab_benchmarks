# Experiment: Activation Compare

**Status:** Completed
**Started:** 2026-02-26 18:25:06  
**Duration:** 1 minutes 9 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Plab
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
**Output Format:** JSON
**Dataset:** plab

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
  _target_: cotlab.prompts.PLABPromptStrategy
  name: plab
  few_shot: false
  output_format: json
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.PLABDataset
  name: plab
  split: main
  filename: plab/data.json
  topics_filename: plab/topics.json
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
  prompt=plab \
  prompt.few_shot=false \
  dataset=plab
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 1652
- **Pooling:** last_token
- **Layer Stride:** 1
- **Activation Norms:** {0: 223.4621, 1: 26.0431, 2: 63.5067, 3: 55.9481, 4: 403.0549, 5: 90.288, 6: 68.8781, 7: 243.116, 8: 704.7095, 9: 876.0465, 10: 349.8532, 11: 201.1455, 12: 148.9467, 13: 311.5602, 14: 324.6624, 15: 599.7582, 16: 721.5245, 17: 1410.6925, 18: 469.6725, 19: 620.9531, 20: 799.975, 21: 1447.2223, 22: 668.3734, 23: 1115.0997, 24: 2235.1638, 25: 1857.3556, 26: 1850.8179, 27: 3332.0569, 28: 2891.019, 29: 4015.2629, 30: 5555.2783, 31: 1749.248, 32: 1846.4187, 33: 3243.5562, 34: 4410.4268, 35: 2805.1135, 36: 5963.2236, 37: 3499.4211, 38: 2709.4397, 39: 3729.5588, 40: 2494.0615, 41: 2643.0325, 42: 1981.6948, 43: 2317.1931, 44: 2367.9214, 45: 2826.6562, 46: 4593.5132, 47: 1670.6443, 48: 3437.1921, 49: 2709.0989, 50: 2793.5659, 51: 2030.0109, 52: 7179.5586, 53: 3712.7363, 54: 5504.3921, 55: 11146.0771, 56: 10616.8984, 57: 17090.2031, 58: 21665.623, 59: 10152.0352, 60: 10046.9092, 61: 36892.0703}
- **Activation Std:** {0: 0.002631, 1: 0.003559, 2: 0.006512, 3: 0.009264, 4: 0.006017, 5: 0.003155, 6: 0.009097, 7: 0.010564, 8: 0.01711, 9: 0.027463, 10: 0.038801, 11: 0.077815, 12: 0.055206, 13: 0.06236, 14: 0.066234, 15: 0.129597, 16: 0.125654, 17: 0.211619, 18: 0.242701, 19: 0.310823, 20: 0.43923, 21: 0.634877, 22: 0.70185, 23: 1.052851, 24: 1.458361, 25: 1.863639, 26: 2.72962, 27: 3.709901, 28: 4.293248, 29: 5.222004, 30: 5.537744, 31: 5.040956, 32: 5.358297, 33: 4.976536, 34: 5.846005, 35: 10.411384, 36: 10.745449, 37: 9.632526, 38: 9.439273, 39: 11.717125, 40: 8.831541, 41: 9.555542, 42: 9.182374, 43: 10.026934, 44: 9.709726, 45: 10.995295, 46: 13.227939, 47: 7.531399, 48: 14.61878, 49: 12.782968, 50: 11.42303, 51: 8.135344, 52: 23.566402, 53: 20.528652, 54: 18.181843, 55: 36.068554, 56: 30.428856, 57: 37.840179, 58: 52.294724, 59: 42.346302, 60: 31.076488, 61: 22.649508}

