# Experiment: Plab Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-12 13:10:33  
**Duration:** 18 minutes 20 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
**Output Format:** JSON
**Dataset:** plab

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
  name: google/medgemma-27b-it
  variant: 27b
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b_it
prompt:
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: false
  output_format: json
  answer_first: false
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.PLABDataset
  name: plab
  split: main
  filename: plab/data.json
  topics_filename: plab/topics.json
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
  prompt.few_shot=false \
  dataset=plab
```

## Results

- **Accuracy:** 23.2%
- **Samples Processed:** 1652
- **Correct:** 342
- **Incorrect:** 1129
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.2873303167420814, 'recall': 0.3239795918367347, 'f1-score': 0.30455635491606714, 'support': 392.0}, 'B': {'precision': 0.28837209302325584, 'recall': 0.17270194986072424, 'f1-score': 0.21602787456445993, 'support': 359.0}, 'C': {'precision': 0.25311203319502074, 'recall': 0.20819112627986347, 'f1-score': 0.22846441947565543, 'support': 293.0}, 'D': {'precision': 0.2222222222222222, 'recall': 0.199203187250996, 'f1-score': 0.21008403361344538, 'support': 251.0}, 'E': {'precision': 0.22988505747126436, 'recall': 0.25, 'f1-score': 0.23952095808383234, 'support': 160.0}, 'F': {'precision': 0.3333333333333333, 'recall': 0.18181818181818182, 'f1-score': 0.23529411764705882, 'support': 11.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 5.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'J': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'M': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'R': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.23249490142760026, 'macro avg': {'precision': 0.07686928838034181, 'recall': 0.06361400176411906, 'f1-score': 0.068283226585739, 'support': 1471.0}, 'weighted avg': {'precision': 0.2627783446119868, 'recall': 0.23249490142760026, 'f1-score': 0.24304748744161261, 'support': 1471.0}}
- **Macro Precision:** 0.077
- **Macro Recall:** 0.064
- **Macro F1:** 0.068
- **Weighted F1:** 0.243
- **Confusion Matrix:** [[127, 58, 56, 60, 32, 1, 1, 0, 2, 0, 7, 13, 2, 1, 1, 4, 1, 5, 4, 1, 16], [94, 62, 75, 58, 35, 1, 0, 3, 3, 1, 5, 5, 0, 1, 2, 1, 0, 2, 1, 3, 7], [86, 39, 61, 40, 35, 1, 0, 2, 1, 0, 2, 6, 1, 1, 1, 0, 0, 0, 1, 3, 13], [82, 35, 31, 50, 30, 0, 3, 3, 1, 1, 2, 2, 0, 0, 1, 0, 0, 1, 1, 2, 6], [49, 20, 16, 16, 40, 1, 0, 1, 0, 0, 4, 4, 0, 0, 0, 0, 0, 3, 1, 0, 5], [2, 1, 2, 1, 1, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X']
- **Top Confused Pairs:** [('B', 'A', 94), ('C', 'A', 86), ('D', 'A', 82), ('B', 'C', 75), ('A', 'D', 60), ('A', 'B', 58), ('B', 'D', 58), ('A', 'C', 56), ('E', 'A', 49), ('C', 'D', 40)]
- **True Class Distribution:** {'B': 359, 'C': 293, 'D': 251, 'A': 392, 'E': 160, 'G': 5, 'F': 11}
- **Pred Class Distribution:** {'A': 442, 'B': 215, 'D': 225, 'C': 241, 'I': 7, 'E': 174, 'L': 31, 'X': 48, 'H': 10, 'F': 6, 'K': 20, 'M': 3, 'R': 1, 'P': 5, 'G': 4, 'T': 9, 'Q': 5, 'S': 11, 'N': 3, 'V': 9, 'J': 2}
- **Num Classes:** 21

