"""
Master script to run all MedGemma mechanistic analysis experiments.

This script orchestrates all experiments and generates a comprehensive
summary report of the findings.
"""

import sys
sys.path.insert(0, '/home/ubuntu/TransformerLens')

import os
import json
import datetime
from typing import Dict

from config import (
    MODEL_NAME, OUTPUT_DIR, RESULTS_DIR, PLOTS_DIR,
    CONTRARIAN_COMMIT_LAYER, COT_COMMIT_LAYER, DIRECT_COMMIT_LAYER,
    MEDICAL_CASES, PROMPT_STRATEGIES
)
from utils import save_results, load_results, get_gpu_memory_usage


def run_all_experiments():
    """Run all experiments sequentially."""
    
    print("=" * 80)
    print("MedGemma Mechanistic Analysis - Full Experiment Suite")
    print("=" * 80)
    print(f"Start time: {datetime.datetime.now()}")
    print(f"GPU Memory: {get_gpu_memory_usage()}")
    print(f"Model: {MODEL_NAME}")
    print(f"Output directory: {OUTPUT_DIR}")
    print("=" * 80)
    
    results = {}
    
    # =========================================================================
    # Experiment 1: LogitLens Analysis
    # =========================================================================
    print("\n" + "▶" * 40)
    print("EXPERIMENT 1: LogitLens Analysis")
    print("▶" * 40)
    
    try:
        from logit_lens_analysis import main as run_logit_lens
        logit_results, logit_summary = run_logit_lens()
        results['logit_lens'] = {
            'status': 'success',
            'summary': logit_summary,
        }
    except Exception as e:
        print(f"Error in LogitLens: {e}")
        results['logit_lens'] = {'status': 'error', 'error': str(e)}
    
    # =========================================================================
    # Experiment 2: Activation Patching
    # =========================================================================
    print("\n" + "▶" * 40)
    print("EXPERIMENT 2: Activation Patching")
    print("▶" * 40)
    
    try:
        from activation_patching import main as run_patching
        patch_results, patch_summary = run_patching()
        results['patching'] = {
            'status': 'success',
            'summary': patch_summary,
        }
    except Exception as e:
        print(f"Error in Patching: {e}")
        results['patching'] = {'status': 'error', 'error': str(e)}
    
    # =========================================================================
    # Experiment 3: Attention Analysis
    # =========================================================================
    print("\n" + "▶" * 40)
    print("EXPERIMENT 3: Attention Pattern Analysis")
    print("▶" * 40)
    
    try:
        from attention_analysis import main as run_attention
        attention_results = run_attention()
        results['attention'] = {
            'status': 'success',
        }
    except Exception as e:
        print(f"Error in Attention: {e}")
        results['attention'] = {'status': 'error', 'error': str(e)}
    
    # =========================================================================
    # Experiment 4: Direct Logit Attribution
    # =========================================================================
    print("\n" + "▶" * 40)
    print("EXPERIMENT 4: Direct Logit Attribution")
    print("▶" * 40)
    
    try:
        from logit_attribution import main as run_attribution
        attr_results, attr_comparison = run_attribution()
        results['attribution'] = {
            'status': 'success',
            'comparison': attr_comparison,
        }
    except Exception as e:
        print(f"Error in Attribution: {e}")
        results['attribution'] = {'status': 'error', 'error': str(e)}
    
    # =========================================================================
    # Experiment 5: Ablation Study
    # =========================================================================
    print("\n" + "▶" * 40)
    print("EXPERIMENT 5: Prompt Ablation Study")
    print("▶" * 40)
    
    try:
        from ablation_study import main as run_ablation
        ablation_results, ablation_impact, ablation_essential = run_ablation()
        results['ablation'] = {
            'status': 'success',
            'impact': ablation_impact,
            'essential_components': ablation_essential,
        }
    except Exception as e:
        print(f"Error in Ablation: {e}")
        results['ablation'] = {'status': 'error', 'error': str(e)}
    
    # =========================================================================
    # Experiment 6: Layer Sweep Visualization
    # =========================================================================
    print("\n" + "▶" * 40)
    print("EXPERIMENT 6: Layer Sweep Visualization")
    print("▶" * 40)
    
    try:
        from layer_sweep import main as run_sweep
        sweep_results = run_sweep()
        results['layer_sweep'] = {
            'status': 'success',
        }
    except Exception as e:
        print(f"Error in Layer Sweep: {e}")
        results['layer_sweep'] = {'status': 'error', 'error': str(e)}
    
    # =========================================================================
    # Generate Summary Report
    # =========================================================================
    print("\n" + "=" * 80)
    print("GENERATING SUMMARY REPORT")
    print("=" * 80)
    
    generate_summary_report(results)
    
    return results


def generate_summary_report(results: Dict):
    """Generate a markdown summary report of all experiments."""
    
    report_path = os.path.join(OUTPUT_DIR, "SUMMARY_REPORT.md")
    
    with open(report_path, 'w') as f:
        f.write("# MedGemma Mechanistic Analysis Report\n\n")
        f.write(f"**Generated:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Model:** `{MODEL_NAME}`\n\n")
        
        f.write("## Executive Summary\n\n")
        f.write("This report analyzes why the contrarian prompting strategy achieves ")
        f.write("significantly higher accuracy (88-94%) compared to standard Chain-of-Thought ")
        f.write("(52-69%) on medical diagnosis tasks.\n\n")
        
        f.write("### Key Hypothesis\n\n")
        f.write(f"- Contrarian prompts commit to the diagnosis at **Layer {CONTRARIAN_COMMIT_LAYER}** (early)\n")
        f.write(f"- CoT prompts commit to the diagnosis at **Layer {COT_COMMIT_LAYER}** (late)\n")
        f.write(f"- Direct answer prompts commit at **Layer {DIRECT_COMMIT_LAYER}** (late)\n\n")
        
        f.write("---\n\n")
        
        # Experiment Results
        f.write("## Experiment Results\n\n")
        
        # 1. LogitLens
        f.write("### 1. LogitLens Analysis\n\n")
        if results.get('logit_lens', {}).get('status') == 'success':
            summary = results['logit_lens'].get('summary', {})
            f.write("**Status:** ✅ Success\n\n")
            f.write("| Strategy | Mean Commitment Layer | Final Probability |\n")
            f.write("|----------|----------------------|-------------------|\n")
            for strategy, data in summary.items():
                commit = data.get('mean_commitment_layer', 'N/A')
                prob = data.get('mean_final_probability', 'N/A')
                if isinstance(commit, (int, float)) and commit >= 0:
                    f.write(f"| {strategy} | L{commit:.1f} | {prob:.4f} |\n")
                else:
                    f.write(f"| {strategy} | - | {prob:.4f} |\n")
            f.write("\n")
        else:
            f.write("**Status:** ❌ Error\n\n")
            f.write(f"Error: {results.get('logit_lens', {}).get('error', 'Unknown')}\n\n")
        
        # 2. Patching
        f.write("### 2. Activation Patching\n\n")
        if results.get('patching', {}).get('status') == 'success':
            f.write("**Status:** ✅ Success\n\n")
            summary = results['patching'].get('summary', {})
            
            cot_imp = summary.get('contrarian_to_cot', {}).get('mean_improvement', {})
            if isinstance(cot_imp, dict):
                mean_imp = cot_imp.get('mean', 0)
            else:
                mean_imp = cot_imp
            
            f.write(f"**Key Finding:** Patching L{CONTRARIAN_COMMIT_LAYER} from contrarian into CoT ")
            if mean_imp > 0:
                f.write(f"**improves** probability by {mean_imp:.4f}\n\n")
                f.write("✅ This supports the hypothesis that early commitment is the mechanism.\n\n")
            else:
                f.write(f"**does not improve** probability ({mean_imp:.4f})\n\n")
                f.write("❌ Patching alone may not transfer the effect.\n\n")
        else:
            f.write("**Status:** ❌ Error\n\n")
        
        # 3. Attention
        f.write("### 3. Attention Pattern Analysis\n\n")
        if results.get('attention', {}).get('status') == 'success':
            f.write("**Status:** ✅ Success\n\n")
            f.write("See `plots/` directory for attention pattern visualizations.\n\n")
        else:
            f.write("**Status:** ❌ Error\n\n")
        
        # 4. Attribution
        f.write("### 4. Direct Logit Attribution\n\n")
        if results.get('attribution', {}).get('status') == 'success':
            f.write("**Status:** ✅ Success\n\n")
            comparison = results['attribution'].get('comparison', {})
            for strategy, data in comparison.items():
                f.write(f"**{strategy}** top contributing heads:\n")
                heads = data.get('top_positive_heads', [])[:3]
                for head, val in heads:
                    f.write(f"- {head}: {val:.4f}\n")
                f.write("\n")
        else:
            f.write("**Status:** ❌ Error\n\n")
        
        # 5. Ablation
        f.write("### 5. Ablation Study\n\n")
        if results.get('ablation', {}).get('status') == 'success':
            f.write("**Status:** ✅ Success\n\n")
            essential = results['ablation'].get('essential_components', {})
            
            f.write("**Essential Components (removing delays commitment):**\n")
            for component, change in essential.get('essential_components', []):
                f.write(f"- \"{component}\" - delays by {change:.1f} layers\n")
            
            if not essential.get('essential_components'):
                f.write("- None identified as individually essential\n")
            
            f.write("\n**Non-essential Components:**\n")
            for component, change in essential.get('non_essential_components', []):
                f.write(f"- \"{component}\" - only {change:.1f} layer change\n")
            f.write("\n")
        else:
            f.write("**Status:** ❌ Error\n\n")
        
        # 6. Layer Sweep
        f.write("### 6. Layer Sweep Visualization\n\n")
        if results.get('layer_sweep', {}).get('status') == 'success':
            f.write("**Status:** ✅ Success\n\n")
            f.write("Comprehensive layer-by-layer visualizations saved to `plots/`.\n\n")
        else:
            f.write("**Status:** ❌ Error\n\n")
        
        f.write("---\n\n")
        
        # Conclusions
        f.write("## Conclusions\n\n")
        f.write("Based on the experiments:\n\n")
        f.write("1. **Early vs Late Commitment:** [Analysis pending - check logit_lens results]\n")
        f.write("2. **Patching Effectiveness:** [Analysis pending - check patching results]\n")
        f.write("3. **Essential Prompt Components:** [Analysis pending - check ablation results]\n")
        f.write("4. **Attention Patterns:** [Analysis pending - check attention plots]\n\n")
        
        f.write("---\n\n")
        
        # Files Generated
        f.write("## Generated Files\n\n")
        f.write("### Results (JSON)\n")
        f.write("- `results/logit_lens_full_results.json`\n")
        f.write("- `results/logit_lens_summary.json`\n")
        f.write("- `results/patching_full_results.json`\n")
        f.write("- `results/patching_summary.json`\n")
        f.write("- `results/attention_analysis_results.json`\n")
        f.write("- `results/logit_attribution_results.json`\n")
        f.write("- `results/ablation_full_results.json`\n")
        f.write("- `results/ablation_essential_components.json`\n")
        f.write("- `results/layer_sweep_results.json`\n\n")
        
        f.write("### Visualizations\n")
        f.write("- `plots/logit_lens_*.png` - Answer probability by layer\n")
        f.write("- `plots/patching_*.png` - Patching experiment results\n")
        f.write("- `plots/attention_*.png` - Attention patterns\n")
        f.write("- `plots/logit_attribution_*.png` - Head/MLP contributions\n")
        f.write("- `plots/ablation_*.png` - Ablation study results\n")
        f.write("- `plots/layer_sweep_*.png` - Complete layer analysis\n")
    
    print(f"\nSummary report saved to: {report_path}")
    
    # Also save experiment status as JSON
    save_results({
        'timestamp': datetime.datetime.now().isoformat(),
        'model': MODEL_NAME,
        'experiments': {k: v.get('status', 'unknown') for k, v in results.items()},
    }, 'experiment_status')


def run_single_experiment(experiment_name: str):
    """Run a single experiment by name."""
    
    experiments = {
        'logit_lens': ('logit_lens_analysis', 'main'),
        'patching': ('activation_patching', 'main'),
        'attention': ('attention_analysis', 'main'),
        'attribution': ('logit_attribution', 'main'),
        'ablation': ('ablation_study', 'main'),
        'layer_sweep': ('layer_sweep', 'main'),
    }
    
    if experiment_name not in experiments:
        print(f"Unknown experiment: {experiment_name}")
        print(f"Available: {list(experiments.keys())}")
        return None
    
    module_name, func_name = experiments[experiment_name]
    
    print(f"Running {experiment_name}...")
    
    module = __import__(module_name)
    func = getattr(module, func_name)
    
    return func()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run MedGemma mechanistic analysis experiments")
    parser.add_argument(
        '--experiment', '-e',
        type=str,
        default='all',
        help='Experiment to run: all, logit_lens, patching, attention, attribution, ablation, layer_sweep'
    )
    
    args = parser.parse_args()
    
    if args.experiment == 'all':
        run_all_experiments()
    else:
        run_single_experiment(args.experiment)
