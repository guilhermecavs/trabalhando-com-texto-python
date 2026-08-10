"""
Modulo de apoio aos exercicios (equivalente ao Mooc.Todo do curso de Haskell).

Use a funcao `todo()` como marcador de "ainda nao resolvido". Enquanto a sua
solucao nao substituir o `todo()`, o exercicio falha nos testes de proposito.
"""


def todo(*args, **kwargs):
    """Marcador de exercicio nao resolvido. Substitua pela sua solucao."""
    raise NotImplementedError(
        "Exercicio ainda nao resolvido: substitua a chamada 'todo(...)' pela sua solucao."
    )
