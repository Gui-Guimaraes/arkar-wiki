---
title: "Ofício-Circular nº 6/2023/CVM/SIN"
tipo: norma
status: revisado
orgao: Comissão de Valores Mobiliários (CVM) - Superintendência de Supervisão de Investidores Institucionais (SIN)
numero: 6
ano: 2023
ementa: "Presta esclarecimentos adicionais aos administradores fiduciários e gestores sobre o envio de dados periódicos, layouts de informes e rotinas operacionais no âmbito do sistema de envio de documentos CVM Web."
vigencia_inicio: 2023-08-10
vigencia_fim:
url_oficial: "https://cvm.gov.br"
revoga: []
revogada_por:
alterada_por: []
aplica_a: ["Administradores fiduciários", "Gestores de recursos (Assets)", "Custodiantes", "Controladores de ativos e passivos"]
verificado_em: 2026-07-24
verificado_por: ""
fontes:
  - "Comissão de Valores Mobiliários - Orientações da CVM (Ofícios Circulares): https://cvm.gov.br"
aliases: [OC SIN 06/23, Guia de Sistemas SIN 2023, Ofício de Informes Digitais SIN]
tags: [norma, ofício-circular, fundos-de-investimento, cvm-web, obrigações-periódicas, compliance]
publish: true
---

O **Ofício-Circular nº 6/2023/CVM/SIN** é uma orientação técnica específica emitida pela Superintendência de Supervisão de Investidores Institucionais da CVM. O documento foi lançado com o objetivo de corrigir falhas sistemáticas de preenchimento e padronizar o fluxo de envio de informes periódicos digitais (diários, mensais e balancetes) submetidos por administradores e custodiantes através do sistema CVM Web, garantindo a qualidade da base de dados aberta que alimenta o mercado financeiro.

## Escopo

O escopo do Ofício-Circular nº 6/2023/SIN disciplina as rotinas de parametrização e transmissão de dados contábeis de fundos de investimento:
* **Padronização de Arquivos Eletrônicos:** Alinhamento técnico sobre os layouts de validação e esquemas XML aceitos pelos servidores da autarquia para o recebimento de informes contábeis.
* **Rotinas de Retificação de Saldos:** Esclarecimentos sobre os procedimentos burocráticos e sistêmicos para que um administrador corrija balancetes ou valores de cotas enviados anteriormente com erros materiais.
* **Envio de Demonstrações Semestrais:** Orientações sobre o fluxo lógico de carregamento de relatórios contábeis intermediários e notas explicativas e o batimento com os dados de auditores independentes.
* **Monitoramento de Contas Passivas:** Diretrizes para a correta identificação cadastral de investidores institucionais e subclasses nas tabelas de controle de concentração de cotistas.

## Consequência operacional

* **Ajuste em Sistemas de Validação Contábil:** Os departamentos de TI de administradores e custodiantes atualizam seus códigos de validação de layouts para espelhar as travas eletrônicas de dados descritas pela SIN.
* **Bloqueio de Rejeições Sistêmicas no CVM Web:** A adequação dos arquivos de dados aos padrões exigidos pelo ofício elimina as rejeições em lote de informes diários, evitando a ocorrência de pendências cadastrais automáticas.
* **Segregação de Contas Contábeis de Classes:** Parametrização analítica nos planos de contas (COSIF) para suportar o desmembramento de despesas e receitas por classe patrimonial isolada, evitando erros de conciliação.
* **Rito Rápido de Substituição Documental:** Utilização de esteiras de retificação automatizadas para relatórios mensais antigos, dispensando a necessidade de abertura de processos físicos de justificativa perante a gerência técnica.
* **Abertura de Dados de Carteira para Auditoria:** As assets organizam suas trilhas de logs de precificação (CPC 46 / CPC 48) para comprovar a consistência dos saldos brutos declarados nos informes mensais consolidados de fim de período.

## Erros comuns

* **Tratar o Ofício de Sistemas como se alterasse Limites de Alocação:** Presumir de forma errônea que o documento modifica regras substantivas de concentração de risco, quando o seu escopo é estritamente procedimental de *envio e layout de dados*.
* **Efetuar retificações contábeis sem memória de cálculo auditável:** Alterar saldos históricos de balancetes contábeis diretamente no sistema CVM Web sem arquivar internamente as notas e papéis de trabalho que justificam matematicamente a correção perante futuras vistorias.
* **Enviar arquivos com campos de subclasses em branco ou corrompidos:** Transmitir lotes de dados em massa omitindo os novos indexadores de subclasses associadas, gerando o travamento acidental da esteira de processamento e aplicação de sanções administrativas.
* **Confundir a alçada de informes da SIN com as tabelas de securitização da SSE:** Enviar informes periódicos de companhias securitizadoras ou séries de CRIs utilizando os layouts de fundos varejo da SIN, o que resulta na invalidação do arquivo pela equipe técnica da SSE.

## Relação com outras notas

* **Comissão de Valores Mobiliários (CVM):** Autarquia federal cuja área de fiscalização de investidores institucionais utiliza as bases de dados geradas pelo ofício para calibrar seus modelos de Supervisão Baseada em Risco.
* **Ofício-Circular nº 2/2023/CVM/SIN (Obrigações Periódicas Anuais):** Relação de complemento técnico; o Ofício 02/2023/SIN traçou o *calendário geral de prazos*, enquanto o Ofício 06/2023/SIN refinou o *layout eletrônico de dados* a serem transmitidos.
* **Resolução CVM 175 (Marco dos Fundos):** A fragmentação de dados em classes e subclasses exigida pela reforma estrutural da 175 é o motivo técnico central que forçou a SIN a emitir o Ofício 06/23 para ajustar os sistemas de recepção de documentos.
* **CPC 26 (Apresentação das Demonstrações Contábeis):** Os balancetes e demonstrações financeiras transmitidos sob os layouts padronizados pelo ofício da SIN devem seguir as regras de nomenclatura e proibição de compensação de saldos brutas da norma contábil CPC 26.
