# Registro de evidências — origem, data e limite

| ID | Fonte | Dado documentado | Força e limite |
| --- | --- | --- | --- |
| EV-01 | Usuário transcreveu achados Ubuntu 24.04, em 23/09 | fwupd/CHIPSEC: Manufacturing Mode, flash, BootGuard | Não é releitura do arquivo bruto CHIPSEC/FWTS |
| EV-02 | Usuário transcreveu FWTS Ubuntu | TPM CRB, _WAK, _PSR, outros ACPI | Códigos relatados; não concluir causalidade geral |
| EV-03 | Auditoria anterior de coleta Windows 29/08 | ACPI Event 13/15, CPU Event 37, WHEA/storage, WLAN | Análise histórica, ZIP bruto não publicado aqui |
| EV-04 | Texto de saída WinDbg de dump em 23/09 | MEMORY_MANAGEMENT 0x1A/0x41792 ONE_BIT | Confirma estrutura corrompida; não identifica agente causador |
| EV-05 | Foto enviada 23/09 | MemTest86 passagem 1 concluída, 2ª em 75%, erros 0 | **Resultado final das quatro passagens não fornecido** |
| EV-06 | Usuário confirmou | Diagnóstico Lenovo pendrive e SMART curto concluídos sem erros | Não repetir automaticamente |
| EV-07 | Auditoria DCOM/permissões 12/09 | RuntimeBroker/TrustedInstaller, Event 10016 | Não prova corrupção do Registro |

**Ingestão:** usar [procedimento](../../runbooks/ingestao-de-resultados.md), preservar observações antigas, acrescentar nova evidência sem dados privados, atualizar [estado](./estado-atual.md).

[Projeto](./README.md) · [Fontes e lacunas](./fontes-e-lacunas.md).