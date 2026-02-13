# Experiment: Plab Standard

**Status:** Completed
**Started:** 2026-02-12 13:49:50  
**Duration:** 3 minutes 59 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Plab
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
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
  few_shot: true
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
  dataset=plab
```

## Results

- **Accuracy:** 74.6%
- **Samples Processed:** 1652
- **Correct:** 730
- **Incorrect:** 249
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.6893203883495146, 'recall': 0.7947761194029851, 'f1-score': 0.7383015597920277, 'support': 268.0}, 'B': {'precision': 0.7551020408163265, 'recall': 0.7838983050847458, 'f1-score': 0.7692307692307693, 'support': 236.0}, 'C': {'precision': 0.8248587570621468, 'recall': 0.7263681592039801, 'f1-score': 0.7724867724867724, 'support': 201.0}, 'D': {'precision': 0.762589928057554, 'recall': 0.6794871794871795, 'f1-score': 0.7186440677966102, 'support': 156.0}, 'E': {'precision': 0.7211538461538461, 'recall': 0.6696428571428571, 'f1-score': 0.6944444444444444, 'support': 112.0}, 'F': {'precision': 1.0, 'recall': 0.8, 'f1-score': 0.8888888888888888, 'support': 5.0}, 'G': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 1.0}, 'accuracy': 0.745658835546476, 'macro avg': {'precision': 0.8218607086341984, 'recall': 0.7791675171888212, 'f1-score': 0.7974280718056447, 'support': 979.0}, 'weighted avg': {'precision': 0.7502265734688701, 'recall': 0.745658835546476, 'f1-score': 0.7456627350674766, 'support': 979.0}}
- **Macro Precision:** 0.822
- **Macro Recall:** 0.779
- **Macro F1:** 0.797
- **Weighted F1:** 0.746
- **Confusion Matrix:** [[213, 21, 9, 12, 13, 0, 0], [30, 185, 8, 7, 6, 0, 0], [24, 18, 146, 9, 4, 0, 0], [25, 11, 8, 106, 6, 0, 0], [17, 10, 5, 5, 75, 0, 0], [0, 0, 1, 0, 0, 4, 0], [0, 0, 0, 0, 0, 0, 1]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Top Confused Pairs:** [('B', 'A', 30), ('D', 'A', 25), ('C', 'A', 24), ('A', 'B', 21), ('C', 'B', 18), ('E', 'A', 17), ('A', 'E', 13), ('A', 'D', 12), ('D', 'B', 11), ('E', 'B', 10)]
- **True Class Distribution:** {'C': 201, 'B': 236, 'D': 156, 'A': 268, 'E': 112, 'F': 5, 'G': 1}
- **Pred Class Distribution:** {'C': 177, 'B': 245, 'A': 309, 'E': 104, 'D': 139, 'F': 4, 'G': 1}
- **Num Classes:** 7

