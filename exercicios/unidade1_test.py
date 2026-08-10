"""
Testes automaticos do Conjunto de Exercicios 1 -- Manipulando texto com Python.

Rode (dentro da pasta 'exercicios'):   python3 -m unittest unidade1_test
Nao edite este arquivo -- edite 'unidade1_exercicios.py'.
"""

import unittest

from unidade1_exercicios import (
    contar_linhas,
    primeiros_n,
    separar_paragrafos,
    padronizar_aspas,
    remover_pontuacao_repetida,
    normalizar_espacos,
)


class TestUnidade1(unittest.TestCase):

    def test_ex1_contar_linhas(self):
        self.assertEqual(contar_linhas("a\nb\nc"), 2)
        self.assertEqual(contar_linhas("abc"), 0)
        self.assertEqual(contar_linhas(""), 0)
        self.assertEqual(contar_linhas("\n\n\n"), 3)

    def test_ex2_primeiros_n(self):
        self.assertEqual(primeiros_n("terrorism", 4), "terr")
        self.assertEqual(primeiros_n("abc", 10), "abc")
        self.assertEqual(primeiros_n("abc", 0), "")

    def test_ex3_separar_paragrafos(self):
        self.assertEqual(separar_paragrafos("meta   p1   p2"), ["meta", "p1", "p2"])
        self.assertEqual(separar_paragrafos("   so um"), ["so um"])
        self.assertEqual(separar_paragrafos("unico"), ["unico"])

    def test_ex4_padronizar_aspas(self):
        self.assertEqual(padronizar_aspas("“oi”"), '"oi"')
        self.assertEqual(padronizar_aspas("‘a’ ‘b’"), '"a" "b"')
        self.assertEqual(padronizar_aspas('ja "reto"'), 'ja "reto"')

    def test_ex5_remover_pontuacao_repetida(self):
        self.assertEqual(remover_pontuacao_repetida("fim.... certo"), "fim certo")
        self.assertEqual(remover_pontuacao_repetida("a,,,,b"), "ab")
        self.assertEqual(remover_pontuacao_repetida("ok. bom, dia"), "ok. bom, dia")

    def test_ex6_normalizar_espacos(self):
        self.assertEqual(normalizar_espacos("a    b   c"), "a b c")
        self.assertEqual(normalizar_espacos("sem extra"), "sem extra")


if __name__ == "__main__":
    unittest.main()
