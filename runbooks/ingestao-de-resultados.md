# Como o agente insere informação nova na memória

**Agente executa este roteiro; o usuário leigo só envia a foto ou resultado.** Ver [protocolo](../context/protocolo-memoria-semantica.md).

1. **Recuperar** [estado atual](../memory/STATE.yaml), [evidências](../projects/formatacao-correta/registro-de-evidencias.md) e a nota temática.
2. **Extrair** sistema operacional, componente, teste, data do evento, mensagem exata, resultado, fonte e risco. Campo desconhecido permanece desconhecido.
3. **Deduplicar:** mesmo exame e mesma ocorrência atualizam nota; observação após reparo é registro novo, preservando a anterior.
4. **Classificar origem:** foto/log diretamente visto, relato do usuário, relatório anterior, hipótese ou validação após ação. Não chamar resumo de log original.
5. **Relacionar** ao [mapa semântico](../projects/formatacao-correta/mapa-de-relacoes.md) e à [matriz Windows/Ubuntu](../projects/formatacao-correta/correlacoes-windows-ubuntu.md), nomeando a relação e seus limites.
6. **Decidir uma próxima ação:** corrigir, já corrigido, histórico encerrado, limitação ou encaminhamento especializado. Atualizar **somente memory/STATE.yaml** para estado operacional; atualizar nota específica e índice quando houver nota nova.
7. **Gravar/validar:** conferir alterações, links relativos, [validador](../tools/validate_memory.py), commit, leitura de volta pelo GitHub e branch HEAD. Só então confirmar persistência.
8. **Responder:** “Faça [uma ação]. Envie [resultado].” Acrescentar risco em frase curta quando existir.

## Campos de nota atômica
Título/ID; SO/componente; data da ocorrência/registro; origem; grau de confirmação; erro exato; funcionamento esperado; notas relacionadas e tipo de relação; ações anteriores e resultados; próxima ação ÚNICA; teste de sucesso; risco/reversão.

**Exemplo:** foto MemTest86 de 23/09: passagem 1 concluída sem erros, passagem 2 em 75%, zero acumulado. Não atualizar para PASS 4/4 sem a imagem final. Não repetir Lenovo Diagnostics e SMART já realizados.

[Índice](./README.md) · [Objetivo de três fases](../projects/formatacao-correta/execucao-em-tres-fases.md).