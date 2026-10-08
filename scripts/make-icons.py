#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["fonttools", "cairosvg", "pillow"]
# ///
"""Export the "rbw" monogram as favicons and an Apple touch icon.

Run by hand when the mark or the accent colour changes: scripts/make-icons.py

The letters are drawn as outlines from IBM Plex Mono Medium, read from
_local/fonts/ (which git ignores), so the icons need no font to render.
Colours come from design/tokens.json. The SVG follows the system theme;
the PNG and ICO files use the light values.
"""

import io
import json
from pathlib import Path

import cairosvg
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "_local" / "fonts" / "ibmplexmono" / "IBMPlexMono-Medium.ttf"

TEXT = "rbw"
SIDE = 64  # viewBox units
# The header mark sets 12.5px type in a 34px square. An icon is seen far
# smaller, so the letters are enlarged to fill most of the square.
FONT_SIZE = 0.44 * SIDE


def letters_path() -> str:
    font = TTFont(FONT)
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    upem = font["head"].unitsPerEm
    scale = FONT_SIZE / upem

    names = [cmap[ord(ch)] for ch in TEXT]
    width = sum(glyphs[n].width for n in names) * scale
    # Centre on the midpoint between the x-height and the ascender of "b".
    os2 = font["OS/2"]
    height = (os2.sxHeight + os2.sCapHeight) / 2 * scale
    x = (SIDE - width) / 2
    baseline = (SIDE + height) / 2

    pen = SVGPathPen(glyphs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    for name in names:
        glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, baseline)))
        x += glyphs[name].width * scale
    return pen.getCommands()


def svg(path: str, light: dict, dark: dict | None) -> str:
    style = f".g{{fill:{light['accent']}}}.t{{fill:{light['on-accent']}}}"
    if dark:
        style += (
            "@media (prefers-color-scheme:dark){"
            f".g{{fill:{dark['accent']}}}.t{{fill:{dark['on-accent']}}}}}"
        )
        fills = ('class="g"', 'class="t"')
        style = f"<style>{style}</style>"
    else:
        fills = (f'fill="{light["accent"]}"', f'fill="{light["on-accent"]}"')
        style = ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIDE} {SIDE}">'
        f"<title>rbw</title>{style}"
        f'<rect {fills[0]} width="{SIDE}" height="{SIDE}"/>'
        f'<path {fills[1]} d="{path}"/></svg>\n'
    )


def png(static_svg: str, size: int) -> Image.Image:
    data = cairosvg.svg2png(bytestring=static_svg.encode(), output_width=size, output_height=size)
    return Image.open(io.BytesIO(data)).convert("RGB")


def main() -> None:
    tokens = json.loads((ROOT / "design" / "tokens.json").read_text(encoding="utf-8"))
    colors = {t["name"]: t["value"] for t in tokens["color"]["tokens"]}
    light = {k: colors[k]["light"] for k in ("accent", "on-accent")}
    dark = {k: colors[k]["dark"] for k in ("accent", "on-accent")}

    path = letters_path()
    img = ROOT / "assets" / "img"
    img.mkdir(parents=True, exist_ok=True)

    (img / "favicon.svg").write_text(svg(path, light, dark), encoding="utf-8")
    static = svg(path, light, None)
    png(static, 32).save(img / "favicon-32.png", optimize=True)
    png(static, 192).save(img / "favicon-192.png", optimize=True)
    png(static, 180).save(ROOT / "apple-touch-icon.png", optimize=True)
    png(static, 48).save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print("Wrote favicon.svg, favicon-32.png, favicon-192.png, apple-touch-icon.png, favicon.ico")


if __name__ == "__main__":
    main()
