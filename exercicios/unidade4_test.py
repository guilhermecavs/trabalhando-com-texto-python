"""
Testes automaticos do Conjunto de Exercicios 4 -- Avaliando modelos de linguagem.
Rode (dentro da pasta 'exercicios'):   python3 -m unittest unidade4_test
Nao edite este arquivo -- edite 'unidade4_exercicios.py'.
"""

import unittest

from unidade4_exercicios import (
    concordancia_percentual,
    kappa_cohen,
    acuracia,
    precisao_classe,
    revocacao_classe,
    f1,
)


class TestUnidade4(unittest.TestCase):

    def test_ex1_concordancia(self):
        self.assertAlmostEqual(concordancia_percentual(["a", "b", "c"], ["a", "x", "c"]), 2 / 3)
        self.assertAlmostEqual(concordancia_percentual(["a", "a"], ["b", "b"]), 0.0)
        self.assertAlmostEqual(concordancia_percentual(["x"], ["x"]), 1.0)

    def test_ex2_kappa(self):
        self.assertAlmostEqual(kappa_cohen(0.8, 0.5), 0.6)
        self.assertAlmostEqual(kappa_cohen(0.5, 0.5), 0.0)

    def test_ex3_acuracia(self):
        self.assertAlmostEqual(acuracia(["ADJ", "NOUN", "VERB"], ["ADJ", "NOUN", "ADJ"]), 2 / 3)
        # exemplo completo do material: 7 de 10 acertos
        gold = ["ADJ", "ADJ", "AUX", "VERB", "AUX", "NOUN", "NOUN", "ADJ", "DET", "PRON"]
        pred = ["NOUN", "ADJ", "AUX", "VERB", "AUX", "NOUN", "VERB", "ADJ", "DET", "PROPN"]
        self.assertAlmostEqual(acuracia(gold, pred), 0.7)

    def test_ex4_precisao(self):
        gold = ["NOUN", "VERB", "VERB"]
        pred = ["VERB", "VERB", "NOUN"]
        self.assertAlmostEqual(precisao_classe(gold, pred, "VERB"), 0.5)
        # classe nunca prevista -> 0.0
        self.assertAlmostEqual(precisao_classe(["A", "A"], ["A", "A"], "Z"), 0.0)

    def test_ex5_revocacao(self):
        gold = ["NOUN", "VERB", "VERB"]
        pred = ["VERB", "VERB", "NOUN"]
        self.assertAlmostEqual(revocacao_classe(gold, pred, "VERB"), 0.5)
        # classe inexistente no gold -> 0.0
        self.assertAlmostEqual(revocacao_classe(["A", "A"], ["A", "A"], "Z"), 0.0)

    def test_ex6_f1(self):
        self.assertAlmostEqual(f1(0.5, 1.0), 2 / 3)
        self.assertAlmostEqual(f1(0.0, 0.0), 0.0)
        self.assertAlmostEqual(f1(1.0, 1.0), 1.0)


if __name__ == "__main__":
    unittest.main()
