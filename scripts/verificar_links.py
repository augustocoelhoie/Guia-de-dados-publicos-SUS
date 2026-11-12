"""Verifica se os links do catálogo e das fontes continuam no ar.

Lê todos os arquivos .md e .csv do repositório, extrai URLs http(s) e ftp
e testa cada uma. Sai com código 1 se algum link quebrar (usado no GitHub Actions).

Uso:
    python scripts/verificar_links.py
"""
from __future__ import annotations

import ftplib
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

RAIZ = Path(__file__).resolve().parents[1]
PADRAO = re.compile(r"(?:https?|ftp)://[^\s)\]\"'|,>]+")
IGNORAR = ("localhost", "example.com", "SEU-USUARIO")
CABECALHO = {"User-Agent": "Mozilla/5.0 (verificador de links guia-dados-sus)"}


def coletar() -> set[str]:
    urls: set[str] = set()
    for arq in list(RAIZ.rglob("*.md")) + list(RAIZ.rglob("*.csv")):
        if ".git" in arq.parts:
            continue
        for u in PADRAO.findall(arq.read_text(encoding="utf-8")):
            u = u.rstrip(".;:")
            if not any(i in u for i in IGNORAR):
                urls.add(u)
    return urls


def testar_http(url: str) -> tuple[bool, str]:
    for metodo in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=metodo, headers=CABECALHO)
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status < 400, str(r.status)
        except urllib.error.HTTPError as e:
            if metodo == "GET":
                return e.code < 400, str(e.code)
        except Exception as e:  # noqa: BLE001
            if metodo == "GET":
                return False, type(e).__name__
    return False, "?"


def testar_ftp(url: str) -> tuple[bool, str]:
    p = urlparse(url)
    try:
        with ftplib.FTP(p.hostname, timeout=30) as ftp:
            ftp.login()
            ftp.cwd(p.path or "/")
        return True, "ok"
    except Exception as e:  # noqa: BLE001
        return False, type(e).__name__


def main() -> None:
    urls = sorted(coletar())
    quebrados = []
    for u in urls:
        ok, info = testar_ftp(u) if u.startswith("ftp") else testar_http(u)
        print(f"{'✅' if ok else '❌'} {info:>6}  {u}")
        if not ok:
            quebrados.append(u)
    print(f"\n{len(urls) - len(quebrados)}/{len(urls)} links OK")
    sys.exit(1 if quebrados else 0)


if __name__ == "__main__":
    main()
