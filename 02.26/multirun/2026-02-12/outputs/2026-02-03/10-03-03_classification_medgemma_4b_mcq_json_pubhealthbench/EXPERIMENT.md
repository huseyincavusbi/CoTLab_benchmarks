# Experiment: Pubhealthbench Answer-First

**Status:** Completed
**Started:** 2026-02-03 10:03:03  
**Duration:** 33 minutes 18 seconds

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

- **Accuracy:** 72.8%
- **Samples Processed:** 760
- **Correct:** 553
- **Incorrect:** 207
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.6594202898550725, 'recall': 0.7583333333333333, 'f1-score': 0.7054263565891473, 'support': 120.0}, 'B': {'precision': 0.7886178861788617, 'recall': 0.8290598290598291, 'f1-score': 0.8083333333333333, 'support': 117.0}, 'C': {'precision': 0.5793650793650794, 'recall': 0.7604166666666666, 'f1-score': 0.6576576576576577, 'support': 96.0}, 'D': {'precision': 0.6979166666666666, 'recall': 0.7127659574468085, 'f1-score': 0.7052631578947368, 'support': 94.0}, 'E': {'precision': 0.7653061224489796, 'recall': 0.7653061224489796, 'f1-score': 0.7653061224489796, 'support': 98.0}, 'F': {'precision': 0.822429906542056, 'recall': 0.7586206896551724, 'f1-score': 0.7892376681614349, 'support': 116.0}, 'G': {'precision': 0.8732394366197183, 'recall': 0.5210084033613446, 'f1-score': 0.6526315789473685, 'support': 119.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.7276315789473684, 'macro avg': {'precision': 0.6482869234595543, 'recall': 0.6381888752465168, 'f1-score': 0.6354819843790822, 'support': 760.0}, 'weighted avg': {'precision': 0.7459727682472036, 'recall': 0.7276315789473684, 'f1-score': 0.727461529170265, 'support': 760.0}}
- **Macro Precision:** 0.648
- **Macro Recall:** 0.638
- **Macro F1:** 0.635
- **Weighted F1:** 0.727
- **Confusion Matrix:** [[91, 3, 10, 6, 5, 4, 1, 0], [6, 97, 6, 1, 2, 3, 2, 0], [7, 5, 73, 4, 0, 5, 2, 0], [6, 6, 7, 67, 6, 1, 1, 0], [2, 5, 9, 4, 75, 2, 1, 0], [6, 2, 8, 6, 3, 88, 2, 1], [20, 5, 13, 8, 7, 4, 62, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T']
- **Top Confused Pairs:** [('G', 'A', 20), ('G', 'C', 13), ('A', 'C', 10), ('E', 'C', 9), ('F', 'C', 8), ('G', 'D', 8), ('C', 'A', 7), ('D', 'C', 7), ('G', 'E', 7), ('A', 'D', 6)]
- **True Class Distribution:** {'F': 116, 'A': 120, 'C': 96, 'G': 119, 'E': 98, 'B': 117, 'D': 94}
- **Pred Class Distribution:** {'F': 107, 'A': 138, 'C': 126, 'E': 98, 'B': 123, 'D': 96, 'G': 71, 'T': 1}
- **Num Classes:** 8

