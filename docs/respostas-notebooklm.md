# Respostas brutas do NotebookLM

Transcrição integral das respostas obtidas no teste das 20 perguntas (13/11/2026), com instruções do notebook na versão 2 e apenas fontes primárias ativas (notas do projeto desmarcadas).

- Gabaritos e placar: [perguntas-teste.md](perguntas-teste.md)
- Erros e achados: [registro-de-erros.md](registro-de-erros.md)

Os números entre colchetes, como [1], são as citações exibidas pelo NotebookLM. Trechos foram mantidos como a ferramenta os apresentou, inclusive com erros, porque eles são a evidência da avaliação.

---

### 1. Qual arquivo do SIH/SUS contém as internações aprovadas e qual é sua periodicidade?

RESPOSTA:

O arquivo do SIH/SUS que contém as internações hospitalares aprovadas e processadas para disseminação é o RD (arquivo reduzido de AIH, com nomenclatura padrão RD*.dbf ou RDufaamm.dbf)[1]. A periodicidade de disponibilização desse arquivo é mensal[4].

Documentos e trechos de referência

1.  Documento: FIOCRUZ_SIH_documentacao_Santos.pdf

-   Trecho: *"Anexo V – Layout do arquivo reduzido – RD"*[1]

-   Trecho: *"arquivo reduzido (layout no anexo V) é formado pelos dados processados pelo SIHD-SUS para serem disseminados"*[2]

2.  Documento: SIH_informe_tecnico_2016-03.pdf

-   Trecho: "2 Layout dos arquivos RD.dbf"*[3]

3.  Documento: GitHub - rfsaldanha/microdatasus: Download de dados do DataSUS e pré-processamento no R. · GitHub

-   Trecho: Na tabela de sistemas suportados, o sistema SIH apresenta a Periodicidade dos arquivos especificada como Mensal[4].

### 2. Contar as linhas do arquivo RD dá o número de pacientes internados?

RESPOSTA:

Não, contar as linhas do arquivo RD não fornece o número de pacientes internados[1][2].

No SIH-SUS, cada linha do arquivo RD representa uma Autorização de Internação Hospitalar (AIH) — ou seja, um registro administrativo de cobrança e pagamento referente a uma internação autorizada ou seu desdobramento —, e não um indivíduo único[1].

Documento e trechos de referência

Documento: FIOCRUZ_SIH_documentacao_Santos.pdf

1.  Unidade de registro é a internação (evento), não o paciente:

-   Trecho: *"Uma característica da AIH é que ela não quantifica os pacientes internados e sim as internações cujo pagamento era efetuado pelo SIH-SUS"*[1].

2.  Reinternações, fracionamento de internações longas e transferências:

-   Trecho: *"A valorização do evento internação no lugar do indivíduo pode possibilitar a emissão de mais de uma AIH para o mesmo (...) permite que re-internações, fracionamento de internações longas e transferências sejam computadas como mais uma ocorrência dentro do que está sendo estudado."*[2].

3.  Tipos de registros no mesmo arquivo (AIH principal vs. continuação/longa permanência):

-   Trechos:

    -   *"AIH de identificação 1: são as AIH que foram permitidas pelo módulo autorizador do SIHD (...) Esta AIH contém todos os dados do paciente."*[3]

    -   *"AIH de identificação 3 conhecida como AIH de continuação. (...) Para cada AIH de identificação 1 que contém mais de 10 ocorrências de procedimentos especiais é gerada uma AIH de identificação 3, podendo neste caso existir várias AIH de continuação para uma AIH principal (tipo 1)."*[4]

    -   *"AIH de identificação 5: este tipo de AIH é utilizado para a internação de longa permanência de pacientes internados nas especialidades Psiquiatria, Pacientes sob Cuidados Prolongados e Internação Domiciliar."*[4]

4.  Registros referentes a mais de um indivíduo:

-   Trecho: *"na maioria das AIH de obstetrícia, esta responde por dois indivíduos (mãe e recém nascido), daí a complexidade em registrar o agravo do recém nascido, identificando a limitação do sistema para acompanhar este tipo de internação."*[5].

5.  Ausência de chave identificadora única obrigatória:

-   Trecho: *"não se pensou em possíveis integrações com outros sistemas (...) o que parcialmente justifica a não inclusão de uma chave identificadora entre eles. Hoje apesar da existência do Cartão Nacional de Saúde (CNS), este não é preenchido de forma obrigatória."*[6].

### 3. Qual a diferença entre `MUNIC_RES` e `MUNIC_MOV` no SIH?

RESPOSTA:

A diferença fundamental entre as duas variáveis no arquivo RD está na dimensão territorial registrada: MUNIC_RES indica o local de origem/moradia do paciente, enquanto MUNIC_MOV indica a localização do hospital onde a internação foi realizada[1][2].

Detalhamento das Variáveis no Arquivo RD

-   MUNIC_RES:

    -   Base de dados: RD[1][2]

    -   Nome exato da variável: MUNIC_RES[1][2]

    -   Unidade / Formato: Código IBGE de 6 dígitos em formato texto (char(6))[1][2]

    -   Documento e Trecho:

        -   FIOCRUZ_SIH_documentacao_Santos.pdf: *"Código do município de residência do paciente; veja a Descrição da tabela de Municípios"*[1].

        -   SIH_informe_tecnico_2016-03.pdf: *"Município de Residência do Paciente"*[2].

-   MUNIC_MOV:

    -   Base de dados: RD[1][2]

    -   Nome exato da variável: MUNIC_MOV[1][2]

    -   Unidade / Formato: Código IBGE de 6 dígitos em formato texto (char(6))[1][2]

    -   Documento e Trecho:

        -   FIOCRUZ_SIH_documentacao_Santos.pdf: *"Código do município onde se localiza o hospital; veja a Descrição da Tabela de Municípios"*[1].

        -   SIH_informe_tecnico_2016-03.pdf: *"Município do Estabelecimento."*[2].

### 4. Se eu filtrar o RD pelo mês de competência "janeiro", obtenho as internações que começaram em janeiro?

RESPOSTA:

Não, ao filtrar o arquivo RD pelo mês de competência "janeiro", você não obtém necessariamente apenas as internações que começaram em janeiro[1].

O mês de competência no arquivo RD refere-se ao mês em que a Autorização de Internação Hospitalar (AIH) foi processada e faturada pelo sistema, e não à data de entrada do paciente no hospital[2][4]. Com isso, internações iniciadas em meses anteriores podem ser apresentadas e processadas na competência de janeiro, assim como internações ocorridas em janeiro podem ser processadas em competências subsequentes[2]. Para analisar o mês exato de início da internação, deve-se utilizar a variável de data de internação presente no registro[3][4].

Documentos e trechos de referência

1.  FIOCRUZ_SIH_documentacao_Santos.pdf:

-   Trecho: Define a variável Competência como *"Representa a competência a qual a AIH será processada no formato Ano (AAAA) e Mês (MM)"*[2].

-   Trecho: Define a Data da internação como *"É a data de entrada no hospital para a internação no formato dia (DD), mês (MM) e ano (AAAA)"*[1].

-   Trecho: No layout do arquivo reduzido, detalha MÊS_CMPT como "Mês de competência da AIH, no formato mm" e DT_INTER como *"Data de internação (zerado nos arquivos de 1992) no formato aaammdd"*[5].

2.  SIH_informe_tecnico_2016-03.pdf:

-   Trecho: No layout dos arquivos RD*.dbf, descreve MÊS_CMPT como "Mês de processamento da AIH, no formato mm" e DI_INTER como *"Data de internação no formato aaammdd"*[4].

3.  GitHub - rfsaldanha/microdatasus: Download de dados do DataSUS e pré-processamento no R. · GitHub:

-   Trecho: Esclarece a distinção entre o mês do arquivo de disseminação e a data do evento: *"Os anos, meses e UFs solicitados identificam as partições publicadas pelo DataSUS. A data e o local analíticos devem ser escolhidos nas variáveis do registro"*[3].

### 5. Quais variáveis do RD trazem diagnóstico, procedimento, valor e óbito?

RESPOSTA:

As variáveis do arquivo RD que contêm informações de diagnóstico, procedimento, valor e óbito são as seguintes:

Diagnóstico

-   DIAG_PRINC

    -   Base de dados: RD

    -   Nome exato da variável: DIAG_PRINC

    -   Unidade / Formato: Código alfanumérico da CID-10 (char(4))

    -   Documento e Trecho: SIH_informe_tecnico_2016-03.pdf: *"Código do diagnóstico principal (CID10)"*[1]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Diagnóstico principal, segundo a CID-10"*[2].

-   DIAG_SECUN (e DIAGSEC1 a DIAGSEC9)

    -   Base de dados: RD

    -   Nome exato da variável: DIAG_SECUN (ou DIAGSEC1 a DIAGSEC9)

    -   Unidade / Formato: Código alfanumérico da CID-10 (char(4))

    -   Documento e Trecho: SIH_informe_tecnico_2016-03.pdf: *"Código do diagnostico secundário (CID10)"*[1]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Diagnóstico secundário, segundo a CID-10"*[2].

-   CID_ASSO

    -   Base de dados: RD

    -   Nome exato da variável: CID_ASSO

    -   Unidade / Formato: Código alfanumérico da CID-10 (char(4))

    -   Documento e Trecho: SIH_informe_tecnico_2016-03.pdf: *"CID causa"*[1]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"CID Associado"*[2].

Procedimento

-   PROC_SOLIC

    -   Base de dados: RD

    -   Nome exato da variável: PROC_SOLIC

    -   Unidade / Formato: Código numérico da Tabela de Procedimentos do SUS (char(10))

    -   Documento e Trecho: SIH_informe_tecnico_2016-03.pdf: *"Procedimento solicitado"*[1]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Procedimento Solicitado"*[2].

-   PROC_REA

    -   Base de dados: RD

    -   Nome exato da variável: PROC_REA

    -   Unidade / Formato: Código numérico da Tabela de Procedimentos do SUS (char(10))

    -   Documento e Trecho: SIH_informe_tecnico_2016-03.pdf: *"Procedimento realizado"*[1]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Procedimento realizado"*[2].

Valor

-   VAL_TOT

    -   Base de dados: RD

    -   Nome exato da variável: VAL_TOT

    -   Unidade / Formato: Moeda nacional / Reais (numeric(14,2) ou numeric(9,2))

    -   Documento e Trecho: SIH_informe_tecnico_2016-03.pdf: *"Valor total da AIH"*[1]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Valor total da AIH"*[2].

-   VAL_SH

    -   Base de dados: RD

    -   Nome exato da variável: VAL_SH

    -   Unidade / Formato: Moeda nacional / Reais (numeric(13,2) ou numeric(8,2))

    -   Documento e Trecho: SIH_informe_tecnico_2016-03.pdf: *"Valor de serviços hospitalares"*[1]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Valor de serviços hospitalares"*[2].

-   VAL_SP

    -   Base de dados: RD

    -   Nome exato da variável: VAL_SP

    -   Unidade / Formato: Moeda nacional / Reais (numeric(13,2) ou numeric(8,2))

    -   Documento e Trecho: SIH_informe_tecnico_2016-03.pdf: *"Valor de serviços profissionais"*[1]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Valor de serviços profissionais"*[2].

-   VAL_UTI

    -   Base de dados: RD

    -   Nome exato da variável: VAL_UTI

    -   Unidade / Formato: Moeda nacional / Reais (numeric(8,2))

    -   Documento e Trecho: SIH_informe_tecnico_2016-03.pdf: *"Valor de UTI"*[1]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Valor referente aos gastos em UTI"*[2].

-   US_TOT

    -   Base de dados: RD

    -   Nome exato da variável: US_TOT

    -   Unidade / Formato: Dólares americanos (numeric(10,2) ou numeric(8,2))

    -   Documento e Trecho: SIH_informe_tecnico_2016-03.pdf: *"Valor total, em dólar"*[1]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Valor total da AIH (VAL_TOT), converted para dólares"*[2].

Óbito

-   MORTE

    -   Base de dados: RD

    -   Nome exato da variável: MORTE

    -   Unidade / Formato: Código indicador (numeric(1) / 0 = Não, 1 = Sim)

    -   Documento e Trecho: SIH_informe_tecnico_2016-03.pdf: *"Indica Óbito"*[1]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Indica se o paciente teve saída com morte: 0: Não 1: Sim"*[2].

-   CID_MORTE

    -   Base de dados: RD

    -   Nome exato da variável: CID_MORTE

    -   Unidade / Formato: Código alfanumérico da CID-10 (char(4))

    -   Documento e Trecho: SIH_informe_tecnico_2016-03.pdf: *"CID da morte"*[1]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"CID Causa Morte"*[2].

-   COBRANCA

    -   Base de dados: RD

    -   Nome exato da variável: COBRANCA

    -   Unidade / Formato: Código numérico de motivo de saída/permanência (char(2), onde o código 4 indica saída por óbito)

    -   Documento e Trecho: SIH_informe_tecnico_2016-03.pdf: *"Motivo de Saída/Permanência"*[1]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Motivo da cobrança, conforme a Tabela de motivos de cobrança"*[2] e *"POR ÓBITO: 4"*[3].

### 6. O que é APAC e quais arquivos do SIA a utilizam?

RESPOSTA:

A APAC é a Autorização de Procedimentos Ambulatoriais de Alta Complexidade (ou Procedimento de Alta Complexidade)[1][2]. Trata-se do instrumento de registro do Sistema de Informações Ambulatoriais do SUS (SIA/SUS) utilizado para autorizar, regular e faturar atendimentos ambulatoriais de alta complexidade, procedimentos especiais e tratamentos continuados (como quimioterapia, radioterapia, hemodiálise e dispensação de medicamentos excepcionais)[2].

Arquivos do SIA que utilizam a APAC

No SIA/SUS, os dados derivados de APAC são disponibilizados em dois grupos principais de arquivos de disseminação:

1. Arquivo Geral de Produção Ambulatorial

-   PA (PAufaamm.dbf): É o arquivo consolidado de produção ambulatorial[2]. Ele contém os registros dos procedimentos gerados por APAC, identificados no campo PA_DOCORIG pelos códigos "P" (procedimento principal lançado por APAC) e "S" (procedimento secundário)[2][5].

2. Arquivos Específicos por Tipo de Laudo de APAC

Além do arquivo geral PA, o DATASUS disponibiliza arquivos individualizados conforme o tipo de laudo/atendimento de APAC[6][7]:

-   AD (ADufaamm.dbf): APAC de Laudos Diversos[6][7]

-   AM (AMufaamm.dbf): APAC de Medicamentos[6][7]

-   AN (ANufaamm.dbf): APAC de Nefrologia[6][7]

-   AQ (AQufaamm.dbf): APAC de Quimioterapia[6][7]

-   AR (ARufaamm.dbf): APAC de Radioterapia[6][7]

-   AB (ABufaamm.dbf): APAC de Acompanhamento à Cirurgia Bariátrica[6][7]

-   ACF (ACFufaamm.dbf): APAC de Confecção de Fístula Arteriovenosa[6][7]

-   ATD (ATDufaamm.dbf): APAC de Tratamento Dialítico[6][7]

-   AMP (AMPufaamm.dbf): APAC de Acompanhamento Multiprofissional

### 7. O arquivo PA do SIA permite contar quantas pessoas foram atendidas?

RESPOSTA:

Não, o arquivo PA do SIA não permite contar diretamente quantas pessoas (indivíduos únicos) foram atendidas[1][2].

Motivos indicados na documentação

1.  Mistura de instrumentos consolidados e individualizados: O arquivo PA reúne registros de produção ambulatorial gerados por diferentes instrumentos de informação (identificados pelo campo PA_DOCORIG)[1][3]:

-   Boletim de Produção Ambulatorial Consolidado (BPA-C): A produção é registrada de forma agregada/consolidada por par de procedimento e CBO, não havendo qualquer identificação individual do paciente[1][2].

-   Boletim de Produção Ambulatorial Individualizado (BPA-I): Cada registro refere-se a um atendimento, sendo possível existir mais de um atendimento gravado para o mesmo paciente[1][2].

-   Autorização de Procedimentos Ambulatoriais de Alta Complexidade (APAC): Uma única APAC gera múltiplos registros no arquivo PA — um para cada procedimento realizado (seja ele o procedimento principal ou secundário)[1][2].

2.  Diferença entre procedimento, atendimento e indivíduo: A contagem de linhas do arquivo PA contabiliza procedimentos/atendimentos registrados, e não pessoas[2]. Um único indivíduo pode gerar dezenas de linhas no arquivo PA ao realizar procedimentos secundários ou múltiplos atendimentos no mês[2].

Documento e trechos de referência

Documento: SIA_informe_tecnico_2019-07.pdf

-   Trecho: *"Dentro do arquivo PAufaamm.dbf constam dados dos procedimentos ambulatoriais obtidos através dos seguintes instrumentos de registro do SIASUS: • APAC: Autorização de Procedimentos Ambulatoriais de Alta Complexidade • BPA-C: Boletim de Produção Ambulatorial Consolidado • BPA-I: Boletim de Produção Ambulatorial Individualizado • RAAS-AD: Registro das Ações Ambulatoriais de Saúde - Atenção Domiciliar • RAAS-PSI: Registro das Ações Ambulatoriais de Saúde - Atenção Psicossocial"*[1].

-   Trecho: *"O preenchimento dos campos de cada registro do arquivo PA varia conforme o tipo de instrumento que o originou, o que é identificado pelo conteúdo do campo PA_DOCORIG."*[3].

-   Trecho: *"A quantidade de registros (linhas) varia conforme o tipo de instrumento. A saber: 1. Um instrumento BPA-C gera diversos registros no arquivo PA: um para cada par [código de procedimento, CBO], correspondendo à respectiva linha no instrumento original em papel; 2. Um instrumento BPA-I gera diversos registros no arquivo de PA: um para cada atendimento. Há casos de registros de um ou mais atendimentos no BPA-I para o mesmo paciente... 3. Um instrumento APAC gera diversos registros no arquivo PA: um para cada código de procedimento realizado na APAC, seja ele procedimento principal (P) ou secundário (S)."*[2].

### 8. Por que somar APACs de vários meses pode superestimar o número de pacientes em quimioterapia?

RESPOSTA:

Somar a quantidade de Autorizações de Procedimentos Ambulatoriais de Alta Complexidade (APAC) de quimioterapia ao longo de vários meses superestima o número de pacientes em tratamento por dois motivos estruturais da base de dados do SIA/SUS:

1.  Tratamento continuado e registros mensais por competência (APAC de Continuidade): A quimioterapia é um tratamento de caráter continuado[1]. O laudo da APAC é autorizado com um horizonte de validade de múltiplos meses, prevendo o número total de meses planejados e autorizados[1]. No entanto, a disseminação dos dados no SIA/SUS ocorre por competência mensal de faturamento/atendimento[1][2]. A cada mês em que o paciente realiza sessões, gera-se um registro na competência correspondente — categorizado como APAC inicial ou APAC de continuidade[1]. Assim, um mesmo indivíduo em tratamento durante 6 meses terá registros emitidos em 6 meses consecutivos; somar as APACs desses meses contabilizará o mesmo paciente 6 vezes[1][2].

2.  Múltiplos registros por autorização no arquivo PA: Quando a análise é realizada no arquivo geral de produção ambulatorial PA, uma única APAC gera diversas linhas de registro na mesma competência: uma para o procedimento principal e uma para cada procedimento secundário associado ao atendimento[3].

Documentos e trechos de referência

-   Documento: SIA_informe_tecnico_2019-07.pdf

    -   Trecho (Item 2.1 - Arquivo PA): *"Um instrumento APAC gera diversos registros no arquivo PA: um para cada código de procedimento realizado na APAC, seja ele procedimento principal (P) ou secundário (S)."*[3]

    -   Trecho (Item 3.1 - Arquivos de APAC): *"As informações contidas nestes arquivos referem-se aos Atendimentos Ambulatoriais realizados em pacientes submetidos à APAC, nas respectivas competências (ano e mês)..."*[2]

    -   Trecho (Item 3.4.4 - Layout do arquivo de APAC de Quimioterapia): O layout estabelece os campos de competência (AP_CMP), tipo de APAC (AP_TPAPAC: 1 - inicial, 2 - continuidade, 3 - única), indicação de continuidade do tratamento (AQ_CONTTR: S = Sim; N = Não), total de meses planejados (AQ_TOTMPL) e total de meses autorizados (AQ_TOTMAU)[1].

### 9. Qual é o documento-base do SIM e desde quando o sistema usa a CID-10?

RESPOSTA:

O documento-base do SIM é a **Declaração de Óbito (DO)**[1][2].

1. Documento-base do SIM

-   Documento: FIOCRUZ_SIH_documentacao_Santos.pdf

    -   Trecho: *"SIM | Sistema de Informações sobre Mortalidade | 1975 | Declaração de óbito"*[1]

    -   Trecho: *"Os dados são extraídos da Declaração de Óbitos (DO) e suas informações compõem as estatísticas vitais"*[3]

-   Documento: SIM_legislacao.pdf

    -   Trecho: *"Considerando que a Declaração de Óbito (DO) é o documento oficial que atesta a morte de um indivíduo, e que o Sistema de Informação sobre Mortalidade (SIM) é o instrumento oficial do Ministério da Saúde para a informação da DO em todo o território nacional..."*[2]

    -   Trecho: *"Deve ser utilizado o formulário da Declaração de Óbito (DO) (...) como documento padrão de uso obrigatório em todo o território nacional, para a coleta dos dados sobre óbitos..."*[4]

2. Ano de adoção da CID-10 no SIM

A informação sobre o ano exato a partir do qual o SIM passou a utilizar a CID-10 não está presente nas fontes fornecidas.

As fontes mostram que o SIM utiliza a CID-10 em suas tabelas de campos e na legislação de vigilância de óbitos[5][6], e indicam que a transição da CID-9 para a CID-10 no SIH ocorreu a partir de 1998[7], mas não especificam a data de início da CID-10 para o SIM.

-   Onde procurar: Sugiro consultar os manuais e notas de documentação histórica do SIM na página de disseminação do DATASUS ou as publicações do Centro Brasileiro de Classificação de Doenças (CBCD).

### 10. Posso usar a variável `IDADE` do SIM diretamente como idade em anos?

RESPOSTA:

Não, você não pode usar a variável IDADE do arquivo DO (Declaração de Óbito) diretamente como idade em anos[1].

Motivo e Estrutura do Campo

No arquivo DO, o campo IDADE é uma variável de 3 caracteres composta por dois subcampos: o primeiro dígito indica a unidade de medida de tempo e os dois últimos dígitos indicam a quantidade nessa unidade[1].

-   **Primeiro dígito (Unidade de medida)**[1]:

    -   1: minutos

    -   2: horas

    -   3: meses (ou dias, conforme o subcampo)

    -   4: anos (para idades entre 00 e 99 anos)

    -   5: idade maior que 100 anos

    -   9: ignorado

-   **Dois últimos dígitos (Quantidade)**[1]:

    -   01 a 59: minutos (quando o 1º dígito é 1)

    -   01 a 23: horas (quando o 1º dígito é 2)

    -   01 a 29: dias (quando o 1º dígito é 3)

    -   01 a 11: meses completos (quando o 1º dígito é 3)

    -   00 a 99: anos (quando o 1º dígito é 4)

Por esse motivo, um valor 415 significa 15 anos (unidade 4 + quantidade 15), enquanto 205 significa 5 horas e 502 representa 102 anos (unidade 5 + 02)[1]. Tratar esse campo diretamente como um valor numérico contínuo distorcerá qualquer análise[1].

Documento e Trecho de Referência

-   Documento: SIM_estrutura_DO_2025.pdf[1]

-   Trecho:

> "Idade: composto de dois subcampos. - O primeiro, de 1 dígito, indica a unidade da idade (se 1 = minuto, se 2 = hora, se 3 = mês, se 4 = ano, se = 5 idade maior que 100 anos). - O segundo, de dois dígitos, indica a quantidade de unidades: Idade menor de 1 hora: subcampo varia de 01 e 59 (minutos); De 1 a 23 Horas: subcampo varia de 01 a 23 (horas); De 24 horas e 29 dias: subcampo varia de 01 a 29 (dias); De 1 a menos de 12 meses completos: subcampo varia de 01 a 11 (meses); Anos - subcampo varia de 00 a 99; - 9 - ignorado"

### 11. Qual variável do SIM traz a causa básica do óbito?

RESPOSTA:

A variável do SIM (no arquivo da Declaração de Óbito — DO) que contém a causa básica do óbito é a CAUSABAS[1].

Informações da Variável

-   Base de dados: DO[1]

-   Nome exato da variável: CAUSABAS[1]

-   Unidade / Formato: Código alfanumérico da CID-10 de 4 caracteres (char(4))[1]

Documento e Trecho de Referência

-   Documento: SIM_estrutura_DO_2025.pdf[1]

-   Trecho:

> *"Causa básica da Morte | CAUSABAS | Caracter | 4 | ;letras; números; | Causa básica da DO"

### 12. Qual a diferença entre analisar óbitos por `CODMUNRES` e por `CODMUNOCOR`?

RESPOSTA:

diferença entre analisar óbitos por CODMUNRES e por CODMUNOCOR no arquivo DO (Declaração de Óbito) do SIM refere-se à dimensão territorial considerada para o evento de mortalidade[1][2]:

-   Análise por CODMUNRES (Município de Residência): Considera o local de moradia do falecido (ou da mãe, em casos de óbito fetal)[2]. É a abordagem principal para o planejamento em saúde pública e para o cálculo de indicadores epidemiológicos populacionais, pois retrata o impacto da mortalidade na população residente[3].

-   Análise por CODMUNOCOR (Município de Ocorrência): Considera o local onde o falecimento efetivamente ocorreu[2][3]. Essa métrica é fortemente influenciada pela presença de estabelecimentos de saúde, hospitais de referência, vias de trânsito ou locais de ocorrência de acidentes e violências[2][3].

A legislação estabelece que o registro do óbito seja realizado no local do falecimento (CODMUNOCOR), porém o maior interesse epidemiológico para a gestão em saúde é a análise distribuída por residência (CODMUNRES)[3]. A comparação entre as duas variáveis permite mapear o fluxo de pacientes que se deslocam entre municípios para obter assistência[3].

Documentos e trechos de referência

1.  SIM_estrutura_DO_2025.pdf:

-   Trecho ( CODMUNRES ): *"Código do município de residência. Em caso de óbito fetal, considerar o município de residência da mãe"*[2].

-   Trecho ( CODMUNOCOR ): *"Código relativo ao município onde ocorreu o óbito"*[2].

2.  SIM_introducao.pdf:

-   Trecho: *"Determina, igualmente, a legislação, que o registro do óbito seja sempre feito 'no lugar do falecimento', isto é, no local da ocorrência do evento. Sabe-se, entretanto, que o dado que mais interessa ao campo da saúde é o dos óbitos distribuídos segundo o local de residência."*[3].

3.  GitHub - rfsaldanha/microdatasus: Download de dados do DataSUS e pré-processamento no R. · GitHub:

-   Trecho: *"distingue residência, ocorrência e outras dimensões territoriais e temporais do óbito."*[1].

### 13. No SINASC, em que variável está o peso ao nascer e em que unidade?

RESPOSTA:

No SINASC (arquivos da base DN), o peso ao nascer é registrado na seguinte variável:

-   Base de dados: DN[1]

-   Nome exato da variável: PESO[1]

-   Unidade / Formato: Gramas (g)[1]

Documento e Trecho de Referência

-   Documento: SINASC_dicionario_arquivos_DBC.pdf[1]

-   Trecho: Na tabela da seção "I - Identificação do Recém Nascido", o dicionário define o item "Peso ao nascer" informando o "Nome do campo no DBF: PESO" e a descrição *"Peso em gramas verificado até a 5ª hora após o nascimento"*[1].

### 14. Os arquivos do CNES são um histórico de eventos ou um retrato?

RESPOSTA:

Os arquivos do CNES representam um retrato (posição ou fotografia cadastral da capacidade instalada, recursos humanos e infraestrutura em cada competência mensal) e não um histórico de eventos assistenciais[1].

Documentos e trechos de referência

1.  CNES_informe_tecnico_2017-06.pdf:

-   Trecho: *"As informações nestes arquivos referem-se aos dados cadastrais dos Estabelecimentos de Saúde cadastrados no Sistema de Cadastro Nacional de Estabelecimentos do SUS."*[1]

-   Trecho: Define a estrutura dos arquivos mensais de posição por dimensão cadastral (como o ST para estabelecimentos, PF para profissionais, LT para leitos e EQ para equipamentos), cuja nomenclatura STufaamm.dbf reflete a Unidade da Federação, ano e mês da competência[2][4].

2.  FIOCRUZ_SIH_documentacao_Santos.pdf:

-   Trecho: *"Este sistema de cadastro abrangia os aspectos de área física, recursos humanos, equipamentos, serviços de apoio diagnóstico e terapêutico, e serviços ambulatoriais e hospitalares das unidades de saúde."*[3]

Diferentemente de sistemas de produção assistencial como o SIH (arquivo RD) ou o SIA (arquivo PA), que acumulam registros de eventos de atendimento e faturamento, os arquivos do CNES (como o ST) registram a fotografia da estrutura e dos vínculos declarados para aquele mês específico[1].

### 15. Como ligo uma internação do SIH ao estabelecimento do CNES e ao município do IBGE?

RESPOSTA:

Para ligar um registro de internação do SIH (arquivo RD) ao cadastro do estabelecimento no CNES (arquivo ST) e às tabelas de municípios do IBGE, utiliza-se o código identificador do estabelecimento (CNES) e os códigos de município do IBGE (MUNIC_RES ou MUNIC_MOV)[1].

1. Ligação entre SIH (arquivo RD) e CNES (arquivo ST)

A conexão entre o registro da internação e o cadastro do hospital é feita por meio de um relacionamento (join) direto entre os campos de código do CNES[1].

-   Código do CNES no SIH:

    -   Base de dados: RD

    -   Nome exato da variável: CNES

    -   Unidade / Formato: Código alfanumérico/texto de 7 dígitos (char(7))

    -   Documento e trecho: SIH_informe_tecnico_2016-03.pdf: *"Código CNES do hospital."*[3]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Código do CNES do estabelecimento"*[2].

-   Código do CNES no CNES:

    -   Base de dados: ST

    -   Nome exato da variável: CNES

    -   Unidade / Formato: Código alfanumérico/texto de 7 dígitos (char(7))

    -   Documento e trecho: CNES_informe_tecnico_2017-06.pdf: *"Número nacional do estabelecimento de saúde"*[1].

2. Ligação entre SIH (arquivo RD) e o Município do IBGE

No arquivo RD, a ligação com a tabela de municípios do IBGE depende da dimensão geográfica que se deseja analisar[2][3]:

A. Município de Residência do Paciente

-   Base de dados: RD

-   Nome exato da variável: MUNIC_RES

-   Unidade / Formato: Código IBGE de 6 dígitos em formato texto (char(6))

-   Documento e trecho: SIH_informe_tecnico_2016-03.pdf: *"Município de Residência do Paciente"*[3]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Código do município de residência do paciente; veja a Descrição da tabela de Municípios"*[2].

B. Município de Localização do Hospital (Ocorrência)

-   Base de dados: RD

-   Nome exato da variável: MUNIC_MOV

-   Unidade / Formato: Código IBGE de 6 dígitos em formato texto (char(6))

-   Documento e trecho: SIH_informe_tecnico_2016-03.pdf: *"Município do Estabelecimento."*[3]; FIOCRUZ_SIH_documentacao_Santos.pdf: *"Código do município onde se localiza o hospital; veja a Descrição da Tabela de Municípios"*[2].

-   Município no cadastro do CNES (arquivo ST):

    -   Base de dados: ST

    -   Nome exato da variável: CODUFMUN

    -   Unidade / Formato: Código IBGE em formato texto de 6 ou 7 dígitos (char(6) ou char(7))

    -   Documento e trecho: CNES_informe_tecnico_2017-06.pdf: *"Código do município do estabelecimento: UF + MUNIC (sem dígito)"*[1].

### 16. Como a LGPD classifica um dado referente à saúde de uma pessoa?

RESPOSTA:

A Lei Geral de Proteção de Dados Pessoais (LGPD) classifica o dado referente à saúde de uma pessoa natural como dado pessoal sensível[1][2].

Documentos e trechos de referência

1.  Documento: LGPD_Lei_13709_2018_compilada.pdf

-   Trecho: No Art. 5º, inciso II, a lei estabelece que é *"dado pessoal sensível: dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural"*[1].

2.  Documento: LGPD_boas_praticas_MCTI.pdf

-   Trecho: A cartilha inclui a "Informação médica" entre os exemplos de dados sujeitos a regras específicas de proteção e privacidade[2].

### 17. Dados anonimizados estão sujeitos à LGPD?

RESPOSTA:

Em regra, não. De acordo com a Lei Geral de Proteção de Dados Pessoais (LGPD), os dados anonimizados não são considerados dados pessoais para os fins da lei[1].

No entanto, a própria lei estabelece exceções em que o dado anonimizado volta a se sujeitar à LGPD:

1.  Reversão da anonimização: Quando o processo de anonimização for revertido (utilizando exclusivamente meios próprios) ou quando puder ser refratado/revertido com esforços razoáveis[1]. Para avaliar o que é "razoável", consideram-se fatores objetivos como custo, tempo necessário e tecnologias disponíveis[2].

2.  Formação de perfil comportamental: Quando os dados forem utilizados para a formação do perfil comportamental de determinada pessoa natural, caso ela seja identificada[2].

Documento e Trechos de Referência

-   Documento: LGPD_Lei_13709_2018_compilada.pdf

-   Trecho (Art. 12, caput ):

> *"Os dados anonimizados não serão considerados dados pessoais para os fins desta Lei, salvo quando o processo de anonimização ao qual foram submetidos for revertido, utilizando exclusivamente meios próprios, ou quando, com esforços razoáveis, puder ser revertido."*[1]

-   Trecho (Art. 12, § 1º):

> *"A determinação do que seja razoável deve levar em consideração fatores objetivos, tais como custo e tempo necessários para reverter o processo de anonimização, de acordo com as tecnologias disponíveis, e a utilização exclusiva de meios próprios."*[2]

-   Trecho (Art. 12, § 2º):

> *"Poderão ser igualmente considerados como dados pessoais, para os fins desta Lei, aqueles utilizados para formação do perfil comportamental de determinada pessoa natural, se identificada."*[2]

-   Trecho (Art. 5º, inciso III):

> "dado anonimizado: dado relativo a titular que não possa ser identificado, considerando a utilização de meios técnicos razoáveis e disponíveis na ocasião de seu tratamento;"

### 18. O que a LGPD prevê para estudos em saúde pública feitos por órgãos de pesquisa?

RESPOSTA:

A Lei Geral de Proteção de Dados Pessoais (LGPD) estabelece regras específicas para o acesso, tratamento, segurança e conservação de dados pessoais em estudos de saúde pública realizados por órgãos de pesquisa.

1. Acesso a Bases de Dados e Finalidade Exclusiva

A LGPD autoriza expressamente o acesso dos órgãos de pesquisa a bases de dados pessoais para estudos em saúde pública, condicionando o tratamento à manutenção de ambiente seguro e à observância de padrões éticos[1].

-   Documento: LGPD_Lei_13709_2018_compilada.pdf

-   Trecho: *"Na realização de estudos em saúde pública, os órgãos de pesquisa poderão ter acesso a bases de dados pessoais, que serão tratados exclusivamente dentro do órgão e estritamente para a finalidade de realização de estudos e pesquisas e mantidos em ambiente controlled e seguro, conforme práticas de segurança previstas em regulamento específico e que incluam, sempre que possível, a anonimização ou pseudonimização dos dados, bem como considerem os devidos padrões éticos relacionados a estudos e pesquisas."*[1]

2. Hipótese de Dispensa de Consentimento (Dados Pessoais e Sensíveis)

A realização de pesquisas por órgãos de pesquisa constitui hipótese legal de tratamento de dados sem a necessidade de consentimento do titular, tanto para dados pessoais gerais quanto para dados pessoais sensíveis (como os dados de saúde)[2][3].

-   Documento: LGPD_Lei_13709_2018_compilada.pdf

-   Trecho (Art. 7º, IV - Dados Pessoais): *"para a realização de estudos por órgão de pesquisa, garantida, sempre que possível, a anonimização dos dados pessoais;"*[2]

-   Trecho (Art. 11, II, c - Dados Pessoais Sensíveis): *"realização de estudos por órgão de pesquisa, garantida, sempre que possível, a anonimização dos dados pessoais sensíveis;"*[3]

3. Proibição de Divulgação de Dados Pessoais e de Transferência a Terceiros

A lei veda rigorosamente a revelação de dados identificáveis na publicação dos resultados e proíbe a transferência das bases de dados a terceiros[4].

-   Documento: LGPD_Lei_13709_2018_compilada.pdf

-   Trecho (Art. 13, § 1º): *"A divulgação dos resultados ou de qualquer excerto do estudo ou da pesquisa de que trata o caput deste artigo em nenhuma hipótese poderá revelar dados pessoais."*[4]

-   Trecho (Art. 13, § 2º): *"O órgão de pesquisa será o responsável pela segurança da informação prevista no caput deste artigo, não permitida, em circunstância alguma, a transferência dos dados a terceiro."*[4]

4. Regulamentação do Acesso e Conceito de Pseudonimização

A LGPD define a pseudonimização como técnica de proteção em ambiente controlado e prevê regulamentação conjunta pelas autoridades sanitárias e de proteção de dados[4].

-   Documento: LGPD_Lei_13709_2018_compilada.pdf

-   Trecho (Art. 13, § 3º): *"O acesso aos dados de que trata este artigo será objeto de regulamentação por parte da autoridade nacional e das autoridades da área de saúde e sanitárias, no âmbito de suas competências."*[4]

-   Trecho (Art. 13, § 4º): *"Para os efeitos deste artigo, a pseudonimização é o tratamento por meio do qual um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente controlado e seguro."*[4]

5. Conservação dos Dados Após o Término do Tratamento

Ao final da pesquisa, os dados pessoais podem ser conservados pelo órgão de pesquisa[5].

-   Documento: LGPD_Lei_13709_2018_compilada.pdf

-   Trecho (Art. 16, II): *"estudo por órgão de pesquisa, garantida, sempre que possível, a anonimização dos dados pessoais;"*[5]

6. Definição Legal de "Órgão de Pesquisa"

Para fazer uso dessas prerrogativas, a entidade precisa se enquadrar na definição legal estabelecida pela LGPD[6].

-   Documento: LGPD_Lei_13709_2018_compilada.pdf

-   Trecho (Art. 5º, XVIII): "órgão de pesquisa: órgão ou entidade da administração pública direta ou indireta ou pessoa jurídica de direito privado sem fins lucrativos legalmente constituída sob as leis brasileiras, com sede e foro no País, que inclua em sua missão institucional ou em seu objetivo social ou estatutário a pesquisa básica ou applied de caráter histórico, científico, tecnológico ou estatístico;"⁶

### 19. Que norma instituiu a RNDS e qual padrão de troca de dados ela adota?

RESPOSTA:

A Rede Nacional de Dados em Saúde (RNDS) foi instituída pela Portaria MS/GM nº 1.434, de 28 de maio de 2020 (que alterou a Portaria de Consolidação nº 1/GM/MS, de 28 de setembro de 2017)[1][2].

O padrão de troca de dados adotado pela RNDS é o HL7 FHIR (Fast Healthcare Interoperability Resources, desenvolvido pela organização Health Level 7)[3].

Documentos e trechos de referência

1.  PORTARIA_1434_2020_ConecteSUS_RNDS.pdf:

-   Trecho (Ementa da Portaria nº 1.434/2020): *"Institui o Programa Conecte SUS e altera a Portaria de Consolidação nº 1/GM/MS, de 28 de setembro de 2017, para instituir a Rede Nacional de Dados em Saúde e dispor sobre a adoção de padrões de interoperabilidade em saúde."*[1]

-   Trecho (Art. 254-A): *"Fica instituída a Rede Nacional de Dados em Saúde - RNDS, componente do Sistema Nacional de Informações em Saúde - SNIS, de que trata o art. 47 da Lei nº 8.080, de 19 de setembro de 1990..."*[4]

2.  Estrutura do Projeto — Ministério da Saúde:

-   Trecho (Interoperabilidade e Padrão FHIR): "A modelagem dos dados na RNDS segue o padrão Fast Healthcare Interoperability Resources, da organização Health Level 7 (HL7 FHIR), um “tradutor digital” que faz a troca de informações entre diferentes sistemas de saúde de forma padronizada e com transmissão de dados em tempo real."³

### 20. (Controle) Quantas internações por pneumonia houve em Minas Gerais em 2024?

RESPOSTA:

A informação com o número exato de internações por pneumonia em Minas Gerais no ano de 2024 não está presente nas fontes fornecidas.

Onde procurar

Para obter esse dado estatístico, você pode consultar:

1.  TABNET / DATASUS: Acesse o sistema TABNET na opção de Morbidade Hospitalar do SUS (SIH/SUS), selecione a abrangência geográfica de Minas Gerais, o período de 2024 e filtre pelo grupo de causa/diagnóstico da CID-10 relativo a Pneumonia nos dados do arquivo RD.

2.  Microdados do DATASUS: Faça o download dos arquivos mensais do tipo RD referentes a Minas Gerais no ano de 2024 (arquivos no padrão RDMG24*.dbc) para realizar a contagem e filtragem direta dos registros.
