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

## Referências oficiais consultadas em 23/09/2026

- fwupd, especificação HSI: https://fwupd.github.io/libfwupdplugin/hsi.html — para `ME not in manufacturing mode` o valor favorável é **locked**, para `ME Flash Descriptor Override` é **locked**; BootGuard tem testes distintos para habilitação, ACM, OTP, Verified e Error Policy. A orientação pública para falhas desses atributos é procurar o **OEM**; isso não é um procedimento de regravação fornecido ao usuário.
- Lenovo, BIOS para Type 80YH: https://pcsupport.lenovo.com/bs/en/products/laptops-and-netbooks/300-series/320-15ikb/80yh/downloads/ds121587 — lista 4WCN47WW, com alterações de segurança e correção de exibição de velocidade da CPU no SMBIOS. A página **não demonstra** que este pacote fecha Manufacturing Mode, altera BootGuard ou configura Flash Descriptor deste equipamento.
- Lenovo, fim do suporte de desenvolvimento do modelo: https://pcsupport.lenovo.com/br/pt/products/laptops-and-netbooks/300-series/320-15ikb/80yh/downloads — não presumir futura atualização oficial, nem converter isso em autorização para usar firmware genérico.

## O que está errado vs. como deveria estar

| Medição relatada Ubuntu | Condição desejada documentada pelo fwupd | Próxima decisão |
| --- | --- | --- |
| CSME Manufacturing Mode: aberto | `locked` / modo de fabricação encerrado | Verificar exata saída original + procedimento/provisionamento OEM. Não é driver Windows. |
| Flash Descriptor: permissões excessivas | Regiões protegidas e `override: locked`, de acordo com desenho da placa | Não aplicar script destravamento e não “fechar todos os bits” indiscriminadamente. |
| BootGuard ACM/OTP/Verified/Policy inválidos | Estados validados para cada recurso que o hardware e a configuração de fabricação implementam | OEM confirma se a configuração era prevista e quais itens são de fato recuperáveis; não prometer alterar fuses. |

## Correção visada
**Apurar o estado e a configuração de produção Lenovo para NM-B242 + BIOS 4WCN47WW e corrigir o provisionamento de firmware se houver procedimento autorizado.** Um laudo especializado precisa identificar exatamente o que pode ser reparado, o que é limitação da plataforma e o que depende de fusíveis irreversíveis. Não substituir o firmware por imagem genérica.

**Não fazer:** FPT/unlock, gravação SPI genérica, apagar Intel ME, mexer em fusíveis, limpar TPM/PTT/PK/KEK/db/dbx ou reset F9 como “conserto” desses achados. Risco real de não inicializar e perda de dados individuais da placa.

**Relação com BSOD:** Manufacturing Mode aberto é problema de proteção, **não foi ligado causalmente** ao dump 0x1A/0x41792.

[Correlações](./correlacoes-windows-ubuntu.md) · [ACPI](./acpi-ec-energia-tpm.md) · [Plano](./plano-corretivo.md) · [Fontes](./fontes-e-lacunas.md).
## Evidencia adicional local 23/09 (EV-25)

O mapa `MAPA_FIRMWARE_OFICIAL.txt` produzido no notebook identifica imagem OEM Lenovo 4WCN47WW de **8 MiB**, regiões Descriptor, Intel ME e BIOS. O próprio mapa informa que **NÃO existe dump da SPI atual**. O conteúdo de uma imagem oficial distribuída NÃO mostra travas reais da placa em funcionamento, nem justifica um flash. Foi preparado no notebook `ENCAMINHAMENTO_FIRMWARE_LENOVO_80YH.md`, com perguntas de baseline OEM, procedimento de provisionamento/end-of-manufacturing e validação. Não foi enviado à Lenovo nem foi alterado firmware. Relato histórico Ubuntu incluiu ainda `_CPC`, GDS e cerca de 43 resultados FWTS desfavoráveis segundo conversa; SEM arquivo bruto para discriminar/contar mecanismos, não tratar isso como 43 defeitos físicos distintos. [EV-25](./registro-de-evidencias.md).
