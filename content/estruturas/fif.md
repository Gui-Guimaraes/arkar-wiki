---
title: "FIF"
titulo: "FIF"
tipo: veiculo
status: revisado
sigla: FIF
norma_base: ["Resolução CVM 175/2022", "Anexo Normativo I", "Lei 14.754/2023"]
anexo_rcvm175: "Anexo Normativo I"
publico_alvo: "Geral (varejo) e qualificados/profissionais, conforme a classe"
tributacao: "Come-cotas em maio e novembro: 15% (carteira de longo prazo) ou 20% (curto prazo); classe de ações fora do come-cotas (15% no resgate)"
prestadores_obrigatorios: ["administrador fiduciário", "gestor de carteira", "custodiante", "auditor independente"]
conceitos_chave: ["fundo 555", "classe", "subclasse", "come-cotas", "renda fixa/ações/cambial/multimercado"]
verificado_em: 2026-07-24
verificado_por: ""
fontes:
  - "Resolução CVM 175/2022 — Anexo Normativo I (FIF): https://conteudo.cvm.gov.br/legislacao/resolucoes/resol175.html"
  - "Lei 14.754/2023 (tributação de fundos): https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14754.htm"
aliases: ["Fundo de Investimento Financeiro", "fundo 555"]
tags: [veículo]
publish: true
---

## Escopo

O FIF é o veículo do **Anexo Normativo I** e sucede os antigos "fundos 555" (ICVM 555). Reúne, sob uma mesma casca, as políticas de **renda fixa, ações, cambial e multimercado** — que passam a ser expressas como **classes** (e subclasses) de um único fundo, e não mais como fundos separados. É o veículo de mercado aberto por excelência: admite condomínio aberto ou fechado, cotização diária típica e distribuição ao varejo. A RCVM 175 ampliou limites de exposição ao exterior (até 100% do PL, inclusive para varejo), incorporou criptoativos e créditos de carbono/descarbonização (CBIO) à definição de ativo financeiro e liberou a recompra de cotas para além do antigo nicho de fundos de acesso.

## Consequência operacional

Cada **classe é tratada como um fundo** para fins de tributação e de escrituração — o administrador precisa segregar patrimônio, cota e IR por classe/subclasse. A tributação segue o **come-cotas** nos últimos dias úteis de maio e novembro: **15%** para carteira de longo prazo (prazo médio superior a 365 dias) e **20%** para curto prazo, com recolhimento complementar pela tabela regressiva no resgate. A **classe de ações não sofre come-cotas** (15% sobre o ganho, no resgate). A contratação do distribuidor passou a ser responsabilidade do **gestor**. Informe mensal, lâmina (quando aplicável) e demais reportes seguem o calendário da parte geral da 175.

## Erros comuns

- Tratar as classes como um só "bolso" tributário — cada classe tem come-cotas e base de cálculo próprios.
- Assumir que todo FIF sofre come-cotas: a classe de ações não sofre.
- Manter a lógica pré-175 de "um CNPJ por estratégia" em vez de classes sob o mesmo fundo.
- Esquecer de checar o prazo médio da carteira ao definir a alíquota (15% x 20%).

## Relação com outras notas

- Casca regulatória: [[rcvm-175]].
- Demais veículos: [[fidc]], [[fii]], [[fip]], [[fiagro]].
- Regime de não residentes: [[inr]] · [[investidor-nao-residente]].