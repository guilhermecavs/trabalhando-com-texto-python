"""
================================================================================
 Conjunto de Exercicios 1 -- Manipulando texto com Python
 Curso: Trabalhando com Texto em Python I (CiberExt 26-29 / FEELT38103 / UFU)
================================================================================

Edite ESTE arquivo, substituindo cada chamada `todo(...)` pela sua solucao.
Depois, verifique suas respostas rodando (dentro da pasta 'exercicios'):

    python3 -m unittest unidade1_test

Voce tambem pode experimentar suas funcoes no interpretador:

    python3 -c "from unidade1_exercicios import contar_linhas; print(contar_linhas('a\\nb'))"

Este conjunto cobre: metodos de string (replace, split, join), pipelines de
substituicao com listas/tuplas e expressoes regulares (modulo 're').
--------------------------------------------------------------------------------
"""

import re

from mooc.todo import todo


# ------------------------------------------------------------------------------
# Ex 1: contar_linhas
# Retorne quantas quebras de linha ('\n') o texto contem.
# Exemplos:
#   contar_linhas("a\nb\nc")  ==>  2
#   contar_linhas("abc")       ==>  0
#   contar_linhas("")          ==>  0
def contar_linhas(texto: str) -> int:
    return todo(texto)


# ------------------------------------------------------------------------------
# Ex 2: primeiros_n
# Retorne os primeiros n caracteres do texto (uma "fatia"). Se n for maior que
# o tamanho do texto, retorne o texto inteiro.
# Exemplos:
#   primeiros_n("terrorism", 4)  ==>  "terr"
#   primeiros_n("abc", 10)        ==>  "abc"
def primeiros_n(texto: str, n: int) -> str:
    return todo(texto, n)


# ------------------------------------------------------------------------------
# Ex 3: separar_paragrafos
# O texto usa TRES espacos em branco como separador de paragrafos. Divida o
# texto nesses separadores e retorne uma lista de paragrafos, DESCARTANDO
# eventuais paragrafos vazios (string vazia).
# Exemplos:
#   separar_paragrafos("meta   p1   p2")  ==>  ["meta", "p1", "p2"]
#   separar_paragrafos("   so um")         ==>  ["so um"]
def separar_paragrafos(texto: str) -> list:
    return todo(texto)


# ------------------------------------------------------------------------------
# Ex 4: padronizar_aspas
# Use um "pipeline" (lista de tuplas) para trocar TODOS os tipos de aspas
# tortas por uma aspa dupla reta ("). Os caracteres a substituir sao:
#   “ (U+201C), ” (U+201D), ‘ (U+2018), ’ (U+2019)
# Exemplos:
#   padronizar_aspas("“oi”")   ==>  '"oi"'
#   padronizar_aspas("‘a’ ‘b’") ==>  "'a' 'b'".replace("'", '"')  (ou seja: "a" "b")
def padronizar_aspas(texto: str) -> str:
    return todo(texto)


# ------------------------------------------------------------------------------
# Ex 5: remover_pontuacao_repetida
# Use uma EXPRESSAO REGULAR para remover sequencias de DOIS OU MAIS pontos
# finais ou virgulas (ex.: '....', ',,,,', '..,,'), substituindo cada sequencia
# por string vazia. Pontos/virgulas isolados devem ser preservados.
# Dica: o padrao r'(\.|,){2,}'
# Exemplos:
#   remover_pontuacao_repetida("fim.... certo")  ==>  "fim certo"
#   remover_pontuacao_repetida("a,,,,b")          ==>  "ab"
#   remover_pontuacao_repetida("ok. bom, dia")    ==>  "ok. bom, dia"
def remover_pontuacao_repetida(texto: str) -> str:
    return todo(texto)


# ------------------------------------------------------------------------------
# Ex 6: normalizar_espacos
# Use uma expressao regular para trocar sequencias de DOIS OU MAIS espacos por
# UM unico espaco. (Considere apenas o caractere de espaco ' '.)
# Exemplos:
#   normalizar_espacos("a    b   c")  ==>  "a b c"
#   normalizar_espacos("sem extra")   ==>  "sem extra"
def normalizar_espacos(texto: str) -> str:
    return todo(texto)
