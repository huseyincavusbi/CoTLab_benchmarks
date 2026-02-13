# Experiment: Plab Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-11 18:37:58  
**Duration:** 4 minutes 14 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Standard
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
  answer_first: false
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
  num_samples: 100
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=100 \
  prompt=mcq \
  prompt.few_shot=false \
  dataset=plab
```

## Results

- **Accuracy:** 61.2%
- **Samples Processed:** 100
- **Correct:** 60
- **Incorrect:** 38
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.7142857142857143, 'recall': 0.6666666666666666, 'f1-score': 0.6896551724137931, 'support': 30.0}, 'B': {'precision': 0.56, 'recall': 0.7, 'f1-score': 0.6222222222222222, 'support': 20.0}, 'C': {'precision': 0.5416666666666666, 'recall': 0.8125, 'f1-score': 0.65, 'support': 16.0}, 'D': {'precision': 0.875, 'recall': 0.3684210526315789, 'f1-score': 0.5185185185185185, 'support': 19.0}, 'E': {'precision': 0.5, 'recall': 0.5, 'f1-score': 0.5, 'support': 12.0}, 'G': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 1.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.6122448979591837, 'macro avg': {'precision': 0.4558503401360544, 'recall': 0.43536967418546363, 'f1-score': 0.425770844736362, 'support': 98.0}, 'weighted avg': {'precision': 0.6522473275024295, 'recall': 0.6122448979591837, 'f1-score': 0.6059790966194907, 'support': 98.0}}
- **Macro Precision:** 0.456
- **Macro Recall:** 0.435
- **Macro F1:** 0.426
- **Weighted F1:** 0.606
- **Confusion Matrix:** [[20, 4, 3, 0, 3, 0, 0], [3, 14, 3, 0, 0, 0, 0], [1, 1, 13, 0, 0, 0, 1], [3, 4, 2, 7, 3, 0, 0], [1, 2, 3, 0, 6, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'G', 'S']
- **Top Confused Pairs:** [('A', 'B', 4), ('D', 'B', 4), ('A', 'C', 3), ('A', 'E', 3), ('B', 'A', 3), ('B', 'C', 3), ('D', 'A', 3), ('D', 'E', 3), ('E', 'C', 3), ('D', 'C', 2)]
- **True Class Distribution:** {'B': 20, 'C': 16, 'D': 19, 'A': 30, 'E': 12, 'G': 1}
- **Pred Class Distribution:** {'B': 25, 'C': 24, 'D': 8, 'A': 28, 'E': 12, 'S': 1}
- **Num Classes:** 7

