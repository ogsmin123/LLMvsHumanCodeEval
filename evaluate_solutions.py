import os, pandas as pd
from pathlib import Path
from utils import metrics, comments, diff_analysis
from utils import coupling

HUMAN_DIR = Path("data/human")
LLM_DIR = Path("data/llm")
HUMAN_DIR.mkdir(parents=True, exist_ok=True)
LLM_DIR.mkdir(parents=True, exist_ok=True)

def evaluate_all():
    rows = []
    for human in HUMAN_DIR.iterdir():
        if human.suffix not in (".py", ".java"):
            continue
        llm = LLM_DIR / human.name
        if not llm.exists():
            print(f"[WARN] Missing LLM solution for {human.name}")
            continue
        lang = "Python" if human.suffix == ".py" else "Java"

        m_h = metrics.compute_metrics(str(human), lang)
        m_l = metrics.compute_metrics(str(llm), lang)
        c_h = comments.analyze_comments(str(human))
        c_l = comments.analyze_comments(str(llm))
        d = diff_analysis.diff_ratio(str(human), str(llm))
        couple_h = coupling.compute_coupling(str(human), lang)
        couple_l = coupling.compute_coupling(str(llm), lang)

        rows.append({
            "problem": human.stem,
            "lang": lang,
            "human_MI": m_h["mi"], "llm_MI": m_l["mi"],
            "human_CC": m_h["cc_avg"], "llm_CC": m_l["cc_avg"],
            "human_comments": c_h["density"], "llm_comments": c_l["density"],
            "why_ratio_h": c_h["why_ratio"], "why_ratio_l": c_l["why_ratio"],
            "diff_ratio": d,
            "fan_in_h": couple_h["fan_in"], "fan_in_l": couple_l["fan_in"],
            "fan_out_h": couple_h["fan_out"], "fan_out_l": couple_l["fan_out"],
            "imports_h": couple_h["imports"], "imports_l": couple_l["imports"],
            "coupling_idx_h": couple_h["coupling_index"], "coupling_idx_l": couple_l["coupling_index"],
        })
    df = pd.DataFrame(rows)
    df.to_csv("analysis_results.csv", index=False)
    print("\n=== SUMMARY ===")
    print(df.describe(include="all"))
    print("\nSaved results to analysis_results.csv")

if __name__ == "__main__":
    evaluate_all()
