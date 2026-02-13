# Experiment: Plab Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-12 14:10:05  
**Duration:** 5 minutes 34 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Plab
**Reasoning Mode:** Answer-First
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
  _target_: cotlab.prompts.PLABPromptStrategy
  name: plab
  few_shot: false
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
  prompt=plab \
  prompt.answer_first=true \
  prompt.few_shot=false \
  dataset=plab
```

## Results

- **Accuracy:** 69.3%
- **Samples Processed:** 1652
- **Correct:** 1142
- **Incorrect:** 506
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.7043879907621247, 'recall': 0.7011494252873564, 'f1-score': 0.7027649769585254, 'support': 435.0}, 'B': {'precision': 0.6643518518518519, 'recall': 0.7034313725490197, 'f1-score': 0.6833333333333333, 'support': 408.0}, 'C': {'precision': 0.7, 'recall': 0.725609756097561, 'f1-score': 0.7125748502994012, 'support': 328.0}, 'D': {'precision': 0.7261904761904762, 'recall': 0.6606498194945848, 'f1-score': 0.6918714555765595, 'support': 277.0}, 'E': {'precision': 0.6610169491525424, 'recall': 0.6358695652173914, 'f1-score': 0.6481994459833795, 'support': 184.0}, 'F': {'precision': 0.7777777777777778, 'recall': 0.6363636363636364, 'f1-score': 0.7, 'support': 11.0}, 'G': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 5.0}, 'accuracy': 0.6929611650485437, 'macro avg': {'precision': 0.747675006533539, 'recall': 0.7232962250013643, 'f1-score': 0.7341062945930285, 'support': 1648.0}, 'weighted avg': {'precision': 0.6938117522096269, 'recall': 0.6929611650485437, 'f1-score': 0.692866751899764, 'support': 1648.0}}
- **Macro Precision:** 0.748
- **Macro Recall:** 0.723
- **Macro F1:** 0.734
- **Weighted F1:** 0.693
- **Confusion Matrix:** [[305, 60, 28, 21, 21, 0, 0], [38, 287, 42, 24, 17, 0, 0], [36, 30, 238, 15, 9, 0, 0], [35, 27, 20, 183, 12, 0, 0], [18, 27, 11, 9, 117, 2, 0], [1, 1, 1, 0, 1, 7, 0], [0, 0, 0, 0, 0, 0, 5]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Top Confused Pairs:** [('A', 'B', 60), ('B', 'C', 42), ('B', 'A', 38), ('C', 'A', 36), ('D', 'A', 35), ('C', 'B', 30), ('A', 'C', 28), ('D', 'B', 27), ('E', 'B', 27), ('B', 'D', 24)]
- **True Class Distribution:** {'B': 408, 'C': 328, 'D': 277, 'A': 435, 'E': 184, 'G': 5, 'F': 11}
- **Pred Class Distribution:** {'B': 432, 'C': 340, 'D': 252, 'A': 433, 'E': 177, 'F': 9, 'G': 5}
- **Num Classes:** 7

