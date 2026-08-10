# Gabarito — Trabalhando com Texto em Python I

Esta pasta contém as **soluções‑modelo** dos conjuntos de exercícios (uma por
unidade). Use apenas **depois** de tentar resolver por conta própria — ou como
referência para monitores/corretores.

| Arquivo | Conjunto |
|---|---|
| `unidade1_respostas.py` | Manipulando texto (string, split/join, regex) |
| `unidade2_respostas.py` | Tokens e entidades (lógica do spaCy) |
| `unidade3_respostas.py` | Pipeline (exclude, add/remove, filtragem) |
| `unidade4_respostas.py` | Métricas (concordância, kappa, acurácia, precisão, revocação, F1) |
| `unidade5_respostas.py` | DataFrame (filtrar, colunas calculadas, NaN) |

## Como conferir uma solução

Cada arquivo tem exatamente os mesmos nomes de função do arquivo de exercícios
correspondente. Para rodar os testes contra a solução‑modelo (útil para o
monitor validar o gabarito), copie a solução por cima do exercício e rode o
teste:

```bash
cp respostas/unidade1_respostas.py exercicios/unidade1_exercicios.py
cd exercicios && python3 -m unittest unidade1_test
```

> ⚠️ Isso **sobrescreve** o arquivo de exercícios do aluno — faça só numa cópia.

## Respostas dos quizzes

As respostas das questões de **quiz** já vêm **marcadas no próprio material** de
cada unidade (destacadas com ✅ no HTML/Markdown e com **(correta)** em verde no
PDF). Um resumo consolidado, para consulta rápida, está em
[`gabarito_quiz.md`](gabarito_quiz.md).
