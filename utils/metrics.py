# utils/metrics.py (drop-in replacement for your compute_metrics)
from __future__ import annotations
import os

# Cyclomatic complexity via lizard (Python API)
try:
    import lizard
except Exception:
    lizard = None

# Maintainability Index via radon (Python API)
try:
    from radon.metrics import mi_visit
except Exception:
    mi_visit = None


def _avg(xs):
    return (sum(xs) / len(xs)) if xs else 0.0


def compute_metrics(filepath: str, lang: str | None = None) -> dict:
    """
    Returns:
      {
        "cc_avg": float,   # average cyclomatic complexity per function in the file
        "mi": float        # maintainability index (Python only; 0.0 if not available)
      }
    """
    if lang is None:
        lang = "Python" if os.path.splitext(filepath)[1].lower() == ".py" else "Java"

    # --- Cyclomatic Complexity (lizard API) ---
    cc_avg = 0.0
    if lizard is not None:
        try:
            result = lizard.analyze_file(filepath)
            ccs = [fn.cyclomatic_complexity for fn in result.function_list]
            cc_avg = float(_avg(ccs))
        except Exception:
            cc_avg = 0.0  # keep going even if analysis fails

    # --- Maintainability Index (radon API; Python only) ---
    mi = 0.0
    if lang == "Python" and mi_visit is not None:
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                code = f.read()
            # multi=False -> single float MI for the whole file
            mi = float(mi_visit(code, multi=False))
        except Exception:
            mi = 0.0

    return {"cc_avg": cc_avg, "mi": mi}
