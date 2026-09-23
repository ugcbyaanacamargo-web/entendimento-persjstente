# Grafo de entendimento — relação NÃO é causa automática

| Achado A | Tipo de relação | Achado B | Decisão |
| --- | --- | --- | --- |
| Ubuntu FWTS ACPI _WAK/_PSR | mesmo-subsistema | Windows EC Event 13/15, CPU Event 37 | Corrigir/validar energia e interface firmware–SO, sem declarar que uma mensagem causou outra |
| Ubuntu CSME Manufacturing Mode/Flash | mesmo-subsistema | Windows MEI Event 4 | Segurança firmware e comunicação ME são questões distintas |
| Ubuntu TPM Bad ACPI memory layout | coexiste-com | Windows reconhece PTT pronto | Não limpar TPM para alterar tabela ACPI |
| Ubuntu nvidia-smi falhou | contrasta-com | Windows ativou 940MX em 3D | Investigar driver/perfil Linux quando necessário, não trocar GPU |
| Windows BSOD 0x1A/0x41792 | causa-nao-demonstrada | Manufacturing Mode/BootGuard | Não prometer que fechar modo de fábrica cura tela azul |
| Windows WHEA storahci/WD Green, agosto | atualizado-por | Teste SATA/PHY 04/09 com controlador Intel iniciado, sem novos eventos storage na janela | Não tratar reboot RST de agosto como pendente nem SSD como avariado por inferência |
| Windows Event 37 e ACPI 13/15 de agosto | atualizado-por | Stress 04/09 sem novos eventos-alvo na janela | Não afirmar limitação constante da CPU; preservar eventos históricos |
| BSOD 0x1A em 23/09 | não-determinado-por | MemTest86 final PASS conforme relato | RAM testada sem defeito detectado pelo exame; autor do bit corrompido segue desconhecido |
| Ubuntu permissões/segurança | implementação-diferente | HKLM/HKCU Windows | Linux não utiliza Registro do Windows |

**Ao inserir novo achado:** atualizar a aresta apropriada com fonte, data e limite; só marcar `corrigido-por` após executar e validar correção.

[Estado](../../memory/STATE.yaml) · [Evidências](./registro-de-evidencias.md) · [Correlações](./correlacoes-windows-ubuntu.md).