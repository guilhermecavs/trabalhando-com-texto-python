#!/usr/bin/env python3
"""
Converte o markdown atual (feito a mao, com callouts em blockquote) para o
markdown-fonte do pandoc: front-matter YAML + callouts como fenced divs.

Uso:  python3 assets/converter.py Unidade-1/unidade1_manipulando_texto.md
Reescreve o proprio arquivo (o historico do git preserva a versao anterior).
"""
import re
import sys

AUTOR = "CiberExt 26-29 · FEELT38103 · Universidade Federal de Uberlândia"

# rotulo do callout -> classe do fenced div
def classe_do_rotulo(rotulo: str) -> str:
    r = rotulo.lower()
    if "aten" in r or "seguran" in r:
        return "atencao"
    if "nota" in r or "em resumo" in r:
        return "nota"
    return "dica"  # dica, dica pratica, resumindo, ponto-chave, bom saber, ...


def converter(texto: str) -> str:
    linhas = texto.split("\n")

    # 1) titulo e subtitulo a partir dos dois primeiros cabecalhos
    titulo, subtitulo = "", ""
    for ln in linhas:
        m = re.match(r"^##\s+Unidade\s+(\d+)\s*[—-]\s*(.+)$", ln)
        if m:
            subtitulo = f"Trabalhando com Texto em Python I · Unidade {m.group(1)}"
            titulo = m.group(2).strip()
            break

    # 2) remove cabecalho antigo (linha '# ...' e '## Unidade ...'), a
    #    blockquote de introducao logo apos, e o primeiro '---'
    corpo = []
    i = 0
    n = len(linhas)
    # pula ate depois do '## Unidade ...'
    while i < n and not re.match(r"^##\s+Unidade\s+\d+", linhas[i]):
        i += 1
    i += 1  # pula a linha '## Unidade ...'
    # pula linhas em branco, a blockquote de introducao e o primeiro '---'
    intro_removida = False
    while i < n:
        s = linhas[i].strip()
        if s == "":
            i += 1
            continue
        if s.startswith(">") and not intro_removida:
            while i < n and linhas[i].strip().startswith(">"):
                i += 1
            intro_removida = True
            continue
        if s == "---" and not corpo:
            i += 1
            continue
        break

    # 3) processa o restante convertendo callouts em fenced divs
    saida = []
    while i < n:
        ln = linhas[i]
        if ln.strip().startswith(">"):
            # coleta o bloco inteiro de blockquote
            bloco = []
            while i < n and linhas[i].strip().startswith(">"):
                bloco.append(re.sub(r"^>\s?", "", linhas[i]))
                i += 1
            primeiro = bloco[0].strip()
            m = re.match(r"^(?:[^\w*]+\s*)?\*\*([^:*]+):\*\*\s*(.*)$", primeiro)
            if m:
                cls = classe_do_rotulo(m.group(1))
                bloco[0] = f"**{m.group(1)}:** {m.group(2)}".rstrip()
                saida.append(f"::: {cls}")
                saida.extend(bloco)
                saida.append(":::")
            else:
                # blockquote comum (ex.: frase de exemplo) — mantem
                for b in bloco:
                    saida.append("> " + b if b else ">")
            continue
        saida.append(ln)
        i += 1

    corpo_txt = "\n".join(saida).strip()

    # 4) monta o front-matter YAML
    yaml = (
        "---\n"
        f'title: "{titulo}"\n'
        f'subtitle: "{subtitulo}"\n'
        f'author: "{AUTOR}"\n'
        'date: "2026"\n'
        "lang: pt-BR\n"
        "---\n\n"
    )
    return yaml + corpo_txt + "\n"


if __name__ == "__main__":
    caminho = sys.argv[1]
    with open(caminho, encoding="utf-8") as f:
        original = f.read()
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(converter(original))
    print(f"convertido: {caminho}")
