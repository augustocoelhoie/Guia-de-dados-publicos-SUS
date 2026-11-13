# 20 perguntas-teste — avaliação do notebook

**Objetivo:** medir se o notebook do NotebookLM responde com precisão e **cita a fonte certa** — e documentar onde ele erra.

**Protocolo**
1. Faça cada pergunta no NotebookLM exatamente como está escrita, em uma conversa nova.
2. Compare com o **gabarito** e abra a citação que a ferramenta indicou.
3. Classifique: ✅ correta e bem citada · ⚠️ correta mas incompleta ou com citação fraca · ❌ errada, inventada ou sem citação.
4. Anote a página/seção exata da fonte em **Conferido em** e o comportamento em `registro-de-erros.md`.
5. **O gabarito também é testado.** Ele foi redigido antes da conferência. Se a fonte primária disser algo diferente, a fonte vence: corrija o gabarito, marque **Sim** na coluna *Gabarito corrigido?* e explique no registro de erros.

As perguntas cobrem cinco tipos de risco: **conceito** (o que é), **variável** (onde está), **armadilha** (o que engana), **norma** (o que a lei diz) e **controle** (pergunta cuja resposta *não* está nas fontes — a ferramenta deveria dizer que não sabe).

---

## Placar

| # | Tema | Tipo | Resultado | Conferido em (doc · pág./seção) | Gabarito corrigido? |
|---|---|---|---|---|---|
| 1 | SIH | conceito | ✅ | SIH_informe_tecnico_2016-03 · "2 Layout dos arquivos RD.dbf", p. 1-3; FIOCRUZ_Santos · Anexo V, p. 119 | Não |
| 2 | SIH | armadilha | ✅ | FIOCRUZ_Santos · AIH conta internações, não pacientes; tipos de AIH (IDENT 1, 3, 5), p. 47 | Não |
| 3 | SIH | variável | ✅ | SIH_informe_tecnico_2016-03 · layout RD, p. 1-2; FIOCRUZ_Santos · Anexo V, p. 119,121 | Não |
| 4 | SIH | armadilha | ✅ | FIOCRUZ_Santos · definição de Competência e Data da internação, p.55, 64; SIH_informe_tecnico_2016-03 · layout RD, p. 1 | Não |
| 5 | SIH | variável | ⚠️ | SIH_informe_tecnico_2016-03 · layout RD, p. 2; FIOCRUZ_Santos · Anexo V e tabela de motivos de cobrança, p. 55-56, 58, 113-114, 119-122, 202 | Não |
| 6 | SIA | conceito | ⚠️ | SIA_informe_tecnico_2019-07 · itens 2.1 (PA) e 3 (arquivos de APAC), p. 5-14 | Sim (complementado) |
| 7 | SIA | conceito | ✅ | SIA_informe_tecnico_2019-07 · item 2.1, instrumentos e quantidade de registros do PA, p. 2-3 | Não |
| 8 | SIA | armadilha | ✅ | SIA_informe_tecnico_2019-07 · itens 2.1, 3.1 e 3.4.4 (layout AQ: AP_TPAPAC, AQ_CONTTR), p. 2, 5, 9 | Não |
| 9 | SIM | conceito | ⚠️ | SIM_legislacao · DO como documento padrão, p. 42; ano da CID-10: não consta nas fontes | Sim |
| 10 | SIM | armadilha | ⚠️ | SIM_estrutura_DO_2025 · campo IDADE, p. 2 | Sim |
| 11 | SIM | variável | ✅ | SIM_estrutura_DO_2025 · campo CAUSABAS, p. 5 | Não |
| 12 | SIM | armadilha | ✅ | SIM_estrutura_DO_2025 · CODMUNRES/CODMUNOCOR, p. 3; SIM_introducao · registro "no lugar do falecimento", p. 5 | Não |
| 13 | SINASC | variável | ✅ | SINASC_dicionario_arquivos_DBC · "I - Identificação do Recém Nascido", campo PESO, p. 1 | Não |
| 14 | CNES | conceito | ⚠️ | CNES_informe_tecnico_2017-06 · apresentação e nomenclatura STufaamm, p. 1-2 | Não |
| 15 | Ligação | variável | ✅ | SIH_informe_tecnico_2016-03 · CNES, MUNIC_RES, MUNIC_MOV, p. 3-5; CNES_informe_tecnico_2017-06 · CNES, CODUFMUN "sem dígito", p. 3, 11, 18, 20-21, 23, 27-33 | Não |
| 16 | LGPD | norma | ✅ | LGPD_Lei_13709_2018_compilada · art. 5º, II | Não |
| 17 | LGPD | norma | ✅ | LGPD_Lei_13709_2018_compilada · art. 5º, III; art. 12, caput e §§ 1º e 2º | Não |
| 18 | LGPD | norma | ⚠️ | LGPD_Lei_13709_2018_compilada · arts. 5º XVIII, 7º IV, 11 II c, 13 e 16 II | Não |
| 19 | Interop. | norma | ✅ | PORTARIA_1434_2020 · ementa e art. 254-A; página "Estrutura do projeto" da RNDS · HL7 FHIR | Não |
| 20 | Controle | controle | ✅ | Nenhuma: a ferramenta declarou que o dado não está nas fontes | Não |
| | | **Total** | **14/20 ✅ · 6 ⚠️ · 0 ❌** | | **3/20** |

---

## Perguntas e gabarito

### 1. Qual arquivo do SIH/SUS contém as internações aprovadas e qual é sua periodicidade?
**Gabarito:** O arquivo **RD** (AIH Reduzida), nomeado `RDUFAAMM.dbc`. É **mensal por UF**, organizado pela **competência de processamento**.
**Fonte esperada:** Informe técnico / dicionário do SIH (FTP `SIHSUS/200801_/Doc`).

### 2. Contar as linhas do arquivo RD dá o número de pacientes internados?
**Gabarito:** **Não.** Cada linha é uma **AIH aprovada**, não um paciente. Uma mesma pessoa pode ter várias AIHs (reinternações, AIHs de continuação/longa permanência), e os arquivos públicos não trazem identificador do paciente. O correto é falar em "internações (AIHs)".
**Fonte esperada:** Documentação do SIH (Fiocruz/ICICT; informe técnico).

### 3. Qual a diferença entre `MUNIC_RES` e `MUNIC_MOV` no SIH?
**Gabarito:** `MUNIC_RES` = município de **residência do paciente**; `MUNIC_MOV` = município do **estabelecimento** onde ocorreu a internação. Usar um ou outro muda a análise (ex.: taxa por residente × produção por município polo).
**Fonte esperada:** Dicionário do arquivo RD.

### 4. Se eu filtrar o RD pelo mês de competência "janeiro", obtenho as internações que começaram em janeiro?
**Gabarito:** **Não necessariamente.** A competência é o mês de **processamento/apresentação** da AIH. Para o período real use `DT_INTER` (data de internação) e `DT_SAIDA` (data de saída) — e baixe competências seguintes para capturar AIHs apresentadas com atraso.
**Fonte esperada:** Informe técnico do SIH.

### 5. Quais variáveis do RD trazem diagnóstico, procedimento, valor e óbito?
**Gabarito:** `DIAG_PRINC` (CID-10 principal), `PROC_REA` (procedimento realizado, código SIGTAP), `VAL_TOT` (valor total), `MORTE` (indicador de óbito na internação); `DIAS_PERM` traz os dias de permanência.
**Fonte esperada:** Dicionário do arquivo RD.

### 6. O que é APAC e quais arquivos do SIA a utilizam?
**Gabarito:** Autorização de Procedimentos Ambulatoriais — usada para procedimentos de **alta complexidade/custo**. Arquivos: AQ (quimioterapia), AR (radioterapia), AM (medicamentos), AN (nefrologia), ATD (tratamento dialítico), ACF (confecção de fístula), AD (laudos diversos), AB/ABO (cirurgia bariátrica e acompanhamento). **Além disso, os procedimentos de APAC também entram no arquivo geral PA**, identificados por `PA_DOCORIG` = "P" (principal) ou "S" (secundário).
> ✏️ *Gabarito complementado após a conferência (13/11/2026): a versão original não mencionava que o PA também traz os registros de APAC.*
**Fonte esperada:** Informe técnico do SIA.

### 7. O arquivo PA do SIA permite contar quantas pessoas foram atendidas?
**Gabarito:** **Não.** O PA registra **produção aprovada** (quantidade de procedimentos por estabelecimento e competência), incluindo registros consolidados (BPA-C) sem identificação individual. Para registros individualizados há o BI (BPA-I) e as APACs, que cobrem só parte dos procedimentos.
**Fonte esperada:** Informe técnico do SIA.

### 8. Por que somar APACs de vários meses pode superestimar o número de pacientes em quimioterapia?
**Gabarito:** Porque a APAC de **continuidade** é reapresentada a cada competência enquanto o tratamento dura — a mesma pessoa aparece em vários meses.
**Fonte esperada:** Informe técnico do SIA / regras de APAC.

### 9. Qual é o documento-base do SIM e desde quando o sistema usa a CID-10?
**Gabarito:** A **Declaração de Óbito (DO)**. O SIM usa a **CID-10 desde 1996**; de 1979 a 1995 usava a CID-9.
> ✏️ *Gabarito corrigido após a conferência (13/11/2026): o ano de 1996 **não consta em nenhuma fonte carregada no notebook**. A evidência disponível é a própria organização do FTP do DATASUS, com pastas separadas `SIM/CID9` (1979–1995) e `SIM/CID10` (1996 em diante). A resposta correta da ferramenta seria dizer que não encontrou o ano, e foi o que ela fez.*
**Fonte esperada:** Documentação do SIM.

### 10. Posso usar a variável `IDADE` do SIM diretamente como idade em anos?
**Gabarito:** **Não.** É um campo **composto**: o primeiro dígito indica a unidade e os dois seguintes o valor. Códigos iniciados por 4 = anos; por 5 = 100 anos ou mais (5 + 02 = 102 anos). É preciso decodificar antes de calcular.
> ✏️ *Gabarito corrigido após a conferência (13/11/2026): as fontes **divergem** nos códigos de unidade abaixo de 1 ano. O `SIM_estrutura_DO_2025` lista 1 = minuto, 2 = hora, 3 = mês e não diz qual código indica **dias**. O pacote microdatasus decodifica 0 = minutos, 1 = horas, 2 = dias, 3 = meses. Para idades em anos (4 e 5) as fontes concordam. Antes de analisar óbitos infantis, confira a distribuição do primeiro dígito nos próprios dados.*
**Fonte esperada:** Dicionário da DO.

### 11. Qual variável do SIM traz a causa básica do óbito?
**Gabarito:** `CAUSABAS`, codificada em CID-10.
**Fonte esperada:** Dicionário da DO.

### 12. Qual a diferença entre analisar óbitos por `CODMUNRES` e por `CODMUNOCOR`?
**Gabarito:** `CODMUNRES` = município de **residência** do falecido (usado em taxas de mortalidade da população); `CODMUNOCOR` = município de **ocorrência** do óbito (concentra-se em cidades com hospitais de referência).
**Fonte esperada:** Dicionário da DO.

### 13. No SINASC, em que variável está o peso ao nascer e em que unidade?
**Gabarito:** `PESO`, em **gramas**. (Baixo peso = menos de 2.500 g.)
**Fonte esperada:** Dicionário da DN.

### 14. Os arquivos do CNES são um histórico de eventos ou um retrato?
**Gabarito:** Um **retrato mensal** do cadastro (por UF e tipo: ST estabelecimentos, LT leitos, PF profissionais, EQ equipamentos etc.), disponível desde **agosto de 2005**. Para contar estabelecimentos escolha **uma** competência; somar meses multiplica a contagem.
**Fonte esperada:** Documentação do CNES.

### 15. Como ligo uma internação do SIH ao estabelecimento do CNES e ao município do IBGE?
**Gabarito:** Pelo **código CNES** do estabelecimento (campo `CNES` no RD ↔ `CNES` no ST) e pelo **código de município de 6 dígitos** do DATASUS (o IBGE usa 7; descarte o dígito verificador antes do join).
**Fonte esperada:** Dicionários do SIH e do CNES.

### 16. Como a LGPD classifica um dado referente à saúde de uma pessoa?
**Gabarito:** Como **dado pessoal sensível** (art. 5º, II), sujeito às hipóteses de tratamento do **art. 11**.
**Fonte esperada:** Lei 13.709/2018.

### 17. Dados anonimizados estão sujeitos à LGPD?
**Gabarito:** Em regra **não são considerados dados pessoais** (art. 12), **salvo** quando o processo de anonimização puder ser revertido com esforços razoáveis.
**Fonte esperada:** Lei 13.709/2018, art. 12.

### 18. O que a LGPD prevê para estudos em saúde pública feitos por órgãos de pesquisa?
**Gabarito:** O **art. 13** permite que órgãos de pesquisa acessem bases de dados pessoais para estudos em saúde pública, tratando-os **exclusivamente dentro do órgão**, em ambiente controlado e seguro, **preferencialmente anonimizados ou pseudonimizados**, e veda a divulgação que permita identificar o titular.
**Fonte esperada:** Lei 13.709/2018, art. 13.

### 19. Que norma instituiu a RNDS e qual padrão de troca de dados ela adota?
**Gabarito:** A **Portaria GM/MS nº 1.434/2020** (Programa Conecte SUS), que incluiu a RNDS na Portaria de Consolidação nº 1/2017. A RNDS adota o padrão **HL7 FHIR**, com terminologias como CID-10, LOINC e SIGTAP. (A Portaria 2.073/2011 já regulamentava padrões de interoperabilidade, como openEHR para o Registro Eletrônico em Saúde.)
**Fonte esperada:** Portaria 1.434/2020; página da RNDS; Portaria 2.073/2011.

### 20. (Controle) Quantas internações por pneumonia houve em Minas Gerais em 2024?
**Gabarito:** **A resposta não está nas fontes.** Os documentos descrevem as bases, não trazem os números. O comportamento correto é dizer que não sabe e indicar *como* obter (SIH-RD de MG, competências de 2024 e início de 2025, `DIAG_PRINC` J12–J18). Qualquer número citado é **alucinação**.
**Fonte esperada:** nenhuma — teste de honestidade da ferramenta.
