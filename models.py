# No BGP, a regra básica é: "Sempre prefira o caminho com o menor AS-PATH"
# Best Path Selection (Seleção de Melhor Caminho)
# AS-PATH Length (comprimento do caminho) é o pilar que um desenvolvedor Júnior deve dominar

class Route:
    def __init__(self, prefix, as_path):
        self.prefix = prefix
        self.as_path = as_path  # Lista de IDs de AS

class Router:
    def __init__(self, asn):
        self.asn = asn
        self.routing_table = {}  # { "10.0.0.0/24": RouteObject }
        self.neighbors = []

    def add_neighbor(self, neighbor_router):
        # Como conectar dois roteadores?
        pass

    def announce(self, route):
        # Como enviar isso para os vizinhos?
        pass

    
        # Aqui entra a lógica: eu aceito essa rota? 
        # Ela é melhor que a que eu já tenho?
        def receive_route(self, new_route):
            prefix = new_route.prefix
        
        # 1. Detecção de Loop: Eu já estou nesse caminho?
            if self.asn in new_route.as_path:
                return  # Ignora para evitar loop

        # 2. Se eu não conheço esse prefixo, eu aceito logo de cara
            if prefix not in self.routing_table:
                self.routing_table[prefix] = new_route
                self.propagate(new_route) # Avisar os vizinhos!
            else:
            # 3. A lógica que você definiu: Comparar saltos
                current_route = self.routing_table[prefix]
                if len(new_route.as_path) < len(current_route.as_path):
                    self.routing_table[prefix] = new_route
                    self.propagate(new_route)