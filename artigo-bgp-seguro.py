"""
Link:
https://research.google/pubs/youtube-hijacking-february-24th-2008-analysis-of-bgp-routing-dynamics/


Contexto: 
Em 2008, incidente BGP youtube fez com que parasse o canal por um dia inteiro


EXECUTIVE SUMMARY da nossa sessão de arquitetura e infraestrutura. 
Este resumo foi desenhado para ser sua "folha de consulta rápida" (Cheat Sheet) para revisões futuras.


💡 Resumo Executivo: O Incidente BGP YouTube (2008)

1. O Contexto (O Cenário)
O governo do Paquistão ordenou o bloqueio local do YouTube. Para isso, a Pakistan Telecom (AS17557) tentou criar um "buraco negro" (null route) para desviar o tráfego do site dentro do país.

2. O Erro (O Sequestro/Hijacking)
Os engenheiros anunciaram essa rota de bloqueio para o provedor global (PCCW).

Falha Técnica: Eles anunciaram um prefixo mais específico (/24) do que o anúncio original do YouTube (/22).

Consequência: Como o protocolo BGP prioriza a rota mais específica, o tráfego mundial "acreditou" que o caminho para o YouTube era através do Paquistão, resultando em um apagão global do serviço por cerca de 2 horas.

3. Termos Técnicos Essenciais
BGP (Border Gateway Protocol): O "GPS da Internet". Um protocolo de fofoca entre redes (Sistemas Autônomos) para decidir o melhor caminho para um IP.

AS (Autonomous System): Uma grande rede (ex: Google, Vivo, Paquistão Telecom) que possui um número de identificação único.

Prefixo (/24 vs /22): Define o tamanho do bloco de IPs. Quanto maior o número após a barra, mais específico é o endereço.

Null Route (Blackhole): Uma rota que descarta pacotes propositalmente.

RPKI: Tecnologia moderna de "assinatura digital" para evitar que alguém anuncie IPs que não possui.

4. Analogia de Ouro: A Malha Ferroviária
Infraestrutura Física (Trilhos): Os cabos de fibra óptica e roteadores físicos espalhados pelo mundo. São caminhos reais, mas "burros".

Lógica de Roteamento (BGP): O painel de controle dos trens. Se o controlador diz que o trem deve ir pela "Linha B" porque é mais curta, o trem vai, mesmo que a "Linha B" termine em um precipício (Buraco Negro). O BGP não checa se o destino é seguro, apenas se o caminho existe.

5. Aprendizados de Engenharia & Boas Práticas
A Internet é baseada em Confiança: O BGP clássico aceita o que o vizinho diz. Por isso, hoje usamos RPKI e Filtros de Rota.

Defesa em Profundidade (SRE): Como desenvolvedor Python/Full-stack, nunca confie 100% na rede. Sempre use Timeouts em suas requisições para evitar que sua aplicação trave em um "sequestro" de rota.

Observabilidade: Monitorar não apenas se o site está ON, mas por onde o pacote está passando (usando ferramentas como traceroute).

Automação Segura: Erros manuais em roteadores podem derrubar países. A prática de Infrastructure as Code (IaC) permite que mudanças sejam revisadas (Code Review) antes de 
irem ao ar.


### Código ###
import socket
import requests
import time
from typing import Dict

# ==========================================
# 1. O CÉREBRO DO ROTEADOR (SIMULAÇÃO BGP)
# ==========================================
class RoteadorSimulado:
    def __init__(self):
        # Tabela de Roteamento (Prefixo IP: Informações da Rota)
        self.tabela_bgp = {
            "208.65.152.0/22": {"dono": "YouTube Global", "via": "Google-ISP"}
        }

    def anunciar_rota(self, prefixo: str, dono: str, via: str):
        # Adiciona ou atualiza uma rota na tabela.

        self.tabela_bgp[prefixo] = {"dono": dono, "via": via}
        print(f"📢 NOVO ANÚNCIO BGP: {dono} agora clama o prefixo {prefixo}")

    def buscar_melhor_rota(self, ip_destino: str) -> dict:
        
        Lógica de 'Longest Prefix Match': 
        Se houver uma rota /24 (específica), ela vence a /22 (genérica).
        
        # Simulando a especificidade: se o IP contém o bloco do incidente
        if "208.65.153" in ip_destino:
            # Tenta achar a mais específica primeiro
            if "208.65.153.0/24" in self.tabela_bgp:
                return self.tabela_bgp["208.65.153.0/24"]
        return self.tabela_bgp.get("208.65.152.0/22")

# ==========================================
# 2. O MONITOR DE STATUS (REAL)
# ==========================================
def realizar_check_real(url: str, roteador: RoteadorSimulado):
    print(f"\n--- Iniciando requisição para {url} ---")
    
    # Passo A: Resolver o DNS (Transformar nome em IP)
    try:
        host = url.replace("https://", "").replace("http://", "").split('/')[0]
        ip_resolvido = socket.gethostbyname(host)
        print(f"🔍 DNS: {host} -> {ip_resolvido}")

        # Passo B: Consultar a Tabela BGP (Simulação)
        rota = roteador.buscar_melhor_rota(ip_resolvido)
        print(f"🛣️  ROTA BGP: O tráfego passará por: {rota['dono']} (Via {rota['via']})")

        # Passo C: Tentar conectar (Real)
        # Usamos timeout=3 para não travar se houver um "buraco negro"
        response = requests.get(url, timeout=3)
        print(f"✅ STATUS: {response.status_code} OK (Latência: {response.elapsed.total_seconds()*1000:.0f}ms)")
        
    except requests.exceptions.Timeout:
        print("⚠️ ALERTA: Timeout detectado! O tráfego caiu em um BURACO NEGRO (Blackhole).")
    except Exception as e:
        print(f"❌ ERRO: Falha na conexão: {e}")

# ==========================================
# 3. EXECUÇÃO DO CENÁRIO
# ==========================================
meu_roteador = RoteadorSimulado()

print("🚀 CENÁRIO 1: INTERNET FUNCIONANDO NORMALMENTE")
realizar_check_real("https://www.youtube.com", meu_roteador)

time.sleep(2) # Pausa dramática para simular o tempo real

print("\n🚀 CENÁRIO 2: O SEQUESTRO (ERRO DO PAQUISTÃO)")
# O Paquistão anuncia uma rota mais específica para o mesmo IP
meu_roteador.anunciar_rota("208.65.153.0/24", "Pakistan Telecom", "Null0-Blackhole")

# Agora tentamos acessar o mesmo site
realizar_check_real("https://www.youtube.com", meu_roteador)"""