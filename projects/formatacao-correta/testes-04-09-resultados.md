# Testes de 04/09/2026 recuperados

**Proveniência:** arquivos originais de anexos anteriores `TESTE_SATA_PHY_20260904_230509.txt` e `STRESS_EVENT37_80YH.txt`, consultados em 23/09. Não enviar os logs brutos a este repositório público: podem conter identificadores.

## SSD e SATA
No teste SATA/PHY de 04/09, o controlador AHCI Intel (DEV_9D03) consta iniciado com driver de dispositivo **15.9.1.1018**. Foram executados **cinco ciclos de aproximadamente 4 GiB escritos e lidos** (aprox. 20 GiB de escrita + 20 GiB de leitura). Os contadores SMART 174 e 199 examinados **não aumentaram**. Não foram observados novos WHEA ou erros de armazenamento **na janela do teste**.

Isso atualiza o retrato de **29/08**, quando Intel RST acabara de ser cadastrado e ainda aguardava reinicialização. O teste de 04/09 não confirma isoladamente a pilha kernel exata, mas impede tratar aquele reboot antigo como etapa pendente atual. O resultado não torna o SSD imune a falhas futuras.

## Energia / CPU
No teste controlado `STRESS_EVENT37_80YH.txt` de **04/09 23:02–23:23**, ocorreram **oito ciclos de carga e repouso**, conectado à tomada; resultado `Trigger: False`. O relatório final não trouxe novos Event 37, WHEA nem ACPI 13/15 naquele intervalo. Não invalida os eventos históricos de agosto, mas **não sustenta dizer que a CPU estava permanentemente limitada**.

## Consequência no plano
Estes dois testes estão **concluídos**, não são novas tarefas. Reabrir SSD/energia apenas diante de novo evento/sintoma específico ou comparação indispensável para uma intervenção. Não reinstalar Intel RST nem repetir stress por rotina.

[Funil causal](./triagem-causal-consolidada.md) · [Armazenamento](./armazenamento-e-whea.md) · [Energia](./acpi-ec-energia-tpm.md) · [Evidências](./registro-de-evidencias.md).