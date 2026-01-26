# Experiment: Medqa Answer-First

**Status:** Completed
**Started:** 2026-01-26 09:10:49  
**Duration:** 1 minutes 48 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
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
  answer_first: true
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
  prompt.answer_first=true \
  dataset=medqa
```

## Results

- **Accuracy:** 53.7%
- **Samples Processed:** 1273
- **Correct:** 683
- **Incorrect:** 590
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.5662650602409639, 'recall': 0.5325779036827195, 'f1-score': 0.5489051094890511, 'support': 353.0}, 'B': {'precision': 0.5173410404624278, 'recall': 0.5792880258899676, 'f1-score': 0.5465648854961832, 'support': 309.0}, 'C': {'precision': 0.5702005730659025, 'recall': 0.5751445086705202, 'f1-score': 0.5726618705035971, 'support': 346.0}, 'D': {'precision': 0.4978723404255319, 'recall': 0.44150943396226416, 'f1-score': 0.468, 'support': 265.0}, 'E': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'H': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.5365278868813825, 'macro avg': {'precision': 0.19560718310862057, 'recall': 0.1935018065641338, 'f1-score': 0.19419380595353014, 'support': 1273.0}, 'weighted avg': {'precision': 0.541221929506299, 'recall': 0.5365278868813825, 'f1-score': 0.537952129192616, 'support': 1273.0}}
- **Macro Precision:** 0.196
- **Macro Recall:** 0.194
- **Macro F1:** 0.194
- **Weighted F1:** 0.538
- **Confusion Matrix:** [[188, 66, 57, 40, 0, 0, 1, 0, 0, 1, 0], [44, 179, 48, 32, 1, 0, 0, 1, 1, 2, 1], [52, 47, 199, 46, 0, 1, 0, 0, 1, 0, 0], [48, 54, 45, 117, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'G', 'H', 'I', 'L', 'T', 'X']
- **Top Confused Pairs:** [('A', 'B', 66), ('A', 'C', 57), ('D', 'B', 54), ('C', 'A', 52), ('B', 'C', 48), ('D', 'A', 48), ('C', 'B', 47), ('C', 'D', 46), ('D', 'C', 45), ('B', 'A', 44)]
- **True Class Distribution:** {'B': 309, 'D': 265, 'C': 346, 'A': 353}
- **Pred Class Distribution:** {'A': 332, 'C': 349, 'B': 346, 'D': 235, 'I': 2, 'T': 3, 'X': 1, 'E': 1, 'H': 1, 'G': 1, 'L': 2}
- **Num Classes:** 11

