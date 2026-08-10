"""
Testes automaticos do Conjunto de Exercicios 2 -- Processando textos com spaCy.
Rode (dentro da pasta 'exercicios'):   python3 -m unittest unidade2_test
Nao edite este arquivo -- edite 'unidade2_exercicios.py'.
"""

import unittest

from unidade2_exercicios import (
    lemas_dos_verbos,
    tokens_sem_pontuacao,
    contar_por_classe,
    entidades_do_tipo,
    classe_mais_frequente,
)

# doc de exemplo: "The FBI tracks Iraqis ."
DOC = [
    {"text": "The", "pos": "DET", "lemma": "the", "tag": "DT"},
    {"text": "FBI", "pos": "PROPN", "lemma": "FBI", "tag": "NNP"},
    {"text": "tracks", "pos": "VERB", "lemma": "track", "tag": "VBZ"},
    {"text": "Iraqis", "pos": "NOUN", "lemma": "iraqi", "tag": "NNS"},
    {"text": "runs", "pos": "VERB", "lemma": "run", "tag": "VBZ"},
    {"text": ".", "pos": "PUNCT", "lemma": ".", "tag": "."},
]

ENTS = [
    {"text": "FBI", "label": "ORG"},
    {"text": "Iraqis", "label": "NORP"},
    {"text": "New Mexico", "label": "GPE"},
]


class TestUnidade2(unittest.TestCase):

    def test_ex1_lemas_dos_verbos(self):
        self.assertEqual(lemas_dos_verbos(DOC), ["track", "run"])
        self.assertEqual(lemas_dos_verbos([]), [])

    def test_ex2_tokens_sem_pontuacao(self):
        self.assertEqual(
            tokens_sem_pontuacao(DOC), ["The", "FBI", "tracks", "Iraqis", "runs"]
        )

    def test_ex3_contar_por_classe(self):
        self.assertEqual(
            contar_por_classe(DOC),
            {"DET": 1, "PROPN": 1, "VERB": 2, "NOUN": 1, "PUNCT": 1},
        )

    def test_ex4_entidades_do_tipo(self):
        self.assertEqual(entidades_do_tipo(ENTS, "GPE"), ["New Mexico"])
        self.assertEqual(entidades_do_tipo(ENTS, "ORG"), ["FBI"])
        self.assertEqual(entidades_do_tipo(ENTS, "PERSON"), [])

    def test_ex5_classe_mais_frequente(self):
        self.assertEqual(classe_mais_frequente(DOC), "VERB")
        self.assertIsNone(classe_mais_frequente([]))
        # empate 1x1 entre DET e NOUN -> vence o primeiro (DET)
        empate = [
            {"text": "a", "pos": "DET", "lemma": "a", "tag": "DT"},
            {"text": "b", "pos": "NOUN", "lemma": "b", "tag": "NN"},
        ]
        self.assertEqual(classe_mais_frequente(empate), "DET")


if __name__ == "__main__":
    unittest.main()
