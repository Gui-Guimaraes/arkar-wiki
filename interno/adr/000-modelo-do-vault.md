---
titulo: "ADR 000 — Modelo do vault e separacao publico/interno"
tipo: adr
status: aceito
data: 2026-07-24
tags: [adr]
---

# ADR 000 — Modelo do vault e separacao publico/interno

## Contexto

O arkar-wiki e ao mesmo tempo (a) referencia regulatoria publica em `wiki.arkar.ai` e (b) repositorio de conhecimento interno da Arkar (ADRs, invariantes, prompts, inteligencia de mercado). Publicar por engano material interno seria vazamento.

## Decisao

Vault unico com **tres barreiras** contra vazamento:

1. **`content/` e o unico diretorio publicado**; `interno/` fica fora do build.
2. **ExplicitPublish (allowlist fail-closed):** sem `publish: true` no frontmatter, a nota nao sai.
3. **`ignorePatterns` (interno, _templates, nao-MD) + `guard-publicacao.py` no build command**, que reprova o deploy diante de: publish sem revisao completa; link `content/`->`interno/`; nao-Markdown em `content/`; PII (CPF/CNPJ/JWT/chave privada).

## Consequencias

- Publicacao e deliberada e auditavel; o default e nao-publicar.
- Notas nascem `stub` e so sobem apos revisao (`status: revisado` + `verificado_em` + `fontes`).
- Tema (cores/fontes) e decisao posterior; a config do Quartz nasce sem cor/fonte definidas.

## Status

aceito
