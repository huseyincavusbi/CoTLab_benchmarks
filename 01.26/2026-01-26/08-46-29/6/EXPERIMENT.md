# Experiment: Medxpertqa Answer-First

**Status:** Completed
**Started:** 2026-01-26 09:16:02  
**Duration:** 3 minutes 53 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
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
  answer_first: true
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
  prompt.answer_first=true \
  dataset=medxpertqa
```

## Results

- **Accuracy:** 12.3%
- **Samples Processed:** 2450
- **Correct:** 301
- **Incorrect:** 2146
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.11246200607902736, 'recall': 0.15352697095435686, 'f1-score': 0.12982456140350876, 'support': 241.0}, 'B': {'precision': 0.08955223880597014, 'recall': 0.14634146341463414, 'f1-score': 0.1111111111111111, 'support': 246.0}, 'C': {'precision': 0.11594202898550725, 'recall': 0.16736401673640167, 'f1-score': 0.136986301369863, 'support': 239.0}, 'D': {'precision': 0.1596244131455399, 'recall': 0.14049586776859505, 'f1-score': 0.14945054945054945, 'support': 242.0}, 'E': {'precision': 0.1457286432160804, 'recall': 0.11026615969581749, 'f1-score': 0.12554112554112554, 'support': 263.0}, 'F': {'precision': 0.10909090909090909, 'recall': 0.09876543209876543, 'f1-score': 0.10367170626349892, 'support': 243.0}, 'G': {'precision': 0.16666666666666666, 'recall': 0.13307984790874525, 'f1-score': 0.14799154334038056, 'support': 263.0}, 'H': {'precision': 0.12322274881516587, 'recall': 0.11711711711711711, 'f1-score': 0.12009237875288684, 'support': 222.0}, 'I': {'precision': 0.175, 'recall': 0.1206896551724138, 'f1-score': 0.14285714285714285, 'support': 232.0}, 'J': {'precision': 0.08759124087591241, 'recall': 0.046875, 'f1-score': 0.061068702290076333, 'support': 256.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Y': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.12300776460972619, 'macro avg': {'precision': 0.07558122915769289, 'recall': 0.07261891358040276, 'f1-score': 0.07227030131647903, 'support': 2447.0}, 'weighted avg': {'precision': 0.12853302510401507, 'recall': 0.12300776460972619, 'f1-score': 0.12263836582596366, 'support': 2447.0}}
- **Macro Precision:** 0.076
- **Macro Recall:** 0.073
- **Macro F1:** 0.072
- **Weighted F1:** 0.123
- **Confusion Matrix:** [[37, 47, 40, 20, 16, 15, 20, 14, 16, 12, 1, 0, 0, 0, 0, 2, 1], [32, 36, 36, 22, 20, 18, 24, 20, 14, 22, 0, 0, 0, 0, 2, 0, 0], [34, 45, 40, 18, 18, 27, 9, 19, 15, 12, 0, 1, 0, 0, 0, 1, 0], [41, 33, 33, 34, 14, 19, 23, 22, 13, 9, 0, 0, 0, 0, 1, 0, 0], [41, 39, 30, 23, 29, 29, 21, 22, 15, 11, 0, 0, 0, 0, 1, 2, 0], [32, 39, 28, 12, 22, 24, 24, 27, 16, 16, 0, 0, 1, 0, 2, 0, 0], [32, 34, 34, 21, 22, 27, 35, 26, 12, 18, 0, 0, 0, 0, 1, 1, 0], [26, 44, 30, 16, 18, 9, 23, 26, 15, 14, 0, 0, 0, 0, 1, 0, 0], [20, 47, 35, 16, 16, 24, 12, 22, 28, 11, 0, 0, 0, 1, 0, 0, 0], [34, 38, 39, 31, 24, 28, 19, 13, 16, 12, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'S', 'T', 'X', 'Y']
- **Top Confused Pairs:** [('A', 'B', 47), ('I', 'B', 47), ('C', 'B', 45), ('H', 'B', 44), ('D', 'A', 41), ('E', 'A', 41), ('A', 'C', 40), ('E', 'B', 39), ('F', 'B', 39), ('J', 'C', 39)]
- **True Class Distribution:** {'E': 263, 'C': 239, 'I': 232, 'J': 256, 'H': 222, 'F': 243, 'B': 246, 'D': 242, 'G': 263, 'A': 241}
- **Pred Class Distribution:** {'C': 345, 'E': 199, 'J': 137, 'F': 220, 'G': 210, 'A': 329, 'B': 402, 'D': 213, 'H': 211, 'I': 160, 'L': 1, 'T': 9, 'K': 1, 'X': 7, 'N': 1, 'S': 1, 'Y': 1}
- **Num Classes:** 17

