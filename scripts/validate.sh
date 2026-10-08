#!/usr/bin/env bash
# Validate the site's HTML and CSS with the Nu Html Checker (needs Java and gh).
# The checker is fetched once into _local/tools/, which git ignores.
# Run from anywhere: scripts/validate.sh [files...]
set -euo pipefail
cd "$(dirname "$0")/.."

jar=_local/tools/vnu.jar
if [ ! -f "$jar" ]; then
  mkdir -p "$(dirname "$jar")"
  gh release download latest -R validator/validator -p vnu.jar -D "$(dirname "$jar")"
fi

if [ "$#" -eq 0 ]; then
  # Every committed or new page and stylesheet, leaving out the design
  # reference previews, the canonical header and footer fragment, and vendored KaTeX.
  mapfile -t files < <(git ls-files -co --exclude-standard -- '*.html' '*.css' \
    ':!design/' ':!scripts/' ':!assets/katex/')
  set -- "${files[@]}"
fi

if [ "$#" -eq 0 ]; then
  echo "No pages to validate yet."
  exit 0
fi

exec java -jar "$jar" --also-check-css --errors-only "$@"
