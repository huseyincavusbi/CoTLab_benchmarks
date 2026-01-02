# Questions & Answers for CoT and Format Research

## Scenario 1: Chain of Thinking - Best Prompting Techniques

### 1.1 How Questions

#### Q1: How do different prompting strategies change model performance?
- **Answer:** 
  - **Dramatic impact**: Performance varies by prompt and format
  - **27B Top 3**: contrarian (84% plain), expert_persona (72% plain), adversarial (62% JSON)
  - **27B Bottom 3**: socratic (8% JSON), uncertainty (11% plain), simple (23% plain)
  - **4B Top 3**: contrarian (67% plain), expert_persona (62% plain), chain_of_thought (54% plain)
  - **4B Bottom 3**: simple (12% JSON), sycophantic (15% JSON), socratic (19% JSON)
  - **CoT generally hurts**: -24.4% penalty for 27B, -12.3% for 4B 

#### Q2: Is our radiology prompt good enough?
- **Answer:** 
  - **Yes, excellent performance**
  - **Model-specific results**:
    - **MedGemma 4B**: 99.0% (both JSON and Plain)
    - **MedGemma 27B**: 97.6% JSON, 97.4% Plain
  - **Previous poor results were misleading**: True prompt, wrong question

#### Q3: How much better is the contrarian approach than others?
- **Answer:** 
  - **27B**: Contrarian is #1 at **84%** (plain text), beating runner-up expert_persona by **+12%** (72%)
  - **4B**: Contrarian is #1 at **67%** (plain text), beating runner-up expert_persona by **+5%** (62%) 

### 1.2 Why Questions

#### Q4: What are the contributing factors for these prompting preferences?
- **Answer:** 
  - **Early decision making (27B)**: Layer 1-2 patching shows **0.845 effect** — model decides immediately
  - **Overthinking penalty**: 27B then has 60 more layers to "doubt" itself → CoT activates doubt circuits
  - **Late decision (4B)**: Critical layers at 29-30-31 (near end of 34-layer network) → only 3 layers left to doubt → less overthinking
  - **Steerability difference**: 4B is **2x more steerable** than 27B (10.44 vs 4.88 effect)
  - **Contrarian success**: Forces answer first, bypassing doubt circuits that hurt other CoT approaches
  - **Model size effect**: Larger models benefit from structure (JSON), smaller models get constrained by it 

#### Q5: Why does the model perform best on contrarian (for example)?
- **Answer:** Hypothesis: "Answer first, then argue" structure may bypass early-decision overthinking — **more mechanistic research needed** 

---

## Scenario 2: Influence of Enforcing Data Structure Standards

### 2.1 How Questions

#### Q6: Is enforcing the model to JSON output helpful?
- **Answer:** 
  - **Depends on model size**:
    - **27B**: Yes, JSON helps (+11.1% CoT accuracy), **8/12 prompts benefit from JSON**
    - **4B**: No, JSON hurts (-11.5% CoT accuracy), **Only 2/12 prompts benefit from JSON**
  - **Exception**: Contrarian loses ~34% with JSON on both models

#### Q7: Which is the best structured output/input format for the model?
- **Answer:** **27B: JSON** (+11.1%), **4B: Plain text** (JSON -11.5%). Hypothesis: 27B has capacity to use JSON as scaffolding for reasoning, while 4B spends limited capacity on syntax generation. Worth exploring TOON, TOML, XML, YAML, or markdown. But JSON is industry standard.

### 2.2 Why Questions

#### Q8: What is the reason for these behaviors?
- **Answer:** Model capacity determines structure benefit: 27B uses JSON as reasoning scaffolding while 4B wastes limited capacity on syntax. MedGemma's early decision-making (Layer 1-2) combined with 60+ doubt-inducing layers causes overthinking penalty, which contrarian bypasses by forcing answer-first structure. 

---

## Deliverables

#### Q9: What notebook have we created?
- **Answer:** 
  - **Tutorial notebook**: [CoTLab Introduction](https://github.com/huseyincavusbi/CoTLab/blob/main/notebooks/cotlab_tutorial.ipynb)
