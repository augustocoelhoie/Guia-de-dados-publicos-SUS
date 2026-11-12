# Roteiro de montagem do notebook (NotebookLM)

Tempo estimado: **40–60 min**.

## 1. Criar o notebook
1. Acesse https://notebooklm.google.com e clique em **Novo notebook**.
2. Nome: **Guia de Dados Públicos do SUS**.

## 2. Adicionar fontes
1. Rode `python scripts/baixar_documentacao.py` e escolha os PDFs indicados em `fontes/fontes-notebooklm.md`.
2. Renomeie os arquivos com nomes claros (`SIM_dicionario_DO.pdf`).
3. Suba os PDFs e cole as URLs (LGPD, portarias, RNDS) em **Adicionar fonte → Site**.
4. Abra cada fonte e confira se o texto foi extraído (PDF escaneado aparece vazio → registre como R1).

## 3. Instruções do notebook
Em **Configurar conversa → Personalizado**, cole:

```
Você é um guia para analistas que vão usar dados públicos do SUS.
Responda em português, sempre citando o documento e o trecho.
Se a resposta não estiver nas fontes, diga claramente que não está
e sugira onde procurar. Nunca invente números, variáveis ou artigos.
Ao falar de uma variável, informe a base, o nome exato e a unidade.
```

## 4. Notas fixas (opcional, mas melhora muito)
Crie notas com: a tabela-resumo do `catalogo/catalogo-bases.md` e o `docs/armadilhas.md`.

## 5. Resumo em áudio (Audio Overview)
Em **Studio → Resumo em áudio → Personalizar**, cole:

```
Episódio para quem vai começar a trabalhar com dados do SUS.
Explique as cinco bases (SIH, SIA, SIM, SINASC, CNES): o que cada uma
registra, a periodicidade e como ligá-las. Dedique um bloco às
armadilhas mais comuns e outro à LGPD. Tom didático, em português.
```

Baixe o áudio, salve em `notebooklm/resumo-audio.mp3` (ou publique e cole o link no README) e ouça conferindo as afirmações — anote os erros em `avaliacao/registro-de-erros.md`.

## 6. Testar e publicar
1. Rode as 20 perguntas de `avaliacao/perguntas-teste.md`.
2. **Compartilhar → Qualquer pessoa com o link** (modo visualização/chat).
3. Cole o link no `README.md` (seção *Entregáveis*).
