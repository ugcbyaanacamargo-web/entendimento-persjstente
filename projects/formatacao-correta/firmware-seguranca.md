# Firmware de segurança — CSME, Flash Descriptor, BootGuard

**Origem:** resumo e trechos do resultado da investigação de Ubuntu 24.04 fornecidos pelo usuário em 23/09/2026. Os arquivos brutos CHIPSEC e FWTS não foram recuperados nesta sessão. **Status:** achados reportados, corrigir sem extrapolar causalidade.

## Significado para leigo
- **Intel ME/CSME:** sistema de gerenciamento e segurança que faz parte da plataforma Intel, independentemente do Windows/Linux.
- **Manufacturing Mode:** acesso especial de fabricação. Usuário relata CHIPSEC/fwupd indicando **modo aberto**; o esperado para uma máquina finalizada é o modo de fabricação encerrado conforme a Lenovo.
- **End of Manufacturing:** conclusão de configuração e bloqueios próprios da fabricação. Não é reinstalar driver Intel MEI.
- **Flash Descriptor:** tabela de quem pode ler/gravar as regiões do chip de firmware. CHIPSEC relatou permissões excessivas; proteção exata esperada requer referência Lenovo da revisão.
- **BootGuard:** verifica partes iniciais do firmware conforme recursos configurados em fabricação. fwupd reportou ACM, OTP/fuse, Verified Boot e Error Policy inválidos. **Não deduzir que todos podem/precisam ser ativados pelo usuário:** suporte, modo de implementação e fusíveis dependem do modelo e de como foi produzido.
- **Secure Boot:** verifica componentes de boot conforme chaves UEFI; estava desativado na coleta Ubuntu, posteriormente usuário confirmou ativado. NÃO confundir com BootGuard.
- **GDS Vulnerable** após microcode 0xd6 → 0xf6: mitigação de vulnerabilidade não reconhecida como ativa no Ubuntu; não explica automaticamente corrupção de memória ou permissões.

## Correção visada
**Apurar o estado e a configuração de produção Lenovo para NM-B242 + BIOS 4WCN47WW e corrigir o provisionamento de firmware se houver procedimento autorizado.** Um laudo especializado precisa identificar exatamente o que pode ser reparado, o que é limitação da plataforma e o que depende de fusíveis irreversíveis. Não substituir o firmware por imagem genérica.

**Não fazer:** FPT/unlock, gravação SPI genérica, apagar Intel ME, mexer em fusíveis, limpar TPM/PTT/PK/KEK/db/dbx ou reset F9 como “conserto” desses achados. Risco real de não inicializar e perda de dados individuais da placa.

**Relação com BSOD:** Manufacturing Mode aberto é problema de proteção, **não foi ligado causalmente** ao dump 0x1A/0x41792.

[Correlações](./correlacoes-windows-ubuntu.md) · [ACPI](./acpi-ec-energia-tpm.md) · [Plano](./plano-corretivo.md) · [Fontes](./fontes-e-lacunas.md).