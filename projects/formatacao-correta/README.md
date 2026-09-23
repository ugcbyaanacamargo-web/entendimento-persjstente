# FORMATAÇÃO CORRETA — centro de entendimento e correção

**Equipamento:** Lenovo IdeaPad 320-15IKB / Type 80YH / NM-B242. **Atualizado:** 2026-09-23.  
**OBJETIVO FINAL:** tratar impedimentos demonstrados na plataforma e então realizar **UMA instalação limpa final pelo pendrive**, com drivers controlados e validação de uso real. Nada de formatar por tentativa ou substituir peça sem razão.

**Para o usuário leigo:** uma ação por vez; agente decide e confere a saída. [Roteiro em 3 fases](./execucao-em-tres-fases.md) e [prioridades](./prioridades-e-provas.md).

## Comece nesta ordem
1. [Inventário/testes já realizados](../../context/lenovo-80yh-inventario-e-testes.md).
2. [Linha do tempo](./linha-do-tempo.md): o que foi feito e quando.
3. [Correlações Windows ↔ Ubuntu](./correlacoes-windows-ubuntu.md): correspondências reais versus coincidências.
4. [Execução em três fases](./execucao-em-tres-fases.md), [prioridades e provas](./prioridades-e-provas.md) e [plano de casos](./plano-corretivo.md).
5. [Fontes, ausências e conflitos](./fontes-e-lacunas.md): não confundir relatório anterior com prova direta.

## Notas por assunto
| Assunto | Nota | Estado |
| --- | --- | --- |
| **Roteiro operacional para a instalação final** | [execucao-em-tres-fases.md](./execucao-em-tres-fases.md) | Ações limitadas para chegar à meta |
| **Prioridades / evidências** | [prioridades-e-provas.md](./prioridades-e-provas.md) | Resolver o que é plausível e comprovável |
| Firmware de segurança / CSME | [firmware-seguranca.md](./firmware-seguranca.md) | Ubuntu reportou anomalias; requer procedimento específico |
| ACPI, EC, energia e TPM | [acpi-ec-energia-tpm.md](./acpi-ec-energia-tpm.md) | Correspondências entre SOs |
| SSD, SATA, WHEA | [armazenamento-e-whea.md](./armazenamento-e-whea.md) | WHEA histórico; driver histórico em transição |
| Tela azul, RAM | [memoria-e-tela-azul.md](./memoria-e-tela-azul.md) | BSOD real; MemTest final pendente |
| Rede, NVIDIA e drivers | [drivers-rede-e-gpu.md](./drivers-rede-e-gpu.md) | Problemas separados |
| Windows Update, Store e HKLM/HKCU | [windows-servicos-registro.md](./windows-servicos-registro.md) | Erros próprios do Windows |
| O que ainda é hipótese | [scratchpad](../../scratchpad/formatacao-correta-hipoteses-abertas.md) | Não publicar como causa |
| Como executar e encerrar | [runbook](../../runbooks/formatacao-correta-ciclo-de-correcao.md) | Sem auditorias circulares |

**Regra central:** a persistência de sintomas entre SOs orienta a investigação da plataforma, mas não transforma todos os eventos em uma única causa comprovada.

[Índice de projetos](../README.md) · [Mapa mental central](../../README.md).