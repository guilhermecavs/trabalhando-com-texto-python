"""
================================================================================
 Conjunto de Exercicios 2 -- Processando textos com spaCy (logica de tokens)
 Curso: Trabalhando com Texto em Python I (CiberExt 26-29 / FEELT38103 / UFU)
================================================================================

Edite ESTE arquivo e verifique com:   python3 -m unittest unidade2_test

Para que os exercicios rodem em qualquer lugar (sem precisar baixar o modelo
'en_core_web_sm'), aqui um TOKEN e representado por um dicionario:

    {"text": "runs", "pos": "VERB", "lemma": "run", "tag": "VBZ"}

e uma ENTIDADE nomeada por:

    {"text": "New Mexico", "label": "GPE"}

No spaCy REAL isso corresponde a:
    token.text  -> "text"      token.pos_   -> "pos"
    token.lemma_-> "lemma"     token.tag_   -> "tag"
    ent.text    -> "text"      ent.label_   -> "label"

A logica que voce pratica aqui e EXATAMENTE a mesma usada com objetos spaCy.
--------------------------------------------------------------------------------
"""

from mooc.todo import todo


# ------------------------------------------------------------------------------
# Ex 1: lemas_dos_verbos
# Dado um 'doc' (lista de tokens), retorne a lista dos LEMAS de todos os tokens
# cuja classe gramatical ('pos') e 'VERB', na ordem em que aparecem.
# No spaCy: [token.lemma_ for token in doc if token.pos_ == 'VERB']
def lemas_dos_verbos(doc: list) -> list:
    return todo(doc)


# ------------------------------------------------------------------------------
# Ex 2: tokens_sem_pontuacao
# Retorne a lista dos TEXTOS ('text') de todos os tokens que NAO sao pontuacao
# (ou seja, 'pos' diferente de 'PUNCT').
def tokens_sem_pontuacao(doc: list) -> list:
    return todo(doc)


# ------------------------------------------------------------------------------
# Ex 3: contar_por_classe
# Retorne um dicionario que conta quantos tokens ha de cada classe ('pos').
# Exemplo: [{pos:'DET'},{pos:'NOUN'},{pos:'NOUN'}] ==> {'DET': 1, 'NOUN': 2}
def contar_por_classe(doc: list) -> dict:
    return todo(doc)


# ------------------------------------------------------------------------------
# Ex 4: entidades_do_tipo
# Dada uma lista de entidades e um 'label', retorne os TEXTOS das entidades
# cujo 'label' seja igual ao pedido.
# No spaCy: [ent.text for ent in doc.ents if ent.label_ == label]
def entidades_do_tipo(entidades: list, label: str) -> list:
    return todo(entidades, label)


# ------------------------------------------------------------------------------
# Ex 5: classe_mais_frequente
# Retorne a classe gramatical ('pos') que aparece MAIS vezes no doc. Em caso de
# empate, retorne a que aparece primeiro ao percorrer o doc. Se o doc estiver
# vazio, retorne None.
def classe_mais_frequente(doc: list):
    return todo(doc)
