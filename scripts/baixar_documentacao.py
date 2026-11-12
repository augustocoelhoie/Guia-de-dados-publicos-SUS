"""Baixa automaticamente os dicionários e manuais do FTP do DATASUS.

Percorre /dissemin/publicos/<SISTEMA>/ procurando pastas de documentação
(Doc, DOC, DOCS, Docs) e baixa PDFs, DOCs e planilhas para fontes/pdf/<SISTEMA>/.
Esses arquivos são as fontes que vão para o NotebookLM.

Uso:
    python scripts/baixar_documentacao.py              # todos os sistemas
    python scripts/baixar_documentacao.py SIM SINASC   # só alguns
    python scripts/baixar_documentacao.py --listar     # só lista, não baixa

Só usa a biblioteca padrão do Python (ftplib).
"""
from __future__ import annotations

import ftplib
import sys
from pathlib import Path

HOST = "ftp.datasus.gov.br"
BASE = "/dissemin/publicos"
SISTEMAS = {
    "SIH": "SIHSUS",
    "SIA": "SIASUS",
    "SIM": "SIM",
    "SINASC": "SINASC",
    "CNES": "CNES",
}
PASTAS_DOC = {"doc", "docs", "documentacao", "documentação"}
EXTENSOES = {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".txt", ".odt"}
PROFUNDIDADE_MAX = 3
DESTINO = Path(__file__).resolve().parents[1] / "fontes" / "pdf"


def eh_pasta(ftp: ftplib.FTP, caminho: str) -> bool:
    atual = ftp.pwd()
    try:
        ftp.cwd(caminho)
        return True
    except ftplib.error_perm:
        return False
    finally:
        ftp.cwd(atual)


def achar_pastas_doc(ftp: ftplib.FTP, raiz: str, nivel: int = 0) -> list[str]:
    if nivel > PROFUNDIDADE_MAX:
        return []
    achadas: list[str] = []
    try:
        itens = ftp.nlst(raiz)
    except ftplib.error_perm:
        return []
    for item in itens:
        nome = item.rstrip("/").split("/")[-1]
        caminho = item if item.startswith("/") else f"{raiz}/{nome}"
        if "." in nome[-5:]:  # parece arquivo
            continue
        if nome.lower() == "dados":  # pasta de dados é enorme: pula
            continue
        if not eh_pasta(ftp, caminho):
            continue
        if nome.lower() in PASTAS_DOC:
            achadas.append(caminho)
        else:
            achadas += achar_pastas_doc(ftp, caminho, nivel + 1)
    return achadas


def baixar(ftp: ftplib.FTP, pasta: str, destino: Path, so_listar: bool) -> int:
    n = 0
    for item in ftp.nlst(pasta):
        nome = item.split("/")[-1]
        if Path(nome).suffix.lower() not in EXTENSOES:
            continue
        caminho = item if item.startswith("/") else f"{pasta}/{nome}"
        alvo = destino / nome
        print(("  [lista] " if so_listar else "  ↓ ") + caminho)
        n += 1
        if so_listar or alvo.exists():
            continue
        destino.mkdir(parents=True, exist_ok=True)
        with alvo.open("wb") as f:
            ftp.retrbinary(f"RETR {caminho}", f.write)
    return n


def main(args: list[str]) -> None:
    so_listar = "--listar" in args
    escolhidos = [a.upper() for a in args if not a.startswith("--")] or list(SISTEMAS)
    with ftplib.FTP(HOST, timeout=60) as ftp:
        ftp.login()  # anônimo
        ftp.encoding = "latin-1"
        total = 0
        for sigla in escolhidos:
            raiz = f"{BASE}/{SISTEMAS[sigla]}"
            print(f"\n== {sigla} ({raiz})")
            for pasta in achar_pastas_doc(ftp, raiz):
                total += baixar(ftp, pasta, DESTINO / sigla, so_listar)
    print(f"\n{total} arquivo(s) {'encontrados' if so_listar else 'processados'} em {DESTINO}")


if __name__ == "__main__":
    main(sys.argv[1:])
