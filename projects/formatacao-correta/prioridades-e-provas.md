# FORMATAÇÃO CORRETA — prioridades operacionais e evidências
**Prioridade é ordem de ação para chegar à instalação limpa; NÃO diagnóstico de causa universal.** Se a falha é apenas histórica, não representar como presente.

| Problema | Prova já disponível | Decisão mais simples e verificável |
| --- | --- | --- |
| MemTest86 concluído | PASS final relatado em 23/09; fotos até quarta passagem com 0 erros acumulados | **Encerrar etapa, não pedir fotografia nem repetir RAM por rotina; BSOD ainda requer causa própria** |
| Firmware de segurança | Ubuntu fwupd/CHIPSEC segundo relato: Manufacturing Mode, Flash Descriptor e BootGuard | Referência de produção NM-B242 + procedimento autorizado ou encaminhamento técnico; não dizer que provocou BSOD/Store |
| Comunicação ACPI/EC/energia | Ubuntu: `_WAK`, `_PSR`, TPM CRB; Windows: Event 13/15/37/41 históricos; teste 04/09 sem novos eventos | Área comum entre SOs. Uma intervenção reversível e um teste funcional definidos |
| BSOD RAM | WinDbg 0x1A/0x41792; MemTest PASS relatado | Não comprar RAM por tentativa; guardar resultado final, identificar causa só com elo real |
| SATA/WD Green | WHEA histórico storahci; SMART curto aprovado; Intel RST em transição EM 29/08; teste SATA de 04/09 sem novos eventos | Não repetir teste nem reboot de agosto; só reabrir se houver falha nova |
| Store/Update/serviços | CBS 0x800F0984, AppX, logon de serviços | Corrigir somente função ainda quebrada ou definir teste de aceitação pós-instalação |
| Registro HKLM/HKCU | Auditorias de ACL/COM sem vínculo demonstrado ao firmware | Não resetar permissões por atacado; reparar chave somente com sintoma demonstrado |
| WLAN/NVIDIA | Windows Intel 3165 Event 5007; Ubuntu nvidia-smi falhou e Windows ativou GPU | Tratar se função necessária ainda falhar, sem declarar peça danificada |

**Após cada tentativa:** corrigido / não corrigido / limitação confirmada / requer especialista. Registrar o que foi feito e não repetir sem informação nova.

**Proibido como atalho não comprovado:** trocar RAM/SSD/placa-mãe, Secure Erase, zerar BIOS/PTT/PK/KEK/db/dbx, programar ME/Flash Descriptor e instalar todos os drivers mais novos.

[Funil](./triagem-causal-consolidada.md) · [Plano em três fases](./execucao-em-tres-fases.md) · [Correlações](./correlacoes-windows-ubuntu.md) · [Fontes/lacunas](./fontes-e-lacunas.md).