"""Gera catalogo/catalogo-bases.md a partir de catalogo/catalogo-bases.csv.

O CSV é a fonte única da verdade: edite o CSV e rode
    python scripts/gerar_catalogo.py
para regenerar o Markdown (tabela-resumo + fichas detalhadas).
"""
from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CSV = RAIZ / "catalogo" / "catalogo-bases.csv"
MD = RAIZ / "catalogo" / "catalogo-bases.md"


def link(url: str, rotulo: str) -> str:
    return f"[{rotulo}]({url})" if url.startswith(("http", "ftp")) else url


def esc(txt: str) -> str:
    return txt.replace("|", "\\|")


def main() -> None:
    with CSV.open(encoding="utf-8") as f:
        linhas = list(csv.DictReader(f))

    out: list[str] = [
        "# Catálogo de bases públicas do SUS",
        "",
        f"> Gerado automaticamente de `catalogo-bases.csv` em {date.today():%d/%m/%Y}. "
        "Não edite este arquivo à mão — edite o CSV e rode `python scripts/gerar_catalogo.py`.",
        "",
        "## Tabela-resumo",
        "",
        "| ID | Base | Granularidade | Periodicidade | Chave de ligação | Dados | Dicionário |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in linhas:
        out.append(
            f"| `{r['id']}` | **{esc(r['sistema'])}** — {esc(r['base'])} | {esc(r['granularidade'])} "
            f"| {esc(r['periodicidade'])} | {esc(r['chaves_ligacao'])} "
            f"| {link(r['onde_baixar'], 'baixar')} | {link(r['dicionario'], 'doc')} |"
        )

    out += ["", "## Fichas por base", ""]
    for r in linhas:
        out += [
            f"### `{r['id']}` — {r['sistema']}: {r['base']}",
            "",
            f"- **Arquivo padrão:** `{r['arquivo_padrao']}` (UF = sigla, AA = ano, MM = mês)",
            f"- **Documento de origem:** {r['documento_origem']}",
            f"- **Unidade de registro (1 linha =):** {r['unidade_registro']}",
            f"- **Granularidade:** {r['granularidade']}",
            f"- **Periodicidade:** {r['periodicidade']}",
            f"- **Cobertura temporal:** {r['cobertura']}",
            f"- **Chaves de ligação:** {r['chaves_ligacao']}",
            f"- **Formato:** {r['formato']}",
            f"- **Onde baixar:** {r['onde_baixar']}",
            f"- **Dicionário / documentação:** {r['dicionario']}",
            f"- ⚠️ **Armadilha principal:** {r['armadilha_principal']}",
            "",
        ]

    MD.write_text("\n".join(out), encoding="utf-8")
    print(f"OK: {len(linhas)} bases -> {MD.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
