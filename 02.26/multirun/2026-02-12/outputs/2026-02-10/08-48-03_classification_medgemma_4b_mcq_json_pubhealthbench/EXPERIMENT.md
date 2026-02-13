# Experiment: Pubhealthbench Answer-First Zero-Shot

**Status:** Completed
**Started:** 2026-02-10 08:48:03  
**Duration:** 30 minutes 42 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** No (zero-shot)
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
  _target_: cotlab.datasets.loaders.PubHealthBenchDataset
  name: pubhealthbench
  split: reviewed
experiment:
  _target_: cotlab.experiments.ClassificationExperiment
  name: classification
  description: Classification from medical reports
  num_samples: 760
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=classification \
  experiment.num_samples=760 \
  prompt=mcq \
  prompt.answer_first=true \
  prompt.few_shot=false \
  dataset=pubhealthbench
```

## Results

- **Accuracy:** 74.7%
- **Samples Processed:** 760
- **Correct:** 568
- **Incorrect:** 192
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.696969696969697, 'recall': 0.7666666666666667, 'f1-score': 0.7301587301587301, 'support': 120.0}, 'B': {'precision': 0.7661290322580645, 'recall': 0.811965811965812, 'f1-score': 0.7883817427385892, 'support': 117.0}, 'C': {'precision': 0.6173913043478261, 'recall': 0.7395833333333334, 'f1-score': 0.6729857819905213, 'support': 96.0}, 'D': {'precision': 0.7764705882352941, 'recall': 0.7021276595744681, 'f1-score': 0.7374301675977654, 'support': 94.0}, 'E': {'precision': 0.8085106382978723, 'recall': 0.7755102040816326, 'f1-score': 0.7916666666666666, 'support': 98.0}, 'F': {'precision': 0.839622641509434, 'recall': 0.7672413793103449, 'f1-score': 0.8018018018018018, 'support': 116.0}, 'G': {'precision': 0.8061224489795918, 'recall': 0.6638655462184874, 'f1-score': 0.728110599078341, 'support': 119.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.7473684210526316, 'macro avg': {'precision': 0.6639020438247225, 'recall': 0.6533700751438432, 'f1-score': 0.656316936254052, 'support': 760.0}, 'weighted avg': {'precision': 0.7606448701564782, 'recall': 0.7473684210526316, 'f1-score': 0.7513451131281678, 'support': 760.0}}
- **Macro Precision:** 0.664
- **Macro Recall:** 0.653
- **Macro F1:** 0.656
- **Weighted F1:** 0.751
- **Confusion Matrix:** [[92, 5, 9, 1, 4, 2, 7, 0], [4, 95, 8, 1, 2, 1, 4, 2], [7, 5, 71, 3, 2, 5, 1, 2], [6, 7, 6, 66, 6, 2, 1, 0], [6, 2, 5, 4, 76, 2, 2, 1], [5, 5, 5, 6, 1, 89, 4, 1], [12, 5, 11, 4, 3, 5, 79, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T']
- **Top Confused Pairs:** [('G', 'A', 12), ('G', 'C', 11), ('A', 'C', 9), ('B', 'C', 8), ('A', 'G', 7), ('C', 'A', 7), ('D', 'B', 7), ('D', 'A', 6), ('D', 'C', 6), ('D', 'E', 6)]
- **True Class Distribution:** {'F': 116, 'A': 120, 'C': 96, 'G': 119, 'E': 98, 'B': 117, 'D': 94}
- **Pred Class Distribution:** {'F': 106, 'A': 132, 'C': 115, 'G': 98, 'D': 85, 'E': 94, 'B': 124, 'T': 6}
- **Num Classes:** 8

