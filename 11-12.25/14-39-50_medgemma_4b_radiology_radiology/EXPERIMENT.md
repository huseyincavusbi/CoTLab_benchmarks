# Experiment: Radiology Standard (PLAIN)

**Status:** Completed
**Started:** 2026-01-09 14:39:50  
**Duration:** 12 seconds

## Research Questions

1. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** radiology

<details>
<summary>Full Configuration (YAML)</summary>

```yaml
backend:
  _target_: cotlab.backends.VLLMBackend
  tensor_parallel_size: 1
  dtype: bfloat16
  trust_remote_code: true
  max_model_len: 4096
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
  few_shot: true
  answer_first: false
  output_format: plain
dataset:
  _target_: cotlab.datasets.RadiologyDataset
  name: radiology
  path: data/radiology.json
experiment:
  _target_: cotlab.experiments.CoTFaithfulnessExperiment
  name: cot_faithfulness
  description: Test whether Chain of Thought reflects true model reasoning
  tests:
  - bias_influence
  - causal_intervention
  - counterfactual
  metrics:
  - bias_acknowledgment_rate
  - intervention_consistency
  - answer_cot_alignment
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  prompt=radiology \
  prompt.output_format=plain \
  dataset=radiology
```

## Results

- **Samples Processed:** 100
- **Cot Direct Agreement:** 0
- **Cot Direct Disagreement:** 100
- **Avg Reasoning Length:** 36.080
- **Reasoning Contains Keywords:** 0
- **Agreement Rate:** 0.000
- **Disagreement Rate:** 1.000
- **Keyword Mention Rate:** 0.000

