---
titulo: "Soft-delete em tudo"
tipo: invariante
status: ativo
tags: [invariante]
---

# Soft-delete em tudo

## Regra

Usar `deleted_at`; jamais DELETE fisico (excecao: tabelas de simulacao de CRM sem `deleted_at`).

## Por que

Deletes fisicos nunca sao feitos; `ON DELETE CASCADE` foi quase-acidente destruindo 2.634 fundos.

## Como verificar

Grep por `DELETE FROM` e por `ON DELETE CASCADE` em migrations.
