from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particula_sa_5.particulacompuesta import ParticulaCompuesta
from particula_sa_5.particula import Particula


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.particula_compuesta = ParticulaCompuesta()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregarFinal_pushB.clicked.connect(self.agregar_final)
        self.ui.agregarInicio_pushB.clicked.connect(self.agregar_inicio)
        self.ui.mostrar_pushB.clicked.connect(self.mostrar)

    @Slot()
    def agregar_final(self):
        identificador = self.ui.id_spinBox.value()
        origen_x = self.ui.origenX_spinBox.value() #Sacamos lo que está ahí
        origen_y = self.ui.origenY_spinBox.value()
        destino_x = self.ui.destinoX_spinBox.value()
        destino_y = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.rojo_spinBox.value()
        green = self.ui.verde_spinBox.value()
        blue = self.ui.azul_spinBox.value()
        particula = Particula(identificador, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)

        self.particula_compuesta.agregar_final(particula)
    
    @Slot()
    def agregar_inicio(self):
        identificador = self.ui.id_spinBox.value()
        origen_x = self.ui.origenX_spinBox.value() #Sacamos lo que está ahí
        origen_y = self.ui.origenY_spinBox.value()
        destino_x = self.ui.destinoX_spinBox.value()
        destino_y = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.rojo_spinBox.value()
        green = self.ui.verde_spinBox.value()
        blue = self.ui.azul_spinBox.value()
        particula = Particula(identificador, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)

        self.particula_compuesta.agregar_inicio(particula)
    
    def mostrar(self):
        self.particula_compuesta.mostrar()