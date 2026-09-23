# Linha do tempo de intervenções — FORMATAÇÃO CORRETA

**Tipo:** memória temporal; o estado de uma data não é automaticamente o estado de hoje.

| Momento | Registro |
| --- | --- |
| Antes de 22/08/2026 | Usuário relata tentativas com Windows 11 e **Ubuntu instalado como sistema operacional**, ambos com problemas. Ubuntu NÃO foi apenas pendrive de formatação. Datas exatas dessas instalações não recuperadas aqui. |
| Ubuntu 24.04 | FWTS, fwupd/HSI e CHIPSEC reportaram achados de firmware, ACPI/TPM e NVIDIA; veja [firmware](./firmware-seguranca.md) e [ACPI](./acpi-ec-energia-tpm.md). |
| 22/08/2026 | Windows 10 Home Single Language 22H2 instalado pelo pendrive. Há relatos de erros no início, inclusive manutenção de componentes Windows 0x800F0984. |
| 22–26/08 | Relatório posterior descreveu três WHEA Event 1; strings CPER remetiam à cadeia WD Green/SATA/StorPort/storahci. |
| 29/08 | Auditorias de energia, EC, WLAN, firmware e drivers. Intel RST cadastrado e reinicialização pendente **naquela data**; não presumir que persiste. |
| 05/09 | Falhas registradas de serviços de sistema/áudio/AppX e virtualização. |
| 12/09 | Auditoria DCOM e permissões: evento 10016 recorrente, proprietário TrustedInstaller para CLSID/APPID examinados. |
| 16–18/09 | Reparos Windows/Store/AppX e atualização do PowerShell; falha da Ferramenta de Captura não encerrada pelo relato. |
| 23/09 | Dump de BSOD MEMORY_MANAGEMENT 0x1A/0x41792; MemTest86 iniciado. Foto mais recente disponível: 2/4, 75% da passagem 2, 0 erros; final não apresentado. |

**Atenção:** diagnósticos Lenovo e SMART curto já haviam sido executados sem erros encontrados. Não reinscrever como tarefas pendentes.

[Projeto](./README.md) · [Fontes e lacunas](./fontes-e-lacunas.md).