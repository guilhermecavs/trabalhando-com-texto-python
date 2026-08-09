# Trabalhando com Texto em Python I

Material do curso massivo aberto (MOOC) **"Trabalhando com Texto em Python I"**, desenvolvido no âmbito do **Programa CiberExt 26‑29** / Atividade Curricular de Extensão **FEELT38103** — Universidade Federal de Uberlândia (UFU).

Conteúdo adaptado e traduzido para o português a partir do curso [*Applied Language Technology*](https://applied-language-technology.mooc.fi/) (Universidade de Helsinque), correspondendo à sua **Parte II: Working with Text in Python**.

## Equipe

- Guilherme Carvalho Santos
- Gabriel Alves Fagundes
- Jean Lineker de Paula Gomes

## Estrutura

```
Unidade-1/   Manipulando texto com Python
             (computadores e texto, encoding, carregar arquivos,
              manipular texto, regex, processar múltiplos arquivos)

Unidade-2/   Processando textos com spaCy
             (tokenização, classes gramaticais, análise morfológica
              e sintática, segmentação de sentenças, lematização, NER)

Unidade-3/   Customizando o pipeline do spaCy
             (modificar o pipeline, processar em lote, atributos
              personalizados, DocBin, mesclar sintagmas e entidades)

Unidade-4/   Avaliando modelos de linguagem
             (padrão-ouro, concordância entre anotadores, kappa de
              Cohen, matriz de confusão, precisão, revocação, F1)

Unidade-5/   Gerenciando dados textuais com pandas
             (importar/examinar/estender/salvar DataFrames, Series,
              value_counts, describe, .loc, apply, pickle)
```

> **Status:** curso completo — as 5 unidades correspondem às 5 seções da
> Parte II ("Working with Text in Python") do curso de referência.

Cada unidade é entregue em três formatos:

- `*.md` — Markdown, base editável
- `*.html` — versão web autossuficiente, com realce de sintaxe
- `*.tex` — versão para compilação em PDF via `pdflatex`

## Compilando o PDF

```bash
cd Unidade-1                              # ou Unidade-2
pdflatex unidade1_manipulando_texto.tex
pdflatex unidade1_manipulando_texto.tex   # rodar 2x para índice/links
```

## Referências

- Rögnvaldsson, E. et al. *Applied Language Technology* (MOOC). Universidade de Helsinque. <https://applied-language-technology.mooc.fi/>
