# diagnostico-fila-impressao

## Descrição do Problema

Ferramenta para priorizar e diagnosticar filas de impressão congestionadas em ambientes corporativos, identificando quais filas precisam de intervenção imediata.

## Requisitos

* Receber dados das filas (nome, documentos pendentes, erro ativo)
* Classificar a criticidade da fila
* Exibir relatório resumido

## Exemplo de Uso

Entrada: ["Impressora_RH", 15, true]
Saída: IMPRESSORA_RH | CRITICA | 15 docs | ERRO