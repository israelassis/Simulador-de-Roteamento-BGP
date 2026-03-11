🚀 Simulador de Roteamento BGP: Caso YouTube (2008)
Este projeto é um laboratório prático para consolidar conceitos de infraestrutura de rede, SRE e segurança cibernética, baseado na análise técnica da falha de roteamento que tirou o YouTube do ar em 24 de fevereiro de 2008.

📖 O Contexto Histórico
Em 2008, um anúncio de BGP (Border Gateway Protocol) mal configurado pela Pakistan Telecom para censurar o YouTube localmente acabou "vazando" para o mundo. O protocolo BGP priorizou a rota mais específica do Paquistão, desviando o tráfego global para um "buraco negro".

>> Como o mundo via as rotas antes do "sequestro"
```
rotas_internet = {
    "208.65.152.0/22": "Google/YouTube (AS15169)",
    "outros_ips": "Outras_Redes"
}

# O Paquistão enviou um anúncio mais específico (mais 'atrativo' para o protocolo)
anuncio_falso = {
    "208.65.153.0/24": "Pakistan Telecom (AS17557)" # Mais específico ganha!
}

def rotear_trafego(destino_ip):
    # O protocolo BGP prioriza o prefixo mais longo/específico
    if destino_ip in anuncio_falso:
        enviar_para("Paquistão") # O tráfego 'cai' aqui e morre.
    else:
        enviar_para("Destino Correto")
````
<br>

🎯 Objetivos do Aprendizado
BGP Hijacking: Entender como anúncios de rotas falsas podem sequestrar tráfego.

Longest Prefix Match: Compreender por que uma rota /24 vence uma /22.

Resiliência (Python): Implementar lógica de timeout para evitar travamentos em falhas de rede.

Arquitetura Modular: Organização de projetos seguindo o padrão Flask/SQLAlchemy.

🛠️ Tecnologias Utilizadas
Python 3.x

Flask (Interface Web)

SQLAlchemy (Abstração de Banco de Dados)

Requests (Monitoramento de Status)

📁 Estrutura do Projeto
Plaintext
├── app.py           # Ponto de entrada e rotas Flask
├── database.py      # Configuração e inicialização do DB
├── models.py        # Definição das tabelas (Rotas/Histórico)
├── requirements.txt # Dependências do projeto
├── static/          # CSS e Assets visuais
└── templates/       # Interface HTML do simulador
🔗 Referência Técnica
O estudo de caso foi baseado no paper oficial do Google Research:
YouTube Hijacking: Analysis of BGP Routing Dynamics