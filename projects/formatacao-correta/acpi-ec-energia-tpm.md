# ACPI, EC, energia e TPM — evidência cruzada

**ACPI:** informações/funções que o firmware fornece ao SO. **EC:** controlador interno de energia e funções da placa. **TPM:** módulo de segurança; PTT é implementação Intel.

## Ubuntu 24.04 — resultados transcritos pelo usuário
- Kernel: `tpm_crb: [Firmware Bug]: Bad ACPI memory layout` e falha de criação `acpi MSFT0101:00 ... -16`.
- FWTS: `_WAK` com variável não inicializada (retorno da suspensão), `ADP0._PSR` retornou NULL (alimentação), `UBTC.CR01._PLD` NULL; falhas FADT/ESRT e outras.
- `_CPC` ausente em CPU1–CPU7; **ausência isolada NÃO demonstra CPU com defeito ou limitação**, porque depende da interface de gerenciamento que essa geração suporta.
- Total transcrito FWTS: 1316 passed, 43 failed, 9 warnings, 62 aborted, 420 skipped; contagens não equivalem a 43 defeitos físicos distintos.

## Windows — relatório 29/08/2026
- ACPI Event 13: EC não respondeu no tempo esperado; Event 15: resposta inesperada.
- Kernel-Processor-Power Event 37: 33 eventos de limitação por firmware; havia plano Alto Desempenho personalizado.
- Dois Kernel-Power Event 41; relatório posterior menciona um em torno de transição de suspensão/retorno.
- BIOS 4WCN47WW e EC 1.47 eram as versões do snapshot. Versão correta não prova implementação sem bugs.
- **04/09: teste original de oito ciclos carga/repouso em AC**: não houve novos Event 37, WHEA ou ACPI 13/15 durante a janela observada. Portanto, é incorreto tratar 33 Event 37 de agosto como limitação permanente e comprovadamente presente. [Resultados](./testes-04-09-resultados.md).

## Correlação e limites
**Mesma área funcional em dois SOs:** comunicação firmware ↔ energia/suspensão/dispositivos. Não afirmar que `_WAK` provocou um determinado Event 41 ou que erro TPM CRB danificou o TPM. Windows reconhecia TPM/PTT pronto. O resultado Ubuntu pode refletir descrição de recurso que um SO tolera e outro rejeita.

## Alvo de correção
Confirmar sintomas concretos (transição suspensão/retorno, energia AC, Event 13/15/37) e tratar primeiro configurações reversíveis de energia, depois compatibilidade OEM do ACPI/Serial IO, sem atualizar BIOS/EC às cegas.

[Funil](./triagem-causal-consolidada.md) · [Correlações](./correlacoes-windows-ubuntu.md) · [Firmware](./firmware-seguranca.md) · [Drivers](./drivers-rede-e-gpu.md) · [Plano](./plano-corretivo.md).