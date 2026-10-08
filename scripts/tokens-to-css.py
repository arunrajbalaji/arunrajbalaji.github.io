#!/usr/bin/env python3
"""Write the custom properties in assets/css/site.css from design/tokens.json.

Only the block between the "tokens:start" and "tokens:end" comments is replaced.

Run by hand after editing the tokens:  python3 scripts/tokens-to-css.py
Check without writing:                 python3 scripts/tokens-to-css.py --check
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "design" / "tokens.json"
CSS = ROOT / "assets" / "css" / "site.css"

START = "/* tokens:start (generated from design/tokens.json by scripts/tokens-to-css.py) */"
END = "/* tokens:end */"


def css_value(value: str) -> str:
    """Turn a "{name}" reference into var(--name); pass other values through."""
    return re.sub(r"\{([a-z0-9-]+)\}", r"var(--\1)", value)


def build() -> str:
    tokens = json.loads(TOKENS.read_text(encoding="utf-8"))
    colors = tokens["color"]["tokens"]

    light = ["  color-scheme: light dark;", ""]
    light += [f"  --{t['name']}: {css_value(t['value']['light'])};" for t in colors]
    light.append("")
    light += [f"  --font-{name}: {stack};" for name, stack in tokens["type"]["families"].items()]
    for group in ("spacing", "radius", "border", "size", "fluid"):
        light.append("")
        light += [f"  --{t['name']}: {t['value']};" for t in tokens[group]["tokens"]]

    # A token that points at another token follows it into the dark theme by itself.
    dark = [
        f"    --{t['name']}: {css_value(t['value']['dark'])};"
        for t in colors
        if t["value"]["dark"] != t["value"]["light"]
    ]

    return "\n".join(
        [START, ":root {", *light, "}", "", "@media (prefers-color-scheme: dark) {", "  :root {", *dark, "  }", "}", END]
    )


def main() -> int:
    css = CSS.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(css):
        print(f"{CSS.relative_to(ROOT)}: token markers not found", file=sys.stderr)
        return 1
    updated = pattern.sub(lambda _: build(), css)
    if "--check" in sys.argv[1:]:
        if updated != css:
            print(f"{CSS.relative_to(ROOT)} is out of date with design/tokens.json", file=sys.stderr)
            return 1
        print("Tokens in site.css match design/tokens.json.")
        return 0
    CSS.write_text(updated, encoding="utf-8")
    print(f"Wrote tokens to {CSS.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
