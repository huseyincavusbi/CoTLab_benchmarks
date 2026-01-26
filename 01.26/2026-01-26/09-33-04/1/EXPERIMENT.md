# Experiment: Tcga Standard

**Status:** Completed
**Started:** 2026-01-26 09:39:57  
**Duration:** 6 minutes 30 seconds

## Research Questions

1. Standard baseline experiment for comparison.

## Configuration

**Prompt Strategy:** Tcga
**Reasoning Mode:** Standard
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
  answer_first: false
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
  dataset=tcga
```

## Results

- **Accuracy:** 83.5%
- **Samples Processed:** 1415
- **Correct:** 1181
- **Incorrect:** 234
- **Parse Errors:** 0
- **Parse Error Rate:** 0.000
- **Classification Report:** {'ACC': {'precision': 1.0, 'recall': 0.07692307692307693, 'f1-score': 0.14285714285714285, 'support': 13.0}, 'ACCA': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'ADRC': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'ADRE': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'BLCA': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 56.0}, 'BRCA': {'precision': 0.9935483870967742, 'recall': 0.9935483870967742, 'f1-score': 0.9935483870967742, 'support': 155.0}, 'CESC': {'precision': 0.975609756097561, 'recall': 0.9302325581395349, 'f1-score': 0.9523809523809523, 'support': 43.0}, 'CHOL': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 6.0}, 'COAD': {'precision': 0.7294117647058823, 'recall': 1.0, 'f1-score': 0.8435374149659864, 'support': 62.0}, 'Cervical Cancer': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'DLBC': {'precision': 1.0, 'recall': 0.8571428571428571, 'f1-score': 0.9230769230769231, 'support': 7.0}, 'ESCA': {'precision': 0.84, 'recall': 1.0, 'f1-score': 0.9130434782608695, 'support': 21.0}, 'GBM': {'precision': 0.6145833333333334, 'recall': 1.0, 'f1-score': 0.7612903225806451, 'support': 59.0}, 'HNSC': {'precision': 0.975, 'recall': 1.0, 'f1-score': 0.9873417721518988, 'support': 78.0}, 'KICH': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 16.0}, 'KIRC': {'precision': 0.5777777777777777, 'recall': 1.0, 'f1-score': 0.7323943661971831, 'support': 78.0}, 'KIRP': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 42.0}, 'LGG': {'precision': 1.0, 'recall': 0.4714285714285714, 'f1-score': 0.6407766990291263, 'support': 70.0}, 'LIHC': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 51.0}, 'LUAD': {'precision': 0.5806451612903226, 'recall': 0.9863013698630136, 'f1-score': 0.7309644670050761, 'support': 73.0}, 'LUSC': {'precision': 1.0, 'recall': 0.2571428571428571, 'f1-score': 0.4090909090909091, 'support': 70.0}, 'MESO': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 11.0}, 'N/A': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'NOS': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'NULL': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'OV': {'precision': 0.9629629629629629, 'recall': 0.9454545454545454, 'f1-score': 0.9541284403669725, 'support': 55.0}, 'PAAD': {'precision': 1.0, 'recall': 0.9230769230769231, 'f1-score': 0.96, 'support': 26.0}, 'PANCAN': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'PCPG': {'precision': 0.9230769230769231, 'recall': 0.46153846153846156, 'f1-score': 0.6153846153846154, 'support': 26.0}, 'PHEO': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'PRAD': {'precision': 0.9850746268656716, 'recall': 1.0, 'f1-score': 0.9924812030075187, 'support': 66.0}, 'READ': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 24.0}, 'SARC': {'precision': 1.0, 'recall': 0.8108108108108109, 'f1-score': 0.8955223880597015, 'support': 37.0}, 'SKCM': {'precision': 1.0, 'recall': 0.9333333333333333, 'f1-score': 0.9655172413793104, 'support': 15.0}, 'STAD': {'precision': 0.9615384615384616, 'recall': 0.9259259259259259, 'f1-score': 0.9433962264150944, 'support': 54.0}, 'TGCT': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 13.0}, 'THCA': {'precision': 0.948051948051948, 'recall': 1.0, 'f1-score': 0.9733333333333334, 'support': 73.0}, 'THYM': {'precision': 1.0, 'recall': 0.7647058823529411, 'f1-score': 0.8666666666666667, 'support': 17.0}, 'UCEC': {'precision': 0.8681318681318682, 'recall': 0.9753086419753086, 'f1-score': 0.9186046511627907, 'support': 81.0}, 'UCS': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 8.0}, 'UVM': {'precision': 1.0, 'recall': 1.0, 'f1-score': 1.0, 'support': 9.0}, 'adrenal cortical carcinoma': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'adrenocortical carcinoma': {'precision': 0.0, 'recall': 0.0, 'f1-score': 0.0, 'support': 0.0}, 'accuracy': 0.8346289752650177, 'macro avg': {'precision': 0.6031491388588253, 'recall': 0.565415679121045, 'f1-score': 0.5608218046620812, 'support': 1415.0}, 'weighted avg': {'precision': 0.8431140408601657, 'recall': 0.8346289752650177, 'f1-score': 0.808725040113454, 'support': 1415.0}}
- **Macro Precision:** 0.603
- **Macro Recall:** 0.565
- **Macro F1:** 0.561
- **Weighted F1:** 0.809
- **Confusion Matrix:** [[1, 1, 1, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 154, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 40, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 62, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 59, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 37, 0, 0, 0, 0, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 72, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 52, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 66, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 1, 4, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 73, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 13, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 79, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- **Class Labels:** ['ACC', 'ACCA', 'ADRC', 'ADRE', 'BLCA', 'BRCA', 'CESC', 'CHOL', 'COAD', 'Cervical Cancer', 'DLBC', 'ESCA', 'GBM', 'HNSC', 'KICH', 'KIRC', 'KIRP', 'LGG', 'LIHC', 'LUAD', 'LUSC', 'MESO', 'N/A', 'NOS', 'NULL', 'OV', 'PAAD', 'PANCAN', 'PCPG', 'PHEO', 'PRAD', 'READ', 'SARC', 'SKCM', 'STAD', 'TGCT', 'THCA', 'THYM', 'UCEC', 'UCS', 'UVM', 'adrenal cortical carcinoma', 'adrenocortical carcinoma']
- **Top Confused Pairs:** [('LUSC', 'LUAD', 52), ('KIRP', 'KIRC', 41), ('LGG', 'GBM', 37), ('READ', 'COAD', 22), ('KICH', 'KIRC', 16), ('PCPG', 'PHEO', 14), ('UCS', 'UCEC', 8), ('ACC', 'ADRE', 6), ('SARC', 'UCS', 4), ('STAD', 'ESCA', 4)]
- **True Class Distribution:** {'ACC': 13, 'BLCA': 56, 'BRCA': 155, 'CESC': 43, 'CHOL': 6, 'COAD': 62, 'DLBC': 7, 'ESCA': 21, 'GBM': 59, 'HNSC': 78, 'KICH': 16, 'KIRC': 78, 'KIRP': 42, 'LGG': 70, 'LIHC': 51, 'LUAD': 73, 'LUSC': 70, 'MESO': 11, 'OV': 55, 'PAAD': 26, 'PCPG': 26, 'PRAD': 66, 'READ': 24, 'SARC': 37, 'SKCM': 15, 'STAD': 54, 'TGCT': 13, 'THCA': 73, 'THYM': 17, 'UCEC': 81, 'UCS': 8, 'UVM': 9}
- **Pred Class Distribution:** {'adrenal cortical carcinoma': 1, 'ADRE': 6, 'ACC': 1, 'adrenocortical carcinoma': 3, 'ACCA': 1, 'ADRC': 1, 'BLCA': 56, 'BRCA': 155, 'NOS': 1, 'CESC': 41, 'UCEC': 91, 'Cervical Cancer': 1, 'CHOL': 6, 'COAD': 85, 'DLBC': 6, 'STAD': 52, 'ESCA': 25, 'GBM': 96, 'HNSC': 80, 'KIRC': 135, 'LGG': 33, 'LIHC': 51, 'LUAD': 124, 'NULL': 1, 'LUSC': 18, 'MESO': 11, 'OV': 54, 'N/A': 1, 'PAAD': 24, 'PCPG': 13, 'PANCAN': 1, 'PHEO': 14, 'PRAD': 67, 'SARC': 30, 'UCS': 4, 'SKCM': 14, 'TGCT': 13, 'THCA': 77, 'THYM': 13, 'UVM': 9}
- **Num Classes:** 43

