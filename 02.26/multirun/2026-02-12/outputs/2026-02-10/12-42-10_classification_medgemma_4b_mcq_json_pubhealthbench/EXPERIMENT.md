# Experiment: Pubhealthbench Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-10 12:42:10  
**Duration:** 12 minutes 2 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
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
  max_new_tokens: 256
  temperature: 0
  top_p: 1
  safe_name: medgemma_4b
prompt:
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: false
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
  prompt.answer_first=true \
  prompt.few_shot=false \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 29.9%
- **Samples Processed:** 760
- **Correct:** 227
- **Incorrect:** 533
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.24766355140186916, 'recall': 0.44166666666666665, 'f1-score': 0.31736526946107785, 'support': 120.0}, 'B': {'precision': 0.5609756097560976, 'recall': 0.19658119658119658, 'f1-score': 0.2911392405063291, 'support': 117.0}, 'C': {'precision': 0.5121951219512195, 'recall': 0.21875, 'f1-score': 0.30656934306569344, 'support': 96.0}, 'D': {'precision': 0.41379310344827586, 'recall': 0.1276595744680851, 'f1-score': 0.1951219512195122, 'support': 94.0}, 'E': {'precision': 0.35802469135802467, 'recall': 0.29591836734693877, 'f1-score': 0.3240223463687151, 'support': 98.0}, 'F': {'precision': 0.2962962962962963, 'recall': 0.41379310344827586, 'f1-score': 0.34532374100719426, 'support': 116.0}, 'G': {'precision': 0.22404371584699453, 'recall': 0.3445378151260504, 'f1-score': 0.271523178807947, 'support': 119.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.2986842105263158, 'macro avg': {'precision': 0.2903324544509753, 'recall': 0.2265451915152459, 'f1-score': 0.22789611893738546, 'support': 760.0}, 'weighted avg': {'precision': 0.3678145371715682, 'recall': 0.2986842105263158, 'f1-score': 0.2947924289508222, 'support': 760.0}}
- **Macro Precision:** 0.290
- **Macro Recall:** 0.227
- **Macro F1:** 0.228
- **Weighted F1:** 0.295
- **Confusion Matrix:** [[53, 5, 3, 2, 9, 16, 31, 0, 1], [27, 23, 1, 3, 10, 23, 26, 1, 3], [21, 3, 21, 3, 7, 19, 22, 0, 0], [31, 2, 1, 12, 8, 16, 23, 0, 1], [20, 2, 5, 3, 29, 19, 19, 0, 1], [30, 2, 5, 3, 5, 48, 21, 0, 2], [32, 4, 5, 3, 13, 21, 41, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Q', 'T']
- **Top Confused Pairs:** [('G', 'A', 32), ('A', 'G', 31), ('D', 'A', 31), ('F', 'A', 30), ('B', 'A', 27), ('B', 'G', 26), ('B', 'F', 23), ('D', 'G', 23), ('C', 'G', 22), ('C', 'A', 21)]
- **True Class Distribution:** {'F': 116, 'A': 120, 'C': 96, 'G': 119, 'E': 98, 'B': 117, 'D': 94}
- **Pred Class Distribution:** {'A': 214, 'C': 41, 'G': 183, 'F': 162, 'T': 8, 'B': 41, 'E': 81, 'D': 29, 'Q': 1}
- **Num Classes:** 9

