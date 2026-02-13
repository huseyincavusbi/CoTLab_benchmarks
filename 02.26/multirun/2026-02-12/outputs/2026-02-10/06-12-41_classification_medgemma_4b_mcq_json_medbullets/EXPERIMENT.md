# Experiment: Medbullets Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-10 06:12:41  
**Duration:** 16 minutes 17 seconds

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
  temperature: 0.7
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

- **Accuracy:** 46.6%
- **Samples Processed:** 308
- **Correct:** 143
- **Incorrect:** 164
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.4215686274509804, 'recall': 0.4942528735632184, 'f1-score': 0.455026455026455, 'support': 87.0}, 'B': {'precision': 0.5569620253164557, 'recall': 0.5789473684210527, 'f1-score': 0.567741935483871, 'support': 76.0}, 'C': {'precision': 0.4864864864864865, 'recall': 0.4675324675324675, 'f1-score': 0.4768211920529801, 'support': 77.0}, 'D': {'precision': 0.425531914893617, 'recall': 0.29850746268656714, 'f1-score': 0.3508771929824561, 'support': 67.0}, 'O': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.46579804560260585, 'macro avg': {'precision': 0.27007843630679135, 'recall': 0.26274859602904366, 'f1-score': 0.26435239650653747, 'support': 307.0}, 'weighted avg': {'precision': 0.47223349273491116, 'recall': 0.46579804560260585, 'f1-score': 0.4656667504950482, 'support': 307.0}}
- **Macro Precision:** 0.270
- **Macro Recall:** 0.263
- **Macro F1:** 0.264
- **Weighted F1:** 0.466
- **Confusion Matrix:** [[43, 12, 17, 14, 0, 1, 0], [13, 44, 11, 7, 0, 0, 1], [25, 9, 36, 6, 0, 1, 0], [21, 14, 10, 20, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'O', 'P', 'T']
- **Top Confused Pairs:** [('C', 'A', 25), ('D', 'A', 21), ('A', 'C', 17), ('A', 'D', 14), ('D', 'B', 14), ('B', 'A', 13), ('A', 'B', 12), ('B', 'C', 11), ('D', 'C', 10), ('C', 'B', 9)]
- **True Class Distribution:** {'B': 76, 'D': 67, 'C': 77, 'A': 87}
- **Pred Class Distribution:** {'B': 79, 'D': 47, 'A': 102, 'C': 74, 'T': 2, 'P': 2, 'O': 1}
- **Num Classes:** 7

