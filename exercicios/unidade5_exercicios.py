"""
================================================================================
 Conjunto de Exercicios 5 -- Gerenciando dados textuais (logica de DataFrame)
 Curso: Trabalhando com Texto em Python I (CiberExt 26-29 / FEELT38103 / UFU)
================================================================================

Edite ESTE arquivo e verifique com:   python3 -m unittest unidade5_test

Para rodar em qualquer lugar (sem pandas), aqui uma TABELA e uma lista de
LINHAS, e cada linha e um dicionario {coluna: valor}:

    [{"filename": "a.txt", "text": "oi"}, {"filename": "b.txt", "text": "ola"}]

Correspondencia com o pandas real:
  socc.loc[socc['col'] == v]                 -> filtrar
  socc['n'] = socc['x'] / socc['y']          -> razao_comentarios
  socc['comments_ratio'].describe() (mean)   -> media_ignorando_none
  socc.loc[(A) & (B)]                        -> filtrar_dois_criterios
--------------------------------------------------------------------------------
"""

from mooc.todo import todo


# ------------------------------------------------------------------------------
# Ex 1: filtrar
# Retorne a lista das linhas em que o valor da coluna 'coluna' e igual a 'valor'.
# Exemplo:
#   linhas = [{'author':'A','n':1}, {'author':'B','n':2}, {'author':'A','n':3}]
#   filtrar(linhas, 'author', 'A')  ==>  [{'author':'A','n':1}, {'author':'A','n':3}]
def filtrar(linhas: list, coluna: str, valor) -> list:
    return todo(linhas, coluna, valor)


# ------------------------------------------------------------------------------
# Ex 2: adicionar_n_chars
# Para cada linha (que tem a coluna 'text'), acrescente a coluna 'n_chars' com o
# numero de caracteres do texto. Retorne uma NOVA lista de linhas (novos dicts);
# nao modifique os dicionarios originais.
# Exemplo:
#   adicionar_n_chars([{'text':'oi'}])  ==>  [{'text':'oi', 'n_chars':2}]
def adicionar_n_chars(linhas: list) -> list:
    return todo(linhas)


# ------------------------------------------------------------------------------
# Ex 3: razao_comentarios
# Cada linha tem 'ntop' e 'ncomments'. Acrescente a coluna 'ratio' = ntop/ncomments.
# Se 'ncomments' for 0, a razao e None (como o NaN do pandas). Retorne nova lista.
# Exemplo:
#   razao_comentarios([{'ntop':1,'ncomments':2}, {'ntop':0,'ncomments':0}])
#     ==>  [{'ntop':1,'ncomments':2,'ratio':0.5}, {'ntop':0,'ncomments':0,'ratio':None}]
def razao_comentarios(linhas: list) -> list:
    return todo(linhas)


# ------------------------------------------------------------------------------
# Ex 4: media_ignorando_none
# Retorne a media dos valores da coluna 'coluna', IGNORANDO valores None (assim
# como o pandas ignora NaN). Se nao houver nenhum valor valido, retorne None.
# Exemplo:
#   media_ignorando_none([{'r':0.5}, {'r':None}, {'r':1.0}], 'r')  ==>  0.75
def media_ignorando_none(linhas: list, coluna: str):
    return todo(linhas, coluna)


# ------------------------------------------------------------------------------
# Ex 5: filtrar_dois_criterios
# Retorne as linhas em que author == autor E ncomments >= min_comentarios
# (o "E" logico, como o operador & do pandas).
def filtrar_dois_criterios(linhas: list, autor: str, min_comentarios: int) -> list:
    return todo(linhas, autor, min_comentarios)
