# FORMATAÇÃO CORRETA — centro de entendimento e correção

**Equipamento:** Lenovo IdeaPad 320-15IKB / Type 80YH / NM-B242. **Atualizado:** 2026-09-23.  
**Objetivo:** corrigir as falhas observadas em Windows 11, Ubuntu 24.04 e Windows 10 **sem reiniciar a investigação do zero, formatar por tentativa ou substituir peças sem indicação**.

## Comece nesta ordem
1. [Inventário/testes já realizados](../../context/lenovo-80yh-inventario-e-testes.md).
2. [Linha do tempo](./linha-do-tempo.md): o que foi feito e quando.
3. [Correlações Windows ↔ Ubuntu](./correlacoes-windows-ubuntu.md): correspondências reais versus coincidências.
4. [Plano corretivo](./plano-corretivo.md): portas de decisão e condição de conclusão.
5. [Fontes, ausências e conflitos](./fontes-e-lacunas.md): não confundir relatório anterior com prova direta.

## Notas por assunto
| Assunto | Nota | Estado |
| --- | --- | --- |
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