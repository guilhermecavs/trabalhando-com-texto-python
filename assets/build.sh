#!/usr/bin/env bash
# ============================================================================
#  build.sh — gera HTML, LaTeX e PDF a partir do markdown-fonte de uma unidade
#  (fonte unica via pandoc). Uso:  assets/build.sh Unidade-1/unidade1_*.md
#  Sem argumento: processa todas as unidades.
# ============================================================================
set -e
export PATH="/opt/homebrew/bin:/Library/TeX/texbin:$PATH"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ASSETS="$ROOT/assets"

build_one() {
  local SRC="$1"
  local DIR BASE
  DIR="$(cd "$(dirname "$SRC")" && pwd)"
  BASE="$(basename "$SRC" .md)"
  ( cd "$DIR"
    # HTML autossuficiente (CSS embutido, math via MathML — funciona offline)
    pandoc "$BASE.md" -s --embed-resources --standalone \
      --css "$ASSETS/estilo.css" --lua-filter "$ASSETS/callouts.lua" \
      --highlight-style breezedark --mathml --toc --toc-depth=2 \
      -o "$BASE.html"
    # LaTeX + PDF
    pandoc "$BASE.md" -s --lua-filter "$ASSETS/callouts.lua" \
      -H "$ASSETS/cabecalho.tex" --highlight-style breezedark \
      -V documentclass=article -V fontsize=11pt -V geometry:margin=2.4cm \
      -V colorlinks=true -V linkcolor=accent -V urlcolor=cyan \
      --toc --toc-depth=2 -o "$BASE.tex"
    pdflatex -interaction=nonstopmode -halt-on-error "$BASE.tex" >/tmp/pl.log 2>&1 || true
    pdflatex -interaction=nonstopmode -halt-on-error "$BASE.tex" >/tmp/pl.log 2>&1 || true
    rm -f "$BASE.aux" "$BASE.log" "$BASE.out" "$BASE.toc"
    if [ -f "$BASE.pdf" ]; then echo "OK  $BASE (.html .tex .pdf)"; else echo "PDF FALHOU: $BASE (veja /tmp/pl.log)"; fi
  )
}

if [ -n "$1" ]; then
  build_one "$1"
else
  for f in "$ROOT"/Unidade-*/unidade*_*.md; do build_one "$f"; done
fi
