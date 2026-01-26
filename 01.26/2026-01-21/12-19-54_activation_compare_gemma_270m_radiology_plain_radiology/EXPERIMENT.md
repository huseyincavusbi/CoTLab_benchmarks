# Experiment: Activation Compare: radiology vs medqa

**Status:** Completed
**Started:** 2026-01-21 12:20:04  
**Duration:** 1 seconds

## Research Questions

1. How do residual stream activations differ across runs and datasets?
2. Which layers show the largest activation divergence between runs?
3. Do activation differences align with task or prompt changes?

## Configuration

**Prompt Strategy:** Radiology
**Reasoning Mode:** Standard
**Few-Shot Examples:** Yes
**Output Format:** PLAIN
**Dataset:** radiology

**Variants:**
- radiology: dataset=radiology, prompt=radiology, samples=default, seed=default
- medqa: dataset={'_target_': 'cotlab.datasets.loaders.MedQADataset', 'name': 'medqa', 'filename': 'medqa/test.jsonl', 'split': 'test'}, prompt={'_target_': 'cotlab.prompts.mcq.MCQPromptStrategy', 'name': 'mcq', 'few_shot': True, 'output_format': 'plain', 'answer_first': False, 'contrarian': False}, samples=default, seed=default

<details>
<summary>Full Configuration (YAML)</summary>

```yaml
{OmegaConf.to_yaml(self.config)}
```
</details>

## Reproduce

```bash
{repro_cmd}
```

## Results

- **Samples Processed:** 1
- **Num Runs:** 2
- **Num Layers:** 18
- **Comparison Mode:** pairwise
- **Pooling:** last_token
- **Pair Count:** 1

