"""
================================================================================
 Conjunto de Exercicios 3 -- Customizando o pipeline do spaCy (logica)
 Curso: Trabalhando com Texto em Python I (CiberExt 26-29 / FEELT38103 / UFU)
================================================================================

Edite ESTE arquivo e verifique com:   python3 -m unittest unidade3_test

Para rodar em qualquer lugar, aqui:
- um PIPELINE e uma lista de nomes de componentes: ['tok2vec','tagger','ner'];
- a ANALISE do pipeline e um dicionario {componente: [lista de problemas]};
- um DOC com atributo personalizado e um dicionario {'text': ..., 'age': ...}.

Correspondencia com o spaCy real:
  spacy.load(..., exclude=[...])   -> componentes_ativos
  nlp.add_pipe(nome)               -> adicionar_componente
  nlp.remove_pipe(nome)            -> remover_componente
  nlp.analyze_pipes()['problems']  -> pipeline_ok
  [d for d in docs if d._.age<40]  -> filtrar_por_idade
--------------------------------------------------------------------------------
"""

from mooc.todo import todo


# ------------------------------------------------------------------------------
# Ex 1: componentes_ativos
# Dada a lista de TODOS os componentes e uma lista de nomes a EXCLUIR, retorne
# os componentes que permanecem, preservando a ordem original.
# Exemplo:
#   componentes_ativos(['tok2vec','tagger','parser','ner'], ['ner','parser'])
#     ==>  ['tok2vec', 'tagger']
def componentes_ativos(todos: list, excluir: list) -> list:
    return todo(todos, excluir)


# ------------------------------------------------------------------------------
# Ex 2: adicionar_componente
# Retorne uma NOVA lista com 'nome' acrescentado ao FINAL do pipeline. Se o
# componente ja estiver presente, retorne o pipeline inalterado (nao duplique).
# A lista original NAO deve ser modificada.
def adicionar_componente(pipeline: list, nome: str) -> list:
    return todo(pipeline, nome)


# ------------------------------------------------------------------------------
# Ex 3: remover_componente
# Retorne uma NOVA lista sem o componente 'nome'. Se ele nao existir, retorne
# uma copia inalterada. A lista original NAO deve ser modificada.
def remover_componente(pipeline: list, nome: str) -> list:
    return todo(pipeline, nome)


# ------------------------------------------------------------------------------
# Ex 4: pipeline_ok
# Dada a analise {componente: [problemas]}, retorne True se NENHUM componente
# tiver problemas (todas as listas vazias), e False caso contrario.
# Exemplos:
#   pipeline_ok({'tagger': [], 'ner': []})            ==>  True
#   pipeline_ok({'tagger': [], 'ner': ['faltou X']})  ==>  False
def pipeline_ok(analise: dict) -> bool:
    return todo(analise)


# ------------------------------------------------------------------------------
# Ex 5: filtrar_por_idade
# 'docs' e uma lista de dicionarios com as chaves 'text' e 'age'. Retorne a
# lista dos textos ('text') cujo 'age' seja MENOR que 'limite'.
# Exemplo:
#   docs = [{'text':'a','age':23}, {'text':'b','age':58}, {'text':'c','age':35}]
#   filtrar_por_idade(docs, 40)  ==>  ['a', 'c']
def filtrar_por_idade(docs: list, limite: int) -> list:
    return todo(docs, limite)
