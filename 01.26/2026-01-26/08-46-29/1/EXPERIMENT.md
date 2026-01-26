# Experiment: Afrimedqa Standard

**Status:** Completed
**Started:** 2026-01-26 08:53:16  
**Duration:** 4 minutes 53 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** afrimedqa

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
  name: afrimedqa
  filename: afrimedqa/mcq.jsonl
  split: mcq
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
  dataset=afrimedqa
```

## Results

- **Accuracy:** 57.5%
- **Samples Processed:** 3958
- **Correct:** 2271
- **Incorrect:** 1680
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.587991718426501, 'recall': 0.5308411214953271, 'f1-score': 0.5579567779960707, 'support': 1070.0}, 'B': {'precision': 0.5626450116009281, 'recall': 0.5987654320987654, 'f1-score': 0.5801435406698564, 'support': 810.0}, 'C': {'precision': 0.6387878787878788, 'recall': 0.6142191142191142, 'f1-score': 0.6262626262626263, 'support': 858.0}, 'D': {'precision': 0.6160108548168249, 'recall': 0.576874205844981, 'f1-score': 0.5958005249343832, 'support': 787.0}, 'E': {'precision': 0.4505703422053232, 'recall': 0.5563380281690141, 'f1-score': 0.49789915966386555, 'support': 426.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N/A': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'O': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'R': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Y': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.574791192103265, 'macro avg': {'precision': 0.1904003870558304, 'recall': 0.19180252678848012, 'f1-score': 0.19053750863512015, 'support': 3951.0}, 'weighted avg': {'precision': 0.5845905104108876, 'recall': 0.574791192103265, 'f1-score': 0.5784012677478813, 'support': 3951.0}}
- **Macro Precision:** 0.190
- **Macro Recall:** 0.192
- **Macro F1:** 0.191
- **Weighted F1:** 0.578
- **Confusion Matrix:** [[568, 151, 112, 115, 110, 0, 1, 1, 2, 1, 1, 0, 4, 4, 0], [123, 485, 71, 58, 64, 0, 0, 0, 0, 0, 0, 1, 6, 2, 0], [125, 85, 527, 66, 52, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0], [92, 88, 83, 454, 63, 1, 0, 1, 0, 0, 0, 0, 2, 3, 0], [58, 53, 32, 44, 237, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'H', 'L', 'N', 'N/A', 'O', 'R', 'S', 'T', 'X', 'Y']
- **Top Confused Pairs:** [('A', 'B', 151), ('C', 'A', 125), ('B', 'A', 123), ('A', 'D', 115), ('A', 'C', 112), ('A', 'E', 110), ('D', 'A', 92), ('D', 'B', 88), ('C', 'B', 85), ('D', 'C', 83)]
- **True Class Distribution:** {'B': 810, 'E': 426, 'C': 858, 'D': 787, 'A': 1070}
- **Pred Class Distribution:** {'B': 862, 'E': 526, 'C': 825, 'D': 737, 'A': 966, 'X': 11, 'T': 13, 'S': 1, 'R': 1, 'N': 2, 'N/A': 3, 'H': 1, 'O': 1, 'Y': 1, 'L': 1}
- **Num Classes:** 15

