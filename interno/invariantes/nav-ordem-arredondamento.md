---
titulo: "Ordem de arredondamento do NAV"
tipo: invariante
status: ativo
tags: [invariante]
---

# Ordem de arredondamento do NAV

## Regra

Arredondar por lote para 2 casas PRIMEIRO, depois somar — nunca somar e arredondar no fim.

## Por que

A ordem do arredondamento do NAV e requisito legal e deve replicar o incumbente byte-a-byte.

## Como verificar

Comparar saida com o relatorio do incumbente ate o centavo.
