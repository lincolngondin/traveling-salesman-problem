from grafo import *

# funcao para criar o grafo a partir do arquivo de input
# é necessario o arquivo esta bem formado e sem inconsistencias
def extrairGrafoDeArquivoEntrada(nomeArquivo: str) -> Grafo:
    grafo = Grafo()
    
    with open(nomeArquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue

            # extrai cada parte de cada linha
            partes = linha.split()
            # a primeira parte é o nome da cidade que e entao adicionada
            nomeCidade = partes[0]
            grafo.adicionarCidade(nomeCidade)

            # agora percorre cada conexao
            for conexao in partes[1:]:
                conexao = conexao.strip("()")
                distancia_str, cidadeDestino = conexao.split(";")
                distancia = float(distancia_str)
                # adiciona as cidade a qual esta conectada
                grafo.conectarCidade(nomeCidade, distancia, cidadeDestino)

    return grafo