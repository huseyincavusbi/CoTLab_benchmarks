# Experiment: Radiology Standard Zero-Shot (PLAIN)

**Status:** Completed
**Started:** 2026-01-24 17:36:40  
**Duration:** 1 seconds

## Research Questions

1. Does the model perform well without few-shot examples (zero-shot)?
2. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Standard
**Few-Shot Examples:** No (zero-shot)
**Output Format:** PLAIN
**Dataset:** radiology

<details>
<summary>Full Configuration (YAML)</summary>

```yaml
backend:
  _target_: cotlab.backends.TransformersBackend
  device: cuda
  dtype: bfloat16
  enable_hooks: true
  trust_remote_code: true
  load_in_4bit: true
  bnb_4bit_quant_type: nf4
  bnb_4bit_compute_dtype: bfloat16
  bnb_4bit_use_double_quant: true
model:
  name: google/medgemma-4b-it
  variant: 4b
  max_new_tokens: 512
  temperature: 0.7
  top_p: 0.9
  safe_name: medgemma_4b
prompt:
  _target_: cotlab.prompts.RadiologyPromptStrategy
  name: radiology
  contrarian: false
  few_shot: false
  answer_first: false
  output_format: plain
dataset:
  _target_: cotlab.datasets.RadiologyDataset
  name: radiology
  path: data/radiology.json
experiment:
  _target_: cotlab.experiments.LogitLensExperiment
  name: logit_lens
  description: Visualize layer-by-layer token predictions
  top_k: 5
  question: The patient has fever and productive cough with shortness of breath for
    three days and elevated CRP.
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  experiment=logit_lens \
  prompt=radiology \
  prompt.few_shot=false \
  prompt.output_format=plain \
  dataset=radiology
```

## Results

- **Samples Processed:** 34
- **Final Prediction:** ```
- **Num Layers Analyzed:** 34
- **Emergence Layer:** 24
- **Emergence Rank:** 1

