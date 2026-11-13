# Roteiro de montagem do notebook (NotebookLM)

Tempo estimado: **40–60 min**.

## 1. Criar o notebook
1. Acesse https://notebooklm.google.com e clique em **Novo notebook**.
2. Nome: **Guia de Dados Públicos do SUS**.

## 2. Adicionar fontes

> O NotebookLM é um site: ele **não abre pastas**. O VS Code serve só para baixar os PDFs; depois você envia os arquivos um a um (ou vários de uma vez) pelo navegador.

### 2a. No VS Code: ver o tamanho e baixar
1. **Arquivo → Abrir pasta** → selecione `guia-dados-sus`.
2. **Terminal → Novo terminal**.
3. Confira o Python: `python --version` (no Windows, se falhar, use `py --version` e troque `python` por `py` nos comandos).
4. Só listar, sem baixar nada (mostra o tamanho e o tempo estimado):
   `python scripts/baixar_documentacao.py --listar`
5. Baixar um sistema por vez, começando pelo menor:
   `python scripts/baixar_documentacao.py SIM` → depois `SINASC`, `CNES`, `SIH`, `SIA`.
6. Os arquivos aparecem em `fontes/pdf/<SISTEMA>/`. Se você rodar de novo, o que já foi baixado é pulado.

### 2b. No explorador de arquivos: escolher e renomear
1. Abra `fontes/pdf/` e escolha os documentos 🟢 de `fontes/fontes-notebooklm.md` (o dicionário ou informe técnico mais recente de cada sistema).
2. Renomeie com nomes claros: `SIM_dicionario_DO.pdf`, `SIH_informe_tecnico_RD.pdf`.
3. Para fontes que são páginas web e não importam bem (ex.: o texto da LGPD no Planalto), abra no navegador e use **Ctrl+P → Salvar como PDF**.

### 2c. No NotebookLM: enviar
1. No notebook, clique em **+ Adicionar fontes** (ou **Fontes → +**).
2. **Fazer upload** → selecione os PDFs renomeados.
3. Para cada URL: **+ Adicionar fontes → Site** → cole o link → **Inserir**.
4. Clique em cada fonte na barra lateral e confira se o texto aparece. PDF escaneado aparece vazio → anote como **R1** em `avaliacao/registro-de-erros.md`.

## 3. Instruções do notebook
Em Configurar conversa → Personalizado, cole:

Você é um guia para analistas que vão usar dados públicos do SUS.
Responda em português, sempre citando o documento e o trecho.
Se a resposta não estiver nas fontes, diga claramente que não está
e sugira onde procurar. Nunca invente números, variáveis ou artigos.
Responda apenas ao que foi perguntado. Liste variáveis só quando a
pergunta pedir; nesse caso, informe a base, o nome exato e a unidade.
Use os nomes de arquivo do DATASUS (RD, SP, PA, DO, DN, ST), não os
nomes usados por pacotes como microdatasus (ex.: "SIH-RD").

Versão 2 das instruções (13/11/2026). A versão 1 pedia "ao falar de uma variável, informe a base, o nome exato e a unidade", o que fazia a ferramenta acrescentar listas de variáveis em toda resposta.

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
