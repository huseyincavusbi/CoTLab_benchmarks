# Experiment: Plab Standard Zero-Shot

**Status:** Completed
**Started:** 2026-02-12 13:55:06  
**Duration:** 8 minutes 33 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?

## Configuration

**Prompt Strategy:** Plab
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
  prompt.few_shot=false \
  dataset=plab
```

## Results

- **Accuracy:** 69.1%
- **Samples Processed:** 1652
- **Correct:** 1140
- **Incorrect:** 509
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.5645161290322581, 'recall': 0.8045977011494253, 'f1-score': 0.6635071090047393, 'support': 435.0}, 'B': {'precision': 0.7472826086956522, 'recall': 0.6740196078431373, 'f1-score': 0.7087628865979382, 'support': 408.0}, 'C': {'precision': 0.7642857142857142, 'recall': 0.6504559270516718, 'f1-score': 0.7027914614121511, 'support': 329.0}, 'D': {'precision': 0.8028169014084507, 'recall': 0.6173285198555957, 'f1-score': 0.6979591836734694, 'support': 277.0}, 'E': {'precision': 0.7727272727272727, 'recall': 0.6467391304347826, 'f1-score': 0.7041420118343196, 'support': 184.0}, 'F': {'precision': 0.875, 'recall': 0.6363636363636364, 'f1-score': 0.7368421052631579, 'support': 11.0}, 'G': {'precision': 0.6666666666666666, 'recall': 0.8, 'f1-score': 0.7272727272727273, 'support': 5.0}, 'accuracy': 0.6913280776228017, 'macro avg': {'precision': 0.741899327545145, 'recall': 0.6899292175283213, 'f1-score': 0.705896783579786, 'support': 1649.0}, 'weighted avg': {'precision': 0.7152372672420564, 'recall': 0.6913280776228017, 'f1-score': 0.6935462048532094, 'support': 1649.0}}
- **Macro Precision:** 0.742
- **Macro Recall:** 0.690
- **Macro F1:** 0.706
- **Weighted F1:** 0.694
- **Confusion Matrix:** [[350, 36, 20, 14, 13, 1, 1], [89, 275, 22, 14, 7, 0, 1], [73, 28, 214, 9, 5, 0, 0], [66, 14, 17, 171, 9, 0, 0], [38, 15, 7, 5, 119, 0, 0], [3, 0, 0, 0, 1, 7, 0], [1, 0, 0, 0, 0, 0, 4]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Top Confused Pairs:** [('B', 'A', 89), ('C', 'A', 73), ('D', 'A', 66), ('E', 'A', 38), ('A', 'B', 36), ('C', 'B', 28), ('B', 'C', 22), ('A', 'C', 20), ('D', 'C', 17), ('E', 'B', 15)]
- **True Class Distribution:** {'B': 408, 'C': 329, 'D': 277, 'A': 435, 'E': 184, 'G': 5, 'F': 11}
- **Pred Class Distribution:** {'B': 368, 'C': 280, 'A': 620, 'D': 213, 'E': 154, 'G': 6, 'F': 8}
- **Num Classes:** 7

