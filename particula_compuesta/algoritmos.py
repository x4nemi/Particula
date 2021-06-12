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

    adyacentes = grafo.get(origen)
    for nodo in adyacentes:
        destino = nodo[1]
        arista = (nodo[0], (origen, destino))
        colaPrioridad.put(arista) #(peso, (o_x, o_y), (d_x, d_y))

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
            for nodo in adyacentes: #iterando a los adyacentes
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

    return grafoRes

def makeSet(origen, destino, disjointSet):
    l = []

    for lista in reversed(disjointSet):
        if destino in lista:
            l = lista
    for lista in disjointSet:
        if origen in lista:
            if l != []:
                l1 = lista + l
                #print("1", l1)
                r = []
                lista.clear()
                for e in l1:
                    if e not in r:
                        lista.append(e)
                        r.append(e)
                
                
                if l in disjointSet:
                    disjointSet.remove(l)

                # if [origen] in disjointSet:
                #     disjointSet.remove([origen])
                #     i -= 1
            

        if [destino] == lista:
            disjointSet.remove([destino])




    # i = 0
    # for lista in disjointSet:
    #     if [destino] == lista:
    #         disjointSet.remove([destino])
    #     # if destino in lista:
    #     #     lista.remove(destino)
    #     if origen in lista:
    #         j = i
    #         for j in range(len(disjointSet)):
    #             lista2 = disjointSet[j]
    #             if destino in lista2:
    #                 l1 = disjointSet[i] + lista2
    #                 disjointSet[i] = l1
    #             if [destino] == lista2:
    #                 disjointSet.remove([destino])
    #     i += 1
        
        
def findSet(vertice, disjointSet):
    for i in range(len(disjointSet)):
        if vertice in disjointSet[i]:
            return disjointSet[i]
    return []

def algoritmoKruskal(grafo):
    grafoRes = dict()
    listaOrdenada = PriorityQueue()
    disjointSet = []

    visitados = []

    for origen in grafo: #(x, y) origen -- keys
        ady = grafo.get(origen)
        disjointSet.append([origen])

        for nodo in ady: #(peso, (destino)) -- values
            destino = nodo[1]
            arista = (nodo[0] * -1, (origen, destino))
            
            if (origen, destino) not in visitados and (destino, origen) not in visitados:
                print(arista)
                listaOrdenada.put(arista)
                visitados.append((origen, destino))
    
    while not listaOrdenada.empty():
        arista = listaOrdenada.get()
        origen = arista[1][0]
        destino = arista[1][1]
        print("a", arista)

        if findSet(origen, disjointSet) != findSet(destino, disjointSet):
            
            peso = arista[0]

            arista_o_d = (peso, destino)
            arista_d_o = (peso, origen)

            if origen in grafoRes:
                grafoRes[origen].append(arista_o_d)
            else:
                grafoRes[origen] = [arista_o_d]
            
            if destino in grafoRes:
                grafoRes[destino].append(arista_d_o)
            else:
                grafoRes[destino] = [arista_d_o]

            makeSet(origen, destino, disjointSet)

 
    
    return grafoRes