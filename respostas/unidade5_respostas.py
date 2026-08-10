"""
Solucoes-modelo do Conjunto de Exercicios 5 -- Gerenciando dados textuais.
(Consulte apenas depois de tentar resolver por conta propria!)
"""


def filtrar(linhas: list, coluna: str, valor) -> list:
    return [linha for linha in linhas if linha[coluna] == valor]


def adicionar_n_chars(linhas: list) -> list:
    novas = []
    for linha in linhas:
        nova = dict(linha)  # copia para nao modificar a original
        nova["n_chars"] = len(linha["text"])
        novas.append(nova)
    return novas


def razao_comentarios(linhas: list) -> list:
    novas = []
    for linha in linhas:
        nova = dict(linha)
        if linha["ncomments"] == 0:
            nova["ratio"] = None
        else:
            nova["ratio"] = linha["ntop"] / linha["ncomments"]
        novas.append(nova)
    return novas


def media_ignorando_none(linhas: list, coluna: str):
    validos = [linha[coluna] for linha in linhas if linha[coluna] is not None]
    if not validos:
        return None
    return sum(validos) / len(validos)


def filtrar_dois_criterios(linhas: list, autor: str, min_comentarios: int) -> list:
    return [
        linha
        for linha in linhas
        if linha["author"] == autor and linha["ncomments"] >= min_comentarios
    ]
