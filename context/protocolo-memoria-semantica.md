# Protocolo de memória semântica

**Data:** 2026-09-23. **Objetivo:** converter achados em uma ação verificável rumo à instalação limpa, não acumular auditorias.

## O que está ativo
Uma base Markdown consultável, versionada, com links entre informações e instruções para o agente. **Não** há sincronização automática de conversas, embeddings, banco vetorial, agente local, monitoramento do Lenovo ou execução remota. A IA precisa efetivamente ler e escrever pelo GitHub em cada sessão relevante.

## Leitura obrigatória
1. [README da raiz](../README.md) → [estado operacional](../memory/STATE.yaml).
2. Ler [registro de evidências](../projects/formatacao-correta/registro-de-evidencias.md), [relações](../projects/formatacao-correta/mapa-de-relacoes.md) e somente a nota temática relacionada.
3. Conferir datas: erro histórico não é erro atual. Comparar resultado novo ao antigo e registrar o que mudou.
4. Escolher uma ação que muda a próxima decisão; só pedir teste extra quando a resposta determina correção distinta.

## Informações com significado definido
- **Fato observado:** foto ou log visto diretamente; dizer exatamente o que mostra.
- **Relato:** resultado fornecido pelo usuário, com data e sem fingir que o arquivo bruto foi lido.
- **Auditoria antiga:** conclusão de uma análise anterior, não prova independente nem estado presente.
- **Hipótese:** explicação ainda não validada; guardar no [scratchpad](../scratchpad/formatacao-correta-hipoteses-abertas.md).
- **Correção comprovada:** ação executada e sintoma original testado novamente com êxito.
- **Limitação:** recurso que a plataforma não suporta ou correção que requer intervenção especializada, com referência adequada.

## Vínculos semânticos
Nomear cada relação: `mesmo-subsistema`, `ocorreu-antes`, `corrobora`, `contradiz`, `depende-de`, `corrigido-por`, `validado-por`, `causa-nao-demonstrada`. Uma coincidência entre Windows/Ubuntu não vira “causou” sem demonstração. Ao corrigir, atualizar relação e estado.

## Destino do registro
`context/`: inventário durável; `projects/formatacao-correta/`: evidências, relações, estado, decisões; `scratchpad/`: hipóteses; `runbooks/`: procedimentos seguros validados.

**Privacidade:** repositório público na consulta de 23/09. Não gravar dados pessoais, números de série, UUID, credenciais, imagens e logs brutos com identificadores.

[Roteador](../memory/ROUTER.yaml) · [Schema](../memory/SCHEMA.yaml) · [Ingestão operacional](../runbooks/ingestao-de-resultados.md) · [Projeto](../projects/formatacao-correta/README.md).