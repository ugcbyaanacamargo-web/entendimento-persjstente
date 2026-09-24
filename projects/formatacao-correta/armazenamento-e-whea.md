# Armazenamento — WD Green, WHEA e driver SATA

**Evidência principal:** análise anterior `AUDITORIA_TOTAL_CONFRONTO_FINAL_LENOVO_80YH_20260829.md`, relativa à coleta de 29/08/2026; não substituir a análise do CPER bruto por palavras soltas do relatório.

## Resultado histórico
- Três eventos WHEA-Logger Event ID 1; relatório final diz que CPER/RawData traz `STORPORT`, `storahci`, `WD`, `Green 2.5 1000GB` (datas 22/25/26 agosto).
- Isso relaciona os **registros** à cadeia de armazenamento, mas NÃO identifica SSD fisicamente defeituoso nem prova que os três eventos causaram os erros da Store/BSOD de setembro.
- Controlador Intel SATA AHCI hardware ID terminado em `DEV_9D03`. Durante a coleta de 29/08 Intel RST 15.9.1.1018 (`iaStorA`) havia sido instalado/cadastrado, `storahci` ainda estava carregado e reinicialização pendente. **Estado transitório daquela data; pode ter mudado após os reboots.**
- SMART curto concluiu sem erros; WD Dashboard exibiu firmware 42077100 como atualizado, conforme usuário.
- **Evidência posterior: teste original SATA/PHY de 04/09**: controlador Intel 15.9.1.1018 iniciado, cinco ciclos de escrita/leitura 4 GiB, SMART examinado sem aumento e nenhum novo WHEA ou erro de armazenamento na janela do teste. [Resultados e limites](./testes-04-09-resultados.md).

## Conclusão operacional
O reboot do RST de 29/08 não é pendência atual: o controlador já consta iniciado com a versão Intel no teste posterior de 04/09. **Não reinstalar RST nem mudar modo SATA sem evidência nova.** Reabrir somente se surgirem WHEA ou sintomas atuais; o log 04/09 não prova ausência de defeito intermitente. O SSD não herda HKLM/HKCU por si próprio.

[Funil](./triagem-causal-consolidada.md) · [Projeto](./README.md) · [Plano](./plano-corretivo.md) · [Tela azul](./memoria-e-tela-azul.md) · [Fontes](./fontes-e-lacunas.md).
## Estado local atualizado pelo Codex em 23/09 ~17h30

Controlador Intel SATA AHCI DEV_9D03 com servico **iaStorAC**, driver **17.8.1.1066** (oem54.inf), PnP sem codigo de erro. E uma versao distinta da 15.9.1.1018 usada no teste de 04/09; diferenca nao e falha em si. Nenhum WHEA, disk, storahci ou iaStorA retornou na consulta filtrada de 14 dias, mas o provedor iaStorAC nao foi consultado separadamente. Nao reinstalar RST nem substituir SSD sem evidencia nova. Fonte [EV-13](./registro-de-evidencias.md).

## REABERTURA POR EVIDENCIA ATUAL 23/09 as 21h46 — nao usar conclusao historica de "estavel" (EV-31/33)

O controlador `Intel(R) 6th Generation Core Processor Family Platform I/O SATA AHCI Controller` `DEV_9D03 SUBSYS_383F17AA` esta de fato carregado com `iaStorAC 17.8.1.1066` / oem54.inf. Foi recuperado **iaStorAC EventID129 23/09/2026 21:46:19: reset de \\Device\\RaidPort0**. Um segundo depois, SCM 7009/7000: `AppXSvc` nao respondeu em 30000 ms. `Start-Service AppXSvc` em 22h19 concluiu OK e nenhum novo 129/7000/7009 apareceu no reteste pontual, logo a falha AppXSvc pode ser transitória. **A causa da coincidencia NAO esta demonstrada.** Fonte Microsoft [storage timeout Event129](https://learn.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/troubleshoot-data-corruption-and-disk-errors).

SMART via classe nativa de ATA: IDs 5=0, 187=0, 188=0, 199=0; 174=8 (em 04/09 foi 7). `Get-PhysicalDisk` relata Healthy/OK, temperatura 30 Celsius, read errors 0, firmware 42077100. Mas `MSFT_StorageReliabilityCounter.ReadLatencyMax=64138` e `WriteLatencyMax=64059` **milissegundos** (mais de 64s), anormais segundo [documentacao Microsoft](https://learn.microsoft.com/en-us/windows-hardware/drivers/storage/msft-storagereliabilitycounter): mais de 10s pode indicar disco/controlador com problema. Estes contadores nao trazem o momento exato da demora; nao afirmar que sao a mesma operacao do evento129. C: nao esta dirty; nenhum novo WHEA no filtro recente NAO contradiz evento129 (outro provedor).

**Mudanca importante:** `iaStorA 15.9.1.1018` passou teste controlado SATA/PHY em 04/09; hoje `iaStorAC 17.8.1.1066` foi encontrado num reset de porta. A Lenovo publica 15.9.1.1018 para alguns IdeaPad 320-15IKB 80XL/80YE ([DS121515](https://pcsupport.lenovo.com/bs/en/products/laptops-and-netbooks/300-series/320-touch-15ikb/downloads/ds121515)), **nao comprova suporte exato OEM Type80YH**. Intel RST 17.x inclui DEV_9D03 nos INF, assim a versao nova nao e categoricamente incompatível. Nao inferir que driver, conector, SSD ou energia individualmente causou reset sem prova adicional. **Nao executar rollback/troca do driver Boot, Secure Erase, alteracao BIOS SATA nem novo estresse de disco sem plano de recuperacao.**

[EV-31,32,33](./registro-de-evidencias.md) · [Checkpoint global](./checkpoint-remoto-23-09.md) · [Estado](../../memory/STATE.yaml).
