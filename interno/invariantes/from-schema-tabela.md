---
titulo: "Fail-silent do .from('schema.tabela')"
tipo: invariante
status: ativo
tags: [invariante]
---

# Fail-silent do .from('schema.tabela')

## Regra

Nunca usar ponto em `.from()`; usar o schema configurado no client.

## Por que

A notacao PostgREST com ponto (`schema.tabela`) em `.from()` falha silenciosamente.

## Como verificar

Grep literal por `.from('` com ponto no argumento — o grep comum passa batido.
