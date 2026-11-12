# Armadilhas dos dados públicos do SUS

Os erros que mais aparecem em análises com bases do DATASUS — e como evitá-los.

## Transversais (valem para todas as bases)

| Armadilha | O que acontece | Como evitar |
|---|---|---|
| **Formato .dbc** | É um DBF comprimido; não abre no Excel nem no pandas direto | R: `read.dbc` / `microdatasus`; Python: `PySUS`; ou TabWin |
| **Código de município com 6 dígitos** | O IBGE usa 7 (com dígito verificador); o join falha silenciosamente | Corte o 7º dígito do código IBGE antes de ligar |
| **Residência × ocorrência** | Cidades-polo "importam" internações e óbitos | Taxas populacionais → residência; carga de serviços → ocorrência/movimento |
| **Layout muda no tempo** | Variáveis entram, saem ou mudam de código | Leia o dicionário da época e documente o recorte temporal |
| **Dados preliminares** | Anos recentes ainda recebem registros | Indique se o ano é preliminar; refaça a análise quando fechar |
| **Subnotificação desigual** | Cobertura varia por região e período | Compare com estimativas de cobertura antes de comparar regiões |
| **Desidentificação** | Microdados públicos não identificam pessoas | Não tente reidentificar (ver `lgpd-e-interoperabilidade.md`) |

## SIH (internações)

- **AIH ≠ paciente ≠ internação única.** Reinternações e AIHs de continuação geram várias linhas por pessoa.
- **Competência ≠ data do evento.** Use `DT_INTER`/`DT_SAIDA` e baixe meses posteriores.
- **Só o SUS.** Internações na saúde suplementar e particulares não estão aqui.
- **Valores são de tabela SUS**, não custo real do hospital.
- **Arquivo SP tem várias linhas por AIH** — somar sem cuidado infla o gasto.

## SIA (ambulatorial)

- **Mede procedimentos, não pessoas** (sobretudo o PA).
- **APAC de continuidade se repete** a cada mês do tratamento.
- **UFs grandes têm arquivos fatiados** (sufixos a, b, c) — baixe todos.

## SIM (óbitos)

- **`IDADE` codificada** (unidade + valor).
- **Causa básica (`CAUSABAS`) ≠ causas da linha A–D** da DO.
- **Causas mal definidas** (capítulo XVIII da CID-10) variam por região — afetam comparações.
- **Recortes DOFET/DOINF/DOMAT/DOEXT** são subconjuntos; não some com o DO por UF.

## SINASC (nascidos vivos)

- **Novo modelo de DN em 2011** mudou variáveis (idade gestacional em semanas, por exemplo).
- **`PESO` em gramas**; valores extremos exigem checagem.

## CNES (estabelecimentos)

- **É um retrato mensal**: escolha uma competência; somar meses multiplica.
- **Cadastrado ≠ funcionando ≠ atende SUS.** Filtre leitos SUS, vínculo SUS etc.
- **Profissional aparece uma vez por vínculo.**
