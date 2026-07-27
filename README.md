# arkar-wiki

**Arkar Funds Brain** — cerebro regulatorio de fundos de investimento brasileiros
(CVM · CMN · BACEN · RFB · ANBIMA).

Base de conhecimento estruturada — normas, estruturas, conceitos e obrigacoes, ligados
entre si — que serve a dois consumidores ao mesmo tempo:

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

## Estrutura do conteudo — 206 notas (154 publicam)

Cada pasta de `content/` e uma **secao** do site. A divisao nao e cosmetica: existe para que
uma nota tenha um lugar obvio e para que os links entre secoes formem o grafo
(norma -> estrutura -> conceito -> obrigacao).

| Secao | Notas | Funcao |
|---|---|---|
| [`estruturas/`](content/estruturas) | 6 + indice | **O veiculo.** FIP, FII, FIAGRO, FIF, FIDC e INR: anexo da RCVM 175 aplicavel, publico-alvo, tributacao, prestadores obrigatorios e conceitos-chave. |
| [`entidades/`](content/entidades) | 5 + indice | **Quem regula.** CVM, CMN, BACEN, RFB e ANBIMA: competencia de cada um, o que emite e onde entra no ciclo de vida do fundo. Evita atribuir a norma ao orgao errado. |
| [`normas/`](content/normas) | 83 + indice | **A regra**, subdividida por **tipo de ato** (ver abaixo). |
| [`conceitos/`](content/conceitos) | 34 + indice | **O vocabulario.** Glossario operacional, agrupado em `fundos/` (21), `ofertas/` (6), `servicos-qualificados/` (3) e `lgpd/` (a redigir). `kyc`, `pld-ft` e `icp-brasil` ficam na raiz — sao compliance e nao cabem nos quatro grupos. Secao mais linkada: normas e estruturas apontam para ca em vez de reexplicar o termo. |
| [`obrigacoes/`](content/obrigacoes) | 67 + indice | **O calendario.** `calendario/` tem a hierarquia ano (2026–2030) -> mes; `informes/` guarda os informes periodicos. **Os 66 indices de ano/mes sao esqueleto:** o conteudo vem do Postgres (`v_obrigacao_regulatoria_efetiva`), com `sistema_slug` no frontmatter fazendo a ponte com `obrigacoes_regulatorias`. Ver `_templates/T-obrigacao`. **So 2026 publica** — 2027–2030 estao com `publish: false` para nao encher o Explorador e o grafo de paginas vazias; virar `true` quando o ano chegar. |
| [`jurisprudencia/`](content/jurisprudencia) | so indice | **O precedente.** Decisoes do Colegiado da CVM, termos de compromisso e PAS. A redigir. |
| [`meta/`](content/meta) | 3 + indice | **As regras da wiki:** `aviso-legal`, `como-usar` e `politica-de-revisao`. **Oculta no Explorador** (as paginas seguem acessiveis por URL e busca). |

### `normas/` por tipo de ato

| Subsecao | Notas | Conteudo |
|---|---|---|
| `leis/` | 6 | Leis federais (14.754/2023, 12.431/2011, 11.478/2007, 11.033/2004, 8.668/1993). |
| `resolucoes/` | 26 | Resolucoes CVM e CMN — o corpo principal da regra vigente. Inclui a **RCVM 175 em 14 notas**: `rcvm-175-parte-geral`, os anexos `01`–`12` e `rcvm-175-suplementos`. Tambem CMN 4.373, RCVM 160, 161, 19, 21, 23, 32, 33, 35, 50 e a Conjunta BCB/CVM 13. |
| `instrucoes/` | 2 | Instrucoes CVM anteriores ao regime de resolucoes, ainda aplicaveis (ICVM 579). |
| `oficios/` | 28 | **A interpretacao.** Oficios-Circulares da CVM: onde esta o entendimento pratico do regulador sobre o que a norma nao diz explicitamente. |
| `cpc/` | 14 | Pronunciamentos contabeis (CPC) que alcancam fundos, com a correspondencia IFRS/IAS. |
| `autorregulacao/` | 6 | Codigos ANBIMA — obrigam por adesao, nao por lei. |
| `deliberacoes/` | 1 | Deliberacoes do Colegiado da CVM. |

---

## Navegacao do site

**Explorador** (barra esquerda) espelha a arvore de `content/`: criar pasta cria um no, sem
configuracao. A **ordem** das secoes e imposta por CSS em `quartz/styles/custom.scss`
(Estruturas, Entidades, Normas, Conceitos, Obrigacoes, Jurisprudencia) porque as opcoes
`sortFn`/`filterFn` do plugin sao funcoes JS e nao existem no YAML — o mesmo mecanismo
oculta `meta/`.

O nome exibido de cada pasta vem do **`title` do `index.md`** dela. Sem `index.md`, o
Explorador mostra o nome cru do diretorio (minusculo, sem acento) — por isso **toda pasta
tem um `index.md`**.

Tambem automaticos: **Busca**, **Grafo**, **Sumario** e **Links** (backlinks), alem de tema
claro/escuro e modo leitor.

### Grafo e tags

O grafo e montado no cliente: **nos** = notas **+ tags**; **arestas** = uso de tag e
`[[wikilinks]]` no corpo. Estado atual: **302 nos** (206 notas + 96 tags) e **506 arestas** —
mas **90% delas vem de tag**, porque apenas **8 notas** usam wikilink (50 links, todos em
`estruturas/`, na home e no `meta/index`). Enquanto isso nao mudar, o grafo e "notas agrupadas
por assunto", nao um mapa de relacoes: as arestas dizem *"tem a mesma tag"*, nao *"se refere a"*.

Convencoes de tag:

- **Tudo acentuado** (`índice`, `securitização`, `ofício-circular`). A convencao mista era a
  origem de tags duplicadas que viravam dois nos para o mesmo conceito (`balanco-` vs `balanço-`).
- **`índice` esta em `removeTags`** do grafo: e tag estrutural (uma por pasta) e criava um hub
  sem significado. Efeito colateral aceito: os `index.md` ficam sem aresta e aparecem soltos.
- **97 tags distintas.** Ao criar tag nova, prefira reusar uma existente: cada tag de uso unico
  e um no a mais no grafo sem ganho de navegacao. Evite tambem tag que duplique uma nota
  existente (ex.: tag `fip` competindo com `estruturas/fip`) — nesse caso o `[[wikilink]]` e
  melhor, porque gera aresta real em vez de um no paralelo.

**Aliases nao poluem o grafo.** Os 240 `aliases:` do frontmatter geram 232 paginas de redirect
(`meta refresh` + `canonical` + `noindex`), mas nenhuma entra no `contentIndex.json` — logo nao
viram no nem aresta. Verificado. Usar alias e a forma barata de manter link antigo funcionando
depois de renomear uma nota.

---

## Modelo de publicacao (fail-closed)

Nada publica por acidente. Sao tres barreiras independentes:

1. **`ExplicitPublish`** — allowlist: sem `publish: true` no frontmatter, a nota nao entra no site.
2. **`ignorePatterns`** — `interno/`, `_templates/` e `.obsidian/` ficam fora do que o build enxerga.
3. **`scripts/guard-publicacao.py`** — roda **antes** do build (`exit != 0` aborta o deploy) e reprova:
   nota com `publish: true` sem revisao completa, link de `content/` -> `interno/`, arquivo
   nao-Markdown em `content/`, e PII (CPF/CNPJ/JWT/chave privada).

```bash
python3 scripts/guard-publicacao.py   # esperado: erros: 0 (exit 0)
```

### Frontmatter

Para publicar, o guard exige: `status: revisado` + `verificado_em: YYYY-MM-DD` + `fontes:` (>= 1)
+ `publish: true`. O fluxo previsto e `stub` -> `rascunho` -> `revisado`
(ver [`content/meta/politica-de-revisao.md`](content/meta/politica-de-revisao.md)).

> [!important] `title` e obrigatorio
> O rotulo da nota vive em **um unico campo: `title`** — o que o Quartz le
> (`quartz/components/Head.tsx`). Sem ele, a pagina publicada herda o **nome do arquivo**
> no `<title>`, no `og:title` e no `<h1>`; e o `title` do `index.md` de uma pasta e o que
> nomeia a secao no Explorador. Os templates em `_templates/` ja trazem o campo.
>
> O schema antigo tinha tambem um `titulo` (denominacao formal, lido por ninguem no build).
> Foi removido das notas para nao manter dois rotulos divergindo em silencio — a revisao dos
> CPC (R1/R2/R3), que so existia nele, foi incorporada ao `title`.

> [!warning] Estado atual da revisao
> As 206 notas estao com `status: revisado`, e 154 com `publish: true` (as 52 de 2027–2030
> ficam `false`). Mas isso foi aplicado **em lote** para levar o site ao ar: o **pacote
> formal** esta completo, a **revisao editorial de conteudo nao**. Varias notas ainda sao
> esqueleto, e `verificado_por` esta `""` em todas.

---

## Tema

Grayscale fiel ao design system do app (`arkar-system-frontend/styles/globals.css`), sem
nenhuma cromatica na chrome. Link em corpo = cor do texto + **underline persistente** (a
affordancia vem do sublinhado, nao da cor). Fontes **Space Grotesk** e **JetBrains Mono**
self-hosted em `quartz/static/fonts/`; favicon e logo da Arkar em `quartz/static/brand/`.
Detalhes e armadilhas em [SETUP.md](SETUP.md).

---

## `interno/` (nunca publica)

Fica no repo (versionado, repo privado), fora do site:

- `adr/` — decisoes de arquitetura do proprio vault.
- `invariantes/` — invariantes de engenharia do ArkarSystem (RLS, soft-delete, ordem de arredondamento do NAV…).
- `dados-oficios/` — subprodutos do parse dos oficios: `manifest.json`, `graph.json`,
  `vinculos-edges.csv` e `relatorio-parse-vinculos.md`. Sao `.json`/`.csv`: nao poderiam morar
  em `content/` de qualquer forma, porque o guard reprova nao-Markdown la.
- `mercado/`, `prompts/` — material de trabalho.

**Nunca** linkar `content/` -> `interno/`: o guard reprova o build.
