"""
Solucoes-modelo do Conjunto de Exercicios 1 -- Manipulando texto com Python.
(Consulte apenas depois de tentar resolver por conta propria!)
"""

import re


def contar_linhas(texto: str) -> int:
    return texto.count("\n")


def primeiros_n(texto: str, n: int) -> str:
    return texto[:n]


def separar_paragrafos(texto: str) -> list:
    return [p for p in texto.split("   ") if p != ""]


def padronizar_aspas(texto: str) -> str:
    pipeline = [("“", '"'), ("”", '"'), ("‘", '"'), ("’", '"')]
    for antigo, novo in pipeline:
        texto = texto.replace(antigo, novo)
    return texto


def remover_pontuacao_repetida(texto: str) -> str:
    padrao = re.compile(r"(\.|,){2,}")
    return padrao.sub("", texto)


def normalizar_espacos(texto: str) -> str:
    return re.sub(r" {2,}", " ", texto)
