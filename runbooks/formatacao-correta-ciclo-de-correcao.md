# Ciclo de correção sem diagnóstico infinito — FORMATAÇÃO CORRETA

**Propósito:** corrigir bloqueios de forma enxuta para chegar à **formatação limpa final**, com fim observável para cada erro. [Três fases](../projects/formatacao-correta/execucao-em-tres-fases.md). Aplicável ao [Lenovo 80YH](../projects/formatacao-correta/README.md).

1. **Recuperar o caso existente:** ler [linha do tempo](../projects/formatacao-correta/linha-do-tempo.md), [correlações](../projects/formatacao-correta/correlacoes-windows-ubuntu.md) e [fontes](../projects/formatacao-correta/fontes-e-lacunas.md). Não repetir ferramentas Lenovo Diagnostics/SMART/formatar sem justificativa concreta.
2. **Definir UMA falha observável:** mensagem exata, data, efeito ao usuário, como reproduzir e status após reparos prévios. Distinguir histórica de atual.
3. **Explicar em português simples:** o que falhou, como deveria funcionar, se é configuração, firmware, driver, SO ou peça. Dizer “hipótese” quando não há nexo.
4. **Escolher menor correção possível:** um ajuste por vez, registrar estado anterior, criar backup quando adequado, definir riscos de boot/dados e rollback quando seguro.
5. **Verificar o defeito real:** repetir o ato que falhava; não usar ausência de alertas vagos como única prova.
6. **Registrar resultado:** corrigido / não corrigido / limitação verificada / encaminhamento especializado. Inclua data, versão, fonte e resultado funcional.
7. **Atualizar nota temática + índice:** registrar também tentativas fracassadas, para não repeti-las em outros chats.

## Restrições destrutivas
Nenhum Secure Erase, formatação, limpeza TPM/PK/KEK/db/dbx, alteração SATA mode, FPT, gravação SPI/ME/EC, desativação de proteções ou troca de peças por tentativa. Alterações de firmware requerem referência adequada à NM-B242, dados originais preservados e procedimento do fabricante/especialista.

## Modelos de encerramento
- “Falha AppX X, correção Y, instalação/abertura Z passou em data T.”
- “ACPI/EC: dispositivo Z voltou de suspensão N vezes; eventos-alvo X/Y não reapareceram nessa janela.”
- “Manufacturing Mode: relatório técnico confirmou configuração de produção/reparo ou limite da placa.”

[Plano corretivo](../projects/formatacao-correta/plano-corretivo.md) · [Índice de procedimentos](./README.md).