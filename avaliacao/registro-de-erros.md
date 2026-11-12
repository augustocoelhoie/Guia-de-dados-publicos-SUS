# Registro de erros e limitações da ferramenta

> Esta é a parte que diferencia o projeto: **onde o NotebookLM errou e por quê**.
> Preencha durante o teste das 20 perguntas e ao gerar o resumo em áudio.

## Como classificar a causa do erro

| Código | Causa | Exemplo típico |
|---|---|---|
| **F1** | Fonte ausente | A informação não estava em nenhum documento carregado |
| **F2** | Fonte desatualizada | O PDF descreve um layout antigo do arquivo |
| **R1** | Recuperação falhou | A resposta estava na fonte, mas o trecho não foi encontrado (tabelas em PDF escaneado, por ex.) |
| **R2** | Mistura de fontes | Combinou regras de dois sistemas diferentes (SIH × SIA) |
| **G1** | Alucinação | Afirmou algo que não está em nenhuma fonte (número, artigo de lei, variável inexistente) |
| **G2** | Generalização indevida | Transformou uma regra específica em regra geral |
| **C1** | Citação errada | Resposta certa, mas apontou o documento/trecho errado |

## Registro

| # pergunta | O que a ferramenta respondeu (resumo) | Código | Por que errou | Correção aplicada |
|---|---|---|---|---|
| | | | | |

## Resumo em áudio (Audio Overview)

| Minuto | Afirmação no áudio | Correta? | Comentário |
|---|---|---|---|
| | | | |

## Lições de curadoria

- _Ex.: PDFs escaneados do FTP não foram lidos — substituídos por versão em texto (R1)._
- _Ex.: Retirada a fonte X porque misturava layouts de 2007 e 2008 (F2)._
