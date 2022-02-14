
from covidApi import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
form_class = uic.loadUiType("covid.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.covidapi = covidApi()
        self.setTableWidgetData()
    def setTableWidgetData(self):
        for j in range(0, 18):
            for i in range(0, 6):
                item = QTableWidgetItem(self.covidapi.data[i][j].text)
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                self.tableWidget.setItem(j, i, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()





















