# -*- coding: utf-8 -*-
"""
脱敏脚本：将 SKILL.md 中的 Windows 绝对路径替换为 <YOUR_SKILL_PATH>
"""
import re
from pathlib import Path

SKILL_FILE = Path(__file__).resolve().parent / "SKILL.md"
PLACEHOLDER = "<YOUR_SKILL_PATH>"

# Windows 绝对路径：盘符 + 反斜杠 + 路径（允许空格、中文等）
# 匹配如 C:\Users\Administrator\... 或 c:\Users\Administrator\Desktop\Github分享\...
PATTERN = re.compile(
    r"[A-Za-z]:\\(?:[^\\<>*?|\n]+\\)*[^\\<>*?|\n]*",
    re.UNICODE
)

def main():
    if not SKILL_FILE.exists():
        print(f"ERROR: {SKILL_FILE} not found.")
        return 1
    text = SKILL_FILE.read_text(encoding="utf-8")
    original = text
    replacements = PATTERN.findall(text)
    if replacements:
        text = PATTERN.sub(PLACEHOLDER, text)
        SKILL_FILE.write_text(text, encoding="utf-8")
        print(f"Sanitized {len(replacements)} path(s) -> {PLACEHOLDER}")
    else:
        print("No Windows absolute paths found; SKILL.md unchanged.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
