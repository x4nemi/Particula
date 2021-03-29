from .particula import Particula

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