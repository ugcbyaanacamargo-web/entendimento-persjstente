# Grafo de entendimento — relação NÃO é causa automática

| Achado A | Tipo de relação | Achado B | Decisão |
| --- | --- | --- | --- |
| Ubuntu FWTS ACPI _WAK/_PSR | mesmo-subsistema | Windows EC Event 13/15, CPU Event 37 | Corrigir/validar energia e interface firmware–SO, sem declarar que uma mensagem causou outra |
| Ubuntu CSME Manufacturing Mode/Flash | mesmo-subsistema | Windows MEI Event 4 | Segurança firmware e comunicação ME são questões distintas |
| Ubuntu TPM Bad ACPI memory layout | coexiste-com | Windows reconhece PTT pronto | Não limpar TPM para alterar tabela ACPI |
| Ubuntu nvidia-smi falhou | contrasta-com | Windows ativou 940MX em 3D | Investigar driver/perfil Linux quando necessário, não trocar GPU |
| Windows BSOD 0x1A/0x41792 | causa-nao-demonstrada | Manufacturing Mode/BootGuard | Não prometer que fechar modo de fábrica cura tela azul |
| Windows WHEA storahci/WD Green | não-equivalente-a | SMART curto aprovado | Erros diferentes medem coisas diferentes; não declarar SSD avariado |
| Ubuntu permissões/segurança | implementação-diferente | HKLM/HKCU Windows | Linux não utiliza Registro do Windows |

**Ao inserir novo achado:** atualizar a aresta apropriada com fonte, data e limite; só marcar `corrigido-por` após executar e validar correção.

[Estado](./estado-atual.md) · [Evidências](./registro-de-evidencias.md) · [Correlações](./correlacoes-windows-ubuntu.md).