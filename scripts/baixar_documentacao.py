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


def tamanho(ftp: ftplib.FTP, caminho: str) -> int:
    """Tamanho do arquivo em bytes (0 se o servidor não informar)."""
    try:
        ftp.voidcmd("TYPE I")
        return ftp.size(caminho) or 0
    except ftplib.all_errors:
        return 0


def fmt(nbytes: int) -> str:
    return f"{nbytes / 1024 / 1024:6.2f} MB" if nbytes else "   ? MB"


def baixar(ftp: ftplib.FTP, pasta: str, destino: Path, so_listar: bool) -> tuple[int, int]:
    n, soma = 0, 0
    for item in ftp.nlst(pasta):
        nome = item.split("/")[-1]
        if Path(nome).suffix.lower() not in EXTENSOES:
            continue
        caminho = item if item.startswith("/") else f"{pasta}/{nome}"
        alvo = destino / nome
        tam = tamanho(ftp, caminho)
        n, soma = n + 1, soma + tam
        print(f"  {'[lista]' if so_listar else '↓'} {fmt(tam)}  {caminho}")
        if so_listar or alvo.exists():
            continue
        destino.mkdir(parents=True, exist_ok=True)
        with alvo.open("wb") as f:
            ftp.retrbinary(f"RETR {caminho}", f.write)
    return n, soma


def main(args: list[str]) -> None:
    so_listar = "--listar" in args
    escolhidos = [a.upper() for a in args if not a.startswith("--")] or list(SISTEMAS)
    total, bytes_total = 0, 0
    with ftplib.FTP(HOST, timeout=60) as ftp:
        ftp.login()  # anônimo
        ftp.encoding = "latin-1"
        for sigla in escolhidos:
            raiz = f"{BASE}/{SISTEMAS[sigla]}"
            print(f"\n== {sigla} ({raiz})")
            n_sis, b_sis = 0, 0
            for pasta in achar_pastas_doc(ftp, raiz):
                n, b = baixar(ftp, pasta, DESTINO / sigla, so_listar)
                n_sis, b_sis = n_sis + n, b_sis + b
            print(f"   subtotal {sigla}: {n_sis} arquivo(s), {fmt(b_sis).strip()}")
            total, bytes_total = total + n_sis, bytes_total + b_sis
    acao = "encontrados" if so_listar else "processados"
    print(f"\nTOTAL: {total} arquivo(s) {acao}, {fmt(bytes_total).strip()} em {DESTINO}")
    if so_listar and bytes_total:
        # estimativa grosseira: FTP do DATASUS costuma entregar ~1-5 MB/s
        rapido, lento = bytes_total / 5e6 / 60, bytes_total / 1e6 / 60
        print(f"Tempo estimado de download: {max(rapido, 1):.0f} a {max(lento, 1):.0f} min")


if __name__ == "__main__":
    main(sys.argv[1:])
