import random
from grafo import Grafo

# implementacao da algoritmo heuristico vizinho mais proximo(Nearest Neighbour)
# para a resolucao do problema do caixeiro viajante
# retorna a lista de cidade vizitadas
def nearestNeighbour(grafo: Grafo) -> list[str]:
    cidades = grafo.getTodasAsCidades()
    if not cidades:
        return []
    # cria o dicionario de todas as cidade e inicializa elas como não visitadas(False)
    visiteds: dict[str, bool] = {key: False for key in cidades}
    # comeca de uma cidade aleatoria
    u: str = random.choice(cidades)
    visiteds[u] = True

    # cria a lista de caminhos visitados
    caminho: list[str] = [u]

    while len(caminho) < len(cidades):
        vizinhos = grafo.getCidadesVizinhas(u)

        # filtra vizinhos ainda não visitados
        vizinhosNaoVisitados = [(dist, cidade) for dist, cidade in vizinhos if not visiteds[cidade]]

        if not vizinhosNaoVisitados:
            # se não há mais vizinhos não visitados conectados, termina o grafo (possivelmente desconexo)
            break

        # escolhe o vizinho mais próximo (menor distância)
        _, proximaCidade = min(vizinhosNaoVisitados, key=lambda x: x[0])

        # marca como visitada e atualiza a cidade atual
        visiteds[proximaCidade] = True
        caminho.append(proximaCidade)
        u = proximaCidade

    return caminho