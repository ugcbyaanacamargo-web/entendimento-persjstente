# Matriz semântica — Windows 11, Ubuntu 24.04 e Windows 10

**Objetivo:** separar “mesma área envolvida” de “mesma causa demonstrada”. Os dados detalhados recuperados são especialmente Ubuntu 24.04 (resumo do usuário), Windows 10 (logs 2026) e experiências relatadas com Windows 11; **logs originais do Windows 11 não recuperados**.

| Área | Ubuntu | Windows 10 | Conexão honesta | O que NÃO concluir |
| --- | --- | --- | --- | --- |
| ACPI / EC / energia | `_WAK`, `_PSR`, FADT, TPM CRB | EC Event 13/15; Event 37; Kernel-Power 41 | Ambos relataram problemas na comunicação/energia de firmware | Não afirmar que uma função específica causou toda tela azul |
| CSME / ME | Manufacturing Mode reportado aberto, Flash Descriptor, BootGuard / HSI | MEIx64 Event 4 e pilha software ME de versões distintas | Mesma família de plataforma, eventos de natureza diferente | Não dizer que Manufacturing Mode corrompe HKLM |
| TPM | `Bad ACPI memory layout` | Intel PTT 2.0 pronto | Firmware expõe dispositivo reconhecido de forma diferente pelos SOs | Não limpar TPM para corrigir tabela ACPI |
| Gráficos | `nvidia-smi` falhou | NVIDIA 940MX funcionou em teste 3D | Configuração/perfil SO difere | Não trocar GPU |
| Armazenamento | Sem equivalente específico no resumo | WHEA histórico com cadeia storahci/WD Green | Nenhuma evidência cruzada específica ainda | Não apontar SSD físico como culpado |
| Memória | Sem equivalente demonstrado no resumo | BSOD 0x1A/0x41792 em 23/09 | Não comprovada causa comum | MemTest parcial 0 erro não identifica driver culpado |
| Permissões | Usuário relata questões de segurança e permissões Linux; FWTS/fwupd fornecem detalhes de firmware | HKLM/HKCU, AppX, DCOM e serviços | “segurança” é tema, mecanismos são diferentes | Linux NÃO utiliza Registro Windows; eventos não equivalentes |
| WLAN | Não demonstrado no resumo Ubuntu | Netwtw04 5007 | Caso Windows/rede documentado | Não atribuir a BIOS sem elo |

**Síntese:** problemas compartilhados de plataforma/firmware **e** problemas próprios de cada SO podem coexistir. A existência dos dois não autoriza uma causa universal nem nova formatação automática.

[Projeto](./README.md) · [Firmware](./firmware-seguranca.md) · [ACPI](./acpi-ec-energia-tpm.md) · [Memória](./memoria-e-tela-azul.md) · [Fontes](./fontes-e-lacunas.md).