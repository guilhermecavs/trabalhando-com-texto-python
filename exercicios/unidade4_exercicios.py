"""
================================================================================
 Conjunto de Exercicios 4 -- Avaliando modelos de linguagem
 Curso: Trabalhando com Texto em Python I (CiberExt 26-29 / FEELT38103 / UFU)
================================================================================

Edite ESTE arquivo, substituindo cada `todo(...)` pela sua solucao.
Verifique (dentro da pasta 'exercicios'):

    python3 -m unittest unidade4_test

Aqui voce IMPLEMENTA as metricas na mao (sem bibliotecas), para entender como
funcionam a concordancia, o kappa de Cohen, a acuracia, a precisao, a
revocacao e o F1-score.
--------------------------------------------------------------------------------
"""

from mooc.todo import todo


# ------------------------------------------------------------------------------
# Ex 1: concordancia_percentual
# Duas listas de anotacoes (mesmo tamanho). Retorne a proporcao de posicoes em
# que os dois anotadores concordaram (numero entre 0.0 e 1.0).
# Exemplos:
#   concordancia_percentual(['a','b','c'], ['a','x','c'])  ==>  0.6666...
#   concordancia_percentual(['a','a'], ['b','b'])           ==>  0.0
def concordancia_percentual(anot_a: list, anot_b: list) -> float:
    return todo(anot_a, anot_b)


# ------------------------------------------------------------------------------
# Ex 2: kappa_cohen
# Dado a concordancia observada e a esperada por acaso, calcule o kappa de Cohen:
#   kappa = (observada - esperada) / (1 - esperada)
# Exemplos:
#   kappa_cohen(0.8, 0.5)  ==>  0.6
#   kappa_cohen(0.5, 0.5)  ==>  0.0
def kappa_cohen(observada: float, esperada: float) -> float:
    return todo(observada, esperada)


# ------------------------------------------------------------------------------
# Ex 3: acuracia
# Listas 'gold' (padrao-ouro) e 'pred' (previsoes), mesmo tamanho. Retorne a
# proporcao de previsoes corretas.
# Exemplo:
#   acuracia(['ADJ','NOUN','VERB'], ['ADJ','NOUN','ADJ'])  ==>  0.6666...
def acuracia(gold: list, pred: list) -> float:
    return todo(gold, pred)


# ------------------------------------------------------------------------------
# Ex 4: precisao_classe
# Precisao para uma classe especifica: das vezes em que o modelo PREVIU essa
# classe, quantas estavam certas. Se o modelo nunca previu essa classe, retorne
# 0.0 (evite divisao por zero).
# Exemplo (classe 'VERB'):
#   gold = ['NOUN','VERB','VERB'], pred = ['VERB','VERB','NOUN']
#   previu 'VERB' 2 vezes (indices 0 e 1); acertou 1 (indice 1) -> 0.5
def precisao_classe(gold: list, pred: list, classe) -> float:
    return todo(gold, pred, classe)


# ------------------------------------------------------------------------------
# Ex 5: revocacao_classe
# Revocacao para uma classe: dos exemplos que REALMENTE sao dessa classe (no
# gold), quantos o modelo encontrou. Se a classe nao aparece no gold, retorne
# 0.0.
# Exemplo (classe 'VERB'):
#   gold = ['NOUN','VERB','VERB'], pred = ['VERB','VERB','NOUN']
#   ha 2 'VERB' no gold (indices 1 e 2); o modelo acertou 1 (indice 1) -> 0.5
def revocacao_classe(gold: list, pred: list, classe) -> float:
    return todo(gold, pred, classe)


# ------------------------------------------------------------------------------
# Ex 6: f1
# F1-score a partir da precisao e da revocacao:
#   f1 = 2 * (p * r) / (p + r)
# Se p + r == 0, retorne 0.0.
# Exemplo:
#   f1(0.5, 1.0)  ==>  0.6666...
def f1(precisao: float, revocacao: float) -> float:
    return todo(precisao, revocacao)
