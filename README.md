# Mapa mental central — entendimento persistente

> Índice de memória de trabalho em Markdown, versionada no GitHub. **Repositório público:** não publicar nomes de usuário, números de série, UUIDs, e-mails, credenciais, dumps brutos ou detalhes privados.

**Atualizado em:** 2026-09-23  
**Referência estrutural:** [AI Knowledge Base (AIKB)](https://github.com/mcglothi/ai-knowledge-base). Adaptação documental: não instala nem executa o motor do AIKB.

## Comece por aqui

| Área | Para que serve | Índice |
| --- | --- | --- |
| Contexto | Hardware e fatos duráveis | [context/README.md](./context/README.md) |
| Projetos | Investigações, decisões e estado de correção | [projects/README.md](./projects/README.md) |
| Rascunhos | Hipóteses ainda não demonstradas | [scratchpad/README.md](./scratchpad/README.md) |
| Procedimentos | Ações delimitadas e critérios de encerramento | [runbooks/README.md](./runbooks/README.md) |

## Motor para ChatGPT Web

**[STATE.yaml](./memory/STATE.yaml) é a única fonte operacional**, [ROUTER.yaml](./memory/ROUTER.yaml) escolhe as notas e [SCHEMA.yaml](./memory/SCHEMA.yaml) define os contratos. [Índice do motor](./memory/INDEX.md) · [Validação do GitHub](./.github/workflows/validate-memory.yml).

## Memória semântica em operação documental

[Protocolo](./context/protocolo-memoria-semantica.md) · [Como inserir dados](./runbooks/ingestao-de-resultados.md) · [Estado e ação atual](./memory/STATE.yaml) · [Relações](./projects/formatacao-correta/mapa-de-relacoes.md) · [Registro de provas](./projects/formatacao-correta/registro-de-evidencias.md).

## Funil da investigação

**[Leia primeiro a triagem causal após o MemTest86 PASS](./projects/formatacao-correta/triagem-causal-consolidada.md).** Os [testes reais de 04/09](./projects/formatacao-correta/testes-04-09-resultados.md) atualizaram os erros de armazenamento e energia observados em agosto. Não tratar observações antigas como falhas atuais.

## Memória já consolidada

| Nota | Assunto |
| --- | --- |
| [Estrutura de memória](./context/2026-09-23-estrutura-memoria.md) | Convenções e limites |
| [Inventário técnico do Lenovo](./context/lenovo-80yh-inventario-e-testes.md) | Peças e verificações já realizadas |
| [FORMATAÇÃO CORRETA — projeto central](./projects/formatacao-correta/README.md) | **Leia antes de orientar qualquer intervenção no notebook** |
| [Correlações Windows ↔ Ubuntu](./projects/formatacao-correta/correlacoes-windows-ubuntu.md) | O que coincide e o que não coincide |
| [Três fases até a instalação limpa](./projects/formatacao-correta/execucao-em-tres-fases.md) | **Meta final: formatação correta após sanar impedimentos** |
| [Prioridades baseadas em provas](./projects/formatacao-correta/prioridades-e-provas.md) | Como escolher menor ação e encerrar |
| [Plano corretivo com encerramento](./projects/formatacao-correta/plano-corretivo.md) | Próximas decisões, sem auditoria infinita |
| [Procedimento de decisão e validação](./runbooks/formatacao-correta-ciclo-de-correcao.md) | Como não repetir tentativas |

## Como recuperar o entendimento

1. Consulte [AGENTS.md](./AGENTS.md), [protocolo](./context/protocolo-memoria-semantica.md) e [estado atual](./memory/STATE.yaml).
2. Leia a nota sobre o problema solicitado, mais [correlações](./projects/formatacao-correta/correlacoes-windows-ubuntu.md) e [fontes/lacunas](./projects/formatacao-correta/fontes-e-lacunas.md).
3. **Não transforme um resultado de agosto em estado atual de setembro.** Distinga log original, resumo anterior, declaração do usuário, inferência e correção verificada.
4. Não repita teste já encerrado sem justificar qual nova informação ele acrescentará.
5. Grave uma conclusão nova em nota atômica e atualize os índices somente quando houver conexão/autorização e ação efetivamente executada.

**Nota:** GitHub armazena o entendimento; não lê automaticamente todos os chats, não monitora o Lenovo e não executa consertos.