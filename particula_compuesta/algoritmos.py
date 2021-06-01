import math
from collections import deque
from queue import PriorityQueue

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    en_x = math.pow(x_1 - x_2, 2)
    en_y = math.pow(y_1 - y_2, 2)
    distancia = math.sqrt(en_x + en_y)
    return distancia

def amplitud(origen, grafo):
    visitados = []
    cola = deque()
    resultado = []
    adyacentes = []

    visitados.append(origen)
    cola.append(origen)

    while len(cola) > 0:
        vertice = cola[0]
        resultado.append(vertice)
        cola.popleft()
        adyacentes = grafo.get(vertice)

        
        for i in range(len(adyacentes)):
            ady = adyacentes[i][0]

            if ady not in visitados:
                visitados.append(ady)
                cola.append(ady)
    return resultado

def profundidad(origen, grafo):
    visitados = []
    pila = deque()
    resultado = []

    visitados.append(origen)
    pila.append(origen)

    while len(pila) > 0:
        vertice = pila[-1]
        resultado.append(vertice)
        pila.pop()
        adyacentes = grafo.get(vertice)
        
        for i in range(len(adyacentes)):
            ady = adyacentes[i][0]

            if ady not in visitados:
                visitados.append(ady)
                pila.append(ady)
    
    return resultado