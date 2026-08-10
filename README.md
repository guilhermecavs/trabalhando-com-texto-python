# Trabalhando com Texto em Python I

Material do curso massivo aberto (MOOC) **"Trabalhando com Texto em Python I"**, desenvolvido no âmbito do **Programa CiberExt 26‑29** / Atividade Curricular de Extensão **FEELT38103** — Universidade Federal de Uberlândia (UFU).

Conteúdo adaptado e traduzido para o português a partir do curso [*Applied Language Technology*](https://applied-language-technology.mooc.fi/) (Universidade de Helsinque), correspondendo à sua **Parte II: Working with Text in Python**.

## Equipe

- Guilherme Carvalho Santos
- Gabriel Alves Fagundes
- Jean Lineker de Paula Gomes

## Estrutura

```
Unidade-0/   Preparando o ambiente (Python, venv, bibliotecas, modelo, dados)
Unidade-1/   Manipulando texto com Python (string, encoding, regex, pathlib)
Unidade-2/   Processando textos com spaCy (tokens, POS, morfologia, NER)
Unidade-3/   Customizando o pipeline do spaCy (exclude, pipe, DocBin, merges)
Unidade-4/   Avaliando modelos (kappa de Cohen, matriz de confusão, P/R/F1)
Unidade-5/   Gerenciando dados textuais com pandas (DataFrame, Series, .loc)

exercicios/  Exercícios com correção automática (unittest) — um por unidade
respostas/   Soluções-modelo dos exercícios + gabarito dos quizzes
assets/      Pipeline de build (fonte única via pandoc) — veja abaixo
```

Cada unidade tem uma seção de **objetivos**, conteúdo com **exemplos de código**,
um **quiz** de autoavaliação e um **resumo**. Os exercícios ficam em `exercicios/`.

## Fonte única (pandoc)

A **fonte de cada unidade é o arquivo `.md`**. O HTML, o LaTeX e o PDF são
**gerados** a partir dele com o [pandoc](https://pandoc.org), usando os recursos
compartilhados em `assets/` (CSS, cabeçalho LaTeX e um filtro Lua para as caixas
de destaque). Ou seja: **edite apenas o `.md` e regenere.**

### Gerar os formatos

Requisitos: `pandoc` e uma distribuição LaTeX (`pdflatex`). No macOS:

```bash
brew install pandoc
brew install --cask basictex   # ou mactex-no-gui
sudo tlmgr install framed fvextra upquote xurl bookmark footnotehyper parskip newunicodechar
```

Depois, para (re)gerar **uma** unidade ou **todas**:

```bash
assets/build.sh Unidade-1/unidade1_manipulando_texto.md   # uma unidade
assets/build.sh                                           # todas
```

Cada execução produz o `.html` (autossuficiente, com dark mode), o `.tex` e o
`.pdf` ao lado do `.md`.

## Exercícios (correção automática)

```bash
cd exercicios
python3 -m unittest unidade1_test    # ou ./rodar_testes.sh para todos
```

Os testes usam só a biblioteca padrão do Python — rodam em qualquer lugar,
inclusive em corretores como o **Judge0**. Veja `exercicios/README.md`.

## Referências

- Rögnvaldsson, E. et al. *Applied Language Technology* (MOOC). Universidade de Helsinque. <https://applied-language-technology.mooc.fi/>
