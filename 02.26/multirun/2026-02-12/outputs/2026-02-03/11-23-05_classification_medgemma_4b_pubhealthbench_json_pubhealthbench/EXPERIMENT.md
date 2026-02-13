# Experiment: Pubhealthbench Standard

**Status:** Completed
**Started:** 2026-02-03 11:23:05  
**Duration:** 30 minutes 6 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Pubhealthbench
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** pubhealthbench

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
  max_new_tokens: 64
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_4b
prompt:
  _target_: cotlab.prompts.pubhealthbench.PubHealthBenchMCQPromptStrategy
  name: pubhealthbench
  output_format: json
dataset:
  _target_: cotlab.datasets.loaders.PubHealthBenchDataset
  name: pubhealthbench
  split: reviewed
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
  prompt=pubhealthbench \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 77.6%
- **Samples Processed:** 760
- **Correct:** 589
- **Incorrect:** 170
- **Parse Errors:** 1
- **Parse Error Rate:** 0.001
- **Classification Report:** {'A': {'precision': 0.744, 'recall': 0.775, 'f1-score': 0.7591836734693878, 'support': 120.0}, 'B': {'precision': 0.8727272727272727, 'recall': 0.8205128205128205, 'f1-score': 0.8458149779735683, 'support': 117.0}, 'C': {'precision': 0.6470588235294118, 'recall': 0.8020833333333334, 'f1-score': 0.7162790697674418, 'support': 96.0}, 'D': {'precision': 0.7717391304347826, 'recall': 0.7553191489361702, 'f1-score': 0.7634408602150538, 'support': 94.0}, 'E': {'precision': 0.7289719626168224, 'recall': 0.7959183673469388, 'f1-score': 0.7609756097560976, 'support': 98.0}, 'F': {'precision': 0.8181818181818182, 'recall': 0.853448275862069, 'f1-score': 0.8354430379746836, 'support': 116.0}, 'G': {'precision': 0.8823529411764706, 'recall': 0.635593220338983, 'f1-score': 0.7389162561576355, 'support': 118.0}, 'accuracy': 0.7760210803689065, 'macro avg': {'precision': 0.7807188498095111, 'recall': 0.7768393094757593, 'f1-score': 0.7742933550448382, 'support': 759.0}, 'weighted avg': {'precision': 0.7859238557748973, 'recall': 0.7760210803689065, 'f1-score': 0.7763738408233007, 'support': 759.0}}
- **Macro Precision:** 0.781
- **Macro Recall:** 0.777
- **Macro F1:** 0.774
- **Weighted F1:** 0.776
- **Confusion Matrix:** [[93, 2, 8, 4, 8, 4, 1], [4, 96, 4, 2, 4, 3, 4], [3, 2, 77, 3, 3, 5, 3], [6, 2, 3, 71, 7, 4, 1], [4, 3, 8, 4, 78, 1, 0], [3, 2, 5, 4, 2, 99, 1], [12, 3, 14, 4, 5, 5, 75]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- **Top Confused Pairs:** [('G', 'C', 14), ('G', 'A', 12), ('A', 'C', 8), ('A', 'E', 8), ('E', 'C', 8), ('D', 'E', 7), ('D', 'A', 6), ('C', 'F', 5), ('F', 'C', 5), ('G', 'E', 5)]
- **True Class Distribution:** {'F': 116, 'A': 120, 'C': 96, 'G': 118, 'E': 98, 'B': 117, 'D': 94}
- **Pred Class Distribution:** {'F': 121, 'A': 125, 'C': 119, 'G': 85, 'E': 107, 'D': 92, 'B': 110}
- **Num Classes:** 7

