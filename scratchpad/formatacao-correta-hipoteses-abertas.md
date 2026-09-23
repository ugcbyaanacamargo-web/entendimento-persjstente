# FORMATAÇÃO CORRETA — hipóteses abertas (não fatos)

**Revisão:** 2026-09-23. Notas de trabalho: atualizar apenas com nova evidência. Retornar a [projeto](../projects/formatacao-correta/README.md).

| Hipótese | Evidência favorável | O que impede encerrar como causa |
| --- | --- | --- |
| Há problema compartilhado de interface firmware/ACPI nos SOs | Ubuntu: erros ACPI; Windows: EC Event 13/15 e Event 37 | Não há relação temporal/causal demonstrada para cada falha ou BSOD |
| CSME em Manufacturing Mode aberto ainda hoje | Ubuntu fwupd/CHIPSEC reportaram | Falta saída original/estado atual + referência Lenovo exata; não confundir segurança com estabilidade |
| O erro BSOD 0x1A veio de driver/firmware | Windows detectou PTE corrompida, existência de falhas de plataforma | Dump não identificou escritor; MemTest final pendente |
| SSD/controlador SATA explicam erros de atualização | WHEA antigo cita storahci/WD Green | Sem demonstração de arquivos perdidos causados por WHEA e sem equivalência Ubuntu |
| HKLM/HKCU antigos sobreviveram aos três SOs | Nenhuma demonstração | Instalação realmente limpa cria registros novos; Linux não usa Registro Windows |

**Não ranquear ou recomendar troca/flash sem prova.** Uma hipótese rejeitada deve ficar marcada como rejeitada para não reaparecer.