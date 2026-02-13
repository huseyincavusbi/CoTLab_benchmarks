# Experiment: Pubhealthbench Standard

**Status:** Completed
**Started:** 2026-02-12 09:23:22  
**Duration:** 8 minutes 39 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
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
  max_model_len: null
  quantization: null
  gpu_memory_utilization: 0.9
  enforce_eager: false
  limit_mm_per_prompt: null
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
  prompt=mcq \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 37.7%
- **Samples Processed:** 760
- **Correct:** 286
- **Incorrect:** 473
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.3333333333333333, 'recall': 0.26666666666666666, 'f1-score': 0.2962962962962963, 'support': 120.0}, 'B': {'precision': 0.5967741935483871, 'recall': 0.31896551724137934, 'f1-score': 0.4157303370786517, 'support': 116.0}, 'C': {'precision': 0.5230769230769231, 'recall': 0.3541666666666667, 'f1-score': 0.422360248447205, 'support': 96.0}, 'D': {'precision': 0.6122448979591837, 'recall': 0.3191489361702128, 'f1-score': 0.4195804195804196, 'support': 94.0}, 'E': {'precision': 0.3974358974358974, 'recall': 0.3163265306122449, 'f1-score': 0.3522727272727273, 'support': 98.0}, 'F': {'precision': 0.3560606060606061, 'recall': 0.4051724137931034, 'f1-score': 0.3790322580645161, 'support': 116.0}, 'G': {'precision': 0.2798507462686567, 'recall': 0.6302521008403361, 'f1-score': 0.3875968992248062, 'support': 119.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'M': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.37681159420289856, 'macro avg': {'precision': 0.25823138314024896, 'recall': 0.2175582359992175, 'f1-score': 0.22273909883038515, 'support': 759.0}, 'weighted avg': {'precision': 0.4355022378562308, 'recall': 0.37681159420289856, 'f1-score': 0.379949826303206, 'support': 759.0}}
- **Macro Precision:** 0.258
- **Macro Recall:** 0.218
- **Macro F1:** 0.223
- **Weighted F1:** 0.380
- **Confusion Matrix:** [[32, 5, 10, 5, 8, 16, 43, 0, 0, 1, 0, 0], [10, 37, 5, 6, 12, 15, 30, 1, 0, 0, 0, 0], [10, 5, 34, 2, 7, 9, 26, 1, 0, 1, 0, 1], [7, 5, 7, 30, 6, 16, 23, 0, 0, 0, 0, 0], [8, 5, 2, 2, 31, 12, 38, 0, 0, 0, 0, 0], [18, 2, 2, 2, 9, 47, 33, 1, 1, 0, 1, 0], [11, 3, 5, 2, 5, 17, 75, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'M', 'S', 'T', 'X']
- **Top Confused Pairs:** [('A', 'G', 43), ('E', 'G', 38), ('F', 'G', 33), ('B', 'G', 30), ('C', 'G', 26), ('D', 'G', 23), ('F', 'A', 18), ('G', 'F', 17), ('A', 'F', 16), ('D', 'F', 16)]
- **True Class Distribution:** {'F': 116, 'A': 120, 'C': 96, 'G': 119, 'E': 98, 'B': 116, 'D': 94}
- **Pred Class Distribution:** {'G': 268, 'C': 65, 'A': 96, 'E': 78, 'F': 132, 'D': 49, 'B': 62, 'I': 4, 'S': 2, 'M': 1, 'X': 1, 'T': 1}
- **Num Classes:** 12

