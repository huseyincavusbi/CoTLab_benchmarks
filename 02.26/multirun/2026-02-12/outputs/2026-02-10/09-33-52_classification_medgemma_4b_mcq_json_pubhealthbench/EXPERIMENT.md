# Experiment: Pubhealthbench Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-10 09:33:52  
**Duration:** 30 minutes 20 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
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
  name: google/medgemma-4b-it
  variant: 4b
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_4b
prompt:
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: false
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
  num_samples: 760
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=760 \
  prompt=mcq \
  prompt.few_shot=false \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 75.3%
- **Samples Processed:** 760
- **Correct:** 572
- **Incorrect:** 188
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.7563025210084033, 'recall': 0.75, 'f1-score': 0.7531380753138075, 'support': 120.0}, 'B': {'precision': 0.7886178861788617, 'recall': 0.8290598290598291, 'f1-score': 0.8083333333333333, 'support': 117.0}, 'C': {'precision': 0.6403508771929824, 'recall': 0.7604166666666666, 'f1-score': 0.6952380952380952, 'support': 96.0}, 'D': {'precision': 0.723404255319149, 'recall': 0.723404255319149, 'f1-score': 0.723404255319149, 'support': 94.0}, 'E': {'precision': 0.776595744680851, 'recall': 0.7448979591836735, 'f1-score': 0.7604166666666666, 'support': 98.0}, 'F': {'precision': 0.8256880733944955, 'recall': 0.7758620689655172, 'f1-score': 0.8, 'support': 116.0}, 'G': {'precision': 0.7941176470588235, 'recall': 0.680672268907563, 'f1-score': 0.7330316742081447, 'support': 119.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.7526315789473684, 'macro avg': {'precision': 0.6631346256041958, 'recall': 0.6580391310127999, 'f1-score': 0.6591952625098996, 'support': 760.0}, 'weighted avg': {'precision': 0.7616901038249295, 'recall': 0.7526315789473684, 'f1-score': 0.755586879927127, 'support': 760.0}}
- **Macro Precision:** 0.663
- **Macro Recall:** 0.658
- **Macro F1:** 0.659
- **Weighted F1:** 0.756
- **Confusion Matrix:** [[90, 5, 7, 3, 6, 3, 6, 0], [5, 97, 4, 2, 1, 1, 6, 1], [3, 5, 73, 5, 2, 6, 2, 0], [6, 7, 6, 68, 5, 1, 1, 0], [3, 2, 10, 5, 73, 3, 1, 1], [4, 3, 5, 4, 3, 90, 5, 2], [8, 4, 9, 7, 4, 5, 81, 1], [0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T']
- **Top Confused Pairs:** [('E', 'C', 10), ('G', 'C', 9), ('G', 'A', 8), ('A', 'C', 7), ('D', 'B', 7), ('G', 'D', 7), ('A', 'E', 6), ('A', 'G', 6), ('B', 'G', 6), ('C', 'F', 6)]
- **True Class Distribution:** {'F': 116, 'A': 120, 'C': 96, 'G': 119, 'E': 98, 'B': 117, 'D': 94}
- **Pred Class Distribution:** {'F': 109, 'A': 119, 'C': 114, 'G': 102, 'D': 94, 'E': 94, 'B': 123, 'T': 5}
- **Num Classes:** 8

