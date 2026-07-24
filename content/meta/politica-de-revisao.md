---
title: "Politica de revisao"
titulo: "Politica de revisao"
tipo: meta
status: revisado
tags: [meta]
verificado_em: 2026-07-24
fontes:
  - "CVM - portal de legislacao e regulamentacao: https://www.gov.br/cvm/pt-br"
publish: true
---

# Politica de revisao

**Fluxo de status:** `stub` -> `rascunho` -> `revisado`.

Uma nota so pode receber `publish: true` quando tiver, cumulativamente:

1. `status: revisado`
2. `verificado_em` (data ISO `YYYY-MM-DD`)
3. `fontes` preenchido (≥1 fonte oficial)

O `guard-publicacao.py` reprova o build se qualquer uma faltar. Notas com `verificado_em` > 180 dias geram **aviso** (nao bloqueiam) e devem ser re-revisadas.
