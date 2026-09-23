# Tela azul de 23/09 e RAM — o que foi demonstrado

**Evidência:** texto WinDbg `Markdown(1).md colado`, dump `092326-11734-01.dmp`; fotos parciais do MemTest86 e resultado final informado pelo usuário em 23/09/2026.

- `MEMORY_MANAGEMENT` / Bugcheck `0x1A`, parâmetro `0x41792`.
- Bucket `MEMORY_CORRUPTION_ONE_BIT`; uma entrada usada no gerenciamento da memória estava corrompida.
- `msedge.exe` é o processo registrado no momento, **não autor da corrupção identificado**.
- Diagnóstico Lenovo por pendrive terminou sem erros, segundo usuário.
- MemTest86 v11.7 Free: fotos registraram até a quarta passagem em 66%, com **0 erros acumulados naquele momento**. O usuário voltou ao computador e informou **PASS final**. Resultado de 4/4 comunicado, sem foto final; contagem numérica final não transcrita. **Teste encerrado; não repetir sem nova evidência.**
- RAM física: um módulo Samsung DDR4 de 16 GB. PASS no teste completo reduz a suspeita de defeito da RAM reproduzível nesse teste, mas não identifica o responsável pela tela azul nem elimina falha intermitente.

## Hipóteses abertas, sem ranking artificial
Driver/dispositivo escrevendo memória indevida; caminho RAM/controlador de memória sob condições não testadas; outras instabilidades em operação do sistema. ACPI/EC e CSME existem em paralelo, mas **não há elo demonstrado entre Manufacturing Mode e o bit corrompido**.

## Gatilho para encerrar etapa
**Teste MemTest86 encerrado com PASS informado em 23/09**; não pedir fotografia final nem outro MemTest automaticamente. A tela azul continua caso separado, e o agente só atribuirá autor a partir de evidência específica. [Funil atualizado](./triagem-causal-consolidada.md).

[Inventário](../../context/lenovo-80yh-inventario-e-testes.md) · [ACPI](./acpi-ec-energia-tpm.md) · [Plano](./plano-corretivo.md).
## Analise local intermediaria (23/09 ~17h30; substituida pelo adendo abaixo)

Codex localizou minidumps de 05/09 e 23/09, alem de MEMORY.DMP de ~2,5 GB. Na PRIMEIRA VERSAO do relatorio, uma chamada composta pela ferramenta foi recusada e a depuracao ainda nao havia sido refeita; **a analise foi concluida em uma versao posterior do mesmo dia, abaixo**. WinDbg anterior havia detectado PTE corrompida, sem identificar quem modificou a memoria. Nenhum dispositivo presente apresentou codigo PnP de erro na consulta local. Fonte [EV-14](./registro-de-evidencias.md). Nao inferir que Event 37 contemporaneo causou a tela azul.

## Nova descoberta nos dumps ORIGINAIS em 23/09

O ZIP da coleta contém `090526-19265-01.dmp` e `092326-11734-01.dmp`. Os cabeçalhos brutos de AMBOS confirmam BugCheck 0x1A, Arg1 0x41792, Arg3 0x8000000000 e Arg4 0; Arg2 (endereço da PTE) é diferente. Portanto, não se trata de uma primeira ou única tela azul: a **mesma classe de corrupção de PTE voltou em 18 dias**. A primeira saída WinDbg examinava 23/09. A análise POSTERIOR do próprio dia abriu ambos os minidumps e o dump completo, conforme adendo abaixo; no dia 05/09 a pilha permaneceu limitada por símbolos incompletos. Os cabeçalhos não revelam o autor. [Confronto global](./confronto-global-23-09.md) e [EV-15](./registro-de-evidencias.md).

## Adendo posterior — WinDbgX executado nos tres dumps em 23/09 (EV-19/20)

O usuário enviou `EXPLICACAO_RELATORIO_LENOVO.md` e `DIAGNOSTICO_DIRETO_LENOVO(1).md`, resumos da **análise local efetivamente realizada** com `!analyze -v`: minidumps 05/09 e 23/09, mais `MEMORY.DMP` do 23/09. Ambos os episódios: `0x1A / 0x41792`, `MEMORY_CORRUPTION_ONE_BIT`, `FAILURE_ID_HASH {e3faf315-c3d0-81db-819a-6c43d23c63a7}`. O hash igual indica mesma assinatura de classificação, NÃO comprova um mesmo driver culpado.

No dump de 23/09 e no completo, símbolos locais do kernel permitiram identificar **ONDE ocorreu a detecção**: `nt!MiDeletePagablePteRange`, ao liberar memória de `msedge.exe`. Nem `msedge.exe`, nem `PawnIO`, nem `MODULE_NAME: hardware` identificam o escritor da PTE. O dump de 05/09 apresentou `WRONG_SYMBOLS_TIMESTAMP/SIZE` por símbolos locais incompatíveis/ausentes e, portanto, não permitiu comparar com confiabilidade sua pilha. **A ação de repetir WinDbgX está ENCERRADA; o autor da corrupção permanece desconhecido.** Não pedir outra vez `!analyze -v` desses arquivos.

`verifier /query` retornou `No drivers are currently verified.`. A mensagem anterior `blocked by policy` era da CHAMADA COMPOSTA usada pela ferramenta, não evidência de bloqueio do depurador pelo Windows. Driver Verifier NÃO foi ativado. Possível investigação futura: primeiro preparar análise de risco/recuperação de boot e seleção restrita de drivers de terceiros; só executar após autorização explícita e mecanismo de retorno seguro, pois pode causar novo BSOD ou loop de inicialização. Os achados de firmware do Ubuntu continuam caso independente e não foram medidos de novo no Windows.

[Provas EV-19/20](./registro-de-evidencias.md) · [Confronto global](./confronto-global-23-09.md) · [Estado oficial](../../memory/STATE.yaml).
