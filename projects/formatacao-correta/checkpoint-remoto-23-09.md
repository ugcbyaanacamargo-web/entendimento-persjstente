# Checkpoint REMOTO verificável — Lenovo 80YH — 23/09/2026

**Fontes:** Desktop Commander conectado em sessão administrativa ao Lenovo, documentação do [Intel Wireless-AC 3165](https://www.intel.com/content/www/us/en/products/sku/89450/intel-dual-band-wirelessac-3165/downloads.html), [suporte oficial Lenovo 80YH](https://pcsupport.lenovo.com/br/pt/products/laptops-and-netbooks/300-series/320-15ikb/80yh/downloads) e [registro](./registro-de-evidencias.md). Nenhum log cru, dump, identificador de série ou nome de usuário publicado. Estado TEMPORAL, não promessa de ausência de falha futura.

## Executado, conferido e ENCERRADO

- Intel Computing Improvement Program desinstalado pelas duas entradas oficiais MSI e bundle, retornos 0, após ponto de restauração do Windows; processos, serviços QUEENCREEK, driver e arquivo `semav6msr64` desapareceram; `iaStorAC` e `MEIx64` preservados; PawnIO permanece, Verifier desligado.
- O Windows já concluiu as duas atualizações AppX PC Manager e Codex que antes acusaram `0x80073D02`; ambos pacotes **Status Ok**, versões alvo instaladas. PowerShell 7.6.6, também `Status Ok`, **executou de verdade**. Não reabrir esses erros históricos como falha de instalação corrente.
- Não há dispositivo PnP presente com código de erro no snapshot. SSD SATA ligado por `iaStorAC`; zero novo WHEA na consulta limitada 15 dias; nenhum reteste SATA/estresse foi repetido.
- Sem alteração BIOS, ME, TPM, Driver Verifier, Wi-Fi, Bluetooth, modo SATA, chaves UEFI ou partições. **Sem reboot remoto.**

## Aberto — não transformar em solução inventada

| Caso | Evidência local / alcance | Decisão |
| --- | --- | --- |
| BSOD | Dois 0x1A/0x41792 de 05 e 23/09, WinDbg sem autor; MemTest PASS | Não declarar curado pela retirada do CIP; outro driver opcional PawnIO ainda carregado. Qualquer Verifier exige backup externo e recuperação. |
| Bluetooth | Cinco BTHUSB17 de 04–20/09, dispositivo OK no snapshot | Intel 3165 BT já usa **20.100.10.11**, última versão Intel: [fonte](https://www.intel.com/content/www/us/en/download/823075/intel-wireless-bluetooth-drivers-for-wireless-ac-7265-rev-d-3168-and-3165.html). Não forçar pacote de outra geração; correlacionar funcionamento real/driver OEM específico. |
| Wi-Fi | 22 Netwtw04/5007, último 05/09, conectado no snapshot | Intel 3165 Wi-Fi usa **19.51.50.2**, última versão Intel: [fonte](https://www.intel.com/content/www/us/en/download/823059/intel-wireless-wi-fi-drivers-for-wireless-ac-7265-rev-d-3168-and-3165.html). Sem update genérico a fazer. |
| Firmware/ACPI | Ubuntu relatou Manufacturing Mode/Descriptor/BootGuard; Event37 retornou em Windows, em especial no boot | No Windows não há medição atual das proteções; referência OEM Lenovo requerida. Arquivo BIOS oficial local mapeado, **não há dump SPI atual**. Encaminhamento técnico preparado no PC; não gravar firmware por tentativa. |
| Store/ScreenClipping/WSL | Store push `0x80072ee7` em operação passada, demais sintomas históricos | Só reparar função específica se erro ainda reproduzível; preservar preferência do usuário PrtSc clássico; sem reset geral de rede/Registro. |

## Bloqueio de próxima fase de risco

- Ponto de restauração existente e Windows RE marcado Enabled. C: sem criptografia ativa. **Nenhuma unidade externa de backup apareceu conectada**; nenhum teste de boot por WinRE ou imagem externa foi feito.
- Antes de Driver Verifier/instalação final: usuário conectar armazenamento externo e confirmar espaço, autorizar backup/imagem testável, definir retorno ao Windows. Para firmware, só procedimento OEM/técnico com baseline de revisão e preservação de dados exclusivos.
- **A condição de backup externo aplica-se SOMENTE a Driver Verifier, firmware ou instalação destrutiva, não bloqueia a correção cotidiana de aplicativos.** A fila operacional atual está em [STATE.yaml](../../memory/STATE.yaml): ScreenClippingHost Event1000 atual, reproduzido e documentado; não exigir HD para re-registro ou diagnóstico do Shell.

[Confronto global](./confronto-global-23-09.md) · [Firm. segurança](./firmware-seguranca.md) · [BSOD](./memoria-e-tela-azul.md) · [Evidências EV-21..25](./registro-de-evidencias.md).
## Adendo após a imagem do Event Viewer — 23/09 ~21h05 a 21h22

[EV-27–30](./registro-de-evidencias.md): captura falha de forma reproduzível; re-registro individual `MicrosoftWindows.Client.CBS` SUCESSO, mas teste continuou falhando. Dump completo SOMENTE de ScreenClippingHost (privado, local) confirmou `STOWED_EXCEPTION_80270301` / `E_SHELL_EXTENSION_BLOCKED`; `SearchApp` apresentou mesmo HRESULT, sem extensão exata identificada. O caso captura fica ABERTO, não repetir testes sem hipótese nova. O print do usuário mostrava 3.752 eventos administrativos acumulados, não 3.752 defeitos contemporâneos independentes. [Trilha Windows](./windows-servicos-registro.md) · [STATE](../../memory/STATE.yaml).
