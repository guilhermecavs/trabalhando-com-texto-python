#!/usr/bin/env bash
# ============================================================================
#  gerar_pdfs.sh — compila as 5 unidades (.tex) em PDF com pdflatex
#  Curso: Trabalhando com Texto em Python I (CiberExt 26-29 / FEELT38103 / UFU)
#
#  USO:   ./gerar_pdfs.sh
#  Requer: pdflatex no PATH (MacTeX ou BasicTeX + pacotes).
#          Rode 'chmod +x gerar_pdfs.sh' uma vez para torná-lo executável.
# ============================================================================
set -u

# Garante que o PATH inclui o MacTeX/BasicTeX (caso o terminal nao tenha recarregado)
export PATH="/Library/TeX/texbin:$PATH"

# Pasta onde este script esta (raiz do repositorio)
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT" || exit 1

if ! command -v pdflatex >/dev/null 2>&1; then
  echo "ERRO: pdflatex nao encontrado no PATH."
  echo "Instale o MacTeX (brew install --cask mactex-no-gui) ou o BasicTeX,"
  echo "feche e reabra o terminal, e rode este script de novo."
  exit 1
fi

echo "pdflatex: $(command -v pdflatex)"
echo

ok=0
fail=0
falhas=()

# Encontra todos os .tex nas pastas Unidade-*, em ordem
for tex in Unidade-*/*.tex; do
  [ -e "$tex" ] || continue
  dir="$(dirname "$tex")"
  file="$(basename "$tex")"
  base="${file%.tex}"

  echo "==> Compilando $tex"
  # Roda 2x para resolver indice/links/referencias
  (
    cd "$dir" || exit 1
    pdflatex -interaction=nonstopmode -halt-on-error "$file" >/dev/null 2>&1
    pdflatex -interaction=nonstopmode -halt-on-error "$file" >/dev/null 2>&1
  )

  if [ -f "$dir/$base.pdf" ]; then
    echo "    OK  -> $dir/$base.pdf"
    ok=$((ok+1))
  else
    echo "    FALHOU (veja $dir/$base.log)"
    fail=$((fail+1))
    falhas+=("$dir/$base.log")
  fi
  echo
done

# Limpa arquivos auxiliares gerados pela compilacao.
# Mantem os .log quando houve falha, para inspecionar o erro.
echo "==> Limpando arquivos auxiliares (.aux .out .toc ...)"
LOG_CLEAN=""
[ "$fail" -eq 0 ] && LOG_CLEAN="-o -name *.log"
# shellcheck disable=SC2086
find Unidade-* -type f \( -name '*.aux' -o -name '*.out' \
  -o -name '*.toc' -o -name '*.fls' -o -name '*.fdb_latexmk' \
  -o -name '*.synctex.gz' -o -name '*.listing' $LOG_CLEAN \) -delete 2>/dev/null

echo
echo "======================================"
echo "  Concluido: $ok PDF(s) gerado(s), $fail falha(s)."
if [ "$fail" -gt 0 ]; then
  echo "  Logs com erro:"
  for l in "${falhas[@]}"; do echo "   - $l"; done
  echo "  (Se falhar por pacote ausente no BasicTeX, rode:"
  echo "     sudo tlmgr install <nome-do-pacote>)"
fi
echo "======================================"
