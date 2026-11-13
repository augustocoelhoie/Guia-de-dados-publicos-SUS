# Curadoria: o que ficou de fora do notebook e por quê

Critérios usados para incluir ou excluir uma fonte:

| Código | Critério de exclusão |
|---|---|
| **V** | Versão antiga de documento que tem versão mais recente no notebook (evita mistura de layouts) |
| **R** | Redundante: o conteúdo já está coberto por outra fonte incluída |
| **E** | Fora do escopo: não ajuda a escolher ou interpretar uma base de dados |
| **T** | Técnico demais para o público (desenvolvedores, não analistas) |
| **I** | Indisponível: link quebrado ou fora do ar na data da curadoria |
| **D** | Dado, não documentação: ferramenta de consulta, não texto explicativo |

## PDFs baixados do FTP do DATASUS e não enviados

| Arquivo | Código | Justificativa |
|---|---|---|
| `SIM/Estrutura_SIM_Anterior.pdf` | V | Layout anterior da Declaração de Óbito. Substituído por `SIM_estrutura_DO_2025.pdf`; manter os dois levaria a ferramenta a citar variáveis descontinuadas. |
| `SINASC/Estrutura_SINASC_anterior.pdf` | V | Layout anterior da Declaração de Nascido Vivo (antes do novo modelo de DN). Substituído pela estrutura atual. |
| `SIM/MTAB16M.pdf` | E | Manual do usuário do TabWin (ferramenta de tabulação). Ensina a operar o programa, não descreve as variáveis nem as regras das bases. |

## Links avaliados e não incluídos

| Fonte | Código | Justificativa |
|---|---|---|
| Guia de Boas Práticas da LGPD (Governo Digital) | I | Link fora do ar em 11/2026. Substituído pelo guia "Orientações e Boas Práticas na Proteção de Dados Pessoais" (material de apoio do MCTI). |
| MCTI — "Proteção de Dados Pessoais" | R | Conteúdo coberto pelo texto da LGPD e pelo guia de boas práticas já incluídos. |
| MCTI — "LAI, LGPD e Tarjamento de Dados Pessoais" | E | Trata de ocultar dados pessoais em documentos para responder pedidos da LAI, não de análise de microdados. |
| MCTI — "Passo a Passo para Tarjamento de Dados Pessoais" | E | Mesmo motivo do anterior. |
| RNDS — Atualizações técnicas | E | Histórico de versões de modelos de informação (vacinas, exames COVID). Gera ruído e não ajuda a escolher bases. |
| RNDS — Guia de Integração | T | Manual para desenvolvedores que conectam sistemas via HL7 FHIR. A RNDS não é base aberta para análise; as duas páginas institucionais incluídas bastam. |
| TabNet / DATASUS | D | Ferramenta de consulta de números, não documentação. Usada fora do notebook para conferir totais. |
| OpenDataSUS | R | Disponibiliza SIM e SINASC em CSV, mas a documentação das variáveis é a mesma do FTP já incluída. |
| SIGTAP | D | Tabela de procedimentos consultada pelo código; não é texto explicativo. Citada no catálogo. |
| Portaria GM/MS nº 3.232/2024 (SUS Digital) | E | Trata de financiamento e planejamento da transformação digital, não de uso de dados. |
| Portarias nº 589/2015 (PNIIS) e nº 3.632/2020 (ESD 2020–2028) | R | Citadas no guia `docs/lgpd-e-interoperabilidade.md`; o essencial para o analista (RNDS e padrões) está nas Portarias 1.434/2020 e 2.073/2011. |
| Repositório de Terminologias em Saúde (rts.saude.gov.br) | T | Catálogo técnico de vocabulários; o necessário (CID-10, LOINC, SIGTAP) já aparece na página da RNDS. |
| Espelho do FTP do DATASUS (Raphael Saldanha) | D | Alternativa de download dos arquivos, sem conteúdo explicativo próprio. |

## Observação sobre fonte secundária incluída

A dissertação da Fiocruz/ENSP sobre a documentação do SIH foi **incluída**, mas é anterior a mudanças recentes do sistema. Quando ela divergir do informe técnico do DATASUS, o informe prevalece.
