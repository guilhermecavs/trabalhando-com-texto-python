"""
Solucoes-modelo do Conjunto de Exercicios 3 -- Customizando o pipeline do spaCy.
(Consulte apenas depois de tentar resolver por conta propria!)
"""


def componentes_ativos(todos: list, excluir: list) -> list:
    return [c for c in todos if c not in excluir]


def adicionar_componente(pipeline: list, nome: str) -> list:
    if nome in pipeline:
        return list(pipeline)
    return list(pipeline) + [nome]


def remover_componente(pipeline: list, nome: str) -> list:
    return [c for c in pipeline if c != nome]


def pipeline_ok(analise: dict) -> bool:
    return all(len(problemas) == 0 for problemas in analise.values())


def filtrar_por_idade(docs: list, limite: int) -> list:
    return [d["text"] for d in docs if d["age"] < limite]
