# 🚀 Simulador de Roteamento BGP: O Caso YouTube (2008)

Este projeto é um laboratório prático desenvolvido para consolidar conhecimentos em **Redes de Computadores**, **SRE (Site Reliability Engineering)** e **Desenvolvimento Full-stack com Python**. A aplicação simula o incidente real ocorrido em 24 de fevereiro de 2008, onde uma falha de configuração de BGP tirou o YouTube do ar globalmente.

## 📖 Contexto do Incidente
Em 2008, a **Pakistan Telecom** tentou bloquear o acesso ao YouTube internamente seguindo ordens governamentais. Ao anunciar uma rota BGP mais específica (`/24`) para o mundo, o tráfego global foi "sequestrado" (BGP Hijacking), pois o protocolo prioriza o prefixo mais longo. Isso resultou em um "buraco negro" (blackhole) que interrompeu o serviço por cerca de duas horas.



## 🎯 Objetivos do Aprendizado
* **BGP Hijacking:** Simulação de como anúncios de rotas falsas impactam o tráfego global.
* **Longest Prefix Match:** Entendimento prático de por que uma rota mais específica tem prioridade no roteamento.
* **Resiliência em Python:** Implementação de `timeouts` em requisições para evitar travamentos de software em falhas de rede.
* **Arquitetura Modular:** Organização de projeto seguindo boas práticas (Separação de responsabilidades em `models`, `logic` e `app`).

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python 3.x
* **Framework Web:** Flask (para o Dashboard de monitoramento)
* **ORM:** SQLAlchemy (abstração de banco de dados SQLite/PostgreSQL)
* **Controle de Versão:** Git & GitHub

## 📂 Estrutura do Projeto
```text
├── app.py              # Ponto de entrada e rotas da aplicação
├── database.py         # Configuração e inicialização do Banco de Dados
├── models.py           # Definição das classes e tabelas (SQLAlchemy)
├── requirements.txt    # Gerenciamento de dependências
├── static/             # Arquivos CSS e assets visuais
└── templates/          # Interfaces HTML (Jinja2)
