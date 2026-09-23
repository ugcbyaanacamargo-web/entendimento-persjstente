# Funil causal — corrigir o Lenovo sem repetir exames

**Revisão:** 2026-09-23. **Objetivo:** corrigir impedimentos demonstrados, decidir o que realmente exige bancada e executar UMA instalação limpa final. Fontes com origem e limite estão no [registro de evidências](./registro-de-evidencias.md).

**Regra:** separar (1) falha observada, (2) subsistema envolvido, (3) causa confirmada, (4) próxima decisão. A mesma palavra “segurança” em Ubuntu e Windows NÃO significa a mesma falha.

| Caso | O que foi demonstrado | O que já diminuiu a suspeita / mudou desde então | Decisão prática |
| --- | --- | --- | --- |
| Memória / tela azul de 23/09 | Dump WinDbg: MEMORY_MANAGEMENT 0x1A, 0x41792, corrupção de PTE, bucket ONE_BIT. Não identificou autor. | MemTest86 11.7 Free **PASS final relatado em 23/09**; fotos na quarta passagem mostravam zero erros até 66%. Diagnóstico Lenovo pelo pendrive já havia passado. | Marcar teste de RAM concluído. **NÃO trocar pente** ou repetir MemTest por inércia. Se tela azul voltar, usar ocorrência nova para distinguir driver/dispositivo, RAM/controlador e energia. |
| SSD / Intel SATA | Relatório da coleta 29/08: três WHEA CPER associados à cadeia StorPort/storahci/WD Green. No mesmo snapshot iaStorA instalado e reboot ainda pendente. | **Teste original de 04/09**: controlador Intel 15.9.1.1018 iniciado, cinco ciclos 4 GiB escrita/leitura, SMART observado sem aumento, sem WHEA/erro storage no período. | Não tratar reboot de agosto como pendente ou recomendar substituir SSD; reabrir só com falha nova. |
| Energia / EC / ACPI | Ubuntu FWTS relatado: _WAK, _PSR, TPM CRB e outras inconsistências. Windows 29/08: EC 13/15, Event 37, dois Kernel-Power 41. | **Teste original 04/09**: oito ciclos carga/repouso conectado à tomada, nenhum novo Event 37, WHEA ou ACPI 13/15. | Área comum de investigação, mas sem “CPU sempre limitada” nem causa física provada. Corrigir apenas sintoma reproduzido. |
| Segurança de firmware | Ubuntu fwupd/CHIPSEC, segundo relato detalhado: CSME Manufacturing Mode, proteção Flash Descriptor, BootGuard sem validação e HSI baixo. | BIOS na versão 4WCN47WW e TPM/PTT reconhecido no Windows **não comprovam** que a configuração interna está correta. Arquivos brutos Ubuntu ainda não recuperados aqui. | **Próxima decisão documental:** comparar resultados originais e suporte OEM ao Type 80YH/NM-B242; definir procedimento Lenovo comprovado ou assistência especializada. Não regravar ME/BIOS, mexer nos fuses, limpar TPM ou apagar chaves UEFI por tentativa. |
| Windows Store / permissões / serviços | Logs Windows de AppX, instalador WSL e falha ScreenClippingHost; avisos DCOM/ACL em recortes históricos. | Não há Registro HKLM/HKCU no Ubuntu; mudanças permissivas no Linux são mecanismos diferentes. Reparos feitos em setembro precisam ser julgados pela função que persiste quebrada. | Tratar após definição da plataforma e durante o aceite da instalação; sem resetar permissões de toda Classes/COM. |
| NVIDIA | Ubuntu: nvidia-smi falhava; Windows: GeForce 940MX ativou em teste 3D. | Comportamento distinto por sistema e configuração Optimus; nenhuma prova de dano físico. | Somente reabrir se a função necessária falhar; não trocar GPU. |
| Wi-Fi | Windows 29/08: Intel AC3165 22 eventos Netwtw04 5007 na auditoria histórica. | Sem prova de recorrência contemporânea ou homólogo Linux recuperado. | Verificar apenas com sintoma novo; um driver por alteração, nunca pacote de todos os drivers. |

## Driver adicional documentado, sem condenação precipitada
A listagem de drivers do Windows inclui `ROOT/PAWNIO` com `pawnio.inf` versão 2.2.0.0, identificado como iniciado no instante da coleta. **Não consta identificado como autor no WinDbg**; só entra na verificação de programas com acesso de baixo nível se houver nova tela azul ou reprodução específica. [Evidência EV-11](./registro-de-evidencias.md).

## Passos já encerrados
MemTest86 PASS relatado; teste diagnóstico Lenovo pendrive; SMART curto WD; teste SATA/PHY 04/09; stress CPU/Event37 04/09. **Não abrir novo diagnóstico geral nem repetir esses exames sem novo fato.**

## O que faltará antes de formatar
1. Decisão limitada e objetiva sobre **segurança do firmware** — o que pode ser corrigido por pacote/procedimento Lenovo, o que é implementação de fábrica, e o que exige assistência. Ausência do arquivo CHIPSEC/FWTS bruto impede um veredito final sobre cada proteção.
2. Fechar sintomas **ativos**, se algum existir após os testes/reparos, com uma única prova e uma correção por vez.
3. Backup verificado e autorização expressa antes de excluir partições. Instalação final com mídia oficial e checagem de funcionamento, sem promessa de zero erros eternos.

[STATE oficial](../../memory/STATE.yaml) · [Resultados 04/09](./testes-04-09-resultados.md) · [Origem e lacunas](./fontes-e-lacunas.md) · [Plano em 3 fases](./execucao-em-tres-fases.md).