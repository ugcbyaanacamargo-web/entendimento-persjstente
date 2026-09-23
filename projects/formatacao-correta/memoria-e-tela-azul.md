# Tela azul de 23/09 e RAM — o que foi demonstrado

**Evidência:** texto WinDbg `Markdown(1).md colado`, dump `092326-11734-01.dmp`; foto MemTest86 nesta conversa 23/09/2026.

- `MEMORY_MANAGEMENT` / Bugcheck `0x1A`, parâmetro `0x41792`.
- Bucket `MEMORY_CORRUPTION_ONE_BIT`; uma entrada usada no gerenciamento da memória estava corrompida.
- `msedge.exe` é o processo registrado no momento, **não autor da corrupção identificado**.
- Diagnóstico Lenovo por pendrive terminou sem erros, segundo usuário.
- MemTest86 v11.7: primeira passagem completa sem erros; última foto: segunda passagem em 75%, **0 erros acumulados**. O resultado final de 4/4 não foi apresentado aqui.
- RAM física: um módulo Samsung DDR4 de 16 GB. Zero erros na parte executada reduz suspeita de falha reproduzível na RAM, não determina causa da tela azul.

## Hipóteses abertas, sem ranking artificial
Driver/dispositivo escrevendo memória indevida; caminho RAM/controlador de memória sob condições não testadas; outras instabilidades em operação do sistema. ACPI/EC e CSME existem em paralelo, mas **não há elo demonstrado entre Manufacturing Mode e o bit corrompido**.

## Gatilho para encerrar etapa
Registrar fotografia final MemTest se fornecida e **não pedir novo teste de RAM automaticamente**; se 4/4 PASS sem erros, classificar “MemTest86 sem falhas detectadas”; manter BSOD como ocorrência separada, exigindo evidência específica para apontar causador.

[Inventário](../../context/lenovo-80yh-inventario-e-testes.md) · [ACPI](./acpi-ec-energia-tpm.md) · [Plano](./plano-corretivo.md).