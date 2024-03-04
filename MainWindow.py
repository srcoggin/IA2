from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UserInterface import Ui_Form
from datastore import DataStore






class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ds = DataStore()
        self.ui = Ui_Form()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

        #Banner Buttons
        self.ui.HomeButton_PatientsPage.clicked.connect(self.PatientsPageSelect)

    def show(self):
        self.main_win.show()
        
    def PatientsPageSelect(self):
        pass

      

