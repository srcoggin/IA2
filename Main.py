# imports the relevant classes from each of our modular files
from MainWindow import NewMainWindow
import sys
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)
ui = NewMainWindow()
ui.show()
app.exec()
