from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from ui_mainwindow import Ui_MainWindow
from particula_compuesta.particulacompuesta import ParticulaCompuesta
from particula_compuesta.particula import Particula
from random import randint
from particula_compuesta.algoritmos import amplitud, profundidad, algoritmoPrim
from pprint import pformat

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.particula_compuesta = ParticulaCompuesta()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregarFinal_pushB.clicked.connect(self.agregar_final)
        self.ui.agregarInicio_pushB.clicked.connect(self.agregar_inicio)
        self.ui.mostrar_pushB.clicked.connect(self.mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo) # disparo
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        self.ui.actionMostrar_Grafo.triggered.connect(self.action_mostrar_grafo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_titulo)

        self.ui.limpiar_pushB.clicked.connect(self.limpiar)
        self.ui.dibujar_pushb.clicked.connect(self.dibujar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        #Table Widget
        self.ui.orden_id_pb.clicked.connect(self.ordenar_id)
        self.ui.ordenar_d_pb.clicked.connect(self.ordenar_dis)
        self.ui.ordenar_vel_pb.clicked.connect(self.ordenar_vel)

        #Plain Text Widget
        self.ui.sortId.clicked.connect(self.sort_id)
        self.ui.sortDis.clicked.connect(self.sort_dis)
        self.ui.sortVel.clicked.connect(self.sort_vel)

        #Profundidad y anchura
        self.ui.anchura_profundidad.triggered.connect(self.ampl_prof)

        #Prim
        self.ui.actionAlgoritmo_de_Prim.triggered.connect(self.prim)

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
        # self.particula_compuesta.mostrar()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particula_compuesta))
    
    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            "Abrir Archivo",
            ".",
            "JSON (*.json)"
        )[0]
        if self.particula_compuesta.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo abrir el archivo" + ubicacion
            )
    
    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            "Guardar Archivo",
            ".", # desde la carpeta que se está ejecutando
            "JSON (*.json)" # formato
        )[0]

        print(ubicacion)
        self.particula_compuesta.guardar(ubicacion)
        if self.particula_compuesta.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )
    
    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.particula_compuesta))

        row = 0

        for p in self.particula_compuesta:
            id_widget = QTableWidgetItem(str(p.id))
            origenX_widget = QTableWidgetItem(str(p.origen_x))
            origenY_widget = QTableWidgetItem(str(p.origen_y))
            destinoX_widget = QTableWidgetItem(str(p.destino_x))
            destinoY_widget = QTableWidgetItem(str(p.destino_y))
            velocidad_widget = QTableWidgetItem(str(p.velocidad))
            red_widget = QTableWidgetItem(str(p.red))
            green_widget = QTableWidgetItem(str(p.green))
            blue_widget = QTableWidgetItem(str(p.blue))
            distancia_widget = QTableWidgetItem(str(p.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origenX_widget)
            self.ui.tabla.setItem(row, 2, origenY_widget)
            self.ui.tabla.setItem(row, 3, destinoX_widget)
            self.ui.tabla.setItem(row, 4, destinoY_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1
    
    @Slot()
    def buscar_titulo(self):
        p_id = self.ui.buscar.text()
        
        encontrado = False

        for p in self.particula_compuesta:
            if p_id == str(p.id):
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(str(p.id))
                origenX_widget = QTableWidgetItem(str(p.origen_x))
                origenY_widget = QTableWidgetItem(str(p.origen_y))
                destinoX_widget = QTableWidgetItem(str(p.destino_x))
                destinoY_widget = QTableWidgetItem(str(p.destino_y))
                velocidad_widget = QTableWidgetItem(str(p.velocidad))
                red_widget = QTableWidgetItem(str(p.red))
                green_widget = QTableWidgetItem(str(p.green))
                blue_widget = QTableWidgetItem(str(p.blue))
                distancia_widget = QTableWidgetItem(str(p.distancia))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origenX_widget)
                self.ui.tabla.setItem(0, 2, origenY_widget)
                self.ui.tabla.setItem(0, 3, destinoX_widget)
                self.ui.tabla.setItem(0, 4, destinoY_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención!",
                f'La partícula con ID "{p_id}" no fue encontrado'
            )

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for p in self.particula_compuesta:
            r = p.red
            g = p.green
            b = p.blue
            color = QColor(r, g, b)
            pen.setColor(color)

            origen_x = p.origen_x
            origen_y = p.origen_y
            destino_x = p.destino_x
            destino_y = p.destino_y

            self.scene.addEllipse(origen_x, origen_y, 3, 3, pen)
            self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)
            self.scene.addLine(origen_x, origen_y, destino_x, destino_y, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def ordenar_id(self):
        self.particula_compuesta.ordenar_por_id()
        self.mostrar_tabla()
    
    @Slot()
    def ordenar_dis(self):
        self.particula_compuesta.ordenar_por_distancia()
        self.mostrar_tabla()
    
    @Slot()
    def ordenar_vel(self):
        self.particula_compuesta.ordenar_por_velocidad()
        self.mostrar_tabla()

    @Slot()
    def sort_id(self):
        self.particula_compuesta.ordenar_por_id()
        self.mostrar()
    
    @Slot()
    def sort_dis(self):
        self.particula_compuesta.ordenar_por_distancia()
        self.mostrar()
    
    @Slot()
    def sort_vel(self):
        self.particula_compuesta.ordenar_por_velocidad()
        self.mostrar()
    
    @Slot()
    def action_mostrar_grafo(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(self.particula_compuesta.to_dictionary())

    @Slot()
    def ampl_prof(self):
        origen_x = self.ui.origenX_spinBox.value() #Sacamos lo que está ahí
        origen_y = self.ui.origenY_spinBox.value()
        origen = (origen_x, origen_y) 
        grafo = self.particula_compuesta.toGrafo()
        string = "\nAmplitud\n"

        if origen in grafo:
            self.ui.salida.clear()
            recorridoAmplitud = amplitud(origen, grafo)
            string += '\n'.join([str(nodo) for nodo in recorridoAmplitud])
            string += "\n\nProfundidad\n"
            recorridoProfundidad = profundidad(origen, grafo)
            string += '\n'.join([str(nodo) for nodo in recorridoProfundidad])
            self.ui.salida.insertPlainText("\n" + string)
            
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No es posible leer los datos"
            )
    
    @Slot()
    def prim(self):
        origen_x = self.ui.origenX_spinBox.value() #Sacamos lo que está ahí
        origen_y = self.ui.origenY_spinBox.value()
        origen = (origen_x, origen_y) 
        grafo = self.particula_compuesta.toGrafo1()
        
        if origen in grafo:
            grafoPrim = algoritmoPrim(grafo, origen)
            string = pformat(grafoPrim, indent=4, width=40)
            print(string)          

            for v in grafoPrim: #tupla keys
                 
                ady = grafoPrim.get(v)

                for nodo in ady: #(peso, (origen, destino)) valores
                    pen = QPen()
                    pen.setWidth(2)  
                    color = QColor(255, 51, 205)
                    pen.setColor(color) 
                    origen_x = v[0]
                    origen_y = v[1]
                    destino_x = nodo[1][0]
                    destino_y = nodo[1][1]

                    self.scene.addEllipse(origen_x, origen_y, 3, 3, pen)
                    self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)
                    self.scene.addLine(origen_x, origen_y, destino_x, destino_y, pen)
            
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No es posible leer los datos"
            )