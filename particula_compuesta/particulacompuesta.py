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