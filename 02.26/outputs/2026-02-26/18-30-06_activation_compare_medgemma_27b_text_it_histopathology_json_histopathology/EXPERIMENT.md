# Experiment: Activation Compare

**Status:** Completed
**Started:** 2026-02-26 18:30:06  
**Duration:** 1 minutes 33 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Histopathology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** histopathology

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
  _target_: cotlab.prompts.HistopathologyPromptStrategy
  name: histopathology
  output_format: json
  few_shot: true
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.HistopathologyDataset
  name: histopathology
  path: data/histopathology.tsv
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
  prompt=histopathology \
  dataset=histopathology
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 600
- **Pooling:** last_token
- **Layer Stride:** 1
- **Activation Norms:** {0: 227.4877, 1: 26.0404, 2: 57.4777, 3: 55.1634, 4: 393.2486, 5: 90.1911, 6: 66.4723, 7: 212.7512, 8: 742.6447, 9: 809.3125, 10: 315.6959, 11: 314.0569, 12: 143.2564, 13: 440.517, 14: 219.293, 15: 837.5958, 16: 531.8976, 17: 1407.1741, 18: 595.5952, 19: 392.4558, 20: 431.1451, 21: 1298.7667, 22: 654.1371, 23: 1154.551, 24: 2761.7363, 25: 1806.7908, 26: 2558.8164, 27: 3800.061, 28: 3309.3767, 29: 2959.2683, 30: 3815.4404, 31: 2246.304, 32: 1999.7861, 33: 2543.6809, 34: 3577.1489, 35: 3416.0027, 36: 5053.9712, 37: 4445.209, 38: 3372.2061, 39: 4539.3271, 40: 4348.4868, 41: 3848.1245, 42: 2901.5803, 43: 4439.0293, 44: 3830.6196, 45: 4331.5527, 46: 5467.9927, 47: 2104.6311, 48: 4597.1382, 49: 4751.8911, 50: 3914.7227, 51: 2854.2644, 52: 9456.5371, 53: 6124.3438, 54: 5166.5132, 55: 13167.5273, 56: 13154.9541, 57: 18244.1543, 58: 20445.6641, 59: 15468.9082, 60: 12582.5508, 61: 39235.7031}
- **Activation Std:** {0: 0.031013, 1: 0.006504, 2: 0.007477, 3: 0.018667, 4: 0.012912, 5: 0.004852, 6: 0.020301, 7: 0.025723, 8: 0.046686, 9: 0.069238, 10: 0.073514, 11: 0.102125, 12: 0.077777, 13: 0.0937, 14: 0.098261, 15: 0.147185, 16: 0.154347, 17: 0.248614, 18: 0.252166, 19: 0.310625, 20: 0.423448, 21: 0.53236, 22: 0.631071, 23: 0.820436, 24: 1.103471, 25: 1.452078, 26: 1.86304, 27: 2.196258, 28: 2.39596, 29: 3.06452, 30: 2.916011, 31: 2.769018, 32: 2.918317, 33: 2.453048, 34: 2.994435, 35: 4.369248, 36: 4.811095, 37: 4.350133, 38: 4.368152, 39: 6.116529, 40: 5.539417, 41: 4.422741, 42: 5.354258, 43: 7.244401, 44: 6.254732, 45: 7.158988, 46: 8.300325, 47: 3.599183, 48: 7.235631, 49: 7.508961, 50: 7.395313, 51: 4.481635, 52: 13.725242, 53: 12.359491, 54: 8.813706, 55: 19.613432, 56: 20.796139, 57: 31.119783, 58: 37.166214, 59: 31.89838, 60: 26.313864, 61: 16.573664}

