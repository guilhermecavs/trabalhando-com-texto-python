#!/usr/bin/env bash
# Roda todos os conjuntos de exercicios (correcao automatica).
# Uso:  ./rodar_testes.sh
cd "$(dirname "$0")" || exit 1
python3 -m unittest discover -p "unidade*_test.py" -v
