AI vs Human Code Evaluation (Python/Java)

Empirical comparison of pre-LLM human code vs GPT-4o code across algorithmic problems.
This repo contains ready-to-run scripts to compute complexity, coupling, comment quality, rewrite extent, and knowledge-preserving indicators—plus figures and a LaTeX paper draft.

1) Prerequisites

macOS (tested), Linux should also work

Python 3.10+ recommended

git (for optional dataset updates)

(Optional) Jupyter for the analysis notebook

2) Quick Start (Evaluate with bundled data)

If the repo already includes data/human/ and data/llm/, you can evaluate immediately:

# from repo root
python3 -m venv venv
source venv/bin/activate

# install deps
pip install -r requirements.txt
# If you don't have a requirements.txt, use:
# pip install pandas numpy matplotlib lizard radon

# run evaluation
python evaluate_solutions.py

# open the results notebook (optional)
jupyter notebook analyze_results.ipynb


Outputs

analysis_results.csv — per-problem metrics (CC, MI, comments, WHY ratio, coupling, diff)

Figures (if you run the figure scripts): e.g. fig_cc_scatter.png, fig_why_hist.png, fig_coupling_scatter.png, fig_diff_ratio_bars.png

7) What each script does

evaluate_solutions.py — computes metrics per problem:

CC (cyclomatic complexity) via lizard API

MI (maintainability index, Python only) via radon API

Comment density and WHY ratio (rationale keyword hits per comment word)

Coupling (fan-in/fan-out/imports; coupling index)

Diff ratio between human and LLM code (rewrite vs modify proxy)
→ writes analysis_results.csv

8) Troubleshooting

ModuleNotFoundError: No module named 'pandas'
You’re likely outside the venv or missing deps.
source venv/bin/activate && pip install -r requirements.txt

lizard: error: unrecognized arguments: -j
We use the Python API (not CLI JSON). Ensure you’re running the updated utils/metrics.py. If you rely on CLI, upgrade: pip install "lizard>=1.17".

Git “commit before cutoff” error when fetching problems
Unshallow once:
git -C data/src/TheAlgorithms-Python fetch --unshallow --quiet && git -C data/src/TheAlgorithms-Python fetch --all --tags --prune --quiet

Notebook error “NotJSONError: Notebook does not appear to be JSON”
Replace the notebook with a valid .ipynb (we included a working analyze_results.ipynb). You can also use the CLI plotting helpers if you prefer.

9) Repo Layout (key paths)
data/
  human/             # human solutions (.py/.java)
  llm/               # LLM solutions (.py/.java)
analysis_results.csv # produced by evaluate_solutions.py
knowledge_summary.csv
fig_*.png            # figures (when generated)
paper.tex            # LaTeX draft
utils/
  metrics.py         # lizard/radon API-based metrics
  comments.py
  coupling.py
  knowledge.py
evaluate_solutions.py
evaluate_knowledge.py
fetch_problems.py
generate_llm_solutions.py
analyze_results.ipynb
