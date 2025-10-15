# utils/coupling.py
"""
Lightweight coupling metrics for single-file solutions in Python/Java.

Outputs (per file):
- fan_in:  avg inbound calls per function
- fan_out: avg outbound calls per function
- imports: number of import/package dependencies
- coupling_index: (fan_in + fan_out + normalized_imports)
Where normalized_imports = imports / max(total_functions, 1)

Notes:
- Python uses the stdlib 'ast' for precise intra-file call graphs.
- Java uses regex heuristics (good enough for single-class contest code).
"""

from __future__ import annotations
import os, re
from dataclasses import dataclass
from typing import Dict, Set, List

# ---------- Public API ----------

def compute_coupling(filepath: str, lang: str | None = None) -> Dict[str, float]:
    if lang is None:
        lang = "Python" if os.path.splitext(filepath)[1] == ".py" else "Java"
    if lang == "Python":
        return _py_compute(filepath)
    else:
        return _java_compute(filepath)

# ---------- Python (AST-based) ----------

def _py_compute(filepath: str) -> Dict[str, float]:
    import ast

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        src = f.read()

    try:
        tree = ast.parse(src)
    except Exception:
        return {"fan_in": 0.0, "fan_out": 0.0, "imports": 0.0, "coupling_index": 0.0}

    # collect functions
    funcs: Set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            funcs.add(node.name)

    # build intra-file call graph
    edges: List[tuple[str, str]] = []
    func_stack: List[str] = []

    class CallCollector(ast.NodeVisitor):
        def visit_FunctionDef(self, node: ast.FunctionDef):
            func_stack.append(node.name)
            self.generic_visit(node)
            func_stack.pop()

        def visit_Call(self, node: ast.Call):
            if func_stack:
                caller = func_stack[-1]
                callee = _py_call_name(node.func)
                if callee in funcs and callee != caller:
                    edges.append((caller, callee))
            self.generic_visit(node)

    def _py_call_name(n) -> str:
        # foo() or obj.foo()
        if isinstance(n, ast.Name):
            return n.id
        if isinstance(n, ast.Attribute):
            return n.attr
        return ""

    CallCollector().visit(tree)

    # imports
    import_count = 0
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            import_count += 1

    total_funcs = max(len(funcs), 1)
    out_deg = _out_degrees(edges)
    in_deg = _in_degrees(edges)

    fan_out = sum(out_deg.get(f, 0) for f in funcs) / total_funcs
    fan_in = sum(in_deg.get(f, 0) for f in funcs) / total_funcs
    coupling_index = round(fan_in + fan_out + (import_count / total_funcs), 3)

    return {
        "fan_in": round(fan_in, 3),
        "fan_out": round(fan_out, 3),
        "imports": float(import_count),
        "coupling_index": coupling_index,
    }

# ---------- Java (regex heuristics) ----------

JAVA_METHOD_DEF = re.compile(
    r"(?:public|private|protected)?\s*(?:static\s+)?(?:[\w\<\>\[\]]+\s+)+(?P<name>\w+)\s*\(",
    re.MULTILINE,
)
JAVA_METHOD_CALL = re.compile(r"(?P<name>\b[A-Za-z_][A-Za-z0-9_]*\b)\s*\(", re.MULTILINE)
JAVA_IMPORT = re.compile(r"^\s*import\s+[\w\.]+;", re.MULTILINE)

def _java_compute(filepath: str) -> Dict[str, float]:
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            src = f.read()
    except Exception:
        return {"fan_in": 0.0, "fan_out": 0.0, "imports": 0.0, "coupling_index": 0.0}

    # functions/methods declared in the file
    funcs = {m.group("name") for m in JAVA_METHOD_DEF.finditer(src)}
    if not funcs:
        return {"fan_in": 0.0, "fan_out": 0.0, "imports": 0.0, "coupling_index": 0.0}

    # all call-like tokens; filter to known funcs
    calls = [m.group("name") for m in JAVA_METHOD_CALL.finditer(src)]
    # rough partition by method body: attribute-level precision is out-of-scope here,
    # so we approximate: count occurrences of callee names inside file for fan-out.
    edges: List[tuple[str, str]] = []
    for caller in funcs:
        # naive body range: from first occurrence of method signature to next method or EOF
        sig = re.search(rf"\b{re.escape(caller)}\s*\(", src)
        if not sig:
            continue
        start = sig.start()
        # find next method def after 'start'
        nxt = None
        for m in JAVA_METHOD_DEF.finditer(src, start + 1):
            nxt = m.start()
            break
        body = src[start:nxt] if nxt else src[start:]
        body_calls = [m.group("name") for m in JAVA_METHOD_CALL.finditer(body)]
        for callee in body_calls:
            if callee in funcs and callee != caller:
                edges.append((caller, callee))

    import_count = len(JAVA_IMPORT.findall(src))
    total_funcs = max(len(funcs), 1)

    out_deg = _out_degrees(edges)
    in_deg = _in_degrees(edges)

    fan_out = sum(out_deg.get(f, 0) for f in funcs) / total_funcs
    fan_in = sum(in_deg.get(f, 0) for f in funcs) / total_funcs
    coupling_index = round(fan_in + fan_out + (import_count / total_funcs), 3)

    return {
        "fan_in": round(fan_in, 3),
        "fan_out": round(fan_out, 3),
        "imports": float(import_count),
        "coupling_index": coupling_index,
    }

# ---------- helpers ----------

def _out_degrees(edges: List[tuple[str, str]]) -> Dict[str, int]:
    outd: Dict[str, int] = {}
    for u, v in edges:
        outd[u] = outd.get(u, 0) + 1
    return outd

def _in_degrees(edges: List[tuple[str, str]]) -> Dict[str, int]:
    ind: Dict[str, int] = {}
    for u, v in edges:
        ind[v] = ind.get(v, 0) + 1
    return ind
