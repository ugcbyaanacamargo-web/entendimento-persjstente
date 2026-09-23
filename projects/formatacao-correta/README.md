# FORMATAÇÃO CORRETA — centro de entendimento e correção

**Equipamento:** Lenovo IdeaPad 320-15IKB / Type 80YH / NM-B242. **Atualizado:** 2026-09-23.  
**OBJETIVO FINAL:** tratar impedimentos demonstrados na plataforma e então realizar **UMA instalação limpa final pelo pendrive**, com drivers controlados e validação de uso real. Nada de formatar por tentativa ou substituir peça sem razão.

**Para o usuário leigo:** uma ação por vez; agente decide e confere a saída. [Roteiro em 3 fases](./execucao-em-tres-fases.md) e [prioridades](./prioridades-e-provas.md).

## Motor de leitura/ingestão

- [Estado operacional e próxima ação](../../memory/STATE.yaml)
- **[Funil causal consolidado após PASS no MemTest86](./triagem-causal-consolidada.md)**
- [Testes de SATA/energia de 04/09 já concluídos](./testes-04-09-resultados.md)
- [Registro de provas e proveniência](./registro-de-evidencias.md)
- [Mapa semântico entre problemas](./mapa-de-relacoes.md)
- [Instruções para inserir novos resultados](../../runbooks/ingestao-de-resultados.md)

## Comece nesta ordem
1. [Inventário/testes já realizados](../../context/lenovo-80yh-inventario-e-testes.md).
2. [Linha do tempo](./linha-do-tempo.md): o que foi feito e quando.
3. [Correlações Windows ↔ Ubuntu](./correlacoes-windows-ubuntu.md): correspondências reais versus coincidências.
4. [Execução em três fases](./execucao-em-tres-fases.md), [prioridades e provas](./prioridades-e-provas.md) e [plano de casos](./plano-corretivo.md).
5. [Fontes, ausências e conflitos](./fontes-e-lacunas.md): não confundir relatório anterior com prova direta.

## Notas por assunto
| Assunto | Nota | Estado |
| --- | --- | --- |
| **Estado operacional** | [STATE.yaml](../../memory/STATE.yaml) | Fonte única da ação, histórico e não repetição |
| **Funil causal** | [triagem-causal-consolidada.md](./triagem-causal-consolidada.md) | Ligação dos três SOs, o que já foi refutado e a próxima decisão |
| **Testes posteriores** | [testes-04-09-resultados.md](./testes-04-09-resultados.md) | Resultados SATA e CPU posteriores aos eventos históricos |
| **Registro de provas** | [registro-de-evidencias.md](./registro-de-evidencias.md) | Data, fonte e limite |
| **Mapa semântico** | [mapa-de-relacoes.md](./mapa-de-relacoes.md) | Correlação Windows–Ubuntu sem causalidade inventada |
| **Roteiro operacional para a instalação final** | [execucao-em-tres-fases.md](./execucao-em-tres-fases.md) | Ações limitadas para chegar à meta |
| **Prioridades / evidências** | [prioridades-e-provas.md](./prioridades-e-provas.md) | Resolver o que é plausível e comprovável |
| Firmware de segurança / CSME | [firmware-seguranca.md](./firmware-seguranca.md) | Ubuntu reportou anomalias; requer procedimento específico |
| ACPI, EC, energia e TPM | [acpi-ec-energia-tpm.md](./acpi-ec-energia-tpm.md) | Correspondências entre SOs |
| SSD, SATA, WHEA | [armazenamento-e-whea.md](./armazenamento-e-whea.md) | WHEA histórico; teste posterior com controlador iniciado |
| Tela azul, RAM | [memoria-e-tela-azul.md](./memoria-e-tela-azul.md) | BSOD real; MemTest final PASS relatado, autor em aberto |
| Rede, NVIDIA e drivers | [drivers-rede-e-gpu.md](./drivers-rede-e-gpu.md) | Problemas separados |
| Windows Update, Store e HKLM/HKCU | [windows-servicos-registro.md](./windows-servicos-registro.md) | Erros próprios do Windows |
| O que ainda é hipótese | [scratchpad](../../scratchpad/formatacao-correta-hipoteses-abertas.md) | Não publicar como causa |
| Como executar e encerrar | [runbook](../../runbooks/formatacao-correta-ciclo-de-correcao.md) | Sem auditorias circulares |

**Regra central:** a persistência de sintomas entre SOs orienta a investigação da plataforma, mas não transforma todos os eventos em uma única causa comprovada.

[Índice de projetos](../README.md) · [Mapa mental central](../../README.md).
## Confronto global atualizado em 23/09

[Leia o confronto dos DOIS minidumps, CPER WHEA original, Bluetooth, energia, ACPI e Windows](./confronto-global-23-09.md). **Adendo posterior:** WinDbgX ja analisou ambos os minidumps e o dump completo, mas nao identificou quem corrompeu a PTE. O pedido antigo de abrir novamente o dump de 05/09 foi cancelado. A proxima acao oficial esta em [STATE.yaml](../../memory/STATE.yaml). **Nao reduzir o projeto a Event 37/lentidao.**

## Checkpoint remoto verificado

[Estado do Lenovo após intervenções reais de 23/09](./checkpoint-remoto-23-09.md): Intel CIP/QUEENCREEK removido; PC Manager/Codex atualizados; Wi-Fi/BT já na última versão compatível Intel; limites de backup, firmware e tela azul preservados. Não abrir testes arriscados sem a próxima condição de [STATE.yaml](../../memory/STATE.yaml).
