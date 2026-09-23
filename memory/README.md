# Motor adaptado ao ChatGPT Web + GitHub

**Fonte atual:** [STATE.yaml](./STATE.yaml). [Funil causal com PASS no MemTest86](../projects/formatacao-correta/triagem-causal-consolidada.md). [Testes de SATA/CPU já concluídos](../projects/formatacao-correta/testes-04-09-resultados.md). **Roteamento:** [ROUTER.yaml](./ROUTER.yaml). **Índice humano:** [INDEX.md](./INDEX.md). **Regras:** [SCHEMA.yaml](./SCHEMA.yaml).

**Ação do agente:** ler GitHub → recuperar o estado e apenas documentos de assunto relevante → interpretar nova evidência → atualizar o estado e as notas autorizadas → conferir commit/validação. Nenhum agente local, servidor de busca, vetor ou captura automática de chats foi instalado. O repositório é público; não acrescentar dados privados ou dumps brutos.

A verificação automática GitHub Actions usa `tools/validate_memory.py` com permissões de leitura e não tem acesso ao notebook. O ChatGPT deve consultar o commit após cada gravação e não afirmar que CI passou antes do resultado do workflow.
