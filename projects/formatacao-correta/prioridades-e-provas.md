# FORMATAÇÃO CORRETA — prioridades operacionais e evidências
**Prioridade é ordem de ação para chegar à instalação limpa; NÃO diagnóstico de causa universal.** Se a falha é apenas histórica, não representar como presente.

| Problema | Prova já disponível | Decisão mais simples e verificável |
| --- | --- | --- |
| MemTest86 em andamento | Foto 23/09: passagem 1 concluída; 2/4 em 75%; 0 erros | Receber somente tela FINAL 4/4, registrar, não repetir |
| Firmware de segurança | Ubuntu fwupd/CHIPSEC segundo relato: Manufacturing Mode, Flash Descriptor e BootGuard | Referência de produção NM-B242 + procedimento autorizado ou encaminhamento técnico; não dizer que provocou BSOD/Store |
| Comunicação ACPI/EC/energia | Ubuntu: `_WAK`, `_PSR`, TPM CRB; Windows: Event 13/15/37/41 | Área comum entre SOs. Uma intervenção reversível e um teste funcional definidos |
| BSOD RAM | WinDbg 0x1A/0x41792; MemTest parcial 0 | Não comprar RAM por tentativa; guardar resultado final, identificar causa só com elo real |
| SATA/WD Green | WHEA histórico storahci; SMART curto aprovado; Intel RST em transição em 29/08 | Se recorrência, conferir driver ativo HOJE uma vez e corrigir divergência demonstrada |
| Store/Update/serviços | CBS 0x800F0984, AppX, logon de serviços | Corrigir somente função ainda quebrada ou definir teste de aceitação pós-instalação |
| Registro HKLM/HKCU | Auditorias de ACL/COM sem vínculo demonstrado ao firmware | Não resetar permissões por atacado; reparar chave somente com sintoma demonstrado |
| WLAN/NVIDIA | Windows Intel 3165 Event 5007; Ubuntu nvidia-smi falhou e Windows ativou GPU | Tratar se função necessária ainda falhar, sem declarar peça danificada |

**Após cada tentativa:** corrigido / não corrigido / limitação confirmada / requer especialista. Registrar o que foi feito e não repetir sem informação nova.

**Proibido como atalho não comprovado:** trocar RAM/SSD/placa-mãe, Secure Erase, zerar BIOS/PTT/PK/KEK/db/dbx, programar ME/Flash Descriptor e instalar todos os drivers mais novos.

[Plano em três fases](./execucao-em-tres-fases.md) · [Correlações](./correlacoes-windows-ubuntu.md) · [Fontes/lacunas](./fontes-e-lacunas.md).