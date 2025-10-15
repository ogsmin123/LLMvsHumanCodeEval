import os, re
from pathlib import Path
from typing import Tuple
from openai import OpenAI

OPENAI_MODEL = "gpt-4o"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

HUMAN_DIR = Path("data/human")
LLM_DIR = Path("data/llm")
LLM_DIR.mkdir(parents=True, exist_ok=True)

PROMPT = """You are a senior software engineer. Solve the task in the SAME LANGUAGE as the provided human file.
- Write clean, production-quality code using only the standard library.
- Include concise comments that explain WHY (design rationale, trade-offs, edge cases), not just WHAT.
- Do NOT add extra text; return ONLY the code file content (no markdown fences).
Task description and reference (human) are below.

{header}
"""

def _read_header_and_lang(p: Path) -> Tuple[str, str]:
    text = p.read_text(encoding="utf-8", errors="ignore")
    if p.suffix == ".py":
        lang = "Python"
        # Take the top comment block as header
        header = "\n".join(line for line in text.splitlines()[:20] if line.strip().startswith("#"))
    else:
        lang = "Java"
        # Capture top block comment if present
        m = re.search(r"/\*.*?\*/", text, flags=re.DOTALL)
        header = m.group(0) if m else "/* Java task */"
    return header, lang

def _extract_code(raw: str, lang: str) -> str:
    # Strip markdown fences if any; ensure pure code content
    raw = re.sub(r"^```[a-zA-Z]*\s*", "", raw.strip())
    raw = re.sub(r"\s*```$", "", raw)
    # For Java: encourage a single public class named Main (common for judge harnesses)
    if lang == "Java" and "class " not in raw:
        raw = "public class Main {\n" + raw + "\n}\n"
    return raw

def main():
    for src in HUMAN_DIR.glob("*.*"):
        if src.suffix not in (".py", ".java"):
            continue
        out = LLM_DIR / src.name
        print(f"[LLM] Generating for {src.name} ...")
        header, lang = _read_header_and_lang(src)
        prompt = PROMPT.format(header=header)

        # Send the human header only (not code) to avoid leaking solution content;
        # your study compares structures, not copying.
        resp = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        code = _extract_code(resp.choices[0].message.content, lang)
        out.write_text(code, encoding="utf-8")
        print(f"[OK] Saved {out}")

if __name__ == "__main__":
    main()
