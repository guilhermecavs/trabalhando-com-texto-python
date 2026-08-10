# Exercícios — Trabalhando com Texto em Python I

Conjuntos de exercícios com **correção automática**, um por unidade do curso.
Seguem o mesmo padrão do material de referência: você recebe um arquivo com
funções incompletas e um arquivo de testes que verifica suas respostas.

## Como resolver

1. Abra o arquivo da unidade, por exemplo `unidade1_exercicios.py`.
2. Substitua cada chamada `todo(...)` pela sua solução.
3. Rode os testes (dentro desta pasta `exercicios/`):

   ```sh
   python3 -m unittest unidade1_test
   ```

   Enquanto houver `todo(...)`, o teste falha de propósito. Quando aparecer
   `OK`, você acertou todos os exercícios daquela unidade.

Para rodar **todos** os conjuntos de uma vez:

```sh
python3 -m unittest discover -p "unidade*_test.py"
```

ou use o atalho:

```sh
./rodar_testes.sh
```

## Requisitos

Os testes usam **apenas a biblioteca padrão do Python 3** (`unittest`, `re`) —
não é preciso instalar nada. Isso torna os exercícios adequados para correção
automática (ex.: Judge0).

> Os conjuntos das unidades 2, 3 e 5 exercitam a **lógica** do spaCy e do pandas
> usando representações em Python puro (tokens e linhas como dicionários), para
> que rodem em qualquer lugar sem baixar modelos de linguagem nem instalar
> bibliotecas pesadas. Cada arquivo mostra, no cabeçalho, a correspondência com
> a API real. Alunos avançados podem refazê-los com spaCy/pandas de verdade.

## Estrutura

```
exercicios/
  mooc/todo.py            função 'todo()' (marcador de "não resolvido")
  unidadeN_exercicios.py  VOCÊ edita este arquivo
  unidadeN_test.py        testes automáticos (não edite)
  rodar_testes.sh         roda todos os conjuntos

respostas/
  unidadeN_respostas.py   soluções-modelo (consulte só depois de tentar!)
```

## Conteúdo por unidade

| Unidade | Tema | Exercícios |
|:-:|---|:-:|
| 1 | Manipulando texto (string, split/join, regex) | 6 |
| 2 | Tokens e entidades (lógica do spaCy) | 5 |
| 3 | Pipeline (exclude, add/remove, filtragem) | 5 |
| 4 | Métricas (concordância, kappa, acurácia, precisão, revocação, F1) | 6 |
| 5 | DataFrame (filtrar, colunas calculadas, NaN) | 5 |
