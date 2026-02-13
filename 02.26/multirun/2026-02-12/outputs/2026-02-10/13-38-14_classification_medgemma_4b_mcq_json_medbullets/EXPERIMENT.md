# Experiment: Medbullets Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-10 13:38:14  
**Duration:** 6 minutes 27 seconds

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
  max_new_tokens: 256
  temperature: 0
  top_p: 1
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
  split: op5_test
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

- **Accuracy:** 19.3%
- **Samples Processed:** 308
- **Correct:** 57
- **Incorrect:** 238
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.1890547263681592, 'recall': 0.6551724137931034, 'f1-score': 0.29343629343629346, 'support': 58.0}, 'B': {'precision': 0.4, 'recall': 0.08450704225352113, 'f1-score': 0.13953488372093023, 'support': 71.0}, 'C': {'precision': 0.14285714285714285, 'recall': 0.0784313725490196, 'f1-score': 0.10126582278481013, 'support': 51.0}, 'D': {'precision': 0.2727272727272727, 'recall': 0.09523809523809523, 'f1-score': 0.1411764705882353, 'support': 63.0}, 'E': {'precision': 0.14285714285714285, 'recall': 0.057692307692307696, 'f1-score': 0.0821917808219178, 'support': 52.0}, 'F': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'I': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'U': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.19322033898305085, 'macro avg': {'precision': 0.0956246904008098, 'recall': 0.08092010262717059, 'f1-score': 0.06313377094601556, 'support': 295.0}, 'weighted avg': {'precision': 0.24156365432358348, 'recall': 0.19322033898305085, 'f1-score': 0.15342009822140654, 'support': 295.0}}
- **Macro Precision:** 0.096
- **Macro Recall:** 0.081
- **Macro F1:** 0.063
- **Weighted F1:** 0.153
- **Confusion Matrix:** [[38, 1, 5, 3, 11, 0, 0, 0, 0, 0, 0, 0], [50, 6, 4, 5, 5, 0, 0, 0, 1, 0, 0, 0], [37, 2, 4, 2, 1, 0, 1, 1, 0, 1, 0, 2], [41, 4, 9, 6, 1, 1, 0, 0, 0, 0, 1, 0], [35, 2, 6, 6, 3, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'I', 'K', 'L', 'U', 'V', 'X']
- **Top Confused Pairs:** [('B', 'A', 50), ('D', 'A', 41), ('C', 'A', 37), ('E', 'A', 35), ('A', 'E', 11), ('D', 'C', 9), ('E', 'C', 6), ('E', 'D', 6), ('A', 'C', 5), ('B', 'D', 5)]
- **True Class Distribution:** {'B': 71, 'E': 52, 'A': 58, 'D': 63, 'C': 51}
- **Pred Class Distribution:** {'A': 201, 'C': 28, 'D': 22, 'E': 21, 'B': 15, 'U': 1, 'X': 2, 'L': 1, 'V': 1, 'F': 1, 'K': 1, 'I': 1}
- **Num Classes:** 12

