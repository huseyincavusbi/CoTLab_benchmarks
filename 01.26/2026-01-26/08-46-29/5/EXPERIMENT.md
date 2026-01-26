# Experiment: Medqa Standard

**Status:** Completed
**Started:** 2026-01-26 09:13:27  
**Duration:** 1 minutes 45 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medqa

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
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medqa
  filename: medqa/test.jsonl
  split: test
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
  dataset=medqa
```

## Results

- **Accuracy:** 59.9%
- **Samples Processed:** 1273
- **Correct:** 753
- **Incorrect:** 505
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.571072319201995, 'recall': 0.659942363112392, 'f1-score': 0.6122994652406417, 'support': 347.0}, 'B': {'precision': 0.6219931271477663, 'recall': 0.5876623376623377, 'f1-score': 0.6043405676126878, 'support': 308.0}, 'C': {'precision': 0.670926517571885, 'recall': 0.6140350877192983, 'f1-score': 0.6412213740458015, 'support': 342.0}, 'D': {'precision': 0.5757575757575758, 'recall': 0.5095785440613027, 'f1-score': 0.540650406504065, 'support': 261.0}, 'E': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'O': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'R': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.5985691573926868, 'macro avg': {'precision': 0.18767304151378633, 'recall': 0.1824014101965639, 'f1-score': 0.1845009087233228, 'support': 1258.0}, 'weighted avg': {'precision': 0.611657849131094, 'recall': 0.5985691573926868, 'f1-score': 0.6033483905281682, 'support': 1258.0}}
- **Macro Precision:** 0.188
- **Macro Recall:** 0.182
- **Macro F1:** 0.185
- **Weighted F1:** 0.603
- **Confusion Matrix:** [[229, 36, 37, 40, 0, 0, 0, 0, 0, 1, 0, 0, 4], [63, 181, 27, 29, 2, 1, 1, 2, 1, 0, 0, 0, 1], [56, 40, 210, 29, 0, 0, 0, 1, 0, 0, 1, 1, 4], [53, 34, 39, 133, 0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'G', 'I', 'L', 'N', 'O', 'Q', 'R', 'T']
- **Top Confused Pairs:** [('B', 'A', 63), ('C', 'A', 56), ('D', 'A', 53), ('A', 'D', 40), ('C', 'B', 40), ('D', 'C', 39), ('A', 'C', 37), ('A', 'B', 36), ('D', 'B', 34), ('B', 'D', 29)]
- **True Class Distribution:** {'B': 308, 'D': 261, 'C': 342, 'A': 347}
- **Pred Class Distribution:** {'A': 401, 'C': 313, 'B': 291, 'D': 231, 'I': 1, 'T': 11, 'E': 2, 'Q': 1, 'L': 3, 'N': 1, 'R': 1, 'O': 1, 'G': 1}
- **Num Classes:** 13

