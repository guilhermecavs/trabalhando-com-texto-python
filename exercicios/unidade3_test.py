"""
Testes automaticos do Conjunto de Exercicios 3 -- Customizando o pipeline do spaCy.
Rode (dentro da pasta 'exercicios'):   python3 -m unittest unidade3_test
Nao edite este arquivo -- edite 'unidade3_exercicios.py'.
"""

import unittest

from unidade3_exercicios import (
    componentes_ativos,
    adicionar_componente,
    remover_componente,
    pipeline_ok,
    filtrar_por_idade,
)


class TestUnidade3(unittest.TestCase):

    def test_ex1_componentes_ativos(self):
        self.assertEqual(
            componentes_ativos(["tok2vec", "tagger", "parser", "ner"], ["ner", "parser"]),
            ["tok2vec", "tagger"],
        )
        self.assertEqual(componentes_ativos(["a", "b"], []), ["a", "b"])

    def test_ex2_adicionar_componente(self):
        base = ["tok2vec", "tagger"]
        self.assertEqual(
            adicionar_componente(base, "merge_entities"),
            ["tok2vec", "tagger", "merge_entities"],
        )
        # nao duplica
        self.assertEqual(adicionar_componente(base, "tagger"), ["tok2vec", "tagger"])
        # nao modifica a original
        self.assertEqual(base, ["tok2vec", "tagger"])

    def test_ex3_remover_componente(self):
        base = ["tok2vec", "tagger", "ner"]
        self.assertEqual(remover_componente(base, "ner"), ["tok2vec", "tagger"])
        self.assertEqual(remover_componente(base, "inexistente"), ["tok2vec", "tagger", "ner"])
        self.assertEqual(base, ["tok2vec", "tagger", "ner"])

    def test_ex4_pipeline_ok(self):
        self.assertTrue(pipeline_ok({"tagger": [], "ner": []}))
        self.assertFalse(pipeline_ok({"tagger": [], "ner": ["faltou X"]}))
        self.assertTrue(pipeline_ok({}))

    def test_ex5_filtrar_por_idade(self):
        docs = [
            {"text": "a", "age": 23},
            {"text": "b", "age": 58},
            {"text": "c", "age": 35},
        ]
        self.assertEqual(filtrar_por_idade(docs, 40), ["a", "c"])
        self.assertEqual(filtrar_por_idade(docs, 10), [])


if __name__ == "__main__":
    unittest.main()
