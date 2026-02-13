# Experiment: Pubhealthbench Standard

**Status:** Completed
**Started:** 2026-02-03 12:03:11  
**Duration:** 3 minutes 13 seconds

## Research Questions

1. Standard baseline experiment for comparison.

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
  _target_: cotlab.backends.VLLMBackend
  tensor_parallel_size: 1
  dtype: bfloat16
  trust_remote_code: true
  max_model_len: 8192
  quantization: bitsandbytes
  gpu_memory_utilization: 0.7
  enforce_eager: true
  limit_mm_per_prompt:
    image: 0
model:
  name: google/gemma-3-4b-it
  variant: 4b
  max_new_tokens: 64
  temperature: 0.7
  top_p: 0.9
  safe_name: gemma_4b_it
prompt:
  _target_: cotlab.prompts.pubhealthbench.PubHealthBenchMCQPromptStrategy
  name: pubhealthbench
  output_format: json
dataset:
  _target_: cotlab.datasets.loaders.PubHealthBenchDataset
  name: pubhealthbench
  split: reviewed
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: -1
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=-1 \
  prompt=pubhealthbench \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 73.9%
- **Samples Processed:** 760
- **Correct:** 562
- **Incorrect:** 198
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.7964601769911505, 'recall': 0.75, 'f1-score': 0.7725321888412017, 'support': 120.0}, 'B': {'precision': 0.7058823529411765, 'recall': 0.8205128205128205, 'f1-score': 0.758893280632411, 'support': 117.0}, 'C': {'precision': 0.6220472440944882, 'recall': 0.8229166666666666, 'f1-score': 0.7085201793721974, 'support': 96.0}, 'D': {'precision': 0.7222222222222222, 'recall': 0.6914893617021277, 'f1-score': 0.7065217391304348, 'support': 94.0}, 'E': {'precision': 0.7738095238095238, 'recall': 0.6632653061224489, 'f1-score': 0.7142857142857143, 'support': 98.0}, 'F': {'precision': 0.8363636363636363, 'recall': 0.7931034482758621, 'f1-score': 0.8141592920353983, 'support': 116.0}, 'G': {'precision': 0.75, 'recall': 0.6302521008403361, 'f1-score': 0.684931506849315, 'support': 119.0}, 'accuracy': 0.7394736842105263, 'macro avg': {'precision': 0.7438264509174567, 'recall': 0.7387913863028945, 'f1-score': 0.7371205573066676, 'support': 760.0}, 'weighted avg': {'precision': 0.7471978894822772, 'recall': 0.7394736842105263, 'f1-score': 0.7393087952422406, 'support': 760.0}}
- **Macro Precision:** 0.744
- **Macro Recall:** 0.739
- **Macro F1:** 0.737
- **Weighted F1:** 0.739
- **Confusion Matrix:** [[90, 6, 6, 4, 5, 4, 5], [3, 96, 3, 5, 3, 1, 6], [1, 5, 79, 4, 0, 3, 4], [2, 6, 10, 65, 5, 3, 3], [2, 11, 12, 3, 65, 2, 3], [2, 4, 7, 5, 2, 92, 4], [13, 8, 10, 4, 4, 5, 75]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Top Confused Pairs:** [('G', 'A', 13), ('E', 'C', 12), ('E', 'B', 11), ('D', 'C', 10), ('G', 'C', 10), ('G', 'B', 8), ('F', 'C', 7), ('A', 'B', 6), ('A', 'C', 6), ('B', 'G', 6)]
- **True Class Distribution:** {'F': 116, 'A': 120, 'C': 96, 'G': 119, 'E': 98, 'B': 117, 'D': 94}
- **Pred Class Distribution:** {'F': 110, 'A': 113, 'C': 127, 'G': 100, 'D': 90, 'E': 84, 'B': 136}
- **Num Classes:** 7

