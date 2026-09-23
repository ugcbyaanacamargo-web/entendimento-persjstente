# Drivers — WLAN, NVIDIA, ACPI/Serial IO e Intel MEI

**Fonte:** snapshots Windows 29/08/2026 + relato Ubuntu 24.04. Versão diferente NÃO significa automaticamente driver incompatível.

## Windows
- Intel Wireless-AC 3165: driver Netwtw04 19.51.50.2 e cerca de 22 Event 5007 (`TX/CMD timeout / TfdQueue hanged`); erro operacional da fila WLAN naquela data.
- Lenovo ACPIVPC: driver 15.11.29.70 no snapshot; referência histórica de pacote ACPI Lenovo 1.5.0.15. **Não comparar números como se fossem a mesma métrica de versão**.
- Intel Serial IO 30.100.1816.3 versus referência OEM histórica 30.100.1725.1.A: diferença a confrontar com identificação de hardware e sintomas ACPI, não prova de instalação errada.
- MEI/HECI principal 1828.12.0.1152: identificado e assinado; LMS/DAL/iCLS mais recentes, evento MEIx64 4 de desabilitação seguido de retorno. Firmware ME real não extraído na coleta.
- NVIDIA no Windows: a 940MX de 4 GB ativou automaticamente no teste 3D; não ficou provado defeito de GPU.

## Ubuntu
- GPU 940MX detectada, perfil PRIME Intel, `nvidia-smi rc=9`, módulos gráficos detectados e mensagens `Cannot find any crtc or sizes`. Em Optimus sem monitor ligado à dGPU, essas mensagens não identificam isoladamente um defeito físico. Investigar driver/perfil de ativação Linux quando o objetivo for rodar Ubuntu.

## Correções controladas
Usar pacote Lenovo para funções específicas de plataforma quando compatível, sem instalar vários drivers juntos; rede e GPU são casos próprios, não explicar Store e BSOD com eles sem reprodução associada.

[ACPI](./acpi-ec-energia-tpm.md) · [Firmware](./firmware-seguranca.md) · [Plano](./plano-corretivo.md).
## Bluetooth omitido anteriormente — fonte original 23/09

No arquivo completo de eventos incluído no ZIP de 23/09: **BTHUSB Event 17 (20/09 19h15)** relata falha indeterminada do adaptador local e descarregamento do driver; **BTHUSB Event 34 em 23/09** relata apenas ausência de capacidade LE peripheral, não a mesma falha. Tratar separadamente dos 22 Netwtw04 Event5007 do snapshot de agosto; Intel AC3165 combina Wi-Fi e Bluetooth, mas não presumir uma única falha física. O dispositivo aparecer sem código PnP em 23/09 não invalida falha intermitente de 20/09. [Confronto global](./confronto-global-23-09.md) e [EV-17](./registro-de-evidencias.md).
