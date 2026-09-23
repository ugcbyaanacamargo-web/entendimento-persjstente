# FORMATAÇÃO CORRETA — execução em três fases até instalação limpa
**Decisão do usuário em 23/09/2026:** objetivo FINAL é notebook funcional depois de uma reinstalação limpa por pendrive. O agente é responsável por organizar as decisões, preparar instruções e conferir retornos; o usuário leigo recebe uma ação por vez. **Nenhuma ação no notebook foi executada ao escrever esta nota.**

**Antes de cada ação:** abrir [estado atual](../../memory/STATE.yaml) e [evidências](./registro-de-evidencias.md); registrar mudanças pelo [procedimento](../../runbooks/ingestao-de-resultados.md).

## 1 — Fechar o que já foi investigado (sem auditoria geral)
- **Concluído:** MemTest86 v11.7 Free final **PASS relatado pelo usuário** em 23/09; contagem final numérica não transcrita. Não exigir foto/celular nem repetir teste.
- Diagnóstico Lenovo por pendrive e SMART curto WD Green: usuário já informou que passaram. Não repetir.
- **Concluídos:** teste SATA/PHY e stress CPU/energia de 04/09 sem novos eventos-alvo durante as janelas examinadas. Não propor “reinicializar para finalizar RST” como se 29/08 ainda fosse hoje. [Resultados](./testes-04-09-resultados.md).
- Usar dados existentes: Ubuntu (FWTS/CHIPSEC/fwupd resumidos pelo usuário), Windows 10 (ACPI/EC, CPU limitada, WHEA/SATA, WinDbg, serviços, Store, drivers); Windows 11 (falhas relatadas, logs primários não recuperados).
- Um dado adicional SOMENTE se decidir uma ação específica: exemplo estado atual do controlador SATA se novo WHEA ocorrer. O relatório de 29/08 com reinicialização pendente não é o estado atual.
- Registrar cada ocorrência como: corrigir / deixar para pós-instalação / limitação da plataforma / encaminhar fabricante.

**Saída:** uma decisão por caso no [funil causal](./triagem-causal-consolidada.md) e na [matriz de provas](./prioridades-e-provas.md), não uma lista interminável de suspeitos.

## 2 — Resolver o que sobreviveria à formatação
- Segurança firmware: manufacturing mode e acesso flash relatados pelo Ubuntu exigem **referência e procedimento compatíveis com Lenovo NM-B242**, não F9/Secure Erase. BootGuard pode ser decidido em fabricação; não prometer habilitar recurso ausente nem mexer em fuses.
- ACPI/EC/energia: falhas nos dois sistemas. Escolher correção pequena e reversível dirigida ao problema real; validar carregador, frequência e suspensão/retorno. Firmware somente por procedimento OEM confirmado.
- Driver e componentes: corrigir apenas se o erro ainda estiver ativo; um driver por vez, pacote correto para hardware, backup/reversão quando possível.
- Se firmware só puder ser avaliado em bancada: entregar encaminhamento claro e **parar de mandar executar novas ferramentas**. Registrar limite/risco e obter decisão informada antes da formatação final.

**Saída:** problemas persistentes resolvidos, limitações explicitadas ou encaminhamento técnico objetivo.

## 3 — UMA instalação limpa e verificação de verdade
**Requer backup verificado e autorização específica antes de apagar partições.**
1. Mídia oficial do sistema escolhido e drivers confiáveis compatíveis com 80YH. Definir sistema suportado/limites de atualização antes da instalação.
2. Fotografar/registrar configurações de boot/SATA/UEFI existentes; NÃO supor que reset BIOS regrava Intel ME/BootGuard.
3. Identificar disco de destino inequivocamente; apagar partições somente com confirmação do usuário. Não executar Secure Erase como rotina.
4. Instalar offline quando viável; escolher e instalar drivers por subsistema e reinicializar conforme necessidade; controlar entrada de drivers pelo Windows Update antes de expor o sistema à rede quando for tecnicamente possível.
5. Testar uso real: inicialização, energia/suspensão, SSD, rede, áudio, Intel/NVIDIA, Store, atualizações, aplicativo que antes falhava e recorrência de tela azul/eventos alvo.

**Entrega:** computador utilizável, registro de versões e comprovação dos sintomas anteriormente problemáticos. Instalação limpa não promete que nenhum erro voltará jamais.

## Como conversar com o usuário
**Responder só: Faça agora [uma ação]. Envie [resultado].** Aviso curto de risco quando necessário. Explicação detalhada fica nesta memória GitHub. Não exigir que o usuário entenda os subsistemas para executar.

[Projeto](./README.md) · [Matriz de provas](./prioridades-e-provas.md) · [Casos](./plano-corretivo.md) · [Fontes](./fontes-e-lacunas.md).