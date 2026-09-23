# Proveniência, conflitos e lacunas — não inventar continuidade

## Material usado para a consolidação em 2026-09-23
- Conversa atual: resultados detalhados do Ubuntu 24.04 transcritos pelo usuário; confirmação de Linux **instalado como SO**, Lenovo Diagnostics pendrive sem erros, fotos parciais do MemTest86 e relato final PASS, histórico de Windows 11 → Ubuntu → Windows 10.
- Arquivos do projeto acessíveis nesta sessão: `AUDITORIA_TOTAL_CONFRONTO_FINAL_LENOVO_80YH_20260829.md`, `CONFRONTO_MESTRE_REFERENCIA_X_ATUAL_LENOVO_80YH0000BR.md`, `Markdown(1).md colado` (WinDbg), `Texto colado.txt`, `Texto colado(20260913-021922).txt` e demais trechos pesquisados.
- Em 23/09 também foram recuperados **dois arquivos originais posteriores à auditoria de agosto**: `TESTE_SATA_PHY_20260904_230509.txt` e `STRESS_EVENT37_80YH.txt`. Resultados resumidos em [testes 04/09](./testes-04-09-resultados.md); não publicar logs brutos com identificadores.
- O relatório `AUDITORIA_TOTAL_CONFRONTO_FINAL...` é **análise de uma coleta**, não o ZIP bruto reenviado neste commit. Preservar a distinção entre o conteúdo citado por essa análise e decodificação própria independente.
- Consulta ao GitHub: `README.md` e `AGENTS.md` originais verificados na branch main antes de escrever; repositório indicado como **público**.

## Não recuperado integralmente nesta sessão
- ZIP bruto Windows 29/08 e todos os logs originários de Ubuntu 24.04 (`FWTS-RESULTS.log`, `CHIPSEC-RESULTS.log`, JSON CHIPSEC): transcrição detalhada fornecida pelo usuário; consultar arquivos originais se estiverem disponíveis em outro chat/superfície.
- **Nesta etapa posterior:** os relatórios textuais da execução LOCAL do WinDbgX foram enviados em 23/09, mas os logs brutos `%TEMP%\\lenovo_windbg_*.log` não foram anexados aqui; os DOIS dumps brutos tinham sido inspecionados nos cabeçalhos em etapa anterior. O resumo local não substitui revisão independente completa das pilhas.
- Resultado MemTest86: usuário informou **PASS após conclusão** em 23/09; fotos chegam até 4ª passagem em 66%, com 0 erros naquele momento. Sem foto final e sem contagem numérica final, porque o celular descarregou. Relato é suficiente para encerrar o exame; não exigir foto.
- Logs primários específicos do Windows 11; relato do usuário é claro sobre a ocorrência, mas sem matriz de códigos naquele SO.
- **04/09** o controlador SATA constava iniciado com Intel 15.9.1.1018 no teste; isso substitui a necessidade de tratar o reboot pendente de 29/08 como atual.
- Medição direta ATUAL de Intel ME Manufacturing Mode, políticas BootGuard e Flash Descriptor: o relatório do Windows só verificou BIOS 4WCN47WW, Secure Boot, TPM/PTT e MEI, não esses três controles. O driver SATA foi medido em 23/09 como iaStorAC 17.8.1.1066; versões anteriores são históricas.

## Conflitos a preservar
- `CONFRONTO_MESTRE...` descreve os WHEA como ainda não decodificados; `AUDITORIA_TOTAL_CONFRONTO_FINAL...` posterior refere CPER/strings storahci/WD Green. Evolução de análise, não duas conclusões simultâneas.
- A versão BIOS 4WCN47WW/EC1.47 foi reconhecida como correta no Windows; isso não resolve os achados de proteção e ACPI relatados no Ubuntu.
- Secure Boot estava desativado na coleta Ubuntu; posteriormente usuário afirmou que ativou. Não publicar um dos estados como permanente.
- `ACPIVPC 15.11.29.70` e pacote ACPI `1.5.0.15` podem ser tipos de versões diferentes. Comparação numérica sozinha não comprova erro.
- F9 BIOS não reprograma Intel ME/BootGuard/Flash Descriptor; Secure Erase não restaura eletrônica e não impede configurações reincidentes.

**É proibido declarar “li todos os chats por inteiro” usando somente os resumos/arquivos listados.** Esta base registra o que foi efetivamente acessado e os fatos relatados, para que futuras sessões aprofundem apenas lacunas materiais.

[Funil](./triagem-causal-consolidada.md) · [Correlações](./correlacoes-windows-ubuntu.md) · [Plano](./plano-corretivo.md) · [Projeto](./README.md).
## Adendo de origem — anexos posteriores de 23/09/2026

- `EXPLICACAO_RELATORIO_LENOVO.md` e `DIAGNOSTICO_DIRETO_LENOVO(1).md`: RELATORIOS da execucao local posterior, com tres dumps abertos e `!analyze -v`, resumo da pilha de 23/09/full e aviso de simbolos incompletos no dump de 05/09. Os logs locais no TEMP nao foram reenviados; reportar conclusoes como **relato do laudo local**, nao nossa execucao do WinDbg nesta sessao. [EV-19](./registro-de-evidencias.md).
- `historico chat.md` e `historico chat2.md`: repetem essencialmente o resumo explicativo Ubuntu/Windows; `historico chat1.md` inclui repeticoes mais a explicacao da tela azul; nao sao tres coletas originais do Ubuntu nem se devem contar repetições como provas independentes.
- Correcao de conflito: a frase anterior `blocked by policy` foi conclusao de uma CHAMADA COMPOSTA da ferramenta. Versao local posterior obteve sucesso com invocacoes isoladas; nao persiste bloqueio do Windows/WinDbg. O pedido anterior de abrir o dump de 05/09 foi superado pela nova analise. [EV-20](./registro-de-evidencias.md).
