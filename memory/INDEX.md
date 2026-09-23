# Índice do motor de memória — entrada curta

**Ordem de leitura do agente (a cada sessão relevante):** [AGENTS.md](../AGENTS.md) → [STATE.yaml](./STATE.yaml) → [ROUTER.yaml](./ROUTER.yaml) → notas selecionadas pela pergunta. O agente consulta GitHub diretamente; o YAML não executa nada sozinho.

| Documento | Responsabilidade única |
| --- | --- |
| [STATE.yaml](./STATE.yaml) | **Fonte ÚNICA do estado ATUAL, objetivo/fase e próxima ação** |
| [ROUTER.yaml](./ROUTER.yaml) | Assunto/pergunta → arquivos existentes |
| [Funil causal](../projects/formatacao-correta/triagem-causal-consolidada.md) | Como cada evidência altera a próxima decisão sem repetir exames |
| [Testes 04/09](../projects/formatacao-correta/testes-04-09-resultados.md) | SATA e energia: verificações posteriores a agosto já executadas |
| [SCHEMA.yaml](./SCHEMA.yaml) | Contratos estruturais para os dois arquivos YAML |
| [Protocolo](../context/protocolo-memoria-semantica.md) | Evidência x hipótese x decisão |
| [Ingestão](../runbooks/ingestao-de-resultados.md) | Receber resultados, persistir e fechar ciclo |
| [Evidências](../projects/formatacao-correta/registro-de-evidencias.md) | IDs e origens dos resultados |
| [Relações Windows/Ubuntu](../projects/formatacao-correta/mapa-de-relacoes.md) | Assuntos conectados sem inventar causalidade |
| [Plano final](../projects/formatacao-correta/execucao-em-tres-fases.md) | Caminho à instalação limpa |

**Sem espelhos editáveis de STATE:** documentos históricos preservam data própria; [estado-atual.md](../projects/formatacao-correta/estado-atual.md) encaminha para YAML, não copia progresso. Cada alteração é validada por [GitHub Actions](../.github/workflows/validate-memory.yml) quando este workflow é executado.
