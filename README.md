# Mapa mental central — entendimento persistente

> Índice da memória de trabalho baseada em arquivos Markdown e versionada no GitHub.

**Atualizado em:** 2026-09-23  
**Modelo de referência:** [AI Knowledge Base (AIKB)](https://github.com/mcglothi/ai-knowledge-base). Esta é uma adaptação documental mínima, não a instalação do motor ou das automações do AIKB.

## Comece por aqui

| Área | Para que serve | Índice |
| --- | --- | --- |
| Contexto | Histórico, fatos confirmados, entendimentos e decisões gerais | [context/README.md](./context/README.md) |
| Projetos | Índice de projetos ativos, objetivos, decisões e próximos passos | [projects/README.md](./projects/README.md) |
| Rascunhos | Hipóteses, notas temporárias e informações ainda não verificadas | [scratchpad/README.md](./scratchpad/README.md) |
| Procedimentos | Passos repetíveis de coleta, execução, validação e reversão segura | [runbooks/README.md](./runbooks/README.md) |

## Memória já consolidada

| Nota | Assunto |
| --- | --- |
| [Decisão de estrutura inicial](./context/2026-09-23-estrutura-memoria.md) | Origem do modelo, diretórios e limites desta implantação |

## Como recuperar o entendimento

1. Leia este `README.md` para localizar o assunto.
2. Abra apenas o índice e as notas diretamente relacionados à tarefa atual.
3. Confira no sistema ou repositório de origem se informações mutáveis continuam válidas.
4. Diferencie informação confirmada, decisão, hipótese e pendência.
5. Registre aprendizados duradouros em um `.md` curto por assunto; atualize o índice da pasta e este mapa quando houver uma nova nota importante.

## Regras de armazenamento

- Use nomes descritivos em `kebab-case` e links relativos entre arquivos.
- Mantenha rascunhos não confirmados em [scratchpad](./scratchpad/README.md); após validação, mova o conhecimento para [context](./context/README.md), [projects](./projects/README.md) ou [runbooks](./runbooks/README.md).
- Não salve senhas, tokens, chaves privadas ou dados sensíveis. Verifique a visibilidade do repositório antes de registrar detalhes não públicos.
- Não trate o conteúdo como sincronização automática: o agente precisa ter acesso ao repositório e efetivamente consultar/gravar os arquivos em cada sessão relevante.

**Instruções para agentes:** [AGENTS.md](./AGENTS.md).
