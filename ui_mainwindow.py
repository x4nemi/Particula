# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 523)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.agregarInicio_pushB = QPushButton(self.groupBox_2)
        self.agregarInicio_pushB.setObjectName(u"agregarInicio_pushB")

        self.gridLayout_2.addWidget(self.agregarInicio_pushB, 5, 2, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox_2)
        self.id_spinBox.setObjectName(u"id_spinBox")

        self.gridLayout_2.addWidget(self.id_spinBox, 0, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.destinoY_spinBox = QSpinBox(self.groupBox_4)
        self.destinoY_spinBox.setObjectName(u"destinoY_spinBox")
        self.destinoY_spinBox.setMaximum(500)

        self.gridLayout_4.addWidget(self.destinoY_spinBox, 11, 2, 1, 1)

        self.velocidad_spinBox = QSpinBox(self.groupBox_4)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(500)

        self.gridLayout_4.addWidget(self.velocidad_spinBox, 13, 2, 1, 1)

        self.destinoX_spinBox = QSpinBox(self.groupBox_4)
        self.destinoX_spinBox.setObjectName(u"destinoX_spinBox")
        self.destinoX_spinBox.setMaximum(500)

        self.gridLayout_4.addWidget(self.destinoX_spinBox, 8, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 2, 1, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 1, 1, 1, 1)

        self.origenY_spinBox = QSpinBox(self.groupBox_4)
        self.origenY_spinBox.setObjectName(u"origenY_spinBox")
        self.origenY_spinBox.setMaximum(500)

        self.gridLayout_4.addWidget(self.origenY_spinBox, 2, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 11, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 8, 1, 1, 1)

        self.origenX_spinBox = QSpinBox(self.groupBox_4)
        self.origenX_spinBox.setObjectName(u"origenX_spinBox")

        self.gridLayout_4.addWidget(self.origenX_spinBox, 1, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 13, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 3, 0, 4, 1)

        self.mostrar_pushB = QPushButton(self.groupBox_2)
        self.mostrar_pushB.setObjectName(u"mostrar_pushB")

        self.gridLayout_2.addWidget(self.mostrar_pushB, 6, 2, 1, 1)

        self.color = QGroupBox(self.groupBox_2)
        self.color.setObjectName(u"color")
        self.gridLayout_3 = QGridLayout(self.color)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.rojo_spinBox = QSpinBox(self.color)
        self.rojo_spinBox.setObjectName(u"rojo_spinBox")
        self.rojo_spinBox.setMaximum(255)

        self.gridLayout_3.addWidget(self.rojo_spinBox, 0, 1, 1, 1)

        self.label_7 = QLabel(self.color)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.verde_spinBox = QSpinBox(self.color)
        self.verde_spinBox.setObjectName(u"verde_spinBox")
        self.verde_spinBox.setMaximum(255)

        self.gridLayout_3.addWidget(self.verde_spinBox, 2, 1, 1, 1)

        self.azul_spinBox = QSpinBox(self.color)
        self.azul_spinBox.setObjectName(u"azul_spinBox")
        self.azul_spinBox.setMaximum(255)

        self.gridLayout_3.addWidget(self.azul_spinBox, 1, 1, 1, 1)

        self.label_8 = QLabel(self.color)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_9 = QLabel(self.color)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.color, 3, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.agregarFinal_pushB = QPushButton(self.groupBox_2)
        self.agregarFinal_pushB.setObjectName(u"agregarFinal_pushB")

        self.gridLayout_2.addWidget(self.agregarFinal_pushB, 4, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout.addWidget(self.salida, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.buscar = QLineEdit(self.tab_2)
        self.buscar.setObjectName(u"buscar")
        self.buscar.setCursorPosition(0)

        self.gridLayout_5.addWidget(self.buscar, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_5.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_5.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")
        self.tabla.horizontalHeader().setMinimumSectionSize(47)
        self.tabla.horizontalHeader().setDefaultSectionSize(80)
        self.tabla.verticalHeader().setMinimumSectionSize(32)
        self.tabla.verticalHeader().setDefaultSectionSize(39)

        self.gridLayout_5.addWidget(self.tabla, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Actividad 6", None))
        self.agregarInicio_pushB.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Distancia", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino y:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Destino x:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.mostrar_pushB.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.color.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"rojo", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"verde", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"azul", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"id:", None))
        self.agregarFinal_pushB.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID de la part\u00edcula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

