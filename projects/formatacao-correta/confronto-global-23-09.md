# Confronto GLOBAL de falhas — 23/09/2026

**Origem efetivamente consultada:** arquivo ZIP original `DIAGNOSTICO_TELA_AZUL_20260923_032222.zip` com os DOIS minidumps brutos, `RELATORIO_COMPLETO.txt`; `WHEA_FATAL_DETALHADO_20260905_073818.txt` com três CPER brutos; `DIAGNOSTICO_DIRETO_LENOVO.md` do Codex; `Markdown(1).md colado` (WinDbg 23/09); auditoria 29/08; checkpoint pós-reboot RST e testes de 04/09; memória documental Ubuntu/fwupd/CHIPSEC/FWTS. O acesso à URL de chat privado não equivale a acesso ao histórico integral daquela conversa: registrar somente conteúdo recuperado.

## DESCOBERTA NOVA — duas falhas com a MESMA assinatura

Leitura direta dos cabeçalhos dos dois arquivos de minidump reais no ZIP (assinatura `PAGEDU64`, bugcheck em 0x38, argumentos em 0x40/0x48/0x50/0x58):

| Data / nome no ZIP | Bugcheck | Arg1 | Arg2 (PTE) | Arg3 | Arg4 |
| --- | --- | --- | --- | --- | --- |
| 05/09 — `090526-19265-01.dmp` | `0x1A` | `0x41792` | `0xffff973ffe92bb80` | `0x8000000000` | `0x0` |
| 23/09 — `092326-11734-01.dmp` | `0x1A` | `0x41792` | `0xffffca8034e78b80` | `0x8000000000` | `0x0` |

**Conclusão estrita:** há RECORRÊNCIA da mesma CLASSE de corrupção de PTE e do mesmo valor de Arg3/Arg4 em incidentes distintos, mas **PTE em endereços diferentes**. Não declarar que o mesmo driver ou peça causou ambos sem analisar as pilhas e lista de drivers. Microsoft explica 0x41792: https://learn.microsoft.com/pt-br/windows-hardware/drivers/debugger/bug-check-0x1a--memory-management.

O WinDbg já analisou o dump de 23/09 no arquivo `Markdown(1).md colado`; o relatório do Codex que apenas copiou o BugCheck NÃO substitui a análise já feita. O dump de 05/09 ainda demanda confronto orientado entre os dois se a saída WinDbg correspondente não existir.

## WHEA / armazenamento — não fundir com BSOD

Três CPER originais, Event ID 1 de 22, 25, 26/08: strings `STORPORT`, `storahci`, `WD Green 2.5 1000GB`. Arquivo original bruto foi entregue em 23/09. São três ocorrências no CAMINHO SATA/storage histórico, não prova de SSD fisicamente ruim ou causa comprovada dos dois 0x1A. Checkpoint pós-reboot 04/09 documentou explicitamente `\\Driver\\iaStorA` ativo, storahci parado, reboot pendente FALSE e zero WHEA desde boot de 30/08. Teste SATA/PHY 04/09 completou cinco ciclos sem novos erros durante janela. Codex 23/09 observou nova versão `iaStorAC 17.8.1.1066`, PnP OK e nenhum WHEA/storage na consulta filtrada.

## ACPI / EC / energia — indícios repetidos entre SOs

Ubuntu relatou erros de `_WAK`, `_PSR`, TPM CRB e firmware ACPI. Windows 29/08: EC ACPI 13/15 e Event37. Teste 04/09 não reproduziu; Codex encontrou NOVOS 19 Event37 entre 11 e 23/09. O relatório completo da coleta de BSOD tem Event37 às 03h20 **após reinício por falha** (~03h19), portanto NÃO usar esse evento posterior como causa temporal do crash anterior. O Event37 também pode ser aviso sobre processador lógico específico, sem provar 19 ciclos independentes de limitação ou temperatura/fonte culpada.

## Bluetooth — omitido anteriormente

O `RELATORIO_COMPLETO.txt` anexo traz **BTHUSB Event17 (erro, 20/09 19h15): adaptador local falhou e o driver foi descarregado**. Traz também Event34 na inicialização de 23/09 (limitação de papel Bluetooth Low Energy como periférico). Event17 é falha concreta e distinta de Event34, que descreve capacidade ausente. A máquina possui Intel AC3165 Wi-Fi/Bluetooth; histórico adicional de **22 Netwtw04 Event5007** em agosto indica falha operacional da pilha Wi-Fi naquela data, sem prova de mesma causa física ou de persistência da WLAN hoje. PnP sem erro no snapshot 23/09 NÃO apaga falhas históricas/intermitentes.

## BSOD pós-boot — não confundir ordem dos eventos

No log da coleta: BugCheck WER1001 às ~03h22, boot/KernelPower41 às ~03h19 e Event37 às ~03h20; DCOM10016 às ~03h21-22. **WHEA antigo não aparece nessa janela.** `volmgr 161` (falha de criação de dump) aparece no reinício, mas existem minidump e MEMORY.DMP registrados — pode referir a outra tentativa/tipo de dump, não concluir que não houve dump. BTHUSB Event34 às ~03h19 não foi demonstrado como autor da corrupção.

## Windows / Store e serviço — trilha independente

AppX 0x80073D02 foi explicitamente bloqueado por apps em execução; PowerShell empacotado 0x80070005 em AppModel, Store 0x80072ee7 (comunicação), Energy Server Service queencreek 7034, uhssvc 7000 histórico, ScreenClippingHost exception 0xc000027b em 17/09, WSL LxssManager Stop Pending em coleta específica. Primeiro WHEA 22/08 pouco após instalação Windows 22/08; não deduzir que o chipset criou arquivos CBS faltando. Os erros têm correções distintas e precisam de validação da função hoje.

## Firmware de segurança — caso persistente separado

Ubuntu/fwupd/CHIPSEC relatou ME/CSME Manufacturing Mode, Flash Descriptor override/lock, BootGuard/HSI. Windows confirma BIOS 4WCN47WW, Secure Boot ligado e TPM/PTT pronto; **NENHUMA dessas consultas confere os três controles do Intel ME/BootGuard**. Sem CHIPSEC/FWTS originais e baseline OEM NM-B242 não declarar qualquer reflash/limpeza seguro. fwupd: https://fwupd.github.io/libfwupdplugin/hsi.html.

## CORREÇÃO NO FUNIL E AÇÃO ÚNICA

A próxima ação NÃO é perguntar somente sobre lentidão nem executar outra auditoria geral. É **comparar o relatório WinDbg já existente do incidente 23/09 ao dump de 05/09** (dois com 0x1A/0x41792) usando os ARQUIVOS QUE JÁ ESTÃO NO ZIP. Se o arquivo `C:\\Windows\\Minidump\\092326-11734-01.dmp` não existir mais, abrir as cópias em pasta de diagnóstico Desktop criada pela coleta OU extrair o ZIP para uma pasta local e abrir o .dmp extraído por WinDbg; não reinstalar ou coletar outro dump. Não tomar decisões de RAM/SSD/BIOS pelo resultado isolado. Após cruzar os dois, continuar trilhas independentes ACPI/EC; Bluetooth/WLAN; firmware; Windows AppX.

[Provas](./registro-de-evidencias.md) · [Tela azul](./memoria-e-tela-azul.md) · [Funil](./triagem-causal-consolidada.md) · [Estado](../../memory/STATE.yaml).