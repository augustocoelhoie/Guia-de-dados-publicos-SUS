"""Confere nos microdados reais se as variáveis citadas no guia existem.

Baixa UM arquivo pequeno de cada sistema (Acre, que é a menor UF), lê as
colunas e compara com as variáveis usadas no catálogo e nas perguntas-teste.
Nada é salvo no repositório (os arquivos ficam numa pasta temporária).

Não precisa instalar nada: no formato .dbc o cabeçalho com os nomes das
colunas fica SEM compressão no início do arquivo, então basta ler os
primeiros bytes (só a parte de dados é comprimida). Usa apenas a
biblioteca padrão do Python.

Uso:
    python scripts/conferir_variaveis.py
"""
from __future__ import annotations

import ftplib
import tempfile
from pathlib import Path


def colunas_dbc(caminho: Path) -> list[str]:
    """Lê os nomes das colunas do cabeçalho DBF (não comprimido) de um .dbc."""
    dados = caminho.read_bytes()
    tam_cabecalho = int.from_bytes(dados[8:10], "little")
    nomes = []
    for inicio in range(32, tam_cabecalho, 32):  # 1 descritor de 32 bytes por coluna
        if dados[inicio] == 0x0D:  # fim dos descritores
            break
        nomes.append(dados[inicio:inicio + 11].split(b"\x00")[0].decode("latin-1").strip())
    return nomes


HOST = "ftp.datasus.gov.br"
ARQUIVOS = {
    "SIH-RD": ("/dissemin/publicos/SIHSUS/200801_/Dados/RDAC2401.dbc",
               ["MUNIC_RES", "MUNIC_MOV", "DIAG_PRINC", "PROC_REA", "VAL_TOT",
                "MORTE", "DIAS_PERM", "DT_INTER", "DT_SAIDA", "CNES", "N_AIH",
                "ANO_CMPT", "MES_CMPT"]),
    "SIA-PA": ("/dissemin/publicos/SIASUS/200801_/Dados/PAAC2401.dbc",
               ["PA_CODUNI", "PA_UFMUN", "PA_PROC_ID", "PA_CIDPRI"]),
    "SIM-DO": ("/dissemin/publicos/SIM/CID10/DORES/DOAC2022.dbc",
               ["IDADE", "CAUSABAS", "CODMUNRES", "CODMUNOCOR", "CODESTAB"]),
    "SINASC": ("/dissemin/publicos/SINASC/1996_/Dados/DNRES/DNAC2022.dbc",
               ["PESO", "SEMAGESTAC", "CODMUNRES", "CODMUNNASC", "CODESTAB"]),
    "CNES-ST": ("/dissemin/publicos/CNES/200508_/Dados/ST/STAC2401.dbc",
                ["CNES", "CODUFMUN"]),
}


def main() -> None:
    pasta = Path(tempfile.mkdtemp(prefix="sus_"))
    problemas = 0
    with ftplib.FTP(HOST, timeout=120) as ftp:
        ftp.login()
        for nome, (caminho, esperadas) in ARQUIVOS.items():
            dbc = pasta / Path(caminho).name
            print(f"\n== {nome}  ({caminho})")
            try:
                with dbc.open("wb") as f:
                    ftp.retrbinary(f"RETR {caminho}", f.write)
            except ftplib.error_perm as e:
                print(f"   ⚠️ arquivo não encontrado ({e}). Ajuste o ano/mês no script.")
                problemas += 1
                continue
            colunas = set(colunas_dbc(dbc))
            faltando = 0
            for v in esperadas:
                ok = v in colunas
                faltando += not ok
                print(f"   {'✅' if ok else '❌'} {v}")
            if faltando:  # mostra todas as colunas para achar o nome certo
                print("   colunas do arquivo:", ", ".join(sorted(colunas)))
            problemas += faltando
    print(f"\n{'Tudo confere.' if not problemas else f'{problemas} item(ns) para revisar.'}")
    print("Anote o resultado em avaliacao/registro-de-erros.md (Lições de curadoria).")


if __name__ == "__main__":
    main()
