# 20 perguntas-teste — avaliação do notebook

**Objetivo:** medir se o notebook do NotebookLM responde com precisão e **cita a fonte certa** — e documentar onde ele erra.

**Protocolo**
1. Faça cada pergunta no NotebookLM exatamente como está escrita, em uma conversa nova.
2. Compare com o **gabarito** e abra a citação que a ferramenta indicou.
3. Classifique: ✅ correta e bem citada · ⚠️ correta mas incompleta ou com citação fraca · ❌ errada, inventada ou sem citação.
4. Anote a página/seção exata da fonte em **Conferido em** e o comportamento em `registro-de-erros.md`.

As perguntas cobrem cinco tipos de risco: **conceito** (o que é), **variável** (onde está), **armadilha** (o que engana), **norma** (o que a lei diz) e **controle** (pergunta cuja resposta *não* está nas fontes — a ferramenta deveria dizer que não sabe).

---

## Placar

| # | Tema | Tipo | Resultado | Conferido em (doc · pág./seção) |
|---|---|---|---|---|
| 1 | SIH | conceito | | |
| 2 | SIH | armadilha | | |
| 3 | SIH | variável | | |
| 4 | SIH | armadilha | | |
| 5 | SIH | variável | | |
| 6 | SIA | conceito | | |
| 7 | SIA | conceito | | |
| 8 | SIA | armadilha | | |
| 9 | SIM | conceito | | |
| 10 | SIM | armadilha | | |
| 11 | SIM | variável | | |
| 12 | SIM | armadilha | | |
| 13 | SINASC | variável | | |
| 14 | CNES | conceito | | |
| 15 | Ligação | variável | | |
| 16 | LGPD | norma | | |
| 17 | LGPD | norma | | |
| 18 | LGPD | norma | | |
| 19 | Interop. | norma | | |
| 20 | Controle | controle | | |
| | | **Total** | **__/20 ✅ · __ ⚠️ · __ ❌** | |

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
**Gabarito:** Autorização de Procedimentos Ambulatoriais — usada para procedimentos de **alta complexidade/custo**. Arquivos: AQ (quimioterapia), AR (radioterapia), AM (medicamentos), AN (nefrologia), ATD (tratamento dialítico), ACF (confecção de fístula), AD (laudos diversos), AB/ABO (cirurgia bariátrica e acompanhamento).
**Fonte esperada:** Informe técnico do SIA.

### 7. O arquivo PA do SIA permite contar quantas pessoas foram atendidas?
**Gabarito:** **Não.** O PA registra **produção aprovada** (quantidade de procedimentos por estabelecimento e competência), incluindo registros consolidados (BPA-C) sem identificação individual. Para registros individualizados há o BI (BPA-I) e as APACs, que cobrem só parte dos procedimentos.
**Fonte esperada:** Informe técnico do SIA.

### 8. Por que somar APACs de vários meses pode superestimar o número de pacientes em quimioterapia?
**Gabarito:** Porque a APAC de **continuidade** é reapresentada a cada competência enquanto o tratamento dura — a mesma pessoa aparece em vários meses.
**Fonte esperada:** Informe técnico do SIA / regras de APAC.

### 9. Qual é o documento-base do SIM e desde quando o sistema usa a CID-10?
**Gabarito:** A **Declaração de Óbito (DO)**. O SIM usa a **CID-10 desde 1996**; de 1979 a 1995 usava a CID-9 (pastas separadas no FTP).
**Fonte esperada:** Documentação do SIM.

### 10. Posso usar a variável `IDADE` do SIM diretamente como idade em anos?
**Gabarito:** **Não.** É um campo **composto**: o primeiro dígito indica a unidade (minutos, horas, dias, meses, anos) e os seguintes o valor. Ex.: códigos iniciados por 4 = anos; por 5 = 100 anos ou mais. É preciso decodificar antes de calcular.
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
