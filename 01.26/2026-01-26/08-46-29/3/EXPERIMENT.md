# Experiment: Medmcqa Standard

**Status:** Completed
**Started:** 2026-01-26 09:05:09  
**Duration:** 4 minutes 52 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medmcqa

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
  name: medmcqa
  filename: medmcqa/validation.jsonl
  split: validation
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
  dataset=medmcqa
```

## Results

- **Accuracy:** 53.2%
- **Samples Processed:** 4183
- **Correct:** 2216
- **Incorrect:** 1949
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.5668103448275862, 'recall': 0.5870535714285714, 'f1-score': 0.5767543859649122, 'support': 1344.0}, 'B': {'precision': 0.5368007850834151, 'recall': 0.5078922934076138, 'f1-score': 0.5219465648854962, 'support': 1077.0}, 'C': {'precision': 0.5241228070175439, 'recall': 0.5190010857763301, 'f1-score': 0.5215493726132024, 'support': 921.0}, 'D': {'precision': 0.5193798449612403, 'recall': 0.488456865127582, 'f1-score': 0.5034439574201628, 'support': 823.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'M': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'NONE OF THE OPTIONS ARE CORRECT. THE QUESTION IS A TEST QUESTION AND NOT A MEDICAL QUESTION.': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'O': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Z': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.5320528211284514, 'macro avg': {'precision': 0.15336527013498472, 'recall': 0.15017170112429268, 'f1-score': 0.15169244863455525, 'support': 4165.0}, 'weighted avg': {'precision': 0.5402387194836429, 'recall': 0.5320528211284514, 'f1-score': 0.5358885220293097, 'support': 4165.0}}
- **Macro Precision:** 0.153
- **Macro Recall:** 0.150
- **Macro F1:** 0.152
- **Weighted F1:** 0.536
- **Confusion Matrix:** [[789, 218, 185, 134, 1, 1, 0, 0, 0, 2, 3, 0, 11, 0], [229, 547, 144, 130, 0, 0, 0, 0, 1, 0, 2, 0, 24, 0], [188, 139, 478, 108, 1, 0, 0, 0, 0, 0, 0, 1, 5, 1], [186, 115, 105, 402, 2, 0, 1, 1, 0, 0, 2, 0, 9, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'L', 'M', 'N', 'NONE OF THE OPTIONS ARE CORRECT. THE QUESTION IS A TEST QUESTION AND NOT A MEDICAL QUESTION.', 'O', 'S', 'T', 'V', 'X', 'Z']
- **Top Confused Pairs:** [('B', 'A', 229), ('A', 'B', 218), ('C', 'A', 188), ('D', 'A', 186), ('A', 'C', 185), ('B', 'C', 144), ('C', 'B', 139), ('A', 'D', 134), ('B', 'D', 130), ('D', 'B', 115)]
- **True Class Distribution:** {'A': 1344, 'C': 921, 'B': 1077, 'D': 823}
- **Pred Class Distribution:** {'A': 1392, 'B': 1019, 'C': 912, 'D': 774, 'X': 49, 'NONE OF THE OPTIONS ARE CORRECT. THE QUESTION IS A TEST QUESTION AND NOT A MEDICAL QUESTION.': 1, 'T': 7, 'Z': 1, 'N': 1, 'O': 1, 'L': 4, 'S': 2, 'M': 1, 'V': 1}
- **Num Classes:** 14

