#!/usr/bin/env python3
"""Check that every page repeats the canonical skip link, header and footer.

The canonical copy is scripts/chrome.html. A page may differ from it only by
aria-current="page" on at most one header navigation link. Redirect stubs
(pages with a meta refresh) carry no header or footer and are skipped.

Run before every commit that touches a page:  python3 scripts/check-chrome.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = ROOT / "scripts" / "chrome.html"
SKIP_DIRS = {".git", "_local", "assets", "content", "design", "docs", "scripts", "wp-content"}

BLOCKS = {
    "skip link": re.compile(r'<a class="rb-skip".*?</a>', re.S),
    "header": re.compile(r'<header class="rb-header">.*?</header>', re.S),
    "footer": re.compile(r'<footer class="rb-footer">.*?</footer>', re.S),
}
CURRENT = ' aria-current="page"'
REFRESH = re.compile(r'<meta[^>]+http-equiv="refresh"', re.I)


def normalise(block: str) -> str:
    """Drop indentation and trailing space, so nesting depth does not matter."""
    return "\n".join(line.strip() for line in block.strip().splitlines())


def pages() -> list[Path]:
    found = []
    for path in sorted(ROOT.rglob("*.html")):
        parts = path.relative_to(ROOT).parts
        if parts[0] in SKIP_DIRS or any(p.startswith(".") for p in parts):
            continue
        found.append(path)
    return found


def check(path: Path, canonical: dict[str, str]) -> list[str]:
    html = path.read_text(encoding="utf-8")
    if REFRESH.search(html):
        return []
    problems = []
    for name, pattern in BLOCKS.items():
        matches = pattern.findall(html)
        if len(matches) != 1:
            problems.append(f"expected one {name}, found {len(matches)}")
            continue
        block = normalise(matches[0])
        if name == "header":
            if block.count(CURRENT) > 1:
                problems.append("more than one aria-current in the header")
            if re.search(r'<a class="rb-brand"[^>]*aria-current', block):
                problems.append("aria-current belongs on a navigation link, not the name")
            block = block.replace(CURRENT, "")
        elif CURRENT in block:
            problems.append(f"aria-current is not allowed in the {name}")
        if block != canonical[name]:
            problems.append(f"{name} differs from scripts/chrome.html")
    return problems


def main() -> int:
    source = CANONICAL.read_text(encoding="utf-8")
    canonical = {name: normalise(pattern.search(source).group(0)) for name, pattern in BLOCKS.items()}

    failed = 0
    checked = pages()
    for path in checked:
        for problem in check(path, canonical):
            print(f"{path.relative_to(ROOT)}: {problem}")
            failed += 1
    if failed:
        return 1
    print(f"Header and footer match on {len(checked)} page(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
