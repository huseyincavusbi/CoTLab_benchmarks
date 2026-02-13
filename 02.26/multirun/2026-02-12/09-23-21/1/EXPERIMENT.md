# Experiment: Pubhealthbench Answer-First

**Status:** Completed
**Started:** 2026-02-12 09:34:38  
**Duration:** 8 minutes 36 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
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
  answer_first: true
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
  prompt.answer_first=true \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 35.7%
- **Samples Processed:** 760
- **Correct:** 271
- **Incorrect:** 488
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.3225806451612903, 'recall': 0.25, 'f1-score': 0.28169014084507044, 'support': 120.0}, 'B': {'precision': 0.5882352941176471, 'recall': 0.2564102564102564, 'f1-score': 0.35714285714285715, 'support': 117.0}, 'C': {'precision': 0.5, 'recall': 0.3125, 'f1-score': 0.38461538461538464, 'support': 96.0}, 'D': {'precision': 0.5555555555555556, 'recall': 0.3191489361702128, 'f1-score': 0.40540540540540543, 'support': 94.0}, 'E': {'precision': 0.375, 'recall': 0.3979591836734694, 'f1-score': 0.38613861386138615, 'support': 98.0}, 'F': {'precision': 0.4166666666666667, 'recall': 0.43478260869565216, 'f1-score': 0.425531914893617, 'support': 115.0}, 'G': {'precision': 0.2339622641509434, 'recall': 0.5210084033613446, 'f1-score': 0.3229166666666667, 'support': 119.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'M': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Y': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.3570487483530962, 'macro avg': {'precision': 0.21371431611800734, 'recall': 0.17798638487935253, 'f1-score': 0.18310292738788483, 'support': 759.0}, 'weighted avg': {'precision': 0.4219546839973264, 'recall': 0.3570487483530962, 'f1-score': 0.36340520938448345, 'support': 759.0}}
- **Macro Precision:** 0.214
- **Macro Recall:** 0.178
- **Macro F1:** 0.183
- **Weighted F1:** 0.363
- **Confusion Matrix:** [[30, 6, 4, 4, 9, 13, 49, 2, 1, 0, 0, 1, 1, 0], [13, 30, 4, 5, 15, 14, 35, 0, 1, 0, 0, 0, 0, 0], [9, 3, 30, 6, 11, 11, 26, 0, 0, 0, 0, 0, 0, 0], [9, 1, 4, 30, 10, 7, 32, 0, 0, 1, 0, 0, 0, 0], [10, 8, 2, 0, 39, 11, 27, 0, 1, 0, 0, 0, 0, 0], [11, 2, 8, 3, 6, 50, 34, 0, 0, 0, 1, 0, 0, 0], [11, 1, 8, 6, 14, 14, 62, 0, 1, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'M', 'S', 'T', 'Y']
- **Top Confused Pairs:** [('A', 'G', 49), ('B', 'G', 35), ('F', 'G', 34), ('D', 'G', 32), ('E', 'G', 27), ('C', 'G', 26), ('B', 'E', 15), ('B', 'F', 14), ('G', 'E', 14), ('G', 'F', 14)]
- **True Class Distribution:** {'F': 115, 'A': 120, 'C': 96, 'G': 119, 'E': 98, 'B': 117, 'D': 94}
- **Pred Class Distribution:** {'G': 265, 'F': 120, 'C': 60, 'E': 104, 'D': 54, 'A': 93, 'B': 51, 'I': 4, 'H': 2, 'Y': 1, 'T': 2, 'M': 1, 'S': 1, 'K': 1}
- **Num Classes:** 14

