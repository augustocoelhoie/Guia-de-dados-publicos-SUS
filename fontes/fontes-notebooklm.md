# Fontes curadas para o NotebookLM

Lista do que entra no notebook, por bloco. A versão gratuita do NotebookLM aceita um número limitado de fontes por notebook (confira o limite atual na própria ferramenta) — por isso a curadoria abaixo prioriza **qualidade sobre volume**.

Legenda de prioridade: 🟢 obrigatória · 🟡 recomendada · ⚪ opcional
Tipo de upload: **PDF** (arquivo baixado pelo script) · **URL** (colar em *Adicionar fonte → Site*)

---

## 1. Documentação técnica do DATASUS

Rode `python scripts/baixar_documentacao.py` — ele percorre o FTP e salva tudo em `fontes/pdf/<SISTEMA>/`. Depois escolha os arquivos abaixo.

| Prioridade | Sistema | O que procurar na pasta baixada | Tipo | Onde fica |
|---|---|---|---|---|
| 🟢 | SIH | Informe técnico / dicionário do arquivo RD (AIH reduzida) | PDF | `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/` |
| 🟢 | SIA | Informe técnico do SIA (layout PA, BI, APAC) | PDF | `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/` |
| 🟢 | SIM | Estrutura / dicionário da DO (variáveis do SIM) | PDF | `ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/` (pasta de documentação) |
| 🟢 | SINASC | Estrutura / dicionário da DN | PDF | `ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1996_/Doc/` |
| 🟢 | CNES | Dicionário dos arquivos ST, LT, PF | PDF | `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Doc/` |
| 🟡 | SIH | Manual técnico operacional do SIH (regras de AIH, permanência, IDENT) | PDF | Portal do SIH / BVS MS |
| 🟡 | Geral | Página de Transferência de Arquivos do DATASUS | URL | https://datasus.saude.gov.br/transferencia-de-arquivos/ |
| ⚪ | Geral | TabNet (para conferir totais) | URL | https://datasus.saude.gov.br/informacoes-de-saude-tabnet/ |

> 💡 Se o FTP estiver instável, o pesquisador Raphael Saldanha mantém um espelho público: https://rfsaldanha.github.io/data-projects/s3-datasus-ftp-mirror.html

## 2. Documentação secundária de alta qualidade

| Prioridade | Fonte | Por que entra | Tipo | Link |
|---|---|---|---|---|
| 🟢 | Fiocruz/ICICT — *SIH/SUS: documentação do sistema para auxiliar o uso das suas informações* | Explica regras do SIH que os dicionários não explicam | PDF | https://www.arca.fiocruz.br/handle/icict/2372 |
| 🟡 | Pacote **microdatasus** (R) | Lista de todos os tipos de arquivo e rotinas de leitura | URL | https://github.com/rfsaldanha/microdatasus |
| 🟡 | Pacote **PySUS** (Python) | Leitura de .dbc em Python | URL | https://github.com/AlertaDengue/PySUS |
| ⚪ | OpenDataSUS | SIM e SINASC também em CSV | URL | https://opendatasus.saude.gov.br/ |
| ⚪ | SIGTAP | Tabela de procedimentos (código de 10 dígitos) | URL | http://sigtap.datasus.gov.br/ |

## 3. Proteção de dados (LGPD)

| Prioridade | Fonte | Artigos-chave | Tipo | Link |
|---|---|---|---|---|
| 🟢 | Lei nº 13.709/2018 (LGPD) — texto compilado | Art. 5º (definições, dado sensível), 7º, 11 (dados sensíveis), 12 (anonimização), 13 (estudos em saúde pública) | URL ou PDF | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm |
| 🟡 | Guia "Orientações e Boas Práticas na Proteção de Dados Pessoais" (material de apoio LGPD do MCTI) | Aplicação da LGPD no setor público | PDF | https://www.gov.br/mcti/pt-br/acesso-a-informacao/lei-geral-de-protecao-de-dados-pessoais-lgpd/material-de-apoio-1 |

> Nota de curadoria: o link original do Guia de Boas Práticas da LGPD (Governo Digital) estava fora do ar em 11/2026 e foi substituído pela página de material de apoio do MCTI. Os guias de *tarjamento* foram deixados de fora porque tratam de ocultar dados em documentos para a LAI, não de análise de dados.

## 4. Interoperabilidade e RNDS

| Prioridade | Fonte | O que traz | Tipo | Link |
|---|---|---|---|---|
| 🟢 | Portaria GM/MS nº 2.073/2011 | Padrões de interoperabilidade no SUS (openEHR para RES, HL7 etc.) | URL | https://bvsms.saude.gov.br/bvs/saudelegis/gm/2011/prt2073_31_08_2011.html |
| 🟢 | Portaria GM/MS nº 1.434/2020 | Institui o Conecte SUS e a RNDS (arts. 254-A a 254-C da PRC nº 1/2017) | URL | https://bvsms.saude.gov.br/bvs/saudelegis/gm/2020/prt1434_29_05_2020.html |
| 🟢 | Página oficial da RNDS (Ministério da Saúde) | Estrutura, FHIR, terminologias | URL | https://www.gov.br/saude/pt-br/composicao/seidigi/rnds |
| 🟡 | Estrutura do projeto RNDS | Modelos de informação, CID-10, LOINC, SIGTAP | URL | https://www.gov.br/saude/pt-br/composicao/seidigi/rnds/estrutura-do-projeto |
| 🟡 | Guia de Integração da RNDS | Como sistemas se conectam (FHIR) | URL | https://rnds-guia.prod.saude.gov.br/ |
| ⚪ | Portaria GM/MS nº 3.232/2024 | Programa SUS Digital | URL | https://bvsms.saude.gov.br/bvs/saudelegis/gm/2024/prt3232_04_03_2024.html |
| ⚪ | Repositório de Terminologias em Saúde | Vocabulários controlados | URL | https://rts.saude.gov.br |

---

## Dicas de curadoria

1. **Uma fonte = um assunto.** Se um PDF do FTP mistura vários layouts antigos, prefira a versão mais recente.
2. **Renomeie os PDFs** antes de subir (`SIH_dicionario_RD_2024.pdf`). O NotebookLM cita pelo nome do arquivo — nomes claros deixam as citações auditáveis.
3. **Registre o que ficou de fora** e por quê em `avaliacao/registro-de-erros.md` — isso também é curadoria.
