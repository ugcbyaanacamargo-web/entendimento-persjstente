# Windows — servicing, Store/AppX, serviços e Registro

**Fontes:** logs `Texto colado.txt`, `Texto colado(20260913-021922).txt` e auditoria DCOM/instalação/permissões de 12/09. Problemas ESPECÍFICOS do Windows, não eventos idênticos ao Ubuntu.

## Ocorrências objetivas
- Desde início da instalação 22/08: `0x800F0984`, arquivo esperado `wvmbusr.inf` ausente numa operação de atualização/manutenção do Windows. Não atribuir a BIOS/SSD sem conexão comprovada.
- AppX/Store: `0x80073D02` em operações que exigiam fechar aplicativo; outros erros como `0x80070490`, `0x8007042B`, `0x8007010B`. Cada código tem causa/condição própria.
- 05/09: falhas de inicialização de `AppXSvc` dependente de `StateRepository`, `AudioEndpointBuilder` (logon `SYSTEM`), `Audiosrv`, entre outros. Ocorrências históricas, não necessariamente falhas presentes após reparos.
- DCOM 10016 para PerAppRuntimeBroker recorrente; auditoria específica de 12/09 encontrou proprietário `TrustedInstaller`, assinatura válida do RuntimeBroker e **sem override HKCU para aqueles CLSID/APPID**. Não “liberar” permissões por número de eventos.
- Auditoria separada sinalizou ACL/herança em algumas chaves de `HKLM\\SOFTWARE\\Classes` e diferenças HKCU/HKLM; **a existência de ACL protegida/herança desativada ou diferença de classes não prova corrupção de Registro**. Vincular mudança a falha reproduzível antes de modificar.

## Estado posterior
DISM/SFC e reparos Store/AppX executados em setembro; Ferramenta de Captura/ScreenClippingHost apresentou falha persistente em relato posterior. Não classificar Store ou todo Windows como resolvido só pelo êxito do DISM.

## Correção visada
Verificar somente a funcionalidade que ainda falha; corrigir arquivo/pacote/serviço/ACL preciso com backup e validação. **Nunca resetar todo HKLM/HKCU ou reatribuir permissões de TrustedInstaller em lote.**

[Correlações](./correlacoes-windows-ubuntu.md) · [Plano](./plano-corretivo.md) · [Linha do tempo](./linha-do-tempo.md).
## Recorrencia observada por Codex local, 23/09 ~17h30

- AppX 0x80073D02 (Codex/PC Manager, 23/09): erro especifico de pacote em uso; evento 419 indicou aplicativo aberto. Para essa instalacao, fechar o aplicativo indicado e tentar a atualizacao focalizada. Referencia Microsoft: https://learn.microsoft.com/en-us/windows/win32/appxpkg/troubleshooting.
- PowerShell empacotado: AppModel-Runtime 208/212, 0x80070005; falha de ativacao real em 23/09, sem prova de ACL geral danificada.
- Store: Push-To-Install 6003, 0x80072ee7, falha de comunicacao sem causa de rede determinada.
- Energy Server Service queencreek: 7034 em 21 e 23/09; servico estava executando na consulta posterior. uhssvc 7000 em 11/09 (arquivo nao encontrado), atualmente parado/desabilitado.
- Eventos Update de 01/01/2027 tem horario inconsistente, nao classificar como falha recente: auditoria anterior ja associara saltos de data a Lenovo Diagnostics/RTC test, mas este conjunto novo nao foi ligado individualmente ao teste.

Nenhum item acima e causa demonstrada do BugCheck 0x1A. Fonte [EV-12](./registro-de-evidencias.md).

## Correcao focalizada executada pelo Desktop Commander em 23/09 (EV-21)

O programa OPT-IN Intel Computing Improvement Program, associado aos avisos de encerramento inesperado `ESRV_SVC_QUEENCREEK` (SCM 7034), foi removido por seus desinstaladores oficiais MSI/bundle com retorno 0, apos criar ponto de restauracao. Verificacao independente: servicos e processos QUEENCREEK ausentes, driver `semav6msr64` removido, nenhum registro do aplicativo persistiu; drivers essenciais Intel RST e Intel MEI intactos. **Falha de servico historica tratada pela remocao do componente opcional**; nao confundir com correcao confirmada da tela azul nem de AppX/Store. [EV-21](./registro-de-evidencias.md).

## Verificacao direta de 23/09 ~20h33 (EV-23)

O Windows ja concluiu as atualizacoes anteriormente bloqueadas com `0x80073D02`: PC Manager **3.22.6.0** e Codex **26.917.6896.0** aparecem como `Status Ok`; PowerShell empacotado 7.6.6 tambem `Status Ok` e uma invocacao real de `pwsh` retornou `PWSH_OK`. **Nao executar re-registro em massa nem repetir instalacao das duas atualizacoes**. Store Push-To-Install `0x80072ee7` consta as 16h42, mas sem teste de endpoint/funcao atual nao escolher reset de DNS, proxy ou Registro. Servicos Queencreek removidos e nenhum novo 7034 apos as 20h20 naquela janela. [EV-23](./registro-de-evidencias.md).

## CASO ATUAL — ScreenClippingHost Event1000 em 23/09 ~21h00 (EV-27 a EV-29)

- 4 falhas de `ScreenClippingHost.exe` 20h47–21h00, `ScreenClipping.dll`, excecao `0xc000027b`. `ms-screenclip:` reproduziu tres vezes: 21h09, 21h11, 21h15. **Esta e falha funcional atual; nao apenas lista antiga**.
- `MicrosoftWindows.Client.CBS` Status Ok/manifest presente; `CaptureService` e `StateRepository` ativos; preferencia `PrintScreenKeyForSnippingEnabled=0` preservada para PrintScreen classico.
- Um re-registro SOMENTE CBS inicial falhou `0x80073D02` (pacote em uso por `TextInputHost`); segundo com `-ForceTargetApplicationShutdown` concluiu, mas reteste 21h11 criou novo Event1000. **Nao repetir/nao chamar resolvido**. Documentacao Microsoft [reparo apps](https://learn.microsoft.com/en-us/troubleshoot/windows-client/shell-experience/modern-inbox-store-apps-troubleshooting-guidance) e [Add-AppxPackage](https://learn.microsoft.com/en-us/powershell/module/appx/add-appxpackage).
- WER LocalDumps temporario por aplicativo foi REMOVIDO; dump de aplicativo foi localizado APOS atraso de gravacao e analisado pelo WinDbgX instalado: `STOWED_EXCEPTION_c000027b_combase.dll`, `ScreenClipping!StartApplication`, HRESULT interno **0x80270301 = E_SHELL_EXTENSION_BLOCKED**. Em 19h17 `SearchApp.exe` tambem caiu `0xc000027b` e relatou mesmo HRESULT no WER; pista de ativacao Shell comum, mas **nenhuma extensao, CLSID, politica ou ACL foi identificada como causa**. Chaves usuais `Shell Extensions\\Blocked` e `Policies\\Explorer` consultadas estavam ausentes; ausencia nao exclui outras fontes de bloqueio.
- NENHUM Driver Verifier, dump kernel inducido, DISM/SFC repetido, reset CBS data/registro global, Windows reinstalado ou reiniciado nesta etapa. Dumps e logs detalhados sao locais/privados. [Registro EV-27–29](./registro-de-evidencias.md).

### Adendo definitivo da ETAPA de captura de dump (23/09 ~21h21)

Foi criado **um full dump somente do processo ScreenClippingHost (274.635.594 bytes)** no disco local após uma reprodução focal, com WER LocalDumps temporário por aplicativo e REMOVIDO no fim. WinDbgX do dump completo confirmou **`STOWED_EXCEPTION_80270301`** e pilha original passando por `vccorlib140_app!__abi_WinRTraiseCOMException` e `ScreenClipping.dll`/COM/RPC. O código é `E_SHELL_EXTENSION_BLOCKED`: identifica classe de falha do Shell, NÃO identifica sozinho extensão, CLSID nem origem da restrição. O WinDbgX local não possui a extensão opcional PDE; símbolos públicos não expõem o tipo privado de COM. O app permaneceu quebrado em todos os testes (ate 21h21). **Nao repetir o re-registro CBS, gerar novos crashes ou mudar ACLs aleatoriamente**. Pela janela 20h20–21h22, `EngHost.exe` caiu uma vez 20h31 (problema de cache de símbolos no log .NET); depois WinDbgX concluiu analises dos dumps. Queencreek não apresentou mais 7034 após remoção. [EV-30](./registro-de-evidencias.md). Microsoft descreve `0xc000027b` como stowed exception: https://learn.microsoft.com/en-us/shows/inside/c000027b .
