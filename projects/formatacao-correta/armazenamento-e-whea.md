# Armazenamento — WD Green, WHEA e driver SATA

**Evidência principal:** análise anterior `AUDITORIA_TOTAL_CONFRONTO_FINAL_LENOVO_80YH_20260829.md`, relativa à coleta de 29/08/2026; não substituir a análise do CPER bruto por palavras soltas do relatório.

## Resultado histórico
- Três eventos WHEA-Logger Event ID 1; relatório final diz que CPER/RawData traz `STORPORT`, `storahci`, `WD`, `Green 2.5 1000GB` (datas 22/25/26 agosto).
- Isso relaciona os **registros** à cadeia de armazenamento, mas NÃO identifica SSD fisicamente defeituoso nem prova que os três eventos causaram os erros da Store/BSOD de setembro.
- Controlador Intel SATA AHCI hardware ID terminado em `DEV_9D03`. Durante a coleta de 29/08 Intel RST 15.9.1.1018 (`iaStorA`) havia sido instalado/cadastrado, `storahci` ainda estava carregado e reinicialização pendente. **Estado transitório daquela data; pode ter mudado após os reboots.**
- SMART curto concluiu sem erros; WD Dashboard exibiu firmware 42077100 como atualizado, conforme usuário.

## Conclusão operacional
Não instalar Intel RST em cima do atual nem mudar modo SATA até saber qual driver controla o dispositivo HOJE e se novas falhas do mesmo tipo ocorreram; se não há falha atual, registrar histórico e não reabrir por inércia. O SSD não herda HKLM/HKCU por si próprio.

[Projeto](./README.md) · [Plano](./plano-corretivo.md) · [Tela azul](./memoria-e-tela-azul.md) · [Fontes](./fontes-e-lacunas.md).