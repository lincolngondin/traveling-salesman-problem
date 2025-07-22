type Distancia = float
# cada cidade é formada por uma lista de tuplas de dois elementos
# a distancia da cidade conectada e o nome da cidade conectada obrigatoriamente nessa ordem
type Cidade = list[tuple[Distancia, str]]
class Grafo:
    def __init__(self):
        self.cidades: dict[str, Cidade] = dict()

    def adicionarCidade(self, cidade: str):
        # se a cidade ja não foi adicionada antes
        if cidade not in self.cidades:
            self.cidades[cidade] = list()
    def conectarCidade(self, cidade: str, distancia: Distancia, cidadeAConectar: str):
        # se a cidade a qual esta tentado adicionar as conexoes não existe, nao fazer nada
        # a cidade a conectar pode ou não existir, essa funcao nao checa isso (rever isso aqui dps).
        if cidade in self.cidades:
            self.cidades[cidade].append((distancia, cidadeAConectar))
    def getCidade(self, cidade) -> Cidade:
        return self.cidades[cidade]