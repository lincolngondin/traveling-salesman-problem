import time
from grafo import Grafo

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