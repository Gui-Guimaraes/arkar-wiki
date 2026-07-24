# arkar-wiki

Cerebro regulatorio de fundos de investimento brasileiros (CVM · CMN · BACEN · RFB · ANBIMA).

Base de conhecimento estruturada — normas, conceitos, veiculos e obrigacoes, ligados entre
si — que serve a dois consumidores ao mesmo tempo:

1. **Referencia operacional** da equipe da Arkar (o que a norma obriga na pratica).
2. **Corpus do RAG** dos produtos de IA da Arkar (as notas sao a fonte que o modelo cita).

Por isso o formato importa tanto quanto o conteudo: cada nota tem frontmatter tipado e
descreve **consequencia operacional**, **erros comuns** e **relacoes** — nunca a citacao
literal do artigo. Quem precisa do texto da lei vai a fonte oficial; a wiki explica o efeito.

- **Edicao:** Obsidian (abrir esta pasta como vault).
- **Site:** Quartz v5 -> `wiki.arkar.ai` (Vercel). So `content/` e publicado.
- **Repo privado.** `interno/` nunca vai ao site (tres barreiras: ExplicitPublish + ignorePatterns + guard).

Setup, tema e publicacao em [SETUP.md](SETUP.md).

---

## Estrutura do conteudo

Cada pasta de `content/` e uma **secao** do site, com um papel distinto. A divisao nao e
cosmetica: ela existe para que uma nota tenha um lugar obvio e para que os links entre
secoes formem o grafo (norma -> veiculo -> conceito -> obrigacao).

| Secao | Notas | Funcao |
|---|---|---|
| [`normas/`](content/normas) | 7 + indice | **A regra.** Uma nota por norma (RCVM 175, RCVM 21, RCVM 50, ICVM 579, CMN 4373, Lei 14.754/2023, Codigos ANBIMA). Escopo, o que muda na operacao, erros comuns e o que ela revoga/altera. |
| [`veiculos/`](content/veiculos) | 5 + indice | **A estrutura.** Um tipo de fundo por nota (FIP, FIDC, FII, FIAGRO, FIF): anexo da RCVM 175 aplicavel, publico-alvo, tributacao, prestadores obrigatorios e conceitos-chave. |
| [`conceitos/`](content/conceitos) | 30 + indice | **O vocabulario.** Glossario operacional do dominio (classe, subclasse, serie, cota, NAV, come-cotas, chamada de capital, patrimonio segregado, KYC, PLD/FT, investidor qualificado/profissional, prestadores...). E a secao mais linkada: normas e veiculos apontam para ca em vez de reexplicar o termo. |
| [`entidades/`](content/entidades) | 5 | **Quem regula.** CVM, CMN, BACEN, RFB e ANBIMA: competencia de cada um, o que emite e onde entra no ciclo de vida do fundo. Evita a confusao classica de atribuir a norma ao orgao errado. |
| [`oficios/`](content/oficios) | 271 | **A interpretacao.** Perguntas e respostas dos Oficios-Circulares da CVM sobre a RCVM 175 (inteiro teor, com `oficio`, `area_cvm`, `data_publicacao`, `tipos_de_fundos`, `palavras_chave` e `vinculos` entre itens). E onde esta o entendimento pratico do regulador — o que a norma nao diz explicitamente. |
| [`obrigacoes/`](content/obrigacoes) | so indice | **O calendario.** Entregas, prazos e periodicidades. **Propositalmente vazia no vault:** os dados vem do Postgres (`v_obrigacao_regulatoria_efetiva`), e o campo `sistema_slug` no frontmatter faz a ponte com `obrigacoes_regulatorias` no banco. Ver `_templates/T-obrigacao`. |
| [`meta/`](content/meta) | 3 | **As regras da wiki.** `aviso-legal` (nao e aconselhamento juridico e nao substitui a fonte oficial), `como-usar` (fluxo de edicao) e `politica-de-revisao` (o que uma nota precisa cumprir para publicar). |

Total: **326 notas**.

### Explorador

O **Explorador** e a navegacao na barra esquerda do site: ele espelha automaticamente a
arvore de pastas de `content/`, entao as secoes acima aparecem la sem configuracao manual —
criar uma pasta em `content/` cria um no no Explorador. Nao e um indice curado: a ordem e a
hierarquia saem do sistema de arquivos.

O resto da chrome do site tambem e automatica: **Busca** (indice de texto completo),
**Grafo** (as notas como nos e os links entre elas como arestas — util para ver o que esta
orfao), **Sumario** dos titulos da nota, **Links** (backlinks), alem de **tema claro/escuro**
e **modo leitor**.

---

## Modelo de publicacao (fail-closed)

Nada publica por acidente. Sao tres barreiras independentes:

1. **`ExplicitPublish`** — allowlist: sem `publish: true` no frontmatter, a nota nao entra no site.
2. **`ignorePatterns`** — `interno/`, `_templates/` e `.obsidian/` ficam fora do que o build enxerga.
3. **`scripts/guard-publicacao.py`** — roda **antes** do build (`exit != 0` aborta o deploy) e reprova:
   nota com `publish: true` sem revisao completa, link de `content/` -> `interno/`, arquivo
   nao-Markdown em `content/`, e PII (CPF/CNPJ/JWT/chave privada).

### Frontmatter

Campos que o fluxo exige para publicar: `status: revisado` + `verificado_em: YYYY-MM-DD` +
`fontes:` (>= 1). O fluxo de status previsto e `stub` -> `rascunho` -> `revisado`
(ver `content/meta/politica-de-revisao.md`).

> [!important] `title` vs `titulo`
> O schema do vault usa **`titulo`**, mas o **Quartz le `title`**. Sem `title`, a pagina
> publicada herda o **nome do arquivo** no `<title>`, no `og:title` e no `<h1>` — um oficio
> sairia como `seq-001__oficio-circular-no-1-2023-sin-sse`. Toda nota deve ter os dois.

---

## `interno/` (nunca publica)

Fica no repo (versionado, repo privado), fora do site:

- `adr/` — decisoes de arquitetura do proprio vault.
- `invariantes/` — invariantes de engenharia do ArkarSystem (RLS, soft-delete, ordem de arredondamento do NAV...).
- `dados-oficios/` — subprodutos do parse dos oficios: `manifest.json` (indice), `graph.json` e `vinculos-edges.csv` (grafo de vinculos entre itens) e `relatorio-parse-vinculos.md` (cobertura do parse). Sao `.json`/`.csv`: nao poderiam morar em `content/` de qualquer forma, porque o guard reprova nao-Markdown la.
- `mercado/`, `prompts/` — material de trabalho.

**Nunca** linkar `content/` -> `interno/`: o guard reprova o build.
