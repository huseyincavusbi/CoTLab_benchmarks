# Experiment: Medxpertqa Answer-First

**Status:** Completed
**Started:** 2026-01-27 16:30:10  
**Duration:** 38 minutes 56 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Mcq
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** medxpertqa

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
  name: google/medgemma-27b-text-it
  variant: 27b-text
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_27b_text_it
prompt:
  _target_: cotlab.prompts.mcq.MCQPromptStrategy
  name: mcq
  few_shot: true
  output_format: json
  answer_first: true
  contrarian: false
dataset:
  _target_: cotlab.datasets.loaders.MedQADataset
  name: medxpertqa
  filename: medxpertqa/test.jsonl
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
  dataset=medxpertqa
```

## Results

- **Accuracy:** 10.1%
- **Samples Processed:** 2450
- **Correct:** 223
- **Incorrect:** 1983
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'A': {'precision': 0.10628019323671498, 'recall': 0.20465116279069767, 'f1-score': 0.13990461049284578, 'support': 215.0}, 'B': {'precision': 0.10232558139534884, 'recall': 0.09606986899563319, 'f1-score': 0.0990990990990991, 'support': 229.0}, 'C': {'precision': 0.09926470588235294, 'recall': 0.12442396313364056, 'f1-score': 0.11042944785276074, 'support': 217.0}, 'D': {'precision': 0.1223021582733813, 'recall': 0.14977973568281938, 'f1-score': 0.13465346534653466, 'support': 227.0}, 'E': {'precision': 0.112, 'recall': 0.11715481171548117, 'f1-score': 0.11451942740286299, 'support': 239.0}, 'F': {'precision': 0.12807881773399016, 'recall': 0.12093023255813953, 'f1-score': 0.12440191387559808, 'support': 215.0}, 'G': {'precision': 0.1223021582733813, 'recall': 0.07112970711297072, 'f1-score': 0.08994708994708994, 'support': 239.0}, 'H': {'precision': 0.14432989690721648, 'recall': 0.07291666666666667, 'f1-score': 0.09688581314878893, 'support': 192.0}, 'I': {'precision': 0.08823529411764706, 'recall': 0.029556650246305417, 'f1-score': 0.04428044280442804, 'support': 203.0}, 'J': {'precision': 0.07352941176470588, 'recall': 0.021739130434782608, 'f1-score': 0.03355704697986577, 'support': 230.0}, 'K': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'L': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'M': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'N': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'O': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'P': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Q': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'R': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'S': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'T': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'U': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'V': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'W': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'X': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Y': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'Z': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.10108794197642793, 'macro avg': {'precision': 0.04225570067633611, 'recall': 0.0387827665129668, 'f1-score': 0.0379876291134567, 'support': 2206.0}, 'weighted avg': {'precision': 0.1095448150716469, 'recall': 0.10108794197642793, 'f1-score': 0.09892372969922748, 'support': 2206.0}}
- **Macro Precision:** 0.042
- **Macro Recall:** 0.039
- **Macro F1:** 0.038
- **Weighted F1:** 0.099
- **Confusion Matrix:** [[44, 21, 32, 32, 19, 17, 7, 8, 5, 14, 0, 10, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 2, 0, 0], [43, 22, 27, 28, 21, 29, 14, 12, 6, 8, 2, 5, 0, 0, 0, 1, 1, 0, 1, 2, 0, 1, 0, 5, 0, 1], [40, 19, 27, 30, 24, 23, 16, 10, 7, 3, 2, 6, 0, 1, 0, 0, 1, 0, 0, 0, 0, 2, 0, 4, 2, 0], [43, 18, 25, 34, 33, 17, 15, 11, 9, 3, 1, 5, 0, 2, 0, 0, 0, 2, 0, 5, 1, 1, 0, 2, 0, 0], [42, 30, 26, 31, 28, 16, 13, 12, 13, 7, 2, 5, 0, 0, 0, 3, 1, 2, 1, 2, 0, 0, 0, 4, 1, 0], [37, 17, 31, 23, 20, 26, 19, 5, 2, 5, 5, 5, 1, 0, 1, 0, 0, 1, 3, 1, 1, 2, 0, 10, 0, 0], [47, 29, 31, 19, 24, 27, 17, 10, 9, 5, 1, 10, 0, 1, 1, 2, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0], [31, 20, 17, 21, 26, 15, 15, 14, 5, 8, 2, 3, 0, 2, 0, 0, 0, 3, 3, 1, 0, 1, 0, 5, 0, 0], [41, 13, 24, 35, 23, 11, 11, 8, 6, 10, 5, 4, 1, 1, 0, 0, 1, 1, 3, 1, 0, 0, 1, 2, 1, 0], [46, 26, 32, 25, 32, 22, 12, 7, 6, 5, 4, 4, 0, 1, 0, 1, 0, 0, 0, 3, 0, 1, 0, 3, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
- **Top Confused Pairs:** [('G', 'A', 47), ('J', 'A', 46), ('B', 'A', 43), ('D', 'A', 43), ('E', 'A', 42), ('I', 'A', 41), ('C', 'A', 40), ('F', 'A', 37), ('I', 'D', 35), ('D', 'E', 33)]
- **True Class Distribution:** {'E': 239, 'C': 217, 'H': 192, 'F': 215, 'B': 229, 'D': 227, 'I': 203, 'G': 239, 'A': 215, 'J': 230}
- **Pred Class Distribution:** {'B': 215, 'A': 414, 'G': 139, 'J': 68, 'H': 97, 'S': 12, 'C': 272, 'F': 203, 'D': 278, 'E': 250, 'K': 24, 'U': 2, 'L': 57, 'X': 40, 'R': 13, 'O': 2, 'T': 16, 'Z': 1, 'I': 68, 'V': 8, 'P': 7, 'W': 1, 'Q': 4, 'Y': 4, 'N': 9, 'M': 2}
- **Num Classes:** 26

