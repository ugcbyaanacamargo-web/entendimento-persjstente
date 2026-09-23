# Instruções para agentes — entendimento persistente

## Ao iniciar tarefa complexa
1. Leia [README.md](./README.md), [índice FORMATAÇÃO CORRETA](./projects/formatacao-correta/README.md) quando pertinente, e a nota temática.
2. Identifique a data do achado, a fonte e se representa um **estado histórico**, **observação atual**, **hipótese**, **resultado resolvido** ou **pendência**.
3. Leia [fontes e lacunas](./projects/formatacao-correta/fontes-e-lacunas.md); esta base não equivale ao acesso integral a todas as mensagens/anexos anteriores.
4. Na presença de dados contraditórios, não escolha silenciosamente o relatório mais recente: explique a diferença de data, método ou prova.
5. Fale com usuário leigo: UMA instrução operacional por vez (execute/clique/baixe/envie), o que esperar e risco somente quando necessário. Sem aula técnica nem 10 possibilidades na mesma resposta. Detalhes ficam nas notas.
6. **META FINAL FORMATAÇÃO CORRETA: uma instalação limpa pelo pendrive depois de resolver/documentar impedimentos persistentes**, conforme [roteiro de três fases](./projects/formatacao-correta/execucao-em-tres-fases.md).

## Regras de memória obrigatórias
- **Ler a cada tarefa complexa:** [protocolo](./context/protocolo-memoria-semantica.md), [estado atual](./projects/formatacao-correta/estado-atual.md), [provas](./projects/formatacao-correta/registro-de-evidencias.md) e [relações](./projects/formatacao-correta/mapa-de-relacoes.md), mais nota temática.
- **Novo resultado:** aplicar [ingestão de informações](./runbooks/ingestao-de-resultados.md): fonte, data, deduplicação, tipo de relação, decisão, atualização GitHub e conferência do commit.
- “Ativar memória” aqui significa seguir documentação e efetivamente usar o conector; não significa sincronização ou execução automática.

## Ao consolidar conhecimento
- Uma nota Markdown por assunto; fonte, data, nível de confirmação, ligações relativas e próximo ponto de decisão.
- Atualize índice local e o [mapa central](./README.md). Guarde hipóteses em [scratchpad](./scratchpad/README.md).
- **Não declarar que BSOD foi causado por CSME, SSD ou RAM apenas por coexistirem achados; distinguir correlação de causalidade.**
- Diagnóstico aprovado não resolve outra falha; diagnóstico negativo não significa componente infalível.
- Trabalhe com problema → ação focalizada → verificação do sintoma → encerramento ou encaminhamento, conforme [runbook](./runbooks/formatacao-correta-ciclo-de-correcao.md). Uma nova coleta só se alterar próxima ação; priorizar provas e decisões na [matriz](./projects/formatacao-correta/prioridades-e-provas.md).
- O agente estrutura, decide, prepara e acompanha os comandos que o usuário executa; **não alegar acesso direto ao Lenovo, correção aplicada ou teste executado quando não houver ferramenta e resultado reais**.
- Nunca sugerir como correção genérica: formatar novamente, Secure Erase, F9/CMOS, limpar TPM, trocar peça ou gravar BIOS/ME/Flash Descriptor sem procedimento e evidência específicos.
- Não alterar GitHub, aparelho ou recursos externos sem pedido e autorização no escopo; verificar resultado após alterações.
- Não salvar segredos ou dados pessoais sensíveis. **Este repositório está público na consulta de 2026-09-23.**
- Consultar/gravar memória exige uso real da conexão GitHub; nenhuma sincronização de conversas é automática. Repositório é memória documental versionada, não motor de execução remota ou rede neural.

## Navegação
[Contexto](./context/README.md) · [Projetos](./projects/README.md) · [Rascunhos](./scratchpad/README.md) · [Procedimentos](./runbooks/README.md) · [Estrutura de memória](./context/2026-09-23-estrutura-memoria.md).