from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)

        ui.pushButton.clicked.connect(self.click_agregar)

    @Slot()
    def click_agregar(self):
        print("click")
