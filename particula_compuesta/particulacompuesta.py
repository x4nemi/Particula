from .particula import Particula
import json
from pprint import pprint, pformat
from .algoritmos import amplitud, profundidad

class ParticulaCompuesta:
    def __init__(self):
        self.__particulas = []
        self.__grafo = dict()
        grafo = dict()
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
    
    def __str__(self):
        return "".join(
            str(p) for p in self.__particulas #programación funcional
        )
    
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, "w") as archivo:
                lista = [p.to_diccionario() for p in self.__particulas]
                json.dump(lista, archivo, indent = 4)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, "r") as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**p) for p in lista] # con los ** los convierte en parámetros del constructor
            return 1
        except:
            return 0
    
    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self): # para que sea iterable
        self.cont = 0

        return self # regresa el objeto
    
    def __next__(self): # es lo que llama la iteración (como una lista ligada)
        if self.cont < len(self.__particulas):
            p = self.__particulas[self.cont]
            self.cont += 1
            return p
        raise StopIteration #excepción
    
    def ordenar_por_id(self):
        self.__particulas.sort(key = lambda p: p.id)
    
    def ordenar_por_distancia(self):
        self.__particulas.sort(key= lambda p: p.distancia, reverse=True)
    
    def ordenar_por_velocidad(self):
        self.__particulas.sort(key=lambda p: p.velocidad)

    def to_dictionary(self):

        for p in self.__particulas:
            origen_x = p.origen_x
            origen_y = p.origen_y
            origen = (origen_x, origen_y)
            destino_x = p.destino_x
            destino_y = p.destino_y
            destino = (destino_x, destino_y)

            arista_o_d_x = (destino_x, destino_y, p.distancia)
            arista_d_o_x = (origen_x, origen_y, p.distancia)

            if origen in self.__grafo:
                self.__grafo[origen].append(arista_o_d_x)
            else:
                self.__grafo[origen] = [arista_o_d_x]
            if destino in self.__grafo:
                self.__grafo[destino].append(arista_d_o_x)
            else:
                self.__grafo[destino] = [arista_d_o_x]
            
        string = pformat(self.__grafo, indent=4, width=40)
        return string
    
    def toGrafo(self):
        grafo = dict()
        for p in self.__particulas:
            origen_x = p.origen_x
            origen_y = p.origen_y
            origen = (origen_x, origen_y)
            destino_x = p.destino_x
            destino_y = p.destino_y
            destino = (destino_x, destino_y)

            arista_o_d_x = (destino, p.distancia)
            arista_d_o_x = (origen, p.distancia)

            if origen in grafo:
                grafo[origen].append(arista_o_d_x)
            else:
                grafo[origen] = [arista_o_d_x]
            if destino in grafo:
                grafo[destino].append(arista_d_o_x)
            else:
                grafo[destino] = [arista_d_o_x]
        
        return grafo
            
    def toGrafo1(self):
        grafo = dict()
        for p in self.__particulas:
            origen_x = p.origen_x
            origen_y = p.origen_y
            origen = (origen_x, origen_y)
            destino_x = p.destino_x
            destino_y = p.destino_y
            destino = (destino_x, destino_y)

            arista_o_d_x = (p.distancia, destino)
            arista_d_o_x = (p.distancia, origen)

            if origen in grafo:
                grafo[origen].append(arista_o_d_x)
            else:
                grafo[origen] = [arista_o_d_x]
            if destino in grafo:
                grafo[destino].append(arista_d_o_x)
            else:
                grafo[destino] = [arista_d_o_x]
        
        return grafo

    def toGrafo2(self):
        grafo = dict()
        for p in self.__particulas:
            origen_x = p.origen_x
            origen_y = p.origen_y
            origen = (origen_x, origen_y)
            destino_x = p.destino_x
            destino_y = p.destino_y
            destino = (destino_x, destino_y)

            arista_o_d_x = (p.velocidad, destino)
            arista_d_o_x = (p.velocidad, origen)

            if origen in grafo:
                grafo[origen].append(arista_o_d_x)
            else:
                grafo[origen] = [arista_o_d_x]
            if destino in grafo:
                grafo[destino].append(arista_d_o_x)
            else:
                grafo[destino] = [arista_d_o_x]
        
        return grafo

    def isOrigenInPC(self, origen_x, origen_y):
        ox = []
        oy = []
        for p in self.__particulas:
            ox.append(p.origen_x)
            oy.append(p.origen_y)
        
        if origen_x in ox and origen_y in oy:
            return True
        return False     
