---
titulo: "UNIQUE parcial com WHERE deleted_at IS NULL"
tipo: invariante
status: ativo
tags: [invariante]
---

# UNIQUE parcial com WHERE deleted_at IS NULL

## Regra

Todo indice UNIQUE de entidade deve ter `WHERE deleted_at IS NULL`.

## Por que

UNIQUE total em CNPJ bloqueia re-cadastro apos soft-delete.

## Como verificar

Inspecionar `indexdef` em `pg_indexes` — deve conter o predicado parcial.
