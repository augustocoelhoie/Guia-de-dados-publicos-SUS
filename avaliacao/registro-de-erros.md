# Registro de erros e limitações da ferramenta

> Esta é a parte que diferencia o projeto: **onde o NotebookLM errou e por quê**.
> Preencha durante o teste das 20 perguntas e ao gerar o resumo em áudio.

## Como classificar a causa do erro

| Código | Causa | Exemplo típico |
|---|---|---|
| **F1** | Fonte ausente | A informação não estava em nenhum documento carregado |
| **F2** | Fonte desatualizada | O PDF descreve um layout antigo do arquivo |
| **F3** | Fonte com erro | A documentação oficial diverge do que está nos microdados (ex.: grafia de variável) |
| **R1** | Recuperação falhou | A resposta estava na fonte, mas o trecho não foi encontrado (tabelas em PDF escaneado, por ex.) |
| **R2** | Mistura de fontes | Combinou regras de dois sistemas diferentes (SIH × SIA) |
| **G1** | Alucinação | Afirmou algo que não está em nenhuma fonte (número, artigo de lei, variável inexistente) |
| **G2** | Generalização indevida | Transformou uma regra específica em regra geral |
| **C1** | Citação errada | Resposta certa, mas apontou o documento/trecho errado |
| **C2** | Citação alterada | Trecho apresentado como literal, mas com palavras trocadas em relação à fonte |
| **C3** | Afirmação sem citação | Item da resposta sem nenhuma fonte indicada |

## Registro

| # pergunta | O que a ferramenta respondeu (resumo) | Código | Por que errou | Correção aplicada |
|---|---|---|---|---|
| 1 (1ª rodada) | Correta: arquivo RD, mensal, por competência. Citou primeiro a nota "Catálogo – resumo" (conteúdo do próprio projeto). Chamou o arquivo de "SIH-RD" (nome do microdatasus). Listou variáveis sem que a pergunta pedisse. | C1 · R2 | Notas do projeto entravam como evidência; a instrução v1 pedia detalhar variáveis sempre; nomenclatura do microdatasus misturada à do DATASUS. | Notas desativadas; instruções trocadas pela v2; pergunta refeita. |
| 1 (refeita) | Correta, citando só Fiocruz e informe técnico. A periodicidade "mensal" foi sustentada apenas pelo README do microdatasus. | — | Os documentos primários carregados não afirmam a periodicidade de forma explícita; ela fica implícita no padrão de nome RDUFAAMM. | Mantido ✅; registrado como limitação das fontes. |
| 1 e 4 | Reproduziu `MÊS_CMPT`, com acento, como está no informe técnico do SIH e na dissertação da Fiocruz. | F3 | A documentação oficial grafa `MÊS_CMPT`; nos arquivos .dbc a coluna é `MES_CMPT` (conferido com `scripts/conferir_variaveis.py`). | Grafia correta registrada no catálogo e nas lições de curadoria. |
| 4 | No trecho do informe técnico, escreveu `DI_INTER` para a data de internação. | F3 | O informe técnico do SIH (2016) grafa `DI_INTER`; nos arquivos .dbc a coluna é `DT_INTER` (conferido com `scripts/conferir_variaveis.py`). A ferramenta reproduziu fielmente o erro da fonte. | Grafia correta (`DT_INTER`) mantida no catálogo e no gabarito. |
| 5 | Listou variáveis corretas e várias extras. Para `COBRANCA`, disse que "o código 4 indica saída por óbito" e que o campo tem 2 caracteres. Trecho da Fiocruz citado com a palavra inglesa "converted". | F2 · C2 | Na tabela atual de motivos de saída/permanência os óbitos têm códigos de 2 dígitos (41, 42, 43); o "4" vem de um agrupamento da fonte antiga. A palavra "converted" não está no original. | Registrado: para identificar óbito no RD, use `MORTE`; `COBRANCA` exige a tabela de motivos da competência. |
| 6 | Listou corretamente os arquivos de APAC e acrescentou o PA (registros P/S via `PA_DOCORIG`). Incluiu "AMP – APAC de Acompanhamento Multiprofissional" sem citação. | C3 | Item sem trecho de fonte; possivelmente veio do conhecimento prévio do modelo ou da lista do microdatasus. | Gabarito complementado com o PA. AMP mantido fora do gabarito por não ter fonte primária. |
| 9 | Acertou a DO como documento-base. Disse que o ano de adoção da CID-10 no SIM **não está nas fontes** e sugeriu onde procurar. | F1 | O ano de 1996 do gabarito não aparece em nenhum documento carregado. Comportamento correto da ferramenta. | Gabarito corrigido: a evidência do ano é a estrutura de pastas do FTP (`SIM/CID9` × `SIM/CID10`). |
| 10 | Explicou corretamente que `IDADE` é composta. Na lista de unidades, escreveu "3: meses (ou dias, conforme o subcampo)" e atribuiu "dias" ao código 3. | G2 · F3 | A estrutura da DO 2025 não diz qual código indica dias; a ferramenta preencheu a lacuna. O microdatasus decodifica 0 = minutos, 1 = horas, 2 = dias, 3 = meses, divergindo do PDF (1 = minuto, 2 = hora, 3 = mês). | Gabarito corrigido com a divergência e a recomendação de conferir nos dados. |
| 14 | Concluiu corretamente que o CNES é um retrato mensal, mas o trecho citado só diz que são "dados cadastrais". Não mencionou o início em 08/2005. | C1 | A conclusão "retrato" é inferida da nomenclatura mensal, não declarada na fonte. O ano de início não está no informe; vem do nome da pasta `200508_` no FTP. | Mantido o gabarito; registrado que a evidência de 2005 é a estrutura do FTP. |
| 18 | Resposta completa e correta (arts. 5º XVIII, 7º IV, 11 II c, 13 e 16 II). Nos trechos apresentados como literais, trocou "controlado" por "controlled" e "aplicada" por "applied". | C2 | A ferramenta alterou citações literais, inserindo palavras em inglês. O conteúdo jurídico está certo, mas a citação não pode ser copiada como texto da lei. | Registrado; padrão repetido na pergunta 5 ("converted"). |

## Resumo em áudio (Audio Overview)

Áudio no formato **Análise detalhada**, ~22 min, gerado em 13/11/2026. Minutos aproximados, estimados pela posição na [transcrição](transcricao-audio.md). Erros da transcrição automática ("Sinasque", "CIA", "SH", "Fire") não foram contados como erros da ferramenta.

Legenda: ✅ confere · ⚠️ impreciso ou sem fonte · ❌ errado · 🔎 duvidoso, conferir na fonte

| Minuto | Afirmação no áudio | Correta? | Comentário |
|---|---|---|---|
| ~00:00 | Somar dados sem conhecer as regras pode levar a "R$ 1 bilhão em uma semana" | ⚠️ | Exagero de efeito para abrir o episódio; nenhuma fonte traz esse número (G1 leve). |
| ~02:20 | Apresenta o CNES como "o famoso CNES" | ✅ | A transcrição automática registrou "CNS", mas no áudio a sigla está correta (conferido ouvindo). Erro de transcrição, não da ferramenta. |
| ~03:10 | O CNES tem arquivos ST (estabelecimento), PF (profissionais) e LT (leitos) | ✅ | Confere com o catálogo e o informe do CNES. |
| ~03:59 | O CNES é obrigatório para todos os estabelecimentos, inclusive os estritamente privados | ⚠️ | Correto (conferido em fonte externa), mas a informação não está no informe do CNES nem na Fiocruz: a ferramenta usou conhecimento fora das fontes carregadas. F1. |
| ~04:18 | Para separar o que é SUS, usar as colunas de vínculo SUS e o indicador SUS | ✅ | Confere: `VINC_SUS` e `IND_SUS` constam no informe técnico do CNES. |
| ~05:20 | O DBC é um formato "proprietário" dos anos 90 e o DATASUS "criou esse algoritmo de compressão" | ⚠️ | O DATASUS criou o formato, mas a compressão usa o algoritmo PKWare DCL *implode*, que já existia (é o que o read.dbc descomprime). G2. |
| ~06:15 | TabWin ou bibliotecas da comunidade expandem o DBC para DBF | ✅ | Confere. |
| ~06:50 | O SIM começou a ser desenhado em 1975; a DO padronizou o registro e a causa básica pela CID | ✅ | Confere com a tabela da Fiocruz e o SIM_introducao. |
| ~08:00 | A produção básica de alto volume (vacinas, consultas básicas) fica no arquivo BI | ❌ | O BI é o BPA **individualizado**; a produção consolidada de alto volume (BPA-C) está no **PA**, que o áudio nem menciona. Vacinas são registradas em outro sistema (SI-PNI), não no SIA. R2. |
| ~09:10 | Quimioterapia no AQ, radioterapia no AR, diálise no AN | ⚠️ | AQ e AR confere. Diálise tem arquivo próprio, **ATD** (tratamento dialítico); AN é nefrologia. Conferir no informe do SIA. |
| ~09:25 | Os arquivos de APAC são separados para permitir regras antifraude | ⚠️ | Interpretação plausível, mas sem trecho nas fontes (G1 leve). |
| ~10:20 | RD = AIH reduzida, internações aprovadas; RJ = AIHs rejeitadas | ✅ | Confere com o catálogo. |
| ~10:50 | Picos no RJ podem indicar fraude ou erro de faturamento | ⚠️ | Hipótese interpretativa, sem fonte. |
| ~12:10 | O CNS do paciente vem criptografado nas bases públicas | ✅ | O informe do SIA traz o campo "Número do CNS (Cartão Nacional de Saúde) do paciente (criptografia)". Ressalva: vale para os arquivos do SIA; no RD do SIH não há identificador do paciente (pergunta 2). |
| ~12:40 | Pesquisadores fazem *linkage* probabilístico com data de nascimento, município e sexo | ⚠️ | Técnica real, mas o áudio omite o risco de **reidentificação**, que a LGPD (art. 12) e o guia `lgpd-e-interoperabilidade.md` tratam como limite. |
| ~13:10 | A RNDS é uma infraestrutura de interoperabilidade que permite aos sistemas conversarem, "não um super banco de dados" | ✅ | Coerente com a página "Estrutura do projeto" da RNDS (padrão FHIR como "tradutor digital", troca em tempo real). |
| ~14:20 | O padrão adotado é o HL7 FHIR | ✅ | Confere com a pergunta 19. |
| ~14:45 | LOINC para exames e SNOMED CT para termos clínicos | ⚠️ | LOINC confere com a página da RNDS. SNOMED CT não aparece nas fontes carregadas (que citam CID-10, LOINC e SIGTAP). |
| ~15:15 | O arquivo SP tem várias linhas por AIH; somar SP infla gastos; para volume e custo, usar o RD | ✅ | Confere com o catálogo e as armadilhas. O fator "5, 10 ou 20 vezes" é ilustrativo, sem fonte. |
| ~16:25 | No RD, "em regra, cada linha é uma internação" | ⚠️ | Cada linha é uma **AIH**; AIHs de continuação e longa permanência fazem uma internação ter várias linhas (pergunta 2). |
| ~17:00 | Sub-registro de óbitos e causas mal definidas maiores no Norte e Nordeste | ✅ | Confere com as armadilhas do SIM. |
| ~17:50 | A mortalidade proporcional "ajusta a distorção" do sub-registro | ⚠️ | Simplificação: a mortalidade proporcional muda a pergunta, mas não corrige o sub-registro. Não há trecho nas fontes. G2. |
| ~18:45 | Dados de saúde são dados pessoais sensíveis | ✅ | LGPD, art. 5º, II (pergunta 16). |
| ~19:10 | O art. 13 permite que órgãos de pesquisa acessem dados em ambiente controlado, com anonimização ou pseudonimização | ✅ | Confere com a pergunta 18. |
| ~19:25 | Anonimizar torna "computacionalmente impossível" reverter o dado | ⚠️ | A lei fala em reversão com "esforços razoáveis" (art. 12), não em impossibilidade. G2. |
| ~19:27 | É vedado compartilhar dados de saúde para obter vantagem econômica, com exceções (prestação de serviços de saúde, portabilidade, transações financeiras e administrativas), e é proibida a seleção de risco por planos de saúde | ✅ | Confere com a LGPD, art. 11, § 4º, I e II (conferido no texto da lei). A seleção de risco é tratada no § 5º. |
| ~20:45 | O Meu SUS Digital permite ao cidadão ver vacinas e internações; o paciente pode virar "auditor" | ⚠️ | O aplicativo existe; a ideia do paciente auditor é opinião dos apresentadores, sem fonte. |

**O que o áudio deixou de fora**, apesar de o pedido de personalização mencionar periodicidade, ligação entre bases e armadilhas:
- periodicidade das bases e a diferença entre competência e data do evento;
- chaves de ligação (código CNES, município com 6 dígitos × 7 do IBGE, SIGTAP, CID-10);
- `IDADE` codificada no SIM e residência × ocorrência;
- PA conta procedimentos, não pessoas; APAC de continuidade repetida a cada mês;
- CNES como retrato mensal (não somar competências);
- o SINASC é citado só de passagem.

**Placar do áudio (27 afirmações):** 14 ✅ · 12 ⚠️ · 1 ❌ · 0 🔎 (todas as duvidosas conferidas em 13/11/2026).

## Lições de curadoria

- **Conferência nos microdados (13/11/2026):** as variáveis citadas no catálogo e nas perguntas-teste foram verificadas no cabeçalho de arquivos .dbc reais do Acre (SIH-RD 01/2024, SIA-PA 01/2024, SIM-DO 2022, SINASC-DN 2022, CNES-ST 01/2024) com `scripts/conferir_variaveis.py`. Resultado: todas encontradas, incluindo `ANO_CMPT` e `MES_CMPT`.
- **Documentação oficial com erros de grafia (F3):** o informe técnico do SIH (2016) traz `MÊS_CMPT` e `DI_INTER`; nos arquivos .dbc as colunas são `MES_CMPT` e `DT_INTER`. Quem copiar o nome do PDF para o código terá erro. Fonte primária também precisa ser conferida contra os dados.
- **Fontes oficiais divergem entre si (F3):** a codificação de `IDADE` no SIM para menores de 1 ano difere entre a estrutura da DO 2025 e a implementação do microdatasus. Recomendação do guia: conferir a distribuição do primeiro dígito nos próprios dados.
- **Notas como fonte geram autocitação:** com as notas do projeto ativas, a ferramenta as citava como evidência. Para a avaliação, só fontes primárias ficaram ativas.
- **Instruções do notebook, versão 2 (13/11/2026):** a versão 1 fazia a ferramenta listar variáveis em toda resposta e usar o nome "SIH-RD" do microdatasus. As 20 perguntas foram avaliadas com a versão 2; a pergunta 1 foi refeita.
- **Pergunta de controle:** a ferramenta não inventou o número de internações e indicou como obtê-lo (TabNet e arquivos RD de MG). As instruções contra invenção funcionaram.
- **Honestidade sobre lacunas:** na pergunta 9 a ferramenta declarou que o ano da CID-10 não estava nas fontes em vez de completar com conhecimento externo, mesmo sendo um fato conhecido.
- **Citações literais não são confiáveis palavra por palavra (C2):** em duas respostas a ferramenta trocou palavras do texto original por equivalentes em inglês. Trechos usados em documentos devem ser copiados da fonte, não da resposta.
- **Algumas evidências estão na estrutura do FTP, não nos documentos:** o início do CNES (08/2005) e a troca CID-9 → CID-10 no SIM (1996) aparecem nos nomes das pastas do DATASUS, não nos PDFs. Isso explica por que a ferramenta não os encontrou.
- **O resumo em áudio privilegia narrativa sobre precisão:** o formato *Análise detalhada* trouxe analogias boas e acertou os pontos centrais (SP, RD/RJ, sub-registro, LGPD), mas atribuiu ao arquivo BI o papel do PA, trouxe informação correta porém de fora das fontes (obrigatoriedade do CNES para privados) e acrescentou interpretações sem fonte (fraude, "paciente auditor"). Também omitiu metade das armadilhas pedidas no prompt. Serve como introdução; não substitui o catálogo nem as perguntas-teste.
- **Transcrição automática também erra:** a transcrição do áudio registrou "CNS" onde a fala dizia "CNES". Afirmações suspeitas da transcrição foram conferidas ouvindo o trecho antes de serem classificadas como erro.
