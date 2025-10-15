import os, re

WHY_WORDS = [
    "because", "so that", "to avoid", "trade-off", "rationale", "reason",
    "edge case", "complexity", "time complexity", "space complexity", "stability"
]

COMMENT_REGEX = {
    "Python": r"#.*",
    "Java": r"//.*|/\*[\s\S]*?\*/"
}

def analyze_comments(filepath):
    lang = "Python" if os.path.splitext(filepath)[1] == ".py" else "Java"
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        code = f.read()
    pattern = re.compile(COMMENT_REGEX[lang])
    comments = pattern.findall(code)
    comment_text = " ".join(comments).lower()
    density = len(comments) / max(len(code.splitlines()), 1)
    words = len(comment_text.split()) or 1
    why_hits = sum(kw in comment_text for kw in WHY_WORDS)
    why_ratio = why_hits / words
    return {"density": density, "why_ratio": why_ratio}
