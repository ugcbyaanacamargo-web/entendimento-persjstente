# Registro de evidências — origem, data e limite

| ID | Fonte | Dado documentado | Força e limite |
| --- | --- | --- | --- |
| EV-01 | Usuário transcreveu achados Ubuntu 24.04, em 23/09 | fwupd/CHIPSEC: Manufacturing Mode, flash, BootGuard | Não é releitura do arquivo bruto CHIPSEC/FWTS |
| EV-02 | Usuário transcreveu FWTS Ubuntu | TPM CRB, _WAK, _PSR, outros ACPI | Códigos relatados; não concluir causalidade geral |
| EV-03 | Auditoria anterior de coleta Windows 29/08 | ACPI Event 13/15, CPU Event 37, WHEA/storage, WLAN | Análise histórica, ZIP bruto não publicado aqui |
| EV-04 | Texto de saída WinDbg de dump em 23/09 | MEMORY_MANAGEMENT 0x1A/0x41792 ONE_BIT | Confirma estrutura corrompida; não identifica agente causador |
| EV-05 | Foto enviada 23/09 | MemTest86: fotos mostram progressão até 4ª passagem em 66%, erros acumulados 0 | Foto final não disponível |
| EV-06 | Usuário confirmou | Diagnóstico Lenovo pendrive e SMART curto concluídos sem erros | Não repetir automaticamente |
| EV-07 | Auditoria DCOM/permissões 12/09 | RuntimeBroker/TrustedInstaller, Event 10016 | Não prova corrupção do Registro |
| EV-08 | Usuário informou em 23/09, após voltar ao computador | MemTest86 v11.7 Free terminou com **PASS**; teste configurado para 4 passagens | Resultado final comunicado por texto; contagem final numérica de erros não foi transcrita nem fotografada. Fotos durante 4ª passagem registraram 0 erros |
| EV-09 | Arquivo original TESTE_SATA_PHY_20260904_230509.txt, recuperado de anexos anteriores | Teste 04/09: 5 ciclos de 4 GiB escritos/lidos, controlador Intel SATA iniciado com driver 15.9.1.1018; SMART 174/199 sem aumento; sem novos WHEA/erros Disk/SATA no intervalo | Teste posterior ao snapshot de 29/08; não prova inexistência de defeitos intermitentes nem confirma por si a pilha kernel ativa |
| EV-10 | Arquivo original STRESS_EVENT37_80YH.txt, recuperado de anexos anteriores | Teste 04/09: 8 ciclos carga/repouso na tomada; Trigger False; sem novos Event 37, WHEA ou ACPI 13/15 durante a execução | Não apaga os eventos históricos de agosto nem demonstra ausência de falha fora da janela |
| EV-11 | Anexo pasted.txt com enumeração PnP de drivers Windows | Dispositivo ROOT/PAWNIO, driver pawnio.inf, versão 2.2.0.0, exibido como iniciado na captura | Não foi identificado no dump como autor de corrupção de memória; candidato somente se houver nexo comprovado |

**Ingestão:** usar [procedimento](../../runbooks/ingestao-de-resultados.md), preservar observações antigas, acrescentar nova evidência sem dados privados, atualizar [estado](../../memory/STATE.yaml).

[Projeto](./README.md) · [Fontes e lacunas](./fontes-e-lacunas.md).