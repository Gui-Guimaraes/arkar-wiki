---
titulo: "SUPABASE_URL do backend nunca aponta pro dominio custom"
tipo: invariante
status: ativo
tags: [invariante]
---

# SUPABASE_URL do backend nunca aponta pro dominio custom

## Regra

`SUPABASE_URL` no backend = URL original do projeto, nunca o dominio custom.

## Por que

`database.arkar.cloud` serve API/JWKS mas nao e o issuer do GoTrue; o token carrega a URL original do projeto Supabase como `iss`.

## Como verificar

Conferir `iss` de um JWT emitido vs. a env do backend.
