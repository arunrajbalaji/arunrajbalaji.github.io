#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["fonttools[woff]"]
# ///
"""Subset the site's fonts to Latin and write them to assets/fonts/ as WOFF2.

Run by hand when a font changes: scripts/subset-fonts.py

Sources are read from _local/fonts/, which git ignores:
  barlow/Barlow-{Regular,Medium,SemiBold}.ttf      github.com/google/fonts, ofl/barlow
  sourceserif4/SourceSerif4-Italic[opsz,wght].ttf  github.com/google/fonts, ofl/sourceserif4
  plex-official/IBMPlexMono-{Regular,Medium}-Latin1.woff2
                                                   npm @ibm/plex-mono, fonts/split/woff2

IBM Plex reserves its font name, so its files are IBM's own Latin subset,
copied unchanged. Barlow and Source Serif 4 are subset here.
"""

import shutil
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_local" / "fonts"
OUT = ROOT / "assets" / "fonts"

# Basic Latin, Latin-1, common punctuation, arrows and the minus sign.
# Keep in step with the unicode-range in assets/css/site.css.
LATIN = (
    "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,"
    "U+2000-206F,U+20AC,U+2122,U+2190-2193,U+2212,U+2215,U+FEFF,U+FFFD"
)

# Optical size for the figure-label style, which is the only use of the serif.
SERIF_OPSZ = 12


def write_subset(font: TTFont, name: str) -> None:
    options = subset.Options()
    options.flavor = "woff2"
    options.layout_features = ["*"]
    options.unicodes = subset.parse_unicodes(LATIN)
    subsetter = subset.Subsetter(options)
    subsetter.populate(unicodes=options.unicodes)
    subsetter.subset(font)
    path = OUT / name
    subset.save_font(font, str(path), options)
    print(f"{name}: {path.stat().st_size / 1024:.1f} kB")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    for weight in ("Regular", "Medium", "SemiBold"):
        write_subset(TTFont(SRC / "barlow" / f"Barlow-{weight}.ttf"), f"Barlow-{weight}.woff2")

    serif = TTFont(SRC / "sourceserif4" / "SourceSerif4-Italic[opsz,wght].ttf")
    serif = instancer.instantiateVariableFont(serif, {"wght": 400, "opsz": SERIF_OPSZ})
    write_subset(serif, "SourceSerif4-Italic.woff2")

    for weight in ("Regular", "Medium"):
        name = f"IBMPlexMono-{weight}-Latin1.woff2"
        shutil.copyfile(SRC / "plex-official" / name, OUT / name)
        print(f"{name}: {(OUT / name).stat().st_size / 1024:.1f} kB (copied)")

    for family, name in (("barlow", "Barlow"), ("sourceserif4", "SourceSerif4"), ("ibmplexmono", "IBMPlexMono")):
        shutil.copyfile(SRC / family / "OFL.txt", OUT / f"{name}-OFL.txt")


if __name__ == "__main__":
    main()
