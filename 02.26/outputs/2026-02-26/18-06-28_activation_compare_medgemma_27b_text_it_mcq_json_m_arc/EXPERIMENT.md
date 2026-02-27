# Experiment: Activation Compare

**Status:** Completed
**Started:** 2026-02-26 18:06:28  
**Duration:** 16 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** m_arc

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
  _target_: cotlab.datasets.loaders.MARCDataset
  name: m_arc
  filename: m_arc/test-00000-of-00001.parquet
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
  dataset=m_arc
```

## Results

- **Samples Processed:** 1
- **Num Samples:** 100
- **Pooling:** last_token
- **Layer Stride:** 1
- **Activation Norms:** {0: 197.3281, 1: 26.739, 2: 57.3105, 3: 51.3852, 4: 386.9154, 5: 89.5332, 6: 64.2013, 7: 246.8027, 8: 735.1215, 9: 848.4612, 10: 361.4481, 11: 261.892, 12: 153.0354, 13: 305.4277, 14: 287.9794, 15: 658.2435, 16: 554.6824, 17: 1332.9667, 18: 425.814, 19: 399.5609, 20: 468.9774, 21: 1206.8673, 22: 876.463, 23: 934.6662, 24: 850.0434, 25: 2504.3552, 26: 1636.7573, 27: 3700.4731, 28: 3593.2732, 29: 4322.3101, 30: 5182.7729, 31: 2375.1814, 32: 2375.0798, 33: 2625.3315, 34: 3827.5564, 35: 2951.7126, 36: 4906.4194, 37: 3318.6372, 38: 3087.677, 39: 3996.7861, 40: 3540.0742, 41: 3361.677, 42: 2616.6736, 43: 3334.7151, 44: 3102.6492, 45: 3778.7251, 46: 4618.542, 47: 1918.9365, 48: 3597.2273, 49: 3224.1353, 50: 3445.5981, 51: 2288.2136, 52: 6856.6646, 53: 5219.7065, 54: 4802.5845, 55: 11169.4111, 56: 10555.3408, 57: 15208.5234, 58: 19972.7148, 59: 10547.2627, 60: 9934.8896, 61: 36744.0234}
- **Activation Std:** {0: 0.408836, 1: 0.063106, 2: 0.092629, 3: 0.158172, 4: 0.132134, 5: 0.131967, 6: 0.173939, 7: 0.189255, 8: 0.40281, 9: 0.594278, 10: 0.466875, 11: 0.459062, 12: 0.521817, 13: 0.695935, 14: 0.784928, 15: 0.884397, 16: 1.085595, 17: 1.295693, 18: 1.479429, 19: 1.790564, 20: 2.404325, 21: 2.932026, 22: 3.341236, 23: 4.432502, 24: 5.767678, 25: 6.594056, 26: 8.326408, 27: 9.512839, 28: 9.873521, 29: 12.092219, 30: 12.451216, 31: 11.774785, 32: 12.453242, 33: 11.196755, 34: 14.07618, 35: 18.66501, 36: 23.634508, 37: 19.132292, 38: 19.79019, 39: 24.700695, 40: 22.271299, 41: 22.374865, 42: 22.116737, 43: 24.147451, 44: 23.245396, 45: 28.038376, 46: 32.98119, 47: 19.698895, 48: 29.49803, 49: 28.580677, 50: 25.02932, 51: 14.352161, 52: 40.304089, 53: 30.007458, 54: 27.7097, 55: 70.590317, 56: 62.200882, 57: 59.84811, 58: 81.991188, 59: 70.791473, 60: 52.197487, 61: 43.953739}

