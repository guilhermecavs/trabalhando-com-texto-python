"""
Solucoes-modelo do Conjunto de Exercicios 2 -- Processando textos com spaCy.
(Consulte apenas depois de tentar resolver por conta propria!)
"""


def lemas_dos_verbos(doc: list) -> list:
    return [t["lemma"] for t in doc if t["pos"] == "VERB"]


def tokens_sem_pontuacao(doc: list) -> list:
    return [t["text"] for t in doc if t["pos"] != "PUNCT"]


def contar_por_classe(doc: list) -> dict:
    contagem = {}
    for t in doc:
        pos = t["pos"]
        contagem[pos] = contagem.get(pos, 0) + 1
    return contagem


def entidades_do_tipo(entidades: list, label: str) -> list:
    return [e["text"] for e in entidades if e["label"] == label]


def classe_mais_frequente(doc: list):
    if not doc:
        return None
    contagem = {}
    for t in doc:
        pos = t["pos"]
        contagem[pos] = contagem.get(pos, 0) + 1
    # max() preserva o primeiro em caso de empate porque itera na ordem de insercao
    return max(contagem, key=contagem.get)
