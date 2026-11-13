# Automação de Gerência de Redes com Python e Paramiko

Repositório com a implementação completa dos **11 estudos de caso** de automação de infraestrutura e gerência de redes via SSH e SFTP, utilizando **Python 3** e a biblioteca **Paramiko** em ambiente Linux (WSL 2 / Ubuntu).

## Sumário

- [Visão Geral e Arquitetura](#visão-geral-e-arquitetura)
- [Pré-requisitos e Configuração do Ambiente](#pré-requisitos-e-configuração-do-ambiente)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Guia dos Estudos de Caso (1 a 11)](#guia-dos-estudos-de-caso-1-a-11)
- [Diagrama de Topologia — Bastion Host (Caso 10)](#diagrama-de-topologia--bastion-host-caso-10)
- [Respostas das Perguntas de Reflexão](#respostas-das-perguntas-de-reflexão)
- [Boas Práticas de Segurança Aplicadas](#boas-práticas-de-segurança-aplicadas)

---

## Visão Geral e Arquitetura

O laboratório simula um ambiente multi-equipamento local através de usuários isolados no sistema operacional (`r1`, `r2`, `r3` e `bastion`) e múltiplas instâncias do serviço `sshd` (portas `22` e `2222`), permitindo validar cenários reais de operação de redes sem depender de hardware físico dedicado:

* **Gerência centralizada:** Inventário estruturado em `inventario.json` e módulo compartilhado de conexão (`conexao.py`).
* **Transferência e auditoria:** Uso de SFTP para backups com retenção, distribuição de scripts com validação SHA-256 e detecção de *configuration drift*.
* **Concorrência e resiliência:** Monitoramento paralelo com `ThreadPoolExecutor`, tunelamento via *Bastion Host* (`direct-tcpip`) e tratamento de falhas com *exponential backoff*.

---

## Pré-requisitos e Configuração do Ambiente

### 1. Dependências do Sistema e Python
No terminal Linux (Ubuntu / WSL 2), garanta que o servidor SSH e o ambiente virtual estejam ativos:

```bash
sudo apt update && sudo apt install -y python3-venv openssh-server
sudo service ssh start

python3 -m venv venv-linux
source venv-linux/bin/activate
pip install paramiko
