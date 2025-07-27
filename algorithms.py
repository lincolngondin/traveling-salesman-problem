import random
from grafo import Grafo
from itertools import combinations

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

    # tenta retornar à cidade de origem
    cidadeOrigem = caminho[0]
    vizinhos = grafo.getCidadesVizinhas(u)
    if any(vizinho == cidadeOrigem for _, vizinho in vizinhos):
        caminho.append(cidadeOrigem)

    return caminho



def heldKarp(grafo: Grafo) -> list[str]:
    import math

    cidades = grafo.getTodasAsCidades()
    n = len(cidades)
    index_cidade = {cidade: i for i, cidade in enumerate(cidades)}
    cidade_por_index = {i: cidade for cidade, i in index_cidade.items()}

    # matriz de distâncias
    dist = [[math.inf] * n for _ in range(n)]
    for cidade in cidades:
        u = index_cidade[cidade]
        for d, vizinha in grafo.getCidade(cidade):
            v = index_cidade[vizinha]
            dist[u][v] = d

    # memo[(subset, last)] = (custo, penúltima cidade)
    memo = {}

    # Subconjuntos com apenas uma cidade (exceto a inicial)
    for k in range(1, n):
        memo[(frozenset([k]), k)] = (dist[0][k], 0)

    # tamanhos de subconjuntos de 2 até n-1
    for s in range(2, n):
        for subset in combinations(range(1, n), s):
            subset_frozen = frozenset(subset)
            for k in subset:
                prev_subset = subset_frozen - {k}
                min_cost = math.inf
                prev_city = None
                for m in prev_subset:
                    cost = memo[(prev_subset, m)][0] + dist[m][k]
                    if cost < min_cost:
                        min_cost = cost
                        prev_city = m
                memo[(subset_frozen, k)] = (min_cost, prev_city)

    # fim: volta à cidade inicial
    all_cities = frozenset(range(1, n))
    min_total_cost = math.inf
    last_city = None
    for k in range(1, n):
        cost = memo[(all_cities, k)][0] + dist[k][0]
        if cost < min_total_cost:
            min_total_cost = cost
            last_city = k

    # reconstruir caminho
    path = [0]
    subset = frozenset(range(1, n))
    current = last_city
    while subset:
        path.append(current)
        _, prev = memo[(subset, current)]
        subset = subset - {current}
        current = prev
    path.append(0)  # volta à cidade inicial
    path = path[::-1]

    return [cidade_por_index[i] for i in path]

import time

def medir_tempo_execucao(func, *args, **kwargs):
    inicio = time.time() #guardamos o tempo em que se inicia
    resultado = func(*args, **kwargs)
    fim = time.time() #marca  o fim da excução
    tempo = fim - inicio
    return resultado, tempo

def calcular_distancia_total(grafo: Grafo, caminho: list[str]) -> float:
    #primriro verificamos se o caminho é vazio ou com menos de duas cidades
    if not caminho or len(caminho) < 2: 
        return 0.0
    
    distancia_total = 0.0
    
    #aqui vamis pegar os pares de cidades que são consecutivos
    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i + 1]
        vizinhos = grafo.getCidadesVizinhas(u) #pegamos todas as cidades viznhas de u

        # Busca a distância para a cidade seguinte e quando acha, 
        #adiciona a dista^ncia na busca
        for dist, cidade in vizinhos:
            if cidade == v:
                distancia_total += dist
                break

    return distancia_total

