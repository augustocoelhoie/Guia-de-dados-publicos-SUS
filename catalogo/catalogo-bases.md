# Catálogo de bases públicas do SUS

> Gerado automaticamente de `catalogo-bases.csv` em 28/10/2026. Não edite este arquivo à mão — edite o CSV e rode `python scripts/gerar_catalogo.py`.

## Tabela-resumo

| ID | Base | Granularidade | Periodicidade | Chave de ligação | Dados | Dicionário |
|---|---|---|---|---|---|---|
| `SIH-RD` | **SIH/SUS** — AIH Reduzida (internações aprovadas) | Arquivo por UF; registro com município de residência e de internação | Mensal (competência de processamento) | CNES; MUNIC_RES / MUNIC_MOV (IBGE 6 díg.); DIAG_PRINC (CID-10); PROC_REA (SIGTAP) | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/) |
| `SIH-SP` | **SIH/SUS** — Serviços Profissionais | Arquivo por UF | Mensal (competência) | N_AIH (liga ao RD); CNES; SP_PROCREA (SIGTAP); CBO | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/) |
| `SIH-RJ` | **SIH/SUS** — AIH Rejeitadas | Arquivo por UF | Mensal (competência) | CNES; MUNIC_RES; DIAG_PRINC | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/) |
| `SIA-PA` | **SIA/SUS** — Produção Ambulatorial | Arquivo por UF; município do estabelecimento | Mensal (competência) | PA_CODUNI (CNES); PA_UFMUN (IBGE 6 díg.); PA_PROC_ID (SIGTAP); PA_CIDPRI | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Dados/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/) |
| `SIA-BI` | **SIA/SUS** — Boletim de Produção Ambulatorial Individualizado | Arquivo por UF | Mensal (competência) | CNES; município de residência; SIGTAP; CID-10 | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Dados/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/) |
| `SIA-APAC` | **SIA/SUS** — APACs (AQ quimioterapia; AR radioterapia; AM medicamentos; AN nefrologia; ATD diálise; ACF fístula; AD laudos diversos; AB/ABO bariátrica) | Arquivo por UF | Mensal (competência) | CNES; município de residência; SIGTAP; CID-10 | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Dados/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/) |
| `SIA-PS` | **SIA/SUS** — RAAS Psicossocial | Arquivo por UF | Mensal (competência) | CNES; município; SIGTAP; CID-10 | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Dados/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/) |
| `SIM-DO` | **SIM** — Declarações de Óbito | Arquivo por UF de residência; município de residência e de ocorrência | Anual (dados finais com defasagem; há pasta de preliminares) | CODMUNRES / CODMUNOCOR (IBGE 6 díg.); CODESTAB (CNES); CAUSABAS (CID-10) | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DORES/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DOCS/) |
| `SIM-REC` | **SIM** — Recortes temáticos (DOFET fetal; DOINF infantil; DOMAT materno; DOEXT causas externas) | Arquivo nacional por ano | Anual | Iguais ao SIM-DO | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DOFET/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DOCS/) |
| `SINASC-DN` | **SINASC** — Declarações de Nascido Vivo | Arquivo por UF de residência; município de residência e de nascimento | Anual (com preliminares) | CODMUNRES / CODMUNNASC (IBGE 6 díg.); CODESTAB (CNES) | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1996_/Dados/DNRES/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1996_/Doc/) |
| `CNES-ST` | **CNES** — Estabelecimentos | Arquivo por UF; município | Mensal (fotografia do cadastro) | CNES; CODUFMUN (IBGE 6 díg.) | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/ST/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Doc/) |
| `CNES-LT` | **CNES** — Leitos | Arquivo por UF | Mensal | CNES; CODUFMUN | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/LT/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Doc/) |
| `CNES-PF` | **CNES** — Profissionais | Arquivo por UF | Mensal | CNES; CBO; CODUFMUN | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/PF/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Doc/) |
| `CNES-OUT` | **CNES** — Outros (EQ equipamentos; EP equipes; SR serviços especializados; HB habilitações; RC regras contratuais; IN incentivos; EE/EF estab. de ensino/filantrópicos; GM gestão e metas) | Arquivo por UF | Mensal | CNES; CODUFMUN | [baixar](ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/) | [doc](ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Doc/) |
| `REF-SIGTAP` | **Tabela auxiliar** — SIGTAP (procedimentos; medicamentos; OPM) | Nacional | Mensal | Código do procedimento (10 díg.) → SIH PROC_REA; SIA PA_PROC_ID | [baixar](http://sigtap.datasus.gov.br/) | [doc](http://sigtap.datasus.gov.br/) |
| `REF-TERR` | **Tabela auxiliar** — Tabelas territoriais (municípios; regiões de saúde) | Município | Eventual | Código IBGE de 6 dígitos (sem dígito verificador) | [baixar](ftp://ftp.datasus.gov.br/territorio/tabelas/) | [doc](ftp://ftp.datasus.gov.br/territorio/) |

## Fichas por base

### `SIH-RD` — SIH/SUS: AIH Reduzida (internações aprovadas)

- **Arquivo padrão:** `RDUFAAMM.dbc` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** AIH (Autorização de Internação Hospitalar)
- **Unidade de registro (1 linha =):** 1 AIH aprovada
- **Granularidade:** Arquivo por UF; registro com município de residência e de internação
- **Periodicidade:** Mensal (competência de processamento)
- **Cobertura temporal:** 2008– (layout atual); 1992–2007 em pasta separada
- **Chaves de ligação:** CNES; MUNIC_RES / MUNIC_MOV (IBGE 6 díg.); DIAG_PRINC (CID-10); PROC_REA (SIGTAP)
- **Formato:** .dbc (DBF comprimido)
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/
- ⚠️ **Armadilha principal:** Conta AIHs e não pacientes; competência ≠ data da internação (use DT_INTER/DT_SAIDA)

### `SIH-SP` — SIH/SUS: Serviços Profissionais

- **Arquivo padrão:** `SPUFAAMM.dbc` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** AIH
- **Unidade de registro (1 linha =):** 1 ato profissional dentro de uma AIH
- **Granularidade:** Arquivo por UF
- **Periodicidade:** Mensal (competência)
- **Cobertura temporal:** 2008–
- **Chaves de ligação:** N_AIH (liga ao RD); CNES; SP_PROCREA (SIGTAP); CBO
- **Formato:** .dbc
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/
- ⚠️ **Armadilha principal:** Várias linhas por AIH — somar valores sem deduplicar infla o gasto

### `SIH-RJ` — SIH/SUS: AIH Rejeitadas

- **Arquivo padrão:** `RJUFAAMM.dbc` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** AIH
- **Unidade de registro (1 linha =):** 1 AIH rejeitada no processamento
- **Granularidade:** Arquivo por UF
- **Periodicidade:** Mensal (competência)
- **Cobertura temporal:** 2008–
- **Chaves de ligação:** CNES; MUNIC_RES; DIAG_PRINC
- **Formato:** .dbc
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/
- ⚠️ **Armadilha principal:** Rejeitadas podem ser reapresentadas e aprovadas depois — não somar com RD

### `SIA-PA` — SIA/SUS: Produção Ambulatorial

- **Arquivo padrão:** `PAUFAAMM.dbc` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** BPA consolidado / BPA-I / APAC
- **Unidade de registro (1 linha =):** Linha de produção aprovada (procedimento × estabelecimento × competência)
- **Granularidade:** Arquivo por UF; município do estabelecimento
- **Periodicidade:** Mensal (competência)
- **Cobertura temporal:** 2008– (layout atual); 1994–2007 em pasta separada
- **Chaves de ligação:** PA_CODUNI (CNES); PA_UFMUN (IBGE 6 díg.); PA_PROC_ID (SIGTAP); PA_CIDPRI
- **Formato:** .dbc
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Dados/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/
- ⚠️ **Armadilha principal:** Mede procedimentos (quantidades) e não pessoas; arquivos de UFs grandes vêm fatiados (a/b/c)

### `SIA-BI` — SIA/SUS: Boletim de Produção Ambulatorial Individualizado

- **Arquivo padrão:** `BIUFAAMM.dbc` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** BPA-I
- **Unidade de registro (1 linha =):** 1 procedimento individualizado
- **Granularidade:** Arquivo por UF
- **Periodicidade:** Mensal (competência)
- **Cobertura temporal:** 2008–
- **Chaves de ligação:** CNES; município de residência; SIGTAP; CID-10
- **Formato:** .dbc
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Dados/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/
- ⚠️ **Armadilha principal:** Cobre só procedimentos que exigem BPA-I; não é o universo ambulatorial

### `SIA-APAC` — SIA/SUS: APACs (AQ quimioterapia; AR radioterapia; AM medicamentos; AN nefrologia; ATD diálise; ACF fístula; AD laudos diversos; AB/ABO bariátrica)

- **Arquivo padrão:** `AQUFAAMM.dbc (e demais prefixos)` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** APAC (alta complexidade/custo)
- **Unidade de registro (1 linha =):** 1 APAC na competência
- **Granularidade:** Arquivo por UF
- **Periodicidade:** Mensal (competência)
- **Cobertura temporal:** 2008–
- **Chaves de ligação:** CNES; município de residência; SIGTAP; CID-10
- **Formato:** .dbc
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Dados/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/
- ⚠️ **Armadilha principal:** APAC de continuidade se repete mês a mês — mesma pessoa aparece em várias competências

### `SIA-PS` — SIA/SUS: RAAS Psicossocial

- **Arquivo padrão:** `PSUFAAMM.dbc` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** RAAS
- **Unidade de registro (1 linha =):** 1 registro de ação psicossocial
- **Granularidade:** Arquivo por UF
- **Periodicidade:** Mensal (competência)
- **Cobertura temporal:** 2012– (aprox.)
- **Chaves de ligação:** CNES; município; SIGTAP; CID-10
- **Formato:** .dbc
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Dados/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/
- ⚠️ **Armadilha principal:** Cobertura depende da adesão dos CAPS ao registro

### `SIM-DO` — SIM: Declarações de Óbito

- **Arquivo padrão:** `DOUFAAAA.dbc` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** DO (Declaração de Óbito)
- **Unidade de registro (1 linha =):** 1 óbito
- **Granularidade:** Arquivo por UF de residência; município de residência e de ocorrência
- **Periodicidade:** Anual (dados finais com defasagem; há pasta de preliminares)
- **Cobertura temporal:** 1979– (CID-9 até 1995; CID-10 desde 1996)
- **Chaves de ligação:** CODMUNRES / CODMUNOCOR (IBGE 6 díg.); CODESTAB (CNES); CAUSABAS (CID-10)
- **Formato:** .dbc (também CSV no OpenDataSUS)
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DORES/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DOCS/
- ⚠️ **Armadilha principal:** IDADE é codificada (unidade + valor); residência ≠ ocorrência; série com CID-9 e CID-10

### `SIM-REC` — SIM: Recortes temáticos (DOFET fetal; DOINF infantil; DOMAT materno; DOEXT causas externas)

- **Arquivo padrão:** `DOFETAA.dbc etc.` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** DO
- **Unidade de registro (1 linha =):** 1 óbito do recorte
- **Granularidade:** Arquivo nacional por ano
- **Periodicidade:** Anual
- **Cobertura temporal:** 1996–
- **Chaves de ligação:** Iguais ao SIM-DO
- **Formato:** .dbc
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DOFET/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DOCS/
- ⚠️ **Armadilha principal:** Recortes são subconjuntos — não somar com o DO por UF

### `SINASC-DN` — SINASC: Declarações de Nascido Vivo

- **Arquivo padrão:** `DNUFAAAA.dbc` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** DN (Declaração de Nascido Vivo)
- **Unidade de registro (1 linha =):** 1 nascido vivo
- **Granularidade:** Arquivo por UF de residência; município de residência e de nascimento
- **Periodicidade:** Anual (com preliminares)
- **Cobertura temporal:** 1994– (layout atual 1996–)
- **Chaves de ligação:** CODMUNRES / CODMUNNASC (IBGE 6 díg.); CODESTAB (CNES)
- **Formato:** .dbc (também CSV no OpenDataSUS)
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1996_/Dados/DNRES/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1996_/Doc/
- ⚠️ **Armadilha principal:** Novo modelo de DN (2011) mudou variáveis — ex.: idade gestacional em semanas (SEMAGESTAC)

### `CNES-ST` — CNES: Estabelecimentos

- **Arquivo padrão:** `STUFAAMM.dbc` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** Cadastro do estabelecimento
- **Unidade de registro (1 linha =):** 1 estabelecimento na competência
- **Granularidade:** Arquivo por UF; município
- **Periodicidade:** Mensal (fotografia do cadastro)
- **Cobertura temporal:** 2005-08–
- **Chaves de ligação:** CNES; CODUFMUN (IBGE 6 díg.)
- **Formato:** .dbc
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/ST/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Doc/
- ⚠️ **Armadilha principal:** É um retrato mensal — escolha UMA competência para contar; cadastro ≠ funcionamento

### `CNES-LT` — CNES: Leitos

- **Arquivo padrão:** `LTUFAAMM.dbc` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** Cadastro do estabelecimento
- **Unidade de registro (1 linha =):** Tipo de leito × estabelecimento
- **Granularidade:** Arquivo por UF
- **Periodicidade:** Mensal
- **Cobertura temporal:** 2005-08–
- **Chaves de ligação:** CNES; CODUFMUN
- **Formato:** .dbc
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/LT/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Doc/
- ⚠️ **Armadilha principal:** Separe leitos existentes de leitos SUS (QT_EXIST vs QT_SUS)

### `CNES-PF` — CNES: Profissionais

- **Arquivo padrão:** `PFUFAAMM.dbc` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** Cadastro do estabelecimento
- **Unidade de registro (1 linha =):** Vínculo profissional × estabelecimento
- **Granularidade:** Arquivo por UF
- **Periodicidade:** Mensal
- **Cobertura temporal:** 2005-08–
- **Chaves de ligação:** CNES; CBO; CODUFMUN
- **Formato:** .dbc
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/PF/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Doc/
- ⚠️ **Armadilha principal:** Um profissional com vários vínculos aparece várias vezes — conte vínculos ou carga horária

### `CNES-OUT` — CNES: Outros (EQ equipamentos; EP equipes; SR serviços especializados; HB habilitações; RC regras contratuais; IN incentivos; EE/EF estab. de ensino/filantrópicos; GM gestão e metas)

- **Arquivo padrão:** `EQUFAAMM.dbc etc.` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** Cadastro do estabelecimento
- **Unidade de registro (1 linha =):** Varia por tipo
- **Granularidade:** Arquivo por UF
- **Periodicidade:** Mensal
- **Cobertura temporal:** 2005-08– (varia por tipo)
- **Chaves de ligação:** CNES; CODUFMUN
- **Formato:** .dbc
- **Onde baixar:** ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Doc/
- ⚠️ **Armadilha principal:** Cada subpasta tem layout próprio — confira o dicionário do tipo

### `REF-SIGTAP` — Tabela auxiliar: SIGTAP (procedimentos; medicamentos; OPM)

- **Arquivo padrão:** `Download por competência` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** Tabela de Procedimentos do SUS
- **Unidade de registro (1 linha =):** 1 procedimento
- **Granularidade:** Nacional
- **Periodicidade:** Mensal
- **Cobertura temporal:** 2008–
- **Chaves de ligação:** Código do procedimento (10 díg.) → SIH PROC_REA; SIA PA_PROC_ID
- **Formato:** .zip (txt)
- **Onde baixar:** http://sigtap.datasus.gov.br/
- **Dicionário / documentação:** http://sigtap.datasus.gov.br/
- ⚠️ **Armadilha principal:** Valores e regras mudam por competência — use a tabela da mesma competência dos dados

### `REF-TERR` — Tabela auxiliar: Tabelas territoriais (municípios; regiões de saúde)

- **Arquivo padrão:** `Arquivos CSV/DBF` (UF = sigla, AA = ano, MM = mês)
- **Documento de origem:** DATASUS/IBGE
- **Unidade de registro (1 linha =):** 1 município
- **Granularidade:** Município
- **Periodicidade:** Eventual
- **Cobertura temporal:** —
- **Chaves de ligação:** Código IBGE de 6 dígitos (sem dígito verificador)
- **Formato:** .csv/.dbf
- **Onde baixar:** ftp://ftp.datasus.gov.br/territorio/tabelas/
- **Dicionário / documentação:** ftp://ftp.datasus.gov.br/territorio/
- ⚠️ **Armadilha principal:** IBGE usa 7 dígitos e o DATASUS 6 — corte o último dígito antes do join
