# LGPD, ética e interoperabilidade — o essencial para quem analisa dados do SUS

> Resumo de orientação, não parecer jurídico. Consulte sempre o texto vigente das normas.

## LGPD (Lei nº 13.709/2018)

| Artigo | O que diz (em resumo) | Implicação para o analista |
|---|---|---|
| Art. 5º, II | Dado referente à saúde é **dado pessoal sensível** | Microdados com potencial de identificação exigem cuidado redobrado |
| Art. 5º, III e XI | Define dado anonimizado e anonimização | Anonimizar = impossível associar ao titular por meios razoáveis |
| Art. 11 | Hipóteses para tratar dados sensíveis (inclui estudos por órgão de pesquisa e tutela da saúde) | Pesquisa tem base legal, mas com salvaguardas |
| Art. 12 | Dados anonimizados não são dados pessoais, salvo se a anonimização for reversível | Cruzar bases pode **reverter** a anonimização |
| Art. 13 | Estudos em saúde pública: tratamento dentro do órgão, preferencialmente anonimizado/pseudonimizado, sem divulgar dados que identifiquem | Publique só agregados; cuidado com células pequenas |

### Boas práticas para portfólio
- Trabalhe com **microdados públicos já desidentificados**.
- **Não tente reidentificar** pessoas (ex.: cruzar data de nascimento + município pequeno + causa rara).
- Ao publicar tabelas, **suprima células com contagens pequenas** (ex.: < 5) em recortes municipais finos.
- Registre a origem e a data de download de cada arquivo.

## Interoperabilidade

| Norma / iniciativa | O que estabelece |
|---|---|
| **Portaria GM/MS nº 2.073/2011** | Regulamenta padrões de interoperabilidade e informação em saúde no SUS e na saúde suplementar; prevê catálogo de padrões (CPIISS), openEHR para o Registro Eletrônico em Saúde e HL7 para troca de dados de exames |
| **Portaria GM/MS nº 589/2015** | Institui a Política Nacional de Informação e Informática em Saúde (PNIIS) |
| **Portaria GM/MS nº 1.434/2020** | Institui o Programa Conecte SUS e a **RNDS** (arts. 254-A a 254-C da Portaria de Consolidação nº 1/2017) |
| **Portaria GM/MS nº 3.632/2020** | Estratégia de Saúde Digital para o Brasil 2020–2028 |
| **Portaria GM/MS nº 3.232/2024** | Programa SUS Digital |

### RNDS em uma frase
Plataforma nacional de troca de dados clínicos entre estabelecimentos públicos e privados, modelada em **HL7 FHIR** e com terminologias controladas (CID-10, LOINC, SIGTAP). **Não é uma base aberta para pesquisa** — o acesso é do cidadão (Meu SUS Digital) e de profissionais/estabelecimentos integrados. Para análise populacional, as fontes continuam sendo os microdados do DATASUS.
