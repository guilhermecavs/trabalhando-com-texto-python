"""
Testes automaticos do Conjunto de Exercicios 5 -- Gerenciando dados textuais.
Rode (dentro da pasta 'exercicios'):   python3 -m unittest unidade5_test
Nao edite este arquivo -- edite 'unidade5_exercicios.py'.
"""

import unittest

from unidade5_exercicios import (
    filtrar,
    adicionar_n_chars,
    razao_comentarios,
    media_ignorando_none,
    filtrar_dois_criterios,
)


class TestUnidade5(unittest.TestCase):

    def test_ex1_filtrar(self):
        linhas = [{"author": "A", "n": 1}, {"author": "B", "n": 2}, {"author": "A", "n": 3}]
        self.assertEqual(
            filtrar(linhas, "author", "A"),
            [{"author": "A", "n": 1}, {"author": "A", "n": 3}],
        )
        self.assertEqual(filtrar(linhas, "author", "Z"), [])

    def test_ex2_adicionar_n_chars(self):
        entrada = [{"text": "oi"}, {"text": "ola"}]
        self.assertEqual(
            adicionar_n_chars(entrada),
            [{"text": "oi", "n_chars": 2}, {"text": "ola", "n_chars": 3}],
        )
        # nao modifica a original
        self.assertEqual(entrada, [{"text": "oi"}, {"text": "ola"}])

    def test_ex3_razao_comentarios(self):
        self.assertEqual(
            razao_comentarios([{"ntop": 1, "ncomments": 2}, {"ntop": 0, "ncomments": 0}]),
            [
                {"ntop": 1, "ncomments": 2, "ratio": 0.5},
                {"ntop": 0, "ncomments": 0, "ratio": None},
            ],
        )

    def test_ex4_media_ignorando_none(self):
        self.assertAlmostEqual(
            media_ignorando_none([{"r": 0.5}, {"r": None}, {"r": 1.0}], "r"), 0.75
        )
        self.assertIsNone(media_ignorando_none([{"r": None}], "r"))

    def test_ex5_filtrar_dois_criterios(self):
        linhas = [
            {"author": "A", "ncomments": 300},
            {"author": "A", "ncomments": 100},
            {"author": "B", "ncomments": 500},
        ]
        self.assertEqual(
            filtrar_dois_criterios(linhas, "A", 200),
            [{"author": "A", "ncomments": 300}],
        )


if __name__ == "__main__":
    unittest.main()
