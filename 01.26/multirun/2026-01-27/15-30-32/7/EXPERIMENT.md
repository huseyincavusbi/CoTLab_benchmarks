# Experiment: Medxpertqa Standard

**Status:** Completed
**Started:** 2026-01-27 18:50:50  
**Duration:** 39 minutes 1 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medxpertqa

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
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medxpertqa
  filename: medxpertqa/test.jsonl
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
  dataset=medxpertqa
```

## Results

- **Accuracy:** 10.9%
- **Samples Processed:** 2450
- **Correct:** 240
- **Incorrect:** 1970
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.11891891891891893, 'recall': 0.2009132420091324, 'f1-score': 0.1494057724957555, 'support': 219.0}, 'B': {'precision': 0.13306451612903225, 'recall': 0.15, 'f1-score': 0.14102564102564102, 'support': 220.0}, 'C': {'precision': 0.12413793103448276, 'recall': 0.16363636363636364, 'f1-score': 0.1411764705882353, 'support': 220.0}, 'D': {'precision': 0.09885931558935361, 'recall': 0.11981566820276497, 'f1-score': 0.10833333333333334, 'support': 217.0}, 'E': {'precision': 0.1225296442687747, 'recall': 0.12916666666666668, 'f1-score': 0.1257606490872211, 'support': 240.0}, 'F': {'precision': 0.08530805687203792, 'recall': 0.08035714285714286, 'f1-score': 0.08275862068965517, 'support': 224.0}, 'G': {'precision': 0.16666666666666666, 'recall': 0.0912863070539419, 'f1-score': 0.11796246648793565, 'support': 241.0}, 'H': {'precision': 0.11538461538461539, 'recall': 0.06, 'f1-score': 0.07894736842105263, 'support': 200.0}, 'I': {'precision': 0.14942528735632185, 'recall': 0.06310679611650485, 'f1-score': 0.08873720136518772, 'support': 206.0}, 'J': {'precision': 0.09090909090909091, 'recall': 0.02242152466367713, 'f1-score': 0.03597122302158273, 'support': 223.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'M': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'O': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'R': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'U': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Y': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Z': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.1085972850678733, 'macro avg': {'precision': 0.0482081617251718, 'recall': 0.04322814844824777, 'f1-score': 0.042803149860624, 'support': 2210.0}, 'weighted avg': {'precision': 0.12076665098537015, 'recall': 0.1085972850678733, 'f1-score': 0.107490055748062, 'support': 2210.0}}
- **Macro Precision:** 0.048
- **Macro Recall:** 0.043
- **Macro F1:** 0.043
- **Weighted F1:** 0.107
- **Confusion Matrix:** [[44, 22, 37, 27, 23, 14, 6, 11, 9, 10, 1, 6, 0, 0, 0, 4, 0, 2, 0, 0, 0, 0, 2, 1, 0], [35, 33, 27, 27, 19, 25, 12, 12, 7, 4, 1, 3, 0, 1, 0, 1, 1, 0, 2, 3, 0, 0, 7, 0, 0], [32, 28, 36, 28, 30, 19, 11, 7, 6, 9, 0, 5, 0, 1, 0, 1, 1, 0, 2, 0, 1, 0, 2, 1, 0], [31, 34, 19, 26, 30, 20, 12, 10, 11, 2, 2, 5, 0, 0, 1, 1, 0, 0, 1, 6, 0, 2, 3, 1, 0], [57, 21, 22, 31, 31, 18, 13, 8, 9, 6, 0, 9, 0, 3, 1, 0, 0, 0, 4, 1, 0, 1, 4, 1, 0], [47, 22, 37, 25, 22, 18, 15, 10, 9, 2, 2, 4, 0, 0, 0, 1, 0, 0, 3, 1, 1, 0, 5, 0, 0], [31, 30, 34, 20, 29, 21, 22, 14, 8, 5, 1, 16, 2, 0, 1, 1, 1, 1, 0, 1, 0, 1, 2, 0, 0], [25, 19, 25, 22, 28, 25, 11, 12, 9, 7, 2, 5, 0, 1, 0, 0, 0, 2, 1, 2, 0, 2, 1, 1, 0], [33, 17, 21, 26, 22, 24, 17, 8, 13, 5, 5, 3, 1, 1, 0, 1, 0, 0, 2, 1, 0, 0, 6, 0, 0], [35, 22, 32, 31, 19, 27, 13, 12, 6, 5, 2, 4, 0, 0, 0, 3, 2, 1, 1, 1, 0, 0, 6, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
- **Top Confused Pairs:** [('E', 'A', 57), ('F', 'A', 47), ('A', 'C', 37), ('F', 'C', 37), ('B', 'A', 35), ('J', 'A', 35), ('D', 'B', 34), ('G', 'C', 34), ('I', 'A', 33), ('C', 'A', 32)]
- **True Class Distribution:** {'E': 240, 'C': 220, 'J': 223, 'H': 200, 'F': 224, 'B': 220, 'I': 206, 'D': 217, 'G': 241, 'A': 219}
- **Pred Class Distribution:** {'J': 55, 'B': 248, 'C': 290, 'A': 370, 'I': 87, 'S': 16, 'X': 38, 'G': 132, 'F': 211, 'E': 253, 'D': 263, 'L': 60, 'H': 104, 'Y': 5, 'P': 13, 'K': 16, 'V': 6, 'T': 16, 'Q': 5, 'N': 7, 'Z': 1, 'M': 3, 'R': 6, 'O': 3, 'U': 2}
- **Num Classes:** 25

