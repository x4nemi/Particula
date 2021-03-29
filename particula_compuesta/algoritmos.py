import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    en_x = math.pow(x_1 - x_2, 2)
    en_y = math.pow(y_1 - y_2, 2)
    distancia = math.sqrt(en_x + en_y)
    return distancia