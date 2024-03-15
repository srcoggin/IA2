# imports the relevant classes from each of our modular files
from MainWindow import MainWindow
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)
ui = MainWindow()
ui.show()
app.exec()
