# Proveniência, conflitos e lacunas — não inventar continuidade

## Material usado para a consolidação em 2026-09-23
- Conversa atual: resultados detalhados do Ubuntu 24.04 transcritos pelo usuário; confirmação de Linux **instalado como SO**, Lenovo Diagnostics pendrive sem erros, imagem do MemTest86 em andamento, histórico de Windows 11 → Ubuntu → Windows 10.
- Arquivos do projeto acessíveis nesta sessão: `AUDITORIA_TOTAL_CONFRONTO_FINAL_LENOVO_80YH_20260829.md`, `CONFRONTO_MESTRE_REFERENCIA_X_ATUAL_LENOVO_80YH0000BR.md`, `Markdown(1).md colado` (WinDbg), `Texto colado.txt`, `Texto colado(20260913-021922).txt` e demais trechos pesquisados.
- O relatório `AUDITORIA_TOTAL_CONFRONTO_FINAL...` é **análise de uma coleta**, não o ZIP bruto reenviado neste commit. Preservar a distinção entre o conteúdo citado por essa análise e decodificação própria independente.
- Consulta ao GitHub: `README.md` e `AGENTS.md` originais verificados na branch main antes de escrever; repositório indicado como **público**.

## Não recuperado integralmente nesta sessão
- ZIP bruto Windows 29/08 e todos os logs originários de Ubuntu 24.04 (`FWTS-RESULTS.log`, `CHIPSEC-RESULTS.log`, JSON CHIPSEC): transcrição detalhada fornecida pelo usuário; consultar arquivos originais se estiverem disponíveis em outro chat/superfície.
- Dumps brutos da tela azul (apenas saída textual WinDbg).
- Relatório FINAL MemTest86 com quatro passagens; foto disponível mostra só 2/4, 75%, zero erros.
- Logs primários específicos do Windows 11; relato do usuário é claro sobre a ocorrência, mas sem matriz de códigos naquele SO.
- Estado **atual** de drivers iaStorA/storahci, ME Manufacturing Mode, firmware ME/EC e serviços Windows após os reparos: dados históricos não representam presente.

## Conflitos a preservar
- `CONFRONTO_MESTRE...` descreve os WHEA como ainda não decodificados; `AUDITORIA_TOTAL_CONFRONTO_FINAL...` posterior refere CPER/strings storahci/WD Green. Evolução de análise, não duas conclusões simultâneas.
- A versão BIOS 4WCN47WW/EC1.47 foi reconhecida como correta no Windows; isso não resolve os achados de proteção e ACPI relatados no Ubuntu.
- Secure Boot estava desativado na coleta Ubuntu; posteriormente usuário afirmou que ativou. Não publicar um dos estados como permanente.
- `ACPIVPC 15.11.29.70` e pacote ACPI `1.5.0.15` podem ser tipos de versões diferentes. Comparação numérica sozinha não comprova erro.
- F9 BIOS não reprograma Intel ME/BootGuard/Flash Descriptor; Secure Erase não restaura eletrônica e não impede configurações reincidentes.

**É proibido declarar “li todos os chats por inteiro” usando somente os resumos/arquivos listados.** Esta base registra o que foi efetivamente acessado e os fatos relatados, para que futuras sessões aprofundem apenas lacunas materiais.

[Correlações](./correlacoes-windows-ubuntu.md) · [Plano](./plano-corretivo.md) · [Projeto](./README.md).