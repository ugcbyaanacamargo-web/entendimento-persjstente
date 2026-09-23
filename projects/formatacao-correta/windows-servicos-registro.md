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
