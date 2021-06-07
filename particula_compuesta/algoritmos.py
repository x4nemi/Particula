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

def imprimirprio(cola):
    copia = PriorityQueue()
    while not cola.empty():
        arista = cola.get()
        print(arista)
        copia.put(arista)
    cola = copia

def inCola(cola, nodo):
    copia = PriorityQueue()

    while not cola.empty():
        n = cola.get()
        copia.put(n)
    cola = copia
    
    while not copia.empty():
        n = copia.get()
        if nodo == n:
            return False
        
    return True

def algoritmoPrim(grafo, origen):
    visitados = [] #lista de (1, 2)
    colaPrioridad = PriorityQueue()
    grafoRes = dict()
    #colaVisitados = PriorityQueue() ######

    #colaPrioridad.put(origen)
    adyacentes = grafo.get(origen)
    for nodo in adyacentes:
        destino = nodo[1]
        arista = (nodo[0], (origen, destino))
        colaPrioridad.put(arista) #(peso, (o_x, o_y), (d_x, d_y))
        print(nodo)

    #colaPrioridad.put(grafo.get(origen))
    visitados.append(origen)
    
    while not colaPrioridad.empty():
        aristaMin = colaPrioridad.get() #(peso, (o_x, o_y), (d_x, d_y))
        destino = aristaMin[1][1]  #tupla
        # print(aristaMin)
        # print(destino)#colaVisitados.put(aristaMin) #los que salen

        if destino not in visitados: 
            visitados.append(destino)
            adyacentes = grafo.get(destino)
            # for i in len(adyacentes):
            #     destino2 = adyacentes[i][1]
            for nodo in adyacentes: #iterando a los adyacentes
                print("nodo", nodo)
                destino2 = nodo[1] #se vuelve el destino 
                arista = (nodo[0], (destino, destino2)) #el destino anterior se vuelve el origen
                # print("v", visitados)
                # print("d2", destino2)
                if destino2 not in visitados:
                    colaPrioridad.put(arista)
            #colaPrioridad.put(grafo.get(destino)) #adyacentes
#o                  d
#(200, 10)----------(250, 10)
            origen1 = aristaMin[1][0]
            destino1 = aristaMin[1][1]

            arista_o_d = (aristaMin[0], destino1) #peso, destino
            arista_d_o = (aristaMin[0], origen1) #peso, origen

            if origen1 in grafoRes:
                grafoRes[origen1].append(arista_o_d)
            else:
                grafoRes[origen1] = [arista_o_d]
            if destino1 in grafoRes:
                grafoRes[destino1].append(arista_d_o)
            else:
                grafoRes[destino1] = [arista_d_o]
            print("g", grafoRes)
    print(grafoRes)
    return grafoRes


