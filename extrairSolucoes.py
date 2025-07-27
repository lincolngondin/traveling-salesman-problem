from input import extrairGrafoDeArquivoEntrada
from algorithms import nearestNeighbour, heldKarp, medir_tempo_execucao, calcular_distancia_total

def executar_testes_tsp():
    #aqui vamos definir o tamnaho dos grafosque serao testados, 
    #de acordo com os arquivos criados e presentes na pasta teste
    tamanhos = [5, 10, 15, 20] 
    
    for n in tamanhos:
        print(f"\n--- Teste para {n} cidades ---")
        #agora lemos o arquivo da vez (n), e extraimos o garfo
        #a partir do arquivo
        caminho_arquivo = f"./teste/grafo{n}.txt"
        grafo = extrairGrafoDeArquivoEntrada(caminho_arquivo)

        #aqui so escrevemos todas as cidades que estoa no arquivo
        print("Cidades do arquivo:")
        print(grafo.cidades)

        #comecamos agora a aplicar os algoritmos, e juntamenre,
        #calculamos o tempo que leva para executar e a distancia dada como solução

        # Nearest Neighbour
        caminho_nn, tempo_nn = medir_tempo_execucao(nearestNeighbour, grafo)
        distancia_nn = calcular_distancia_total(grafo, caminho_nn)
        print(f"\nNearest Neighbour -> Tempo: {tempo_nn:.8f} s")
        print(f"Distância total: {distancia_nn:.2f}")


        # Held-Karp
        #para grafos com mais de 25 o algoritmo é muito lento
        caminho_hk, tempo_hk = medir_tempo_execucao(heldKarp, grafo)
        distancia_hk = calcular_distancia_total(grafo, caminho_hk)
        print(f"Held-Karp -> Tempo: {tempo_hk:.8f} s")
        print(f"Distância total: {distancia_hk:.2f}")
        
        