# Experiment: Plab Answer-First

**Status:** Completed
**Started:** 2026-02-12 12:53:53  
**Duration:** 15 minutes 29 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
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
  few_shot: true
  output_format: json
  answer_first: true
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
  prompt.answer_first=true \
  dataset=plab
```

## Results

- **Accuracy:** 41.0%
- **Samples Processed:** 1652
- **Correct:** 648
- **Incorrect:** 934
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.35, 'recall': 0.5371702637889688, 'f1-score': 0.423841059602649, 'support': 417.0}, 'B': {'precision': 0.5680933852140078, 'recall': 0.3734015345268542, 'f1-score': 0.4506172839506173, 'support': 391.0}, 'C': {'precision': 0.5260416666666666, 'recall': 0.3247588424437299, 'f1-score': 0.40159045725646125, 'support': 311.0}, 'D': {'precision': 0.4292237442922374, 'recall': 0.35074626865671643, 'f1-score': 0.3860369609856263, 'support': 268.0}, 'E': {'precision': 0.39086294416243655, 'recall': 0.4301675977653631, 'f1-score': 0.4095744680851064, 'support': 179.0}, 'F': {'precision': 1.0, 'recall': 0.36363636363636365, 'f1-score': 0.5333333333333333, 'support': 11.0}, 'G': {'precision': 0.3333333333333333, 'recall': 0.4, 'f1-score': 0.36363636363636365, 'support': 5.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'R': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'U': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.40960809102402024, 'macro avg': {'precision': 0.1798777536834341, 'recall': 0.13899404354089978, 'f1-score': 0.14843149634250785, 'support': 1582.0}, 'weighted avg': {'precision': 0.4610218515133203, 'recall': 0.40960809102402024, 'f1-score': 0.4186373551845675, 'support': 1582.0}}
- **Macro Precision:** 0.180
- **Macro Recall:** 0.139
- **Macro F1:** 0.148
- **Weighted F1:** 0.419
- **Confusion Matrix:** [[224, 58, 34, 42, 41, 0, 1, 1, 1, 3, 6, 0, 0, 0, 1, 0, 1, 0, 0, 4], [124, 146, 34, 40, 29, 0, 0, 1, 1, 1, 2, 1, 4, 0, 0, 0, 1, 0, 1, 6], [133, 16, 101, 26, 24, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 5], [99, 27, 12, 94, 24, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 2, 1, 4], [55, 10, 11, 17, 77, 0, 0, 1, 0, 1, 3, 1, 0, 0, 0, 1, 1, 0, 0, 1], [4, 0, 0, 0, 2, 4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X']
- **Top Confused Pairs:** [('C', 'A', 133), ('B', 'A', 124), ('D', 'A', 99), ('A', 'B', 58), ('E', 'A', 55), ('A', 'D', 42), ('A', 'E', 41), ('B', 'D', 40), ('A', 'C', 34), ('B', 'C', 34)]
- **True Class Distribution:** {'C': 311, 'B': 391, 'A': 417, 'D': 268, 'E': 179, 'G': 5, 'F': 11}
- **Pred Class Distribution:** {'A': 640, 'B': 257, 'D': 219, 'C': 192, 'V': 3, 'E': 197, 'N': 4, 'X': 20, 'G': 6, 'P': 5, 'L': 14, 'K': 5, 'F': 4, 'Q': 1, 'R': 1, 'I': 3, 'H': 4, 'T': 3, 'U': 2, 'S': 2}
- **Num Classes:** 20

