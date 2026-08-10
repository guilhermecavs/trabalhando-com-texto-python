---
title: "Preparando o ambiente"
subtitle: "Trabalhando com Texto em Python I · Unidade 0"
author: "CiberExt 26-29 · FEELT38103 · Universidade Federal de Uberlândia"
date: "2026"
lang: pt-BR
---

### Objetivos

Antes de começar as unidades, você precisa deixar o computador pronto. Ao final desta preparação, você terá:

- **Python 3** instalado e funcionando;
- um **ambiente virtual** isolado para o curso;
- as **bibliotecas** (spaCy, pandas, scikit‑learn, matplotlib, Jupyter);
- o **modelo de linguagem** do spaCy baixado;
- os **dados** (corpus) na pasta certa;
- os **exercícios** rodando com correção automática.

::: dica
**Dica:** faça esta preparação **uma vez**. Depois, sempre que for estudar, basta **ativar o ambiente virtual** (passo 2) e começar.
:::

---

## 1. Python 3

O curso usa **Python 3.9 ou mais novo**. Verifique se já tem, no terminal:

```bash
python3 --version
```

Se aparecer algo como `Python 3.11.x`, está pronto. Se não tiver Python, baixe em [python.org/downloads](https://www.python.org/downloads/) (Windows/macOS) ou instale pelo gerenciador do seu sistema (no macOS, via [Homebrew](https://brew.sh): `brew install python`).

---

## 2. Ambiente virtual (venv)

Um **ambiente virtual** isola as bibliotecas do curso, sem bagunçar o resto do sistema. Crie um na pasta do curso:

```bash
python3 -m venv .venv
```

E **ative‑o** (você repete este passo toda vez que for estudar):

```bash
# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Quando ativo, o nome `(.venv)` aparece no início da linha do terminal. Para sair, use `deactivate`.

---

## 3. Instalar as bibliotecas

Com o ambiente **ativado**, atualize o `pip` e instale tudo de uma vez:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Se preferir instalar manualmente:

```bash
pip install spacy pandas scikit-learn matplotlib jupyterlab
```

---

## 4. Baixar o modelo de linguagem do spaCy

O spaCy separa a biblioteca do **modelo** treinado. As Unidades 2 e 3 usam o modelo **pequeno** de inglês; a Unidade 5 usa o **médio**:

```bash
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
```

Teste se carregou:

```bash
python -c "import spacy; nlp = spacy.load('en_core_web_sm'); print('spaCy OK')"
```

---

## 5. Os dados (corpus)

Os exemplos usam alguns arquivos de texto (notícias) e uma planilha de comentários (o corpus **SOCC**). Coloque‑os numa pasta chamada `data/`, ao lado dos seus notebooks:

```
data/
  NYT_1991-01-16-A15.txt
  WP_1990-08-10-25A.txt
  WP_1991-01-17-A1B.txt
  socc_gnm_articles.csv
```

Esses arquivos vêm do material do curso de referência *Applied Language Technology* — repositório em [github.com/Applied-Language-Technology](https://github.com/Applied-Language-Technology). Baixe‑os de lá e salve na pasta `data/`.

::: nota
**Nota:** os caminhos no material (ex.: `open('data/NYT_1991-01-16-A15.txt')`) supõem que você está rodando o Python **na pasta que contém `data/`**.
:::

---

## 6. Rodar os exemplos

Cada unidade traz blocos de código para você experimentar. A forma mais confortável é o **Jupyter**:

```bash
jupyter lab
```

Isso abre o Jupyter no navegador; crie um notebook novo e cole os blocos de código da unidade, executando célula por célula (`Shift + Enter`). Você também pode salvar o código em um arquivo `.py` e rodar com `python3 arquivo.py`.

---

## 7. Rodar os exercícios (correção automática)

Cada unidade tem um conjunto de exercícios com **testes automáticos**, na pasta `exercicios/`. Edite o arquivo da unidade (ex.: `unidade1_exercicios.py`), substituindo cada `todo(...)` pela sua solução, e rode:

```bash
cd exercicios
python3 -m unittest unidade1_test
```

Quando aparecer `OK`, você acertou todos. Enquanto houver `todo(...)`, o teste falha de propósito.

::: dica
**Bom saber:** os testes dos exercícios usam **só a biblioteca padrão** do Python — não precisam do spaCy nem do pandas. Assim, eles rodam em qualquer lugar, inclusive em corretores automáticos como o **Judge0**.
:::

---

## Checklist final

Antes de ir para a Unidade 1, confirme:

- [ ] `python3 --version` mostra **3.9 ou mais novo**
- [ ] o ambiente virtual está **ativado** (`(.venv)` aparece no terminal)
- [ ] `pip install -r requirements.txt` rodou sem erros
- [ ] `python -c "import spacy; spacy.load('en_core_web_sm')"` imprime **spaCy OK**
- [ ] a pasta `data/` contém os arquivos do corpus
- [ ] `python3 -m unittest unidade1_test` roda (mesmo que os exercícios ainda falhem)

Tudo certo? **Vá para a [Unidade 1 — Manipulando texto com Python](../Unidade-1/unidade1_manipulando_texto.html).**
