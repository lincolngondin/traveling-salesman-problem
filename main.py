from input import extrairGrafoDeArquivoEntrada
from algorithms import nearestNeighbour

g= extrairGrafoDeArquivoEntrada("./teste/entrada1.txt")
print(g.cidades)

print(nearestNeighbour(g))