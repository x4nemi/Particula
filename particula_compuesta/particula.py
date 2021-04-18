from .algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id = 0, origen_x = 0, origen_y = 0, destino_x = 0, destino_y = 0, velocidad = 0, red = 0, green = 0, blue = 0):
        self.__particulas = []
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origen_x, origen_y, destino_x, destino_y)
    
    def __str__(self):
        return(
            "ID: " + str(self.__id) + "\n" +
            "Origen en X: " + str(self.__origen_x) + "\n" +
            "Origen en Y: " + str(self.__origen_y) + "\n" +
            "Destino en X: " + str(self.__destino_x) + "\n" +
            "Destino en Y: " + str(self.__destino_y) + "\n" +
            "Velocidad: " + str(self.__velocidad) + "\n" +
            "Red: " + str(self.__red) + "\n" +
            "Green: " + str(self.__green) + "\n" +
            "Blue: " + str(self.__blue) + "\n" +
            "Distancia: " + str(self.__distancia) + "\n\n"
        )
    
    def to_diccionario(self):
        return{
            "id": self.__id,
            "origen_x": self.__origen_x,
            "origen_y": self.__origen_y,
            "destino_x": self.__destino_x,
            "destino_y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }