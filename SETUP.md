# SETUP — arkar-wiki

Guia em 3 fases: **vault local -> seed -> publicacao**.

## Fase 1 — Vault local (Obsidian)

1. Instale o Obsidian e abra a pasta `arkar-wiki/` como vault.
2. Plugins core ja habilitados (`.obsidian/`): Templates (`_templates/`), Graph, Backlinks, Bases.
3. Teste o guard:

   ```bash
   python3 scripts/guard-publicacao.py
   # esperado: erros: 0 (exit 0). `publicaveis` = quantas notas tem publish: true
   # (hoje 1: content/index.md, a home). Qualquer erro reprova o build.
   ```

## Fase 2 — Seed (preencher conteudo)

1. Notas nascem `status: stub` e **nao publicam**. Preencha a partir da **fonte oficial**.
2. Regra de escrita: cada nota entrega **consequencia operacional**, **erros comuns** e **relacoes** — nunca a citacao literal do artigo.
3. Ao revisar: `status: revisado` + `verificado_em: YYYY-MM-DD` + `fontes:` (≥1) e so entao `publish: true`.
4. `obrigacoes/` fica vazio de proposito — vem do Postgres (`v_obrigacao_regulatoria_efetiva`; ponte por `sistema_slug`).
5. Ofícios (batch de 271, `status: rascunho`) entram em `content/oficios/` e nao publicam ate revisao. Subprodutos (manifest/graph/edges/relatorio) vao para `interno/`.

## Fase 3 — Publicacao (Quartz v5 / Vercel)

O maquinario do Quartz v5.0.0 mora na **raiz** do repo (fork do upstream, branch `v5`),
com as notas em `content/`. Requisitos: **Node >= 22** e **npm >= 10.9.2**.

1. Instalar / atualizar dependencias e plugins:

   ```bash
   npm install
   npx quartz plugin install --from-config
   npx quartz build --serve   # preview em http://localhost:8080
   ```

2. **Config = YAML, na raiz: `quartz.config.yaml`.** A v5 **nao** usa `quartz.config.ts`
   (o `quartz.ts` da raiz e so o entrypoint programatico). O arquivo ativo nasce de
   `quartz.config.default.yaml`; o resolvedor procura `quartz.config.yaml` primeiro
   (`quartz/cli/plugin-data.js`). Ja aplicado: `pageTitle: Arkar Funds Brain`,
   `baseUrl: wiki.arkar.ai`, `locale: pt-BR`, `analytics: null`, `ignorePatterns`
   e o plugin `@quartz-community/explicit-publish` com `enabled: true`.

3. **`ignorePatterns` e GLOBAL — nunca colocar `**/!(*.md)` ali.** O emitter `Static`
   tambem aplica esses padroes (`quartz/plugins/emitters/static.ts`), entao aquele glob
   exclui do site **todos** os assets nao-Markdown (fontes, `icon.png`, `og-image.png`).
   A regra "sem nao-MD em `content/`" e responsabilidade do **guard**, que reprova o build.

4. **Tema — DEFINIDO** (nao e mais decisao posterior): grayscale fiel ao design system
   do app (`arkar-system-frontend/styles/globals.css`), sem nenhuma cromatica na chrome.
   Vive em `configuration.theme` do YAML: `colors.lightMode` / `colors.darkMode`
   (papeis `light`, `lightgray`, `gray`, `darkgray`, `dark`, `secondary`, `tertiary`,
   `highlight`, `textHighlight`), `typography` e `fontOrigin`.
   - **Link** = cor do texto (`secondary` == `dark`) + **underline persistente**; a
     affordancia vem do sublinhado, nao de cor. Regra em `quartz/styles/custom.scss`
     (caminho do CSS custom na v5), escopada a `article` para nao sujar a navegacao.
   - **Realce de sintaxe**: `@quartz-community/syntax-highlighting` com
     `github-light` / `github-dark`.

5. **Fontes self-hosted** — Space Grotesk (titulos + corpo) e JetBrains Mono (codigo).
   Com `fontOrigin: local` o core do Quartz **nao** baixa nada ("let the user do it
   themselves in css"), entao os `.woff2` variaveis ficam versionados em
   `quartz/static/fonts/` (servidos em `/static/fonts/`) e o `@font-face` esta em
   `quartz/styles/custom.scss`. O Space Grotesk e o **mesmo arquivo do app**. Resultado:
   **build e runtime sem dependencia de rede** para fontes.

   ⚠️ **Nao religue o plugin `@quartz-community/quartz-fonts`** (esta `enabled: false`).
   Ele tem opcoes proprias com default `fontOrigin: googleFonts` +
   Schibsted Grotesk/Source Sans Pro/IBM Plex Mono e **ignora**
   `configuration.theme.typography`. Ligado, ele injeta um
   `<link rel="stylesheet">` para `fonts.googleapis.com` pedindo as fontes **erradas** —
   reintroduzindo 3rd-party e dependencia de rede em runtime. Verificado empiricamente:
   com o plugin ligado o `<link>` volta; desligado, o site nao contata o Google.

6. **Callouts em grayscale** — o `quartz/styles/callouts.scss` do upstream hardcoda uma
   paleta Material cromatica por tipo. `quartz/styles/custom.scss` sobrescreve
   `--color`/`--border`/`--bg` para tons da escala cinza, mantendo o invariante
   "nenhuma cromatica na chrome".

7. Guard amarrado ao build em **`vercel.json` na raiz**:
   `python3 scripts/guard-publicacao.py && npx quartz build`, output `public`,
   `cleanUrls: true`. O `&&` garante que `exit != 0` do guard aborta o build.

8. ⚠️ **Pendente de confirmacao em deploy real:** que `python3` exista na imagem de
   build do Vercel. Se o deploy falhar com `python3: not found`, reescrever o guard em
   Node e decisao do dono.

## Invariantes do vault

- `content/` = unico publicado; `interno/` nunca sai.
- Fail-closed: sem `publish: true`, nao publica.
- Nunca linkar `content/` -> `interno/`.
- Sem PII (CPF/CNPJ/JWT/chave privada) em `content/`.
