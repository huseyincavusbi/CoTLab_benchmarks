# Experiment: Activation Compare

**Status:** Completed
**Started:** 2026-02-26 18:26:35  
**Duration:** 49 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Pubhealthbench
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** pubhealthbench

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
  _target_: cotlab.prompts.pubhealthbench.PubHealthBenchMCQPromptStrategy
  name: pubhealthbench
  output_format: json
dataset:
  _target_: cotlab.datasets.loaders.PubHealthBenchDataset
  name: pubhealthbench
  split: reviewed
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
  prompt=pubhealthbench \
  dataset=pubhealthbench
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 760
- **Pooling:** last_token
- **Layer Stride:** 1
- **Activation Norms:** {0: 216.0376, 1: 25.1987, 2: 65.6065, 3: 55.512, 4: 397.4075, 5: 92.5449, 6: 69.8507, 7: 210.9856, 8: 667.5073, 9: 700.801, 10: 421.1611, 11: 270.6318, 12: 145.1381, 13: 252.4593, 14: 250.1025, 15: 901.833, 16: 271.0202, 17: 1489.1758, 18: 756.4149, 19: 529.1939, 20: 573.8997, 21: 962.3637, 22: 1230.4301, 23: 1929.6765, 24: 970.6197, 25: 1200.2111, 26: 3375.8462, 27: 2979.4199, 28: 2246.8865, 29: 3799.3315, 30: 8305.3799, 31: 2038.074, 32: 2069.0999, 33: 3076.8469, 34: 4079.0437, 35: 2999.8816, 36: 6658.0073, 37: 2987.9692, 38: 2628.8462, 39: 3746.8342, 40: 2376.3621, 41: 2413.6643, 42: 1786.2756, 43: 2077.9651, 44: 1972.0782, 45: 3059.4072, 46: 4670.4312, 47: 1977.8131, 48: 2785.9451, 49: 2695.9595, 50: 2934.72, 51: 2733.8845, 52: 6120.0713, 53: 5313.5161, 54: 5452.1699, 55: 8910.5322, 56: 10617.9346, 57: 17231.9648, 58: 21125.4141, 59: 9543.1777, 60: 9350.4307, 61: 22528.3594}
- **Activation Std:** {0: 0.00364, 1: 0.003792, 2: 0.006449, 3: 0.008778, 4: 0.005944, 5: 0.004321, 6: 0.01247, 7: 0.016876, 8: 0.021032, 9: 0.033087, 10: 0.044675, 11: 0.077077, 12: 0.060518, 13: 0.069149, 14: 0.0762, 15: 0.149917, 16: 0.12955, 17: 0.226947, 18: 0.284816, 19: 0.331461, 20: 0.446144, 21: 0.570043, 22: 0.717634, 23: 0.819696, 24: 1.028588, 25: 1.339213, 26: 1.603482, 27: 1.714362, 28: 1.797662, 29: 2.526443, 30: 2.382276, 31: 2.265882, 32: 2.487626, 33: 2.443474, 34: 2.869409, 35: 4.204, 36: 5.627508, 37: 4.973841, 38: 4.721425, 39: 5.499824, 40: 4.085345, 41: 3.713146, 42: 4.003147, 43: 4.397982, 44: 4.58822, 45: 5.928086, 46: 6.921217, 47: 3.971264, 48: 6.099822, 49: 5.070102, 50: 5.185727, 51: 4.591285, 52: 9.302786, 53: 11.59863, 54: 18.050283, 55: 34.944942, 56: 31.783047, 57: 50.278477, 58: 52.716663, 59: 42.377777, 60: 35.995003, 61: 28.13204}

