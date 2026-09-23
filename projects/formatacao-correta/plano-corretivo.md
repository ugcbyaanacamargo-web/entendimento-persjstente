# Plano de correção com decisões e encerramento — Lenovo 80YH

**Este plano prepara a instalação limpa FINAL solicitada pelo usuário; não propõe repetição de formatações.** Veja [roteiro em três fases](./execucao-em-tres-fases.md) e [prioridades](./prioridades-e-provas.md). Cada caso deve ter: erro original → mudança única/encaminhamento → repetição da operação real → resultado. Ler [ciclo de correção](../../runbooks/formatacao-correta-ciclo-de-correcao.md).

| Caso | Próxima decisão limitada | Critério de encerramento | Ação indevida |
| --- | --- | --- | --- |
| Firmware segurança | Usar resultados já obtidos Ubuntu para montar pedido técnico Lenovo/especialista NM-B242: estado Manufacturing Mode, bloqueios flash e BootGuard **segundo baseline desta revisão**; obter laudo/procedimento seguro antes de alterar | Estado conferido com referência e, se reparável, correção específica validada | Gravar imagem genérica, fusíveis, limpar PTT/chaves |
| ACPI/EC/energia | Sintoma e eventos Windows/Ubuntu; stress de 04/09 não reproduziu Event37/ACPI; revisar plano energia reversível AC somente se sintoma atual, ACPIVPC, Serial IO **um item por vez**. Firmware só por procedimento OEM validado | Energia/suspensão/retorno sem repetição do defeito original; eventos-alvo avaliados em intervalo definido | Misturar cinco drivers |
| BSOD/memória | **MemTest86 PASS final relatado 23/09: exame encerrado.** Conservar dump 0x1A/0x41792; só reabrir RAM por evento novo | MemTest registrado e tela azul somente encerrada se causa específica isolada ou falha não reproduzível sob teste definido | “Zero erros = BIOS causou” ou comprar RAM |
| SATA/WHEA | Os 3 WHEA são históricos; teste SATA/PHY de 04/09 não reproduziu falhas, controlador Intel consta iniciado. Só reabrir com ocorrência nova | Não reaparece erro correlato na operação reproduzível; storage funciona | Trocar SSD apesar de SMART sem outros indícios |
| WLAN | Se Event 5007 reaparecer e rede falhar, comparar pacote OEM compatível com driver atual em teste isolado | Uso real da rede sem fila travada na janela de validação | Atualizador indiscriminado |
| Windows servicing/Store | Testar a FUNÇÃO atualmente quebrada; conferir 0x800F0984 ou erro específico pós-DISM, corrigir componente e checar aplicativo | Atualização/aplicativo abre e instala | “DISM 100% = Store curada” |
| Registro/ACL | Somente erro reproduzível vinculado à chave; backup ACL/valores e ajuste mínimo | Função funciona, permissões preservadas | Liberar HKLM inteiro/TrustedInstaller |
| NVIDIA Linux | Se Ubuntu voltar a ser SO, conferir PRIME/driver e reproduzir comando/função | GPU ativa em aplicativo destinado | Concluir GPU avariada com base em `nvidia-smi` |

## Ordem sem investigação infinita
1. **Concluído:** MemTest86 PASS relatado, Lenovo Diagnostics, SMART WD, SATA/PHY 04/09 e stress CPU 04/09. Não repetir.
2. **Abrir caso técnico de firmware baseado nos dados Ubuntu já coletados.** Obter referência específica de produção antes de gravar qualquer coisa; fechar por laudo se irreparável na plataforma.
3. **Resolver a comunicação de energia/ACPI** com mudanças pequenas e reversíveis guiadas pelo sintoma. 
4. **Encerrar separadamente** armazenamento/WHEA, Windows servicing/AppX/Registro, WLAN/GPU e tela azul: não culpar uma camada apenas por ocorrer no mesmo notebook.
5. **Fase final solicitada:** depois de fechar/encaminhar impedimentos persistentes e confirmar backup, realizar UMA instalação limpa oficial pelo pendrive, drivers escolhidos por hardware, validação de uso real. Isso não altera firmware persistente.

## Portas de saída
- **Corrigido:** sintoma original não ocorre no teste reproduzível, estado antes/depois documentado.
- **Limitado pela plataforma:** comprovar baseline fabricante; registrar recurso indisponível sem rodar laços de auditoria.
- **Requer reparo especializado:** entregar laudo/achados e não tentar flash inseguro.
- **Sem nexo identificado:** descrever o evento exato que falta, sem fabricar conclusão ou abrir investigação geral.

[Funil](./triagem-causal-consolidada.md) · [Projeto](./README.md) · [Correlações](./correlacoes-windows-ubuntu.md) · [Fontes](./fontes-e-lacunas.md).