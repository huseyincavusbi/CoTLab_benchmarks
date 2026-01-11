"""
Configuration for MedGemma Mechanistic Analysis.

Contains model settings, prompt templates, and test cases for analyzing
why contrarian prompts outperform standard CoT.
"""

import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional

# ============================================================================
# Model Configuration
# ============================================================================

MODEL_NAME = "google/medgemma-27b-text-it"
DEVICE = "cuda"
DTYPE = "bfloat16"  # For A100 80GB

# MedGemma 27B has 62 layers
N_LAYERS = 62

# Key layers from probing experiments
CONTRARIAN_COMMIT_LAYER = 18  # Where contrarian encodes diagnosis
COT_COMMIT_LAYER = 57  # Where CoT encodes diagnosis
DIRECT_COMMIT_LAYER = 58  # Where direct answer encodes

# Output directories
OUTPUT_DIR = "/home/ubuntu/contrarian_analysis"
PLOTS_DIR = os.path.join(OUTPUT_DIR, "plots")
RESULTS_DIR = os.path.join(OUTPUT_DIR, "results")

# ============================================================================
# Prompt Templates
# ============================================================================

@dataclass
class PromptStrategy:
    """Defines a prompting strategy with system message and template."""
    name: str
    system_message: str
    template: str
    
    def format(self, question: str) -> str:
        """Format the prompt with the given question."""
        return self.template.format(question=question)


# Chain of Thought prompt
COT_PROMPT = PromptStrategy(
    name="chain_of_thought",
    system_message=(
        "You are a medical expert. Think through problems carefully and "
        "explain your reasoning step by step before giving your final answer."
    ),
    template=(
        "Question: {question}\n\n"
        "Let's think through this step by step:"
    )
)

# Direct Answer prompt
DIRECT_PROMPT = PromptStrategy(
    name="direct_answer",
    system_message=(
        "You are a medical expert. Give only the final answer. "
        "Do not explain or show your reasoning."
    ),
    template=(
        "Question: {question}\n\n"
        "Give ONLY the final answer. Do not explain, do not reason, just answer:"
    )
)

# Contrarian prompt - the high performer
CONTRARIAN_PROMPT = PromptStrategy(
    name="contrarian",
    system_message=(
        "You are a skeptical diagnostician who questions obvious conclusions."
    ),
    template=(
        "Play devil's advocate. Argue why the most obvious diagnosis might be WRONG.\n\n"
        "Question: {question}\n\n"
        "First state what the obvious answer would be, then argue against it with alternative explanations:"
    )
)

# All strategies for comparison
PROMPT_STRATEGIES = {
    "contrarian": CONTRARIAN_PROMPT,
    "chain_of_thought": COT_PROMPT,
    "direct_answer": DIRECT_PROMPT,
}

# ============================================================================
# Ablation Prompt Variations
# ============================================================================

ABLATION_PROMPTS = {
    "full": CONTRARIAN_PROMPT,
    
    "no_devils_advocate": PromptStrategy(
        name="no_devils_advocate",
        system_message="You are a skeptical diagnostician who questions obvious conclusions.",
        template=(
            "Argue why the most obvious diagnosis might be WRONG.\n\n"
            "Question: {question}\n\n"
            "First state what the obvious answer would be, then argue against it with alternative explanations:"
        )
    ),
    
    "no_obvious": PromptStrategy(
        name="no_obvious",
        system_message="You are a skeptical diagnostician who questions obvious conclusions.",
        template=(
            "Play devil's advocate. Argue why the diagnosis might be WRONG.\n\n"
            "Question: {question}\n\n"
            "First state what the answer would be, then argue against it with alternative explanations:"
        )
    ),
    
    "no_argue_against": PromptStrategy(
        name="no_argue_against",
        system_message="You are a skeptical diagnostician who questions obvious conclusions.",
        template=(
            "Play devil's advocate.\n\n"
            "Question: {question}\n\n"
            "First state what the obvious answer would be, then discuss alternative explanations:"
        )
    ),
    
    "neutral_system": PromptStrategy(
        name="neutral_system",
        system_message="You are a medical expert.",
        template=(
            "Play devil's advocate. Argue why the most obvious diagnosis might be WRONG.\n\n"
            "Question: {question}\n\n"
            "First state what the obvious answer would be, then argue against it with alternative explanations:"
        )
    ),
    
    "minimal": PromptStrategy(
        name="minimal",
        system_message="You are a medical expert.",
        template=(
            "State the obvious diagnosis for this case.\n\n"
            "Question: {question}\n\n"
            "The obvious diagnosis is:"
        )
    ),
}

# ============================================================================
# Medical Test Cases
# ============================================================================

@dataclass
class MedicalCase:
    """A medical diagnosis test case."""
    name: str
    question: str
    expected_answer: str
    answer_tokens: List[str] = field(default_factory=list)  # Alternative token forms
    
    def __post_init__(self):
        if not self.answer_tokens:
            # Default: include the answer itself and common variations
            self.answer_tokens = [
                self.expected_answer,
                self.expected_answer.lower(),
                f" {self.expected_answer}",
                f" {self.expected_answer.lower()}",
            ]


# Test cases from the research
MEDICAL_CASES = [
    MedicalCase(
        name="diabetes",
        question=(
            "A 45-year-old patient presents with polyuria, polydipsia, and unexplained "
            "weight loss over the past 3 months. Fasting blood glucose is 280 mg/dL. "
            "What is the most likely diagnosis?"
        ),
        expected_answer="Diabetes",
        answer_tokens=["Diabetes", "diabetes", " Diabetes", " diabetes", 
                       "Type 2 Diabetes", "type 2 diabetes", "DM", "T2DM"],
    ),
    MedicalCase(
        name="croup",
        question=(
            "A 2-year-old child presents with a barking cough, inspiratory stridor, "
            "and a low-grade fever. Symptoms started suddenly at night. The child "
            "had a mild upper respiratory infection 2 days ago. What is the most likely diagnosis?"
        ),
        expected_answer="Croup",
        answer_tokens=["Croup", "croup", " Croup", " croup", 
                       "Laryngotracheobronchitis", "laryngotracheobronchitis"],
    ),
    MedicalCase(
        name="appendicitis",
        question=(
            "A 28-year-old patient presents with periumbilical pain that migrated to "
            "the right lower quadrant over 12 hours. Physical exam shows rebound "
            "tenderness at McBurney's point and low-grade fever. WBC is elevated at 14,000. "
            "What is the most likely diagnosis?"
        ),
        expected_answer="Appendicitis",
        answer_tokens=["Appendicitis", "appendicitis", " Appendicitis", " appendicitis",
                       "Acute appendicitis", "acute appendicitis"],
    ),
    MedicalCase(
        name="pneumonia",
        question=(
            "A 65-year-old patient with COPD presents with productive cough with "
            "yellow-green sputum, fever of 101.5°F, and dyspnea. Chest examination "
            "reveals crackles and dullness to percussion in the right lower lobe. "
            "What is the most likely diagnosis?"
        ),
        expected_answer="Pneumonia",
        answer_tokens=["Pneumonia", "pneumonia", " Pneumonia", " pneumonia",
                       "Community-acquired pneumonia", "CAP", "Bacterial pneumonia"],
    ),
]

# Dictionary for easy access by name
CASES_BY_NAME = {case.name: case for case in MEDICAL_CASES}

# ============================================================================
# Analysis Parameters
# ============================================================================

# For LogitLens analysis
TOP_K_PREDICTIONS = 10  # Track if answer appears in top-k

# For attention analysis
ATTENTION_HEADS_TO_ANALYZE = list(range(32))  # All heads in 27B model

# For patching experiments
PATCH_LAYERS = [18, 17, 19, 16, 20]  # Layer 18 and neighbors

# Layers to analyze in detail
KEY_LAYERS = [0, 10, 18, 30, 45, 57, 58, 61]  # Important checkpoints
