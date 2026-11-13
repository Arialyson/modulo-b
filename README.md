# 🐍 Automação de Gerência de Redes com Python e Paramiko

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Paramiko](https://img.shields.io/badge/Paramiko-SSHv2%20%2F%20SFTP-2B5B84?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Ubuntu-WSL%202-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![OpenSSH](https://img.shields.io/badge/OpenSSH-Server-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo%20(11%2F11%20Casos)-success?style=for-the-badge)

> **Projeto Integrador — Gerência de Redes**  
> Implementação completa dos **11 estudos de caso** de automação de infraestrutura e gerência de dispositivos via **SSH** e **SFTP**, utilizando **Python 3** e a biblioteca **Paramiko**.

---

## 📑 Sumário

- [🌐 Visão Geral e Arquitetura](#-visão-geral-e-arquitetura)
- [⚙️ Pré-requisitos e Configuração do Ambiente](#️-pré-requisitos-e-configuração-do-ambiente)
- [📂 Estrutura do Repositório](#-estrutura-do-repositório)
- [🚀 Guia dos Estudos de Caso (01 a 11)](#-guia-dos-estudos-de-caso-01-a-11)
- [🛡️ Diagrama de Topologia — Bastion Host (Caso 10)](#️-diagrama-de-topologia--bastion-host-caso-10)
- [🎓 Respostas das Perguntas de Reflexão (Defesa N2)](#-respostas-das-perguntas-de-reflexão-defesa-n2)
- [🔒 Boas Práticas de Segurança Aplicadas](#-boas-práticas-de-segurança-aplicadas)

---

## 🌐 Visão Geral e Arquitetura

O laboratório simula um ambiente multi-equipamento local através de usuários isolados no sistema operacional Linux (`r1`, `r2`, `r3` e `bastion`) e múltiplas instâncias do serviço `sshd` (portas `22` e `2222`), permitindo validar cenários reais de operação de redes sem depender de hardware físico dedicado:

* 🗂️ **Gerência Centralizada:** Inventário estruturado em `inventario.json` e módulo compartilhado de conexão (`conexao.py`).
* 📦 **Transferência e Auditoria:** Uso de SFTP para backups com retenção automática, distribuição de scripts com validação criptográfica SHA-256 e detecção de *configuration drift*.
* ⚡ **Concorrência e Resiliência:** Monitoramento paralelo com `ThreadPoolExecutor`, tunelamento via *Bastion Host* (`direct-tcpip`) e tratamento inteligente de falhas com *exponential backoff*.

---

## ⚙️ Pré-requisitos e Configuração do Ambiente

### 1️⃣ Dependências do Sistema e Ambiente Virtual Python
No terminal Linux (**Ubuntu / WSL 2**), instale os pacotes necessários, inicie o servidor SSH e ative o ambiente virtual:

```bash
sudo apt update && sudo apt install -y python3-venv openssh-server
sudo service ssh start

python3 -m venv venv-linux
source venv-linux/bin/activate
pip install paramiko
