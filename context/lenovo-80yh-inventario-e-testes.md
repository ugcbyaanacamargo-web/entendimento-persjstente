# Lenovo 320-15IKB 80YH — inventário e testes

**Revisão:** 2026-09-23. **Classe:** fatos do equipamento e resultados históricos; dados individuais identificadores omitidos por o repositório ser público.

## Hardware relatado/documentado
- Lenovo IdeaPad 320-15IKB, Type 80YH, placa NM-B242 Rev. 1.0.
- Intel Core i7-7500U / Intel HD Graphics 620; NVIDIA GeForce 940MX com 4 GB GDDR5 dedicados.
- 16 GB DDR4 em **um** SO-DIMM Samsung, canal único; Wi-Fi Intel Wireless-AC 3165.
- SSD WD Green SATA 2,5 pol., 1 TB, instalado em substituição ao armazenamento de origem.
- BIOS Lenovo **4WCN47WW** e EC **1.47** em coleta de 29/08/2026; TPM Intel PTT 2.0 reconhecido; chipset INF 10.1.1.45 e MEI/HECI 1828.12.0.1152 no snapshot.
- Componentes fotografados: EC ITE IT8586E e flash SPI Winbond W25Q64FV; identificação de chip não é laudo de defeito.

## Testes já efetuados — não recomendar automaticamente outra vez
| Verificação | Último resultado conhecido | Limite |
| --- | --- | --- |
| Diagnóstico Lenovo pelo pendrive | Usuário confirmou **sem erros**, antes do MemTest86 | Não verifica todas as condições intermitentes/firmware |
| SMART curto WD Green | Aprovado, sem erros apresentados | Não encerra os WHEA da comunicação SATA |
| SSD firmware | Dashboard exibiu versão 42077100 como atualizada | Versão declarada não prova integridade de todos os dados |
| MemTest86 v11.7 Free | Foto em 23/09: **passagem 1 completa sem erros; passagem 2/4 com 75%, total 0** | **Resultado final de quatro passagens ainda não fornecido nesta conversa** |
| Windows DISM/SFC | Conclusões bem-sucedidas em coletas/reparos distintos | Não equivale a Store ou BSOD funcionalmente resolvidos |
| NVIDIA Windows | GPU 940MX acionou em teste 3D | Não elimina falha nvidia-smi no Ubuntu |

## Segurança
Não gravar neste GitHub número de série, UUID, credenciais, nomes de conta nem logs brutos com esses dados.

[Índice do projeto](../projects/formatacao-correta/README.md) · [Memória/BSOD](../projects/formatacao-correta/memoria-e-tela-azul.md) · [Armazenamento](../projects/formatacao-correta/armazenamento-e-whea.md).