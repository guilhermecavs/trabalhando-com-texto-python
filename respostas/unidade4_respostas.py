"""
Solucoes-modelo do Conjunto de Exercicios 4 -- Avaliando modelos de linguagem.
(Consulte apenas depois de tentar resolver por conta propria!)
"""


def concordancia_percentual(anot_a: list, anot_b: list) -> float:
    iguais = sum(1 for a, b in zip(anot_a, anot_b) if a == b)
    return iguais / len(anot_a)


def kappa_cohen(observada: float, esperada: float) -> float:
    return (observada - esperada) / (1 - esperada)


def acuracia(gold: list, pred: list) -> float:
    corretos = sum(1 for g, p in zip(gold, pred) if g == p)
    return corretos / len(gold)


def precisao_classe(gold: list, pred: list, classe) -> float:
    previstos = sum(1 for p in pred if p == classe)
    if previstos == 0:
        return 0.0
    corretos = sum(1 for g, p in zip(gold, pred) if p == classe and g == classe)
    return corretos / previstos


def revocacao_classe(gold: list, pred: list, classe) -> float:
    reais = sum(1 for g in gold if g == classe)
    if reais == 0:
        return 0.0
    corretos = sum(1 for g, p in zip(gold, pred) if g == classe and p == classe)
    return corretos / reais


def f1(precisao: float, revocacao: float) -> float:
    if precisao + revocacao == 0:
        return 0.0
    return 2 * (precisao * revocacao) / (precisao + revocacao)
