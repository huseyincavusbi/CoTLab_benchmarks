# Experiment: Pubmedqa Contrarian (PLAIN)

**Status:** Running
**Started:** 2026-01-20 13:38:02

## Research Questions

1. Does skeptical/contrarian reasoning improve diagnostic accuracy?
2. How does PLAIN output format affect parsing and accuracy?

## Configuration

**Prompt Strategy:** Pubmedqa
**Reasoning Mode:** Contrarian (skeptical)
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** pubmedqa

<details>
<summary>Full Configuration (YAML)</summary>

```yaml
backend:
  _target_: cotlab.backends.TransformersBackend
  device: cpu
  dtype: bfloat16
  enable_hooks: true
  trust_remote_code: true
model:
  name: openai-community/gpt2
  variant: gpt2
  max_new_tokens: 256
  temperature: 0.7
  top_p: 0.9
  safe_name: gpt2
prompt:
  _target_: cotlab.prompts.pubmedqa.PubMedQAPromptStrategy
  name: pubmedqa
  output_format: plain
  few_shot: true
  answer_first: false
  contrarian: true
dataset:
  _target_: cotlab.datasets.loaders.PubMedQADataset
  name: pubmedqa
  filename: pubmedqa/test.jsonl
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
  num_samples: 1
seed: 42
verbose: true
dry_run: false

```
</details>

## Reproduce

```bash
python -m cotlab.main \
  prompt=pubmedqa \
  prompt.contrarian=true \
  prompt.output_format=plain \
  dataset=pubmedqa
```

## Results

_Results will be added after experiment completes..._
