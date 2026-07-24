---
titulo: "pg_policies diff-zero"
tipo: invariante
status: ativo
tags: [invariante]
---

# pg_policies diff-zero

## Regra

Antes de prosseguir, o diff de `pg_policies` vs. baseline deve ser zero.

## Por que

Operacoes que tocam RLS nao podem alterar a contagem de policies sem intencao.

## Como verificar

`SELECT count(*) FROM pg_policies` antes/depois; diferenca = 0.
