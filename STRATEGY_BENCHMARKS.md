# Strategy Benchmarks

Performance of each prompt strategy across all models.

## Summary Heatmap

| Prompt | MedGemma 27B | MedGemma 4B | DeepSeek-R1 | Olmo 3.1 | Olmo 3 | Nemotron | Ministral |
|--------|--------------|-------------|-------------|----------|--------|----------|-----------|
| contrarian | **82%** | 63% | 37% | 35% | **46%** | 34% | 47% |
| direct_answer | **78%** | **72%** | 14% | 24% | 31% | 39% | **60%** |
| expert_persona | 76% | 53% | 18% | 8% | 13% | **74%** | 42% |
| few_shot | 75% | 21% | 28% | 27% | 32% | **67%** | 33% |
| arrogance | 63% | 45% | 37% | 18% | 28% | 42% | 54% |
| chain_of_thought | 25% | **63%** | 10% | **51%** | 36% | 37% | 40% |
| no_instruction | 31% | 53% | 9% | 16% | 16% | 56% | 22% |
| adversarial | 28% | 38% | 13% | 2% | 2% | 1% | 10% |
| sycophantic | 17% | 30% | 30% | 5% | 8% | 57% | 9% |
| simple | 12% | 58% | 35% | 35% | 43% | 42% | 37% |
| socratic | 8% | 50% | **46%** | 21% | 19% | 48% | 42% |
| uncertainty | 6% | 34% | 8% | 13% | 21% | 48% | 17% |
| radiology | 0% | 1% | 0% | 3% | 3% | 2% | 0% |

> Note: Values show **CoT Accuracy** (not Direct Accuracy).

---

## MedGemma 27B

| Prompt | CoT Acc | Direct Acc | Δ |
|--------|---------|------------|---|
| contrarian | **82%** | 79% | +3% |
| direct_answer | 78% | 76% | +2% |
| expert_persona | 76% | 80% | -4% |
| few_shot | 75% | 77% | -2% |
| arrogance | 63% | 79% | -16% |
| no_instruction | 31% | 77% | -46% |
| adversarial | 28% | 78% | -50% |
| chain_of_thought | 25% | 78% | **-53%** |
| sycophantic | 17% | 76% | -59% |
| simple | 12% | 76% | -64% |
| socratic | 8% | 80% | **-72%** |
| uncertainty | 6% | 77% | -71% |
| radiology | 0% | 75% | -75% |

**Best**: `contrarian` (82%)  
**Worst**: `socratic`, `uncertainty`

---

## MedGemma 4B

| Prompt | CoT Acc | Direct Acc | Δ |
|--------|---------|------------|---|
| direct_answer | **72%** | 68% | +4% |
| chain_of_thought | 63% | 66% | -3% |
| contrarian | 63% | 61% | +2% |
| simple | 58% | 68% | -10% |
| no_instruction | 53% | 68% | -15% |
| expert_persona | 53% | 62% | -9% |
| socratic | 50% | 71% | -21% |
| arrogance | 45% | 63% | -18% |
| adversarial | 38% | 69% | -31% |
| uncertainty | 34% | 65% | -31% |
| sycophantic | 30% | 59% | -29% |
| few_shot | 21% | 67% | -46% |
| radiology | 1% | 66% | -65% |


---

## DeepSeek-R1 32B

| Prompt | CoT Acc | Direct Acc | Δ |
|--------|---------|------------|---|
| socratic | **46%** | 15% | **+31%** |
| arrogance | 37% | 15% | +22% |
| contrarian | 37% | 13% | +24% |
| simple | 35% | 15% | +20% |
| sycophantic | 30% | 17% | +13% |
| few_shot | 28% | 13% | +15% |
| expert_persona | 18% | 13% | +5% |
| direct_answer | 14% | 16% | -2% |
| adversarial | 13% | 17% | -4% |
| chain_of_thought | 10% | 8% | +2% |
| no_instruction | 9% | 13% | -4% |
| uncertainty | 8% | 15% | -7% |
| radiology | 0% | 14% | -14% |

**Best**: `socratic` (46%)  
**CoT helps on most prompts!**

---

## Olmo 3.1 32B Think

| Prompt | CoT Acc | Direct Acc | Δ |
|--------|---------|------------|---|
| chain_of_thought | **51%** | 5% | **+46%** |
| simple | 35% | 6% | +29% |
| contrarian | 35% | 6% | +29% |
| few_shot | 27% | 5% | +22% |
| direct_answer | 24% | 8% | +16% |
| socratic | 21% | 8% | +13% |
| arrogance | 18% | 5% | +13% |
| no_instruction | 16% | 2% | +14% |
| uncertainty | 13% | 6% | +7% |
| expert_persona | 8% | 3% | +5% |
| sycophantic | 5% | 4% | +1% |
| radiology | 3% | 3% | 0% |
| adversarial | 2% | 4% | -2% |

**Best**: `chain_of_thought` (51%)  
**CoT essential for this model! But it needs medical fine tuning.**

---

## Olmo 3 32B Think

| Prompt | CoT Acc | Direct Acc | Δ |
|--------|---------|------------|---|
| contrarian | **46%** | 7% | +39% |
| simple | 43% | 5% | +38% |
| chain_of_thought | 36% | 4% | +32% |
| few_shot | 32% | 6% | +26% |
| direct_answer | 31% | 7% | +24% |
| arrogance | 28% | 5% | +23% |
| uncertainty | 21% | 6% | +15% |
| socratic | 19% | 6% | +13% |
| no_instruction | 16% | 4% | +12% |
| expert_persona | 13% | 7% | +6% |
| sycophantic | 8% | 3% | +5% |
| radiology | 3% | 4% | -1% |
| adversarial | 2% | 7% | -5% |


---

## Nemotron 30B

| Prompt | CoT Acc | Direct Acc | Δ |
|--------|---------|------------|---|
| expert_persona | **74%** | 36% | +38% |
| few_shot | 67% | 38% | +29% |
| sycophantic | 57% | 39% | +18% |
| no_instruction | 56% | 32% | +24% |
| socratic | 48% | 30% | +18% |
| uncertainty | 48% | 34% | +14% |
| simple | 42% | 35% | +7% |
| arrogance | 42% | 33% | +9% |
| direct_answer | 39% | 31% | +8% |
| chain_of_thought | 37% | 32% | +5% |
| contrarian | 34% | 35% | -1% |
| radiology | 2% | 43% | -41% |
| adversarial | 1% | 38% | -37% |


---

## Ministral 14B

| Prompt | CoT Acc | Direct Acc | Δ |
|--------|---------|------------|---|
| direct_answer | **60%** | 61% | -1% |
| arrogance | 54% | 58% | -4% |
| contrarian | 47% | 69% | -22% |
| socratic | 42% | 61% | -19% |
| expert_persona | 42% | 61% | -19% |
| chain_of_thought | 40% | 62% | -22% |
| simple | 37% | 55% | -18% |
| few_shot | 33% | 61% | -28% |
| no_instruction | 22% | 59% | -37% |
| uncertainty | 17% | 54% | -37% |
| adversarial | 10% | 57% | -47% |
| sycophantic | 9% | 62% | -53% |
| radiology | 0% | 61% | -61% |

**Best**: `direct_answer` (60%)  
**CoT hurts on most prompts**

---

## Key Insights

### Best Strategies by Model Type

| Model Type | Best Strategy | Why |
|------------|--------------|-----|
| **MedGemma 27B** | `contrarian` (82%) | Forces answer first, then reasoning |
| **MedGemma 4B** | `direct_answer` (72%) | Skip reasoning entirely |
| **Reasoning Models** | `chain_of_thought` (51% on Olmo 3.1) | They're trained for it |
| **Nemotron** | `expert_persona` (74%) | Persona helps |

### Worst Strategies

1. **`adversarial`** - Hostile prompts hurt most models
2. **`uncertainty`** - Forcing doubt reduces accuracy
