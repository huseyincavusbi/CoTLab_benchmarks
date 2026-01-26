# Experiment: Medxpertqa Answer-First

**Status:** Completed
**Started:** 2026-01-24 12:34:21  
**Duration:** 2 minutes 5 seconds

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
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medxpertqa
  filename: medxpertqa/test.jsonl
  split: test
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 20
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=20 \
  prompt=mcq \
  prompt.answer_first=true \
  dataset=medxpertqa
```

## Results

- **Accuracy:** 5.0%
- **Samples Processed:** 20
- **Correct:** 1
- **Incorrect:** 19
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.14285714285714285, 'recall': 0.5, 'f1-score': 0.2222222222222222, 'support': 2.0}, 'C': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'D': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 2.0}, 'E': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 4.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 2.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 3.0}, 'J': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 2.0}, 'accuracy': 0.05, 'macro avg': {'precision': 0.015873015873015872, 'recall': 0.05555555555555555, 'f1-score': 0.024691358024691357, 'support': 20.0}, 'weighted avg': {'precision': 0.014285714285714285, 'recall': 0.05, 'f1-score': 0.02222222222222222, 'support': 20.0}}
- **Macro Precision:** 0.016
- **Macro Recall:** 0.056
- **Macro F1:** 0.025
- **Weighted F1:** 0.022
- **Confusion Matrix:** [[1, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0, 0], [1, 1, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
- **Top Confused Pairs:** [('E', 'D', 2), ('A', 'E', 1), ('C', 'A', 1), ('D', 'A', 1), ('D', 'G', 1), ('E', 'A', 1), ('E', 'C', 1), ('F', 'E', 1), ('G', 'A', 1), ('G', 'H', 1)]
- **True Class Distribution:** {'D': 2, 'G': 3, 'E': 4, 'J': 2, 'A': 2, 'F': 1, 'I': 3, 'H': 2, 'C': 1}
- **Pred Class Distribution:** {'G': 2, 'H': 1, 'A': 7, 'D': 3, 'F': 1, 'E': 2, 'C': 2, 'J': 2}
- **Num Classes:** 9

