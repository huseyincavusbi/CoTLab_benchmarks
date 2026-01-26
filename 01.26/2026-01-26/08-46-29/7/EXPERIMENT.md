# Experiment: Medxpertqa Standard

**Status:** Completed
**Started:** 2026-01-26 09:20:44  
**Duration:** 3 minutes 52 seconds

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

- **Accuracy:** 12.1%
- **Samples Processed:** 2450
- **Correct:** 290
- **Incorrect:** 2102
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.14210526315789473, 'recall': 0.2297872340425532, 'f1-score': 0.17560975609756097, 'support': 235.0}, 'B': {'precision': 0.10843373493975904, 'recall': 0.1134453781512605, 'f1-score': 0.11088295687885011, 'support': 238.0}, 'C': {'precision': 0.11981566820276497, 'recall': 0.11063829787234042, 'f1-score': 0.11504424778761062, 'support': 235.0}, 'D': {'precision': 0.1437125748502994, 'recall': 0.100418410041841, 'f1-score': 0.11822660098522167, 'support': 239.0}, 'E': {'precision': 0.15730337078651685, 'recall': 0.10852713178294573, 'f1-score': 0.12844036697247707, 'support': 258.0}, 'F': {'precision': 0.1368421052631579, 'recall': 0.10970464135021098, 'f1-score': 0.12177985948477751, 'support': 237.0}, 'G': {'precision': 0.10152284263959391, 'recall': 0.078125, 'f1-score': 0.08830022075055188, 'support': 256.0}, 'H': {'precision': 0.11688311688311688, 'recall': 0.12442396313364056, 'f1-score': 0.12053571428571429, 'support': 217.0}, 'I': {'precision': 0.12105263157894737, 'recall': 0.10222222222222223, 'f1-score': 0.1108433734939759, 'support': 225.0}, 'J': {'precision': 0.11075949367088607, 'recall': 0.1388888888888889, 'f1-score': 0.12323943661971831, 'support': 252.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'R': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.12123745819397994, 'macro avg': {'precision': 0.06623320010383879, 'recall': 0.06400953513083703, 'f1-score': 0.06383697543981359, 'support': 2392.0}, 'weighted avg': {'precision': 0.12592956537400832, 'recall': 0.12123745819397994, 'f1-score': 0.12111481489920396, 'support': 2392.0}}
- **Macro Precision:** 0.066
- **Macro Recall:** 0.064
- **Macro F1:** 0.064
- **Weighted F1:** 0.121
- **Confusion Matrix:** [[54, 32, 22, 18, 8, 10, 23, 19, 15, 29, 1, 0, 0, 0, 0, 1, 1, 1, 1], [34, 27, 21, 17, 16, 19, 24, 18, 18, 37, 0, 0, 1, 0, 0, 0, 4, 0, 2], [37, 25, 26, 20, 20, 22, 12, 15, 22, 31, 1, 1, 0, 0, 0, 0, 3, 0, 0], [40, 16, 15, 24, 20, 23, 26, 25, 17, 27, 0, 3, 0, 1, 0, 1, 1, 0, 0], [35, 27, 27, 22, 28, 18, 22, 28, 25, 17, 1, 0, 0, 1, 1, 0, 3, 0, 3], [36, 22, 13, 11, 14, 26, 19, 26, 13, 40, 0, 0, 0, 0, 0, 1, 14, 0, 2], [42, 29, 28, 12, 23, 17, 20, 25, 18, 34, 1, 0, 1, 0, 0, 0, 5, 0, 1], [31, 16, 18, 19, 19, 14, 18, 27, 11, 39, 0, 0, 0, 0, 0, 1, 3, 0, 1], [29, 27, 24, 10, 15, 23, 16, 23, 23, 27, 0, 1, 1, 0, 0, 1, 4, 0, 1], [42, 28, 23, 14, 15, 18, 17, 25, 28, 35, 0, 1, 0, 0, 0, 0, 4, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'P', 'Q', 'R', 'S', 'T', 'V', 'X']
- **Top Confused Pairs:** [('G', 'A', 42), ('J', 'A', 42), ('D', 'A', 40), ('F', 'J', 40), ('H', 'J', 39), ('B', 'J', 37), ('C', 'A', 37), ('F', 'A', 36), ('E', 'A', 35), ('B', 'A', 34)]
- **True Class Distribution:** {'E': 258, 'C': 235, 'I': 225, 'J': 252, 'H': 217, 'B': 238, 'D': 239, 'G': 256, 'A': 235, 'F': 237}
- **Pred Class Distribution:** {'H': 231, 'C': 217, 'E': 178, 'I': 190, 'J': 316, 'G': 197, 'A': 380, 'B': 249, 'D': 167, 'R': 1, 'F': 190, 'T': 42, 'P': 3, 'X': 13, 'L': 6, 'S': 5, 'K': 4, 'Q': 2, 'V': 1}
- **Num Classes:** 19

