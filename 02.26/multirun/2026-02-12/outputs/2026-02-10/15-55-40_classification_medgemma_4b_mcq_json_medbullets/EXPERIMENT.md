# Experiment: Medbullets Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-10 15:55:40  
**Duration:** 16 minutes 20 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** No (zero-shot)
**Output Format:** JSON
**Dataset:** medbullets

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
  temperature: 1.0
  top_p: 0.9
  safe_name: medgemma_4b
prompt:
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: false
  output_format: json
  answer_first: true
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MedBulletsDataset
  name: medbullets
  split: op4_test
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 308
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=308 \
  prompt=mcq \
  prompt.answer_first=true \
  prompt.few_shot=false \
  dataset=medbullets
```

## Results

- **Accuracy:** 46.8%
- **Samples Processed:** 308
- **Correct:** 144
- **Incorrect:** 164
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.4883720930232558, 'recall': 0.4827586206896552, 'f1-score': 0.48554913294797686, 'support': 87.0}, 'B': {'precision': 0.4675324675324675, 'recall': 0.47368421052631576, 'f1-score': 0.47058823529411764, 'support': 76.0}, 'C': {'precision': 0.4864864864864865, 'recall': 0.4675324675324675, 'f1-score': 0.4768211920529801, 'support': 77.0}, 'D': {'precision': 0.47619047619047616, 'recall': 0.4411764705882353, 'f1-score': 0.4580152671755725, 'support': 68.0}, 'E': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'O': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.4675324675324675, 'macro avg': {'precision': 0.23982269040408574, 'recall': 0.2331439711670842, 'f1-score': 0.2363717284338309, 'support': 308.0}, 'weighted avg': {'precision': 0.4800689982659176, 'recall': 0.4675324675324675, 'f1-score': 0.47359659222352374, 'support': 308.0}}
- **Macro Precision:** 0.240
- **Macro Recall:** 0.233
- **Macro F1:** 0.236
- **Weighted F1:** 0.474
- **Confusion Matrix:** [[42, 14, 16, 14, 0, 1, 0, 0], [14, 36, 13, 9, 0, 1, 0, 3], [17, 13, 36, 10, 1, 0, 0, 0], [13, 14, 9, 30, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'O', 'S', 'T']
- **Top Confused Pairs:** [('C', 'A', 17), ('A', 'C', 16), ('A', 'B', 14), ('A', 'D', 14), ('B', 'A', 14), ('D', 'B', 14), ('B', 'C', 13), ('C', 'B', 13), ('D', 'A', 13), ('C', 'D', 10)]
- **True Class Distribution:** {'B': 76, 'D': 68, 'C': 77, 'A': 87}
- **Pred Class Distribution:** {'D': 63, 'A': 86, 'B': 77, 'C': 74, 'S': 1, 'T': 4, 'O': 2, 'E': 1}
- **Num Classes:** 8

