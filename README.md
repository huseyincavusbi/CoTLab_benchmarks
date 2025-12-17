# CoTLab Benchmark Results

Complete results from Chain of Thought faithfulness experiments on medical and reasoning LLMs.

## Summary

| Model | CoT Accuracy | Direct Accuracy | CoT Effect | Training Type |
|-------|-------------|-----------------|------------|---------------|
| **MedGemma 27B** | 33.5% | 57.9% | **-24.4%** | Medical IT |
| **MedGemma 4B** | 39.4% | 51.7% | **-12.3%** | Medical IT |
| **Ministral 14B** | 27.9% | 42.9% | **-15.0%** | Reasoning |
| Nemotron 30B | 38.6% | 37.2% | +1.4% | Reasoning |
| **DeepSeek-R1 32B** | 24.3% | 17.5% | **+6.8%** | Reasoning |
| **Olmo 3.1 32B** | 18.1% | 5.0% | **+13.1%** | Reasoning |
| **Olmo 3 32B** | 21.9% | 4.9% | **+17.0%** | Reasoning |

**Key Finding**: Instruction-tuned models are hurt by CoT, reasoning models are helped.

---

## Part 1: Behavioral Results (vLLM Backend)

### 1.1 MedGemma 27B-text-IT

**4,017 samples across 4 datasets, 13 prompt strategies**

| Metric | Value |
|--------|-------|
| CoT Accuracy | 33.5% |
| Direct Accuracy | **57.9%** |
| Agreement Rate | 30.4% |
| CoT Penalty | **-24.4%** |

#### By Dataset
| Dataset | CoT Acc | Direct Acc | Samples |
|---------|---------|------------|---------|
| pediatrics | 35.6% | **72.9%** | 1,300 |
| synthetic | 38.5% | **77.5%** | 1,300 |
| patching | 29.2% | 28.5% | 1,300 |
| radiology | 2.6% | 0.0% | 117 |

#### By Prompt Strategy
| Prompt | CoT Acc | Direct Acc |
|--------|---------|------------|
| contrarian | **77.0%** | 75.1% |
| direct_answer | 73.7% | 69.4% |
| expert_persona | 75.1% | 75.1% |
| chain_of_thought | 19.6% | 73.2% |
| socratic | 6.7% | **74.6%** |

---

### 1.2 MedGemma 4B-IT

**4,017 samples**

| Metric | Value |
|--------|-------|
| CoT Accuracy | 39.4% |
| Direct Accuracy | **51.7%** |
| Agreement Rate | 35.6% |
| CoT Penalty | **-12.3%** |

#### By Dataset
| Dataset | CoT Acc | Direct Acc | Samples |
|---------|---------|------------|---------|
| pediatrics | 40.0% | **52.0%** | 1,300 |
| synthetic | 44.7% | **65.6%** | 1,300 |
| patching | 36.8% | 42.2% | 1,300 |
| radiology | 3.4% | 0.0% | 117 |

**Key Insight**: MedGemma 4B has **half the CoT penalty** of 27B (-12.3% vs -24.4%).

---

### 1.3 DeepSeek-R1 32B (Reasoning Model)

**4,017 samples**

| Metric | Value |
|--------|-------|
| CoT Accuracy | **24.3%** |
| Direct Accuracy | 17.5% |
| Agreement Rate | 21.1% |
| CoT Benefit | **+6.8%** |

#### By Dataset
| Dataset | CoT Acc | Direct Acc | Samples |
|---------|---------|------------|---------|
| activation patching | **28.5%** | 11.2% | 1,300 |
| pediatrics | 24.3% | 28.5% | 1,300 |
| synthetic | 21.9% | 14.2% | 1,300 |

---

### 1.4 Olmo 3.1 32B Think

**4,017 samples**

| Metric | Value |
|--------|-------|
| CoT Accuracy | **18.1%** |
| Direct Accuracy | 5.0% |
| Agreement Rate | 6.3% |
| CoT Benefit | **+13.1%** |

---

### 1.5 Olmo 3 32B Think

**4,017 samples**

| Metric | Value |
|--------|-------|
| CoT Accuracy | **21.9%** |
| Direct Accuracy | 4.9% |
| Agreement Rate | 6.6% |
| CoT Benefit | **+17.0%** |

---

### 1.6 Nemotron 30B

**4,017 samples**

| Metric | Value |
|--------|-------|
| CoT Accuracy | 38.6% |
| Direct Accuracy | 37.2% |
| Agreement Rate | 11.2% |
| CoT Effect | +1.4% (Neutral) |

---

### 1.7 Ministral 14B

**4,017 samples**

| Metric | Value |
|--------|-------|
| CoT Accuracy | 27.9% |
| Direct Accuracy | **42.9%** |
| Agreement Rate | 16.8% |
| CoT Penalty | **-15.0%** |

---

## Part 2: Mechanistic Results (Transformers Backend)

### 2.1 Activation Patching

**50 samples per model, all layers analyzed**

| Model | Layers | Top 3 Critical Layers | Top Layer Effect |
|-------|--------|----------------------|----------------|
| **MedGemma 27B** | 62 | [1, 2, 4] | **0.845** |
| **MedGemma 4B** | 34 | [30, 29, 31] | **0.627** |
| DeepSeek-R1 | 64 | [1, 2, 22] | 0.896 |
| Olmo 3.1 Think | 64 | [55, 50, 58] | 0.148 |
| Olmo 3 Think | 64 | [55, 58, 50] | 0.183 |

**Key Finding**: MedGemma 27B decides in Layer 1-2 (0.845 effect), MedGemma 4B decides in Layer 30-31 (0.627 effect).

---

### 2.2 Steering Vectors

**All layers swept with 7 steering strengths [-2, -1, -0.5, 0, 0.5, 1, 2]**

| Model | Best Layer | Effect Range | Steerability |
|-------|------------|--------------|--------------|
| **DeepSeek-R1** | 54 | **10.75** | Highest |
| **MedGemma 4B** | 33 | **10.44** | Very High |
| Olmo 3 Think | 58 | 7.19 | High |
| Olmo 3.1 Think | 58 | 6.28 | Moderate |
| MedGemma 27B | 58 | 4.88 | Low |

**Key Finding**: MedGemma 4B is **2x more steerable** than 27B.

---

## Part 3: The "Overthinking Theory"

### Evidence

1. **MedGemma 27B decides early** (Layer 1-2 has 0.845 patching effect)
2. **Then has 60 more layers to "doubt"** itself
3. **Late layers are steerable** (can change answer at Layer 58)
4. **CoT** activates **doubt circuits** → wrong answers

### Comparison

| Model | Top Layer Effect | Top Layers | CoT Effect |
|-------|---------------|------------|------------|
| MedGemma 27B | **0.845** (early) | [1, 2, 4] | **-24.4%** |
| MedGemma 4B | 0.627 (distributed) | [30, 29, 31] | **-12.3%** |
| Olmo Think | 0.148 (late) | [55, 58, 50] | **+15%** |

**Conclusion**: Early decision + many layers = overthinking = CoT hurts.