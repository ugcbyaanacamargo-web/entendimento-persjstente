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
