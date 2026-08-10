# Trabalhando com Texto em Python I

<p align="center">
  <a href="https://guilhermecavs.github.io/trabalhando-com-texto-python/"><img src="https://img.shields.io/badge/Acesse%20o%20curso-online-6c4cf1?style=for-the-badge&logo=firefox&logoColor=white" alt="Acesse o curso online"></a>
  <a href="Curso-Trabalhando-com-Texto-em-Python-I.pdf"><img src="https://img.shields.io/badge/PDF%20completo-60%20p%C3%A1ginas-00b4d8?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="PDF completo"></a>
  <img src="https://img.shields.io/badge/licen%C3%A7a-CC%20BY--NC%204.0-10b981?style=for-the-badge" alt="Licença CC BY-NC 4.0">
</p>

Material do curso massivo aberto (MOOC) **"Trabalhando com Texto em Python I"**,
produzido pela equipe discente no âmbito do **Programa CiberExt 26‑29** /
Atividade Curricular de Extensão **FEELT38103** — Universidade Federal de
Uberlândia (UFU).

O conteúdo é uma adaptação e tradução para o português do curso
[*Applied Language Technology*](https://applied-language-technology.mooc.fi/)
(Universidade de Helsinque), correspondendo à sua **Parte II — Working with Text
in Python**. O curso ensina a processar texto em Python: da manipulação de texto
simples e expressões regulares ao **spaCy** (processamento de linguagem natural),
à **avaliação de modelos** e ao **pandas**.

## O que você aprende

Ao final do curso, você será capaz de:

- **manipular textos** com Python (métodos de *string*, substituições, expressões regulares);
- **trabalhar com arquivos e codificações** (texto simples, ASCII/UTF‑8, ler e gravar arquivos);
- **realizar processamento linguístico** com o spaCy (tokenização, classes gramaticais, análise sintática, lematização e entidades nomeadas);
- **customizar e otimizar** um *pipeline* de PLN e salvar resultados em disco;
- **avaliar modelos de linguagem** (concordância entre anotadores, kappa de Cohen, precisão, revocação e F1);
- **extrair características de textos** e organizá‑las em tabelas com o pandas;
- **aplicar técnicas básicas de análise de dados textuais** (filtragem, estatísticas descritivas e visualização).

## Acesso rápido

- 🌐 **Site do curso (navegável):** <https://guilhermecavs.github.io/trabalhando-com-texto-python/>
- 📕 **PDF do curso completo (60 páginas):** [`Curso-Trabalhando-com-Texto-em-Python-I.pdf`](Curso-Trabalhando-com-Texto-em-Python-I.pdf)
- 🧑‍💻 **Exercícios com correção automática:** pasta [`exercicios/`](exercicios/)

## Equipe

- Guilherme Carvalho Santos
- Gabriel Alves Fagundes
- Jean Lineker de Paula Gomes

---

## O que foi produzido

O curso está dividido em **6 unidades** (uma de preparação + 5 de conteúdo). Cada
unidade tem a mesma estrutura pedagógica: uma seção de **objetivos**, o
**conteúdo** com exemplos de código comentados, um **quiz** de autoavaliação (com
a resposta destacada) e um **resumo**. Além do conteúdo, o material inclui:

- **Exercícios de programação com correção automática** (um conjunto por unidade,
  27 no total) — no mesmo modelo do material de referência: o aluno recebe funções
  incompletas e um arquivo de testes que verifica as respostas. Os testes usam
  apenas a biblioteca padrão do Python, então rodam em qualquer lugar, inclusive
  em corretores automáticos como o **Judge0**.
- **Gabarito** dos exercícios (soluções‑modelo) e das questões de quiz.
- **Diagramas** ilustrando os conceitos mais visuais (pipeline do spaCy,
  precisão × revocação, anatomia de um `DataFrame`).
- **Três formatos** por unidade — **web (HTML)**, **LaTeX** e **PDF** — todos
  gerados automaticamente a partir de **uma única fonte** em Markdown (veja
  "Como o material é gerado", abaixo).

### As unidades

| # | Unidade | Conteúdo | Ler |
|:-:|---|---|---|
| 0 | Preparando o ambiente | Instalar Python, ambiente virtual, bibliotecas, modelo do spaCy e dados | [HTML](Unidade-0/unidade0_preparando_ambiente.html) · [PDF](Unidade-0/unidade0_preparando_ambiente.pdf) |
| 1 | Manipulando texto com Python | Texto simples/estruturado, codificação, arquivos, `replace`/`split`/`join`, regex, `pathlib` | [HTML](Unidade-1/unidade1_manipulando_texto.html) · [PDF](Unidade-1/unidade1_manipulando_texto.pdf) |
| 2 | Processando textos com spaCy | Tokenização, classes gramaticais, morfologia, sintaxe, sentenças, lematização, NER | [HTML](Unidade-2/unidade2_processando_com_spacy.html) · [PDF](Unidade-2/unidade2_processando_com_spacy.pdf) |
| 3 | Customizando o pipeline do spaCy | Excluir componentes, processar em lote, atributos personalizados, `DocBin`, mesclar sintagmas/entidades | [HTML](Unidade-3/unidade3_customizando_pipeline_spacy.html) · [PDF](Unidade-3/unidade3_customizando_pipeline_spacy.pdf) |
| 4 | Avaliando modelos de linguagem | Padrão‑ouro, concordância, kappa de Cohen, matriz de confusão, precisão, revocação, F1 | [HTML](Unidade-4/unidade4_avaliando_modelos.html) · [PDF](Unidade-4/unidade4_avaliando_modelos.pdf) |
| 5 | Gerenciando dados textuais com pandas | `DataFrame`, `Series`, `.loc`, `apply`, valores ausentes, salvar/carregar | [HTML](Unidade-5/unidade5_gerenciando_dados_pandas.html) · [PDF](Unidade-5/unidade5_gerenciando_dados_pandas.pdf) |

---

## Como utilizar este curso

1. **Comece pela [Unidade 0](Unidade-0/unidade0_preparando_ambiente.html)** para preparar o ambiente (Python, bibliotecas, modelo do spaCy e dados).
2. **Estude as unidades em ordem** (1 → 5): leia o conteúdo, experimente os exemplos de código no Jupyter ou num arquivo `.py` e responda ao **quiz** ao final de cada unidade.
3. **Faça os exercícios** da unidade em [`exercicios/`](exercicios/): edite o arquivo `unidadeN_exercicios.py`, substituindo cada `todo(...)` pela sua solução, e rode os testes até aparecer `OK` (veja "Como resolver os exercícios", abaixo).
4. **Só depois** confira as soluções em [`respostas/`](respostas/), se precisar.

Você pode ler o conteúdo de três formas: **online** (o [site](https://guilhermecavs.github.io/trabalhando-com-texto-python/)), pelos **arquivos `.html`** de cada unidade ou pelo **PDF**.

---

## O que cada arquivo/pasta significa

```
.
├── index.html                     Página inicial do site (lista e liga as unidades)
├── Curso-...-Python-I.pdf         PDF único com as 6 unidades juntas (60 páginas)
├── requirements.txt               Bibliotecas Python do curso (spaCy, pandas, ...)
├── README.md                      Este arquivo
│
├── Unidade-0/ ... Unidade-5/      Uma pasta por unidade. Em cada uma:
│   ├── unidadeN_*.md                → FONTE (Markdown). É o único arquivo que se edita.
│   ├── unidadeN_*.html              → versão web, gerada a partir do .md
│   ├── unidadeN_*.tex               → versão LaTeX, gerada a partir do .md
│   ├── unidadeN_*.pdf               → PDF, compilado do .tex
│   └── img/                         → diagramas (.svg); o .pdf do diagrama é gerado no build
│
├── exercicios/                    Exercícios de programação (o aluno resolve aqui)
│   ├── unidadeN_exercicios.py       → arquivo COM LACUNAS que o aluno completa
│   ├── unidadeN_test.py             → testes automáticos que verificam as respostas
│   ├── mooc/todo.py                 → função todo() usada como marcador de "não resolvido"
│   ├── rodar_testes.sh              → roda todos os conjuntos de uma vez
│   └── README.md                    → instruções de como resolver e testar
│
├── respostas/                     Gabarito (consultar só depois de tentar!)
│   ├── unidadeN_respostas.py        → soluções‑modelo dos exercícios
│   ├── gabarito_quiz.md             → respostas dos quizzes, consolidadas
│   └── README.md                    → como conferir uma solução
│
└── assets/                        Ferramentas de build (fonte única via pandoc)
    ├── build.sh                     → gera HTML/LaTeX/PDF a partir do .md de cada unidade
    ├── converter.py                 → converteu os .md originais para o formato do pandoc
    ├── estilo.css                   → estilo visual do HTML (cores, dark mode, caixas)
    ├── cabecalho.tex                → estilo visual do LaTeX/PDF
    └── callouts.lua                 → filtro que transforma as caixas de destaque no LaTeX
```

**Em resumo:** dentro de cada `Unidade-N/`, o arquivo **`.md` é a fonte** — é o
único que se edita à mão. O `.html`, o `.tex` e o `.pdf` são **gerados** a partir
dele. Na pasta `exercicios/`, o aluno edita o `unidadeN_exercicios.py`; o
`unidadeN_test.py` corrige. Na pasta `respostas/` está o gabarito.

---

## Tecnologias utilizadas

| Tecnologia | Para quê |
|---|---|
| **Python 3** | linguagem usada em todo o curso e nos exercícios |
| **spaCy** | processamento de linguagem natural (Unidades 2 e 3) |
| **pandas** | dados tabulares / textuais (Unidade 5) |
| **scikit‑learn** | métricas de avaliação (Unidade 4) |
| **matplotlib** | visualização de dados (Unidade 5) |
| **unittest** (biblioteca padrão) | correção automática dos exercícios |
| **Markdown + pandoc** | fonte única que gera HTML, LaTeX e PDF |
| **LaTeX (pdfLaTeX)** | geração dos PDFs |
| **SVG + librsvg** | diagramas (vetoriais no HTML, convertidos para PDF no LaTeX) |
| **Git + GitHub Pages** | versionamento e publicação do site |

---

## Como o material é gerado (fonte única)

Para evitar manter três formatos à mão, o curso usa **fonte única**: escreve‑se
apenas o Markdown de cada unidade e o [pandoc](https://pandoc.org) gera o HTML, o
LaTeX e o PDF, usando os recursos compartilhados em `assets/`.

Requisitos (macOS):

```bash
brew install pandoc librsvg
brew install --cask basictex           # ou mactex-no-gui
sudo tlmgr install framed fvextra upquote xurl bookmark footnotehyper parskip newunicodechar
```

Para (re)gerar **uma** unidade ou **todas**:

```bash
assets/build.sh Unidade-1/unidade1_manipulando_texto.md   # uma unidade
assets/build.sh                                           # todas
```

Cada execução produz, ao lado do `.md`, o `.html` (autossuficiente, com modo
escuro e diagramas embutidos), o `.tex` e o `.pdf`.

> O **site** (GitHub Pages) atualiza sozinho a cada `git push` — não é preciso
> republicar nada.

---

## Como resolver os exercícios

```bash
cd exercicios
python3 -m unittest unidade1_test     # verifica o conjunto da Unidade 1
./rodar_testes.sh                     # roda todos os conjuntos
```

Enquanto houver `todo(...)` no arquivo, os testes falham de propósito. Quando
aparecer `OK`, os exercícios daquela unidade estão corretos. Os testes **não
precisam** de spaCy/pandas — usam só a biblioteca padrão do Python. Detalhes em
[`exercicios/README.md`](exercicios/README.md).

---

## Licença

Este material é uma **adaptação** do curso *Applied Language Technology* (Tuomo
Hiippala / mooc.fi), que é licenciado sob **Creative Commons
Attribution‑NonCommercial 4.0 International (CC BY‑NC 4.0)**. Por ser um trabalho
derivado, este curso é distribuído sob a **mesma licença** — você pode
compartilhá‑lo e adaptá‑lo para **fins não comerciais**, desde que dê o devido
crédito. Detalhes e atribuição completa em [`LICENSE`](LICENSE).

---

## Referências

- Rögnvaldsson, E. et al. *Applied Language Technology* (MOOC). Universidade de Helsinque. <https://applied-language-technology.mooc.fi/>
- Honnibal, M.; Montani, I. et al. *spaCy*. <https://spacy.io/>
- McKinney, W. et al. *pandas*. <https://pandas.pydata.org/>
- Pedregosa, F. et al. (2011). *Scikit‑learn: Machine Learning in Python*. JMLR.
