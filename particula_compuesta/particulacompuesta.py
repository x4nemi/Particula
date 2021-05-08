from .particula import Particula
import json

class ParticulaCompuesta:
    def __init__(self):
        self.__particulas = []
    
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