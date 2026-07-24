---
titulo: "Triple-revoke + FORCE RLS em todo objeto novo em public"
tipo: invariante
status: ativo
tags: [invariante]
---

# Triple-revoke + FORCE RLS em todo objeto novo em public

## Regra

Cada tabela nova exige, na MESMA migration, REVOKE explicito de `anon` + `authenticated` + `backend_api` e `FORCE ROW LEVEL SECURITY`.

## Por que

Todo objeto novo no schema `public` herda privilegios de `anon` por `ALTER DEFAULT PRIVILEGES`.

## Como verificar

Conferir GRANTs em `information_schema.role_table_grants` e `relforcerowsecurity` em `pg_class`.
