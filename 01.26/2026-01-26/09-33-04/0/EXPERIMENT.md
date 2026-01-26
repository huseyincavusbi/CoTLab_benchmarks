# Experiment: Tcga Answer-First

**Status:** Completed
**Started:** 2026-01-26 09:33:04  
**Duration:** 5 minutes 47 seconds

## Research Questions

1. Does "answer first, then justify" reasoning order affect performance?

## Configuration

**Prompt Strategy:** Tcga
**Reasoning Mode:** Answer-First
**Few-Shot Examples:** Yes
**Output Format:** JSON
**Dataset:** tcga

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
  _target_: cotlab.prompts.tcga.TCGAPromptStrategy
  name: tcga
  few_shot: true
  answer_first: true
  contrarian: false
  output_format: json
dataset:
  _target_: cotlab.datasets.loaders.TCGADataset
  name: tcga
  reports_filename: tcga/TCGA_Reports.csv
  labels_filename: tcga/tcga_patient_to_cancer_type.csv
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
  prompt=tcga \
  prompt.answer_first=true \
  dataset=tcga
```

## Results

- **Accuracy:** 85.1%
- **Samples Processed:** 1415
- **Correct:** 1202
- **Incorrect:** 211
- **Parse Errors:** 2
- **Parse Error Rate:** 0.001
- **Classification Report:** {'ACC': {'precision': 1.0, 'recall': 0.15384615384615385, 'f1-score': 0.26666666666666666, 'support': 13.0}, 'ADRE': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'BLCA': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 56.0}, 'BRCA': {'precision': 0.9935483870967742, 'recall': 0.9935483870967742, 'f1-score': 0.9935483870967742, 'support': 155.0}, 'CESC': {'precision': 1.0, 'recall': 0.9534883720930233, 'f1-score': 0.9761904761904762, 'support': 43.0}, 'CHOL': {'precision': 0.8571428571428571, 'recall': 1.0, 'f1-score': 0.9230769230769231, 'support': 6.0}, 'COAD': {'precision': 0.7294117647058823, 'recall': 1.0, 'f1-score': 0.8435374149659864, 'support': 62.0}, 'DLBC': {'precision': 1.0, 'recall': 0.8571428571428571, 'f1-score': 0.9230769230769231, 'support': 7.0}, 'ESCA': {'precision': 0.8076923076923077, 'recall': 1.0, 'f1-score': 0.8936170212765957, 'support': 21.0}, 'GBM': {'precision': 0.5673076923076923, 'recall': 1.0, 'f1-score': 0.7239263803680982, 'support': 59.0}, 'HNSC': {'precision': 1.0, 'recall': 0.9871794871794872, 'f1-score': 0.9935483870967742, 'support': 78.0}, 'KICH': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 16.0}, 'KIRC': {'precision': 0.5777777777777777, 'recall': 1.0, 'f1-score': 0.7323943661971831, 'support': 78.0}, 'KIRP': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 42.0}, 'LGG': {'precision': 1.0, 'recall': 0.3382352941176471, 'f1-score': 0.5054945054945055, 'support': 68.0}, 'LIHC': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 51.0}, 'LUAD': {'precision': 0.8372093023255814, 'recall': 0.9863013698630136, 'f1-score': 0.9056603773584906, 'support': 73.0}, 'LUSC': {'precision': 0.9824561403508771, 'recall': 0.8, 'f1-score': 0.8818897637795275, 'support': 70.0}, 'MESO': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 11.0}, 'N/A': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'NOS': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'OV': {'precision': 0.9454545454545454, 'recall': 0.9454545454545454, 'f1-score': 0.9454545454545454, 'support': 55.0}, 'PAAD': {'precision': 1.0, 'recall': 0.8846153846153846, 'f1-score': 0.9387755102040817, 'support': 26.0}, 'PANCAN': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'PCPG': {'precision': 0.875, 'recall': 0.5384615384615384, 'f1-score': 0.6666666666666666, 'support': 26.0}, 'PHEO': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'PRAD': {'precision': 0.9850746268656716, 'recall': 1.0, 'f1-score': 0.9924812030075187, 'support': 66.0}, 'READ': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 24.0}, 'SARC': {'precision': 1.0, 'recall': 0.8378378378378378, 'f1-score': 0.9117647058823529, 'support': 37.0}, 'SKCM': {'precision': 1.0, 'recall': 0.9333333333333333, 'f1-score': 0.9655172413793104, 'support': 15.0}, 'STAD': {'precision': 0.9607843137254902, 'recall': 0.9074074074074074, 'f1-score': 0.9333333333333333, 'support': 54.0}, 'TGCT': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 13.0}, 'THCA': {'precision': 0.8795180722891566, 'recall': 1.0, 'f1-score': 0.9358974358974359, 'support': 73.0}, 'THYM': {'precision': 1.0, 'recall': 0.4117647058823529, 'f1-score': 0.5833333333333334, 'support': 17.0}, 'UCEC': {'precision': 0.8478260869565217, 'recall': 0.9629629629629629, 'f1-score': 0.9017341040462428, 'support': 81.0}, 'UCS': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 8.0}, 'UVE': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'UVM': {'precision': 1.0, 'recall': 0.7777777777777778, 'f1-score': 0.875, 'support': 9.0}, 'Unknown': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'adrenocortical carcinoma': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.8506723283793347, 'macro avg': {'precision': 0.6461550968672783, 'recall': 0.6067339353768024, 'f1-score': 0.6053146417962436, 'support': 1413.0}, 'weighted avg': {'precision': 0.8480396072598777, 'recall': 0.8506723283793347, 'f1-score': 0.8280809579277877, 'support': 1413.0}}
- **Macro Precision:** 0.646
- **Macro Recall:** 0.607
- **Macro F1:** 0.605
- **Weighted F1:** 0.828
- **Confusion Matrix:** [[2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 154, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 62, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 59, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 77, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 0, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 72, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 66, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 73, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 7, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 78, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 7, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['ACC', 'ADRE', 'BLCA', 'BRCA', 'CESC', 'CHOL', 'COAD', 'DLBC', 'ESCA', 'GBM', 'HNSC', 'KICH', 'KIRC', 'KIRP', 'LGG', 'LIHC', 'LUAD', 'LUSC', 'MESO', 'N/A', 'NOS', 'OV', 'PAAD', 'PANCAN', 'PCPG', 'PHEO', 'PRAD', 'READ', 'SARC', 'SKCM', 'STAD', 'TGCT', 'THCA', 'THYM', 'UCEC', 'UCS', 'UVE', 'UVM', 'Unknown', 'adrenocortical carcinoma']
- **Top Confused Pairs:** [('LGG', 'GBM', 45), ('KIRP', 'KIRC', 41), ('READ', 'COAD', 22), ('KICH', 'KIRC', 16), ('LUSC', 'LUAD', 14), ('PCPG', 'PHEO', 12), ('THYM', 'THCA', 10), ('UCS', 'UCEC', 8), ('ACC', 'ADRE', 6), ('ACC', 'adrenocortical carcinoma', 5)]
- **True Class Distribution:** {'ACC': 13, 'BLCA': 56, 'BRCA': 155, 'CESC': 43, 'CHOL': 6, 'COAD': 62, 'DLBC': 7, 'ESCA': 21, 'GBM': 59, 'HNSC': 78, 'KICH': 16, 'KIRC': 78, 'KIRP': 42, 'LGG': 68, 'LIHC': 51, 'LUAD': 73, 'LUSC': 70, 'MESO': 11, 'OV': 55, 'PAAD': 26, 'PCPG': 26, 'PRAD': 66, 'READ': 24, 'SARC': 37, 'SKCM': 15, 'STAD': 54, 'TGCT': 13, 'THCA': 73, 'THYM': 17, 'UCEC': 81, 'UCS': 8, 'UVM': 9}
- **Pred Class Distribution:** {'adrenocortical carcinoma': 5, 'ACC': 2, 'ADRE': 6, 'BLCA': 56, 'BRCA': 155, 'NOS': 1, 'CESC': 41, 'UCEC': 92, 'CHOL': 7, 'COAD': 85, 'DLBC': 6, 'STAD': 51, 'ESCA': 26, 'GBM': 104, 'HNSC': 77, 'LUSC': 57, 'KIRC': 135, 'LGG': 23, 'LIHC': 51, 'LUAD': 86, 'N/A': 2, 'MESO': 11, 'OV': 55, 'Unknown': 1, 'PAAD': 23, 'PCPG': 16, 'PANCAN': 1, 'PHEO': 12, 'PRAD': 67, 'SARC': 31, 'UCS': 3, 'SKCM': 14, 'TGCT': 13, 'THCA': 83, 'THYM': 7, 'UVM': 7, 'UVE': 1}
- **Num Classes:** 40

