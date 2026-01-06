# MedGemma JSON Output Experiment - Final Results (December 31, 2025)

> **With Fixed JSON Output Support for ALL Prompt Strategies**

## Key Change: JSON Now Works Everywhere

Before this fix, only 2/12 prompts (`chain_of_thought`, `direct_answer`) supported JSON output.  
Now ALL 12 prompts properly append JSON instructions when `json_output=true`.

---

## JSON Compliance (Fixed Code)

| Model | Valid JSON | Malformed | Empty | Pure Text |
|-------|------------|-----------|-------|-----------|
| **27B** | **91.3%** | 0.2% | 8.3% | 0.3% |
| **4B** | **96.5%** | 0.2% | 2.6% | 0.6% |

**Before fix**: ~18% valid JSON (only 2 prompts worked)  
**After fix**: ~91-96% valid JSON (all 12 prompts work)

---

## MedGemma 27B: JSON vs Plain Text

### Overall

| Metric | JSON | Plain | Difference |
|--------|------|-------|------------|
| **CoT Accuracy** | **49.5%** | 38.4% | **+11.1%** ✅ |
| Direct Accuracy | 59.5% | 59.6% | -0.1% |

### By Prompt Strategy

| Prompt | JSON | Plain | Δ | Winner |
|--------|------|-------|---|--------|
| simple | **61.7%** | 23.0% | **+38.7%** | JSON |
| chain_of_thought | **60.3%** | 24.0% | **+36.3%** | JSON |
| adversarial | **62.3%** | 30.7% | **+31.7%** | JSON |
| no_instruction | **60.7%** | 30.0% | **+30.7%** | JSON |
| uncertainty | **39.3%** | 11.0% | **+28.3%** | JSON |
| arrogance | **61.3%** | 42.7% | **+18.7%** | JSON |
| sycophantic | **42.0%** | 27.0% | **+15.0%** | JSON |
| direct_answer | **61.7%** | 60.3% | +1.3% | JSON |
| socratic | 8.0% | 9.0% | -1.0% | ~Same |
| few_shot | 35.3% | **47.7%** | -12.3% | Plain |
| expert_persona | 51.3% | **72.0%** | -20.7% | Plain |
| **contrarian** | 50.3% | **84.0%** | **-33.7%** | **Plain** |

**8/12 prompts benefit from JSON**

---

## MedGemma 4B: JSON vs Plain Text

### Overall

| Metric | JSON | Plain | Difference |
|--------|------|-------|------------|
| **CoT Accuracy** | 32.3% | **43.8%** | **-11.5%** ❌ |
| Direct Accuracy | 53.2% | 53.3% | -0.1% |

### By Prompt Strategy

| Prompt | JSON | Plain | Δ | Winner |
|--------|------|-------|---|--------|
| few_shot | **44.7%** | 20.7% | **+24.0%** | JSON |
| arrogance | **43.7%** | 37.7% | +6.0% | JSON |
| no_instruction | 42.7% | 41.7% | +1.0% | ~Same |
| direct_answer | 51.0% | 52.3% | -1.3% | ~Same |
| sycophantic | 15.0% | 17.7% | -2.7% | ~Same |
| adversarial | 33.7% | 37.0% | -3.3% | Plain |
| chain_of_thought | 40.7% | **54.3%** | -13.7% | Plain |
| uncertainty | 22.7% | **44.7%** | -22.0% | Plain |
| socratic | 19.3% | **46.0%** | -26.7% | Plain |
| expert_persona | 30.0% | **61.7%** | -31.7% | Plain |
| simple | 12.0% | **45.0%** | -33.0% | Plain |
| **contrarian** | 32.7% | **67.3%** | **-34.7%** | **Plain** |

**Only 2/12 prompts benefit from JSON**

---

## Contrarian: Always Best with Plain Text

| Model | JSON | Plain | Δ |
|-------|------|-------|---|
| **27B** | 50.3% | **84.0%** | -33.7% |
| **4B** | 32.7% | **67.3%** | -34.7% |

**Contrarian loses ~34% accuracy when forced to use JSON format!**

---

## Summary Table

| Model | Format | Best Prompt | Accuracy |
|-------|--------|-------------|----------|
| **27B** | **JSON** | simple/adversarial/CoT | ~61% |
| **27B** | **Plain** | **contrarian** | **84%** 🏆 |
| **4B** | JSON | direct_answer | 51% |
| **4B** | **Plain** | **contrarian** | **67%** 🏆 |

---

## Key Findings

### 1. JSON Fix Was Critical
- Before: 17-18% JSON compliance (only 2 prompts worked)
- After: 91-96% JSON compliance (all prompts work)

### 2. Model Size Determines JSON Benefit
- **27B**: JSON +11.1% (8/12 prompts benefit)
- **4B**: JSON -11.5% (only 2/12 prompts benefit)

### 3. Contrarian Hates JSON
- Loses ~34% accuracy in both 27B and 4B
- Plain text = best contrarian performance

### 4. Practical Recommendations

| Use Case | Recommendation |
|----------|----------------|
| **Maximum accuracy** | 27B + Plain + Contrarian = **84%** |
| **Need JSON output** | 27B + JSON + simple/adversarial/CoT = ~61% |
| **Using 4B** | Plain + Contrarian = **67%** (avoid JSON) |
| **Avoid** | 4B + JSON + simple = 12% (worst combo) |

---

## Files

- `09-46-01_medgemma_27b_text_it_vllm_json/` - 27B JSON run
- `10-00-58_medgemma_27b_text_it_vllm_plain/` - 27B Plain run  
- `10-27-26_medgemma_4b_vllm_json/` - 4B JSON run
- `10-36-31_medgemma_4b_vllm_plain/` - 4B Plain run
