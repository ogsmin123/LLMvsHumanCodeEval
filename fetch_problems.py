"""
fetch_problems.py — Python-only (50 problems) from TheAlgorithms/Python, pinned pre-2022.

What it does:
  1) Clones TheAlgorithms/Python (if missing) into data/src/TheAlgorithms-Python.
  2) Checks out the last commit BEFORE 2022-01-01 (pre-LLM baseline).
  3) Scans for Python algorithm files across common categories.
  4) Extracts a concise "problem statement" from docstrings or top comments.
  5) Writes 50 normalized .py files to data/human/, each prefixed with a header:

        # Problem: <slug>
        # Description: <extracted or synthesized description>

Run:
  python fetch_problems.py
"""

from __future__ import annotations
import os
import re
import subprocess
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).parent.resolve()
DATA_DIR = ROOT / "data"
SRC_DIR = DATA_DIR / "src"
HUMAN_DIR = DATA_DIR / "human"
PY_REPO = SRC_DIR / "TheAlgorithms-Python"

HUMAN_DIR.mkdir(parents=True, exist_ok=True)
SRC_DIR.mkdir(parents=True, exist_ok=True)

# Prioritized directories to encourage diversity
CANDIDATE_DIR_NAMES = [
    "searches", "sorts", "graphs", "graph", "dynamic_programming", "dp",
    "strings", "string", "greedy", "maths", "math", "number_theory",
    "tree", "trees", "heaps", "linked_list", "data_structures",
    "recursion", "geometry", "bit_manipulation", "hashing", "arrays",
    "matrix", "backtracking", "game_theory"
]

MAX_PROBLEMS = 50

# ----------------- git helpers -----------------

def _run(cmd: List[str], cwd: Path | None = None) -> str:
    out = subprocess.run(cmd, cwd=cwd, check=True, text=True, capture_output=True)
    return out.stdout.strip()

def _clone_or_update():
    if not PY_REPO.exists():
        print(f"[CLONE] TheAlgorithms/Python -> {PY_REPO}")
        # Full history but no file contents until needed (saves bandwidth/disk)
        _run([
            "git", "clone",
            "--filter=blob:none",        # partial clone (faster than full)
            "--no-tags",
            "https://github.com/TheAlgorithms/Python.git",
            str(PY_REPO),
        ])
    else:
        print("[PULL ] Fetching updates (full history)…")
        # If the repo is shallow, unshallow it first
        try:
            _run(["git", "rev-parse", "--is-shallow-repository"], cwd=PY_REPO)
            _run(["git", "fetch", "--unshallow", "--quiet"], cwd=PY_REPO)
        except subprocess.CalledProcessError:
            pass
        # Always ensure we have all refs/tags
        _run(["git", "fetch", "--all", "--tags", "--prune", "--quiet"], cwd=PY_REPO)

def _default_branch(repo_dir: Path) -> str:
    # Ask Git what the remote default branch is (works even if it's not 'main' or 'master')
    try:
        ref = _run(
            ["git", "symbolic-ref", "refs/remotes/origin/HEAD"],
            cwd=repo_dir
        )
        # returns e.g. "refs/remotes/origin/main"
        return ref.strip().split("/")[-1]
    except subprocess.CalledProcessError:
        # Fallbacks
        for cand in ("main", "master"):
            try:
                _run(["git", "rev-parse", f"origin/{cand}"], cwd=repo_dir)
                return cand
            except subprocess.CalledProcessError:
                continue
        raise SystemExit("[ERROR] Could not determine default branch.")

def _checkout_asof(cutoff_iso: str = "2021-12-31 23:59:59"):
    branch = _default_branch(PY_REPO)  # e.g., "main" or "master"
    print(f"[PIN  ] Find last commit on origin/{branch} <= {cutoff_iso}")

    # Ensure history is present
    _run(["git", "fetch", "origin", branch, "--quiet"], cwd=PY_REPO)

    # Find the commit before cutoff on the default branch
    commit = _run(
        ["git", "rev-list", "-n", "1", f'--before={cutoff_iso}', f"origin/{branch}"],
        cwd=PY_REPO
    )
    if not commit:
        raise SystemExit("[ERROR] Could not find a commit before cutoff. Repository history may be missing.")

    # Checkout detached HEAD at that commit
    _run(["git", "checkout", "--detach", commit], cwd=PY_REPO)
    print(f"[OK   ] Pinned to {commit[:10]} (<= {cutoff_iso})")

# ----------------- file discovery -----------------

SKIP_FILE_RE = re.compile(
    r"""(
        ^__init__\.py$|
        test_.*\.py$|
        .*_test\.py$|
        .*benchmark.*\.py$|
        .*example.*\.py$|
        setup\.py$|
        docs?\/.*|
        scripts?\/.*|
        notebooks?\/.*|
        .*\/tests?\/.*|
        .*\/contrib\/.*
    )""",
    re.IGNORECASE | re.VERBOSE
)

def _is_candidate(path: Path) -> bool:
    if path.suffix != ".py":
        return False
    name = path.name
    full = str(path)
    if SKIP_FILE_RE.search(name) or SKIP_FILE_RE.search(full):
        return False
    return True

def _category_rank(p: Path) -> int:
    parts = [seg.lower() for seg in p.parts]
    for i, cat in enumerate(CANDIDATE_DIR_NAMES):
        if cat in parts:
            return i  # smaller is better
    return len(CANDIDATE_DIR_NAMES) + 1

def _collect_candidates(max_n: int = MAX_PROBLEMS) -> List[Path]:
    print("[SCAN ] Searching for Python algorithm files...")
    files: List[Path] = []
    for p in PY_REPO.rglob("*.py"):
        if _is_candidate(p):
            files.append(p)
    if not files:
        raise SystemExit("[ERROR] No candidate Python files found.")

    # Rank by (category priority, path length) to encourage diversity and stable ordering
    files_sorted = sorted(files, key=lambda p: (_category_rank(p), len(str(p))))
    # Deduplicate by basename to avoid many variants of same algo
    seen = set()
    chosen: List[Path] = []
    for f in files_sorted:
        base = f.stem.lower()
        if base in seen:
            continue
        seen.add(base)
        chosen.append(f)
        if len(chosen) >= max_n:
            break
    print(f"[OK   ] Selected {len(chosen)} files.")
    return chosen

# ----------------- description extraction -----------------

TRIPLE_QUOTE_DOCSTR = re.compile(r'^\s*(?P<q>"""|\'\'\')(?P<doc>.*?)(?P=q)', re.DOTALL)
TOP_COMMENT_BLOCK = re.compile(r'^(?:\s*#.*\n){1,20}', re.MULTILINE)

def _extract_description(src: str) -> str:
    """
    Try docstring at top; else top comment block; else synthesize from filename later.
    """
    m = TRIPLE_QUOTE_DOCSTR.search(src)
    if m:
        doc = m.group("doc").strip()
        # Use first 2 sentences or 300 chars
        doc = re.sub(r"\s+", " ", doc)
        return doc[:300]
    m2 = TOP_COMMENT_BLOCK.search(src)
    if m2:
        block = m2.group(0)
        # Strip '# ' prefixes; collapse lines
        lines = [re.sub(r'^\s*#\s?', '', ln).strip() for ln in block.splitlines()]
        doc = " ".join([ln for ln in lines if ln])
        return doc[:300]
    return ""

def _slug_from_filename(path: Path) -> str:
    s = path.stem.lower()
    s = re.sub(r'[_\-\s]+', '_', s)
    s = re.sub(r'[^a-z0-9_]', '', s)
    return s or "problem"

def _make_header(slug: str, description: str) -> str:
    desc = description if description else (
        "Solve the canonical algorithmic task implied by this filename. "
        "Write clean, efficient code and consider edge cases."
    )
    return f"# Problem: {slug}\n# Description: {desc}\n\n"

# ----------------- main write -----------------

def _write_problem_file(src_path: Path, out_dir: Path):
    code = src_path.read_text(encoding="utf-8", errors="ignore")
    desc = _extract_description(code)
    slug = _slug_from_filename(src_path)
    header = _make_header(slug, desc)
    out_path = out_dir / f"{slug}.py"
    out_path.write_text(header + code, encoding="utf-8")
    print(f"[WRITE] {out_path.relative_to(ROOT)}")

# ----------------- entrypoint -----------------

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print("[STEP ] Clone/update TheAlgorithms/Python")
    _clone_or_update()
    _checkout_asof("2021-12-31 23:59:59")

    print("[STEP ] Select Python files (target = 50)")
    candidates = _collect_candidates(MAX_PROBLEMS)

    print(f"[STEP ] Writing {len(candidates)} Python problems to {HUMAN_DIR}")
    for p in candidates:
        _write_problem_file(p, HUMAN_DIR)

    print("[DONE ] Python-only dataset ready in data/human/")

if __name__ == "__main__":
    main()
