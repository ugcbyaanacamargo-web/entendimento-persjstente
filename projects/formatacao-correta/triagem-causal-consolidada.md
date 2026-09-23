# Funil causal — corrigir o Lenovo sem repetir exames

**Revisão:** 2026-09-23. **Objetivo:** corrigir impedimentos demonstrados, decidir o que realmente exige bancada e executar UMA instalação limpa final. Fontes com origem e limite estão no [registro de evidências](./registro-de-evidencias.md).

**Regra:** separar (1) falha observada, (2) subsistema envolvido, (3) causa confirmada, (4) próxima decisão. A mesma palavra “segurança” em Ubuntu e Windows NÃO significa a mesma falha.

| Caso | O que foi demonstrado | O que já diminuiu a suspeita / mudou desde então | Decisão prática |
| --- | --- | --- | --- |
| Memória / tela azul de 23/09 | Dump WinDbg: MEMORY_MANAGEMENT 0x1A, 0x41792, corrupção de PTE, bucket ONE_BIT. Não identificou autor. | MemTest86 11.7 Free **PASS final relatado em 23/09**; fotos na quarta passagem mostravam zero erros até 66%. Diagnóstico Lenovo pelo pendrive já havia passado. | Marcar teste de RAM concluído. **NÃO trocar pente** ou repetir MemTest por inércia. Duas ocorrencias ja existem, em 05/09 e 23/09. WinDbg posterior analisou ambas e o dump completo, sem identificar escritor da PTE; nao repetir WinDbg nem esperar terceira falha por inercia. Preparar isolamento seletivo reversivel apenas apos definir backup/recuperacao e obter autorizacao. |
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
## Atualizacao apos coleta local do Codex em 23/09 (~17h30)

- **Energia - ativo:** 19 Event 37 novos entre 11 e 23/09, quatro no dia 23; ultimo por volta de 16h40. O teste de 04/09 apenas nao reproduziu a falha naquela janela. Proxima decisao: correlacionar com uso na tomada e lentidao percebida; nao afirmar que causou BSOD.
- **SATA - sem falha atual identificada:** controlador DEV_9D03 agora em servico iaStorAC, INF oem54, versao 17.8.1.1066. Nenhum WHEA/disk/storahci/iaStorA nos filtros de 14 dias. Nao alterar o driver por diferenca com 04/09.
- **Tela azul - relatorio INTERMEDIARIO substituido:** os dumps existiam; uma chamada COMPOSTA da ferramenta foi recusada. A analise POSTERIOR pelo WinDbgX foi concluida no mesmo dia nos tres dumps, conforme adendo abaixo; PTE corrompida, autor ainda desconhecido.
- **Windows - erros distintos:** AppX 0x80073D02 por aplicativos abertos; PowerShell AppModel 0x80070005; Store 0x80072ee7; Energy Server Service queencreek Event 7034. Nao agrupar em uma unica causa.
- **Firmware de seguranca - ainda nao medido:** BIOS 4WCN47WW, Secure Boot ativo e TPM pronto nao determinam Manufacturing Mode, Flash Descriptor e BootGuard.

Fonte: [EV-12 a EV-14](./registro-de-evidencias.md). Este novo achado prevalece sobre a suposicao anterior de que os Event 37 nao teriam retornado apos 04/09.

## Adendo conclusivo da ETAPA WinDbg — 23/09, EV-19 e EV-20

- Foram examinados com WinDbgX os minidumps 05/09 e 23/09, mais `MEMORY.DMP` de 23/09: mesmo `MEMORY_MANAGEMENT 0x1A / 0x41792`, `MEMORY_CORRUPTION_ONE_BIT` e hash do bucket. No 23/09/full, a corrupcao foi DETECTADA em `nt!MiDeletePagablePteRange` durante liberacao de memoria de `msedge.exe`; NAO se viu quem a escreveu. No 05/09, simbolos locais insuficientes limitam a pilha. **Nao pedir novamente a analise dos mesmos dumps**.
- `verifier /query`: nenhum driver verificado. Nao foi aplicado Driver Verifier, que pode causar BSOD ou loop de boot; preparar antes selecao de drivers de terceiros, backup e recuperacao, com autorizacao especifica para eventual execucao.
- Seguranca Intel ME/Flash Descriptor/BootGuard continua outro caso sem medicao atual; nao inferir causa da PTE. Event37 e BTHUSB17 sao trilhas independentes, nao descartar. **A resposta global do projeto permanece multiplas frentes com resultados diferentes, nao uma hipotese universal.**

[Etapa WinDbg](./memoria-e-tela-azul.md) · [Confronto global](./confronto-global-23-09.md) · [EV-19/20](./registro-de-evidencias.md).