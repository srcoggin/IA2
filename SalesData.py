from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UserInterface import Ui_Form
from PyQt5 import QtGui
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime
import datetime
from UserInterface import Ui_Form
from datastore import DataStore
from tkinter import *
from collections import Counter

class Sales():
    def __init__(self, datastore: DataStore, UI: Ui_Form, MW, Log):
        self.LineEdit = QLineEdit()
        self.currentdate = datetime.datetime.now()
        self.main_win = QMainWindow()
        self.ds = datastore
        self.ui = UI
        self.mw = MW
        self.LogFile = Log
    
    def SalesDataComboBox(self):
        data = self.ds.SalesDisplayComboBox()
        values = [key[1:-2] for key in data.keys()]
        print(values)
        self.ui.SalesDataComboBox.addItems(values)
        #TODO - Remove the "(,)" from the inputs so that the function "SalesUpdate" works properly

      

        

    def SalesUpdate(self):
        if self.ui.SalesDataComboBox.currentIndex() == 0:
            self.ui.SpaceTimeLabel.clear()
            self.ui.PaidLabel.clear()
            self.ui.NotPaidLabel.clear()
            self.ui.MostBookedClinicianLabel.clear()
            self.ui.NumberOfAppointmentLabel.clear()
        else:
            item = self.ui.SalesDataComboBox.currentText()
            data = self.ds.SalesDataSearchByComboBox(item)
            self.ui.SpaceTimeLabel.setText(item)
            numb = 0
            othernumb = 0
            countofapp = 0
            moneymade = 0
            for i in data:
                #Counting Paid Appointments
                if 1 == i[4]:
                    numb += 1
                if 0 == i[4]:
                    othernumb += 1
                seventh_values = [i[6] for i in data]
                value_counts = Counter(seventh_values)
                if len(value_counts) == 1:
                    list(value_counts.keys())[0] # Return the only value if there's one
                else:
                    pass
                mostcommonvalue = max(value_counts, key=value_counts.get)
                lemoney = self.ds.countingmoney(i[6])
                moneymade += lemoney[0][0]
                countofapp += 1
                self.ui.MostBookedClinicianLabel.setText(str(mostcommonvalue))
                self.ui.PaidLabel.setText(str(numb))
                self.ui.NotPaidLabel.setText(str(othernumb))
                self.ui.NumberOfAppointmentLabel.setText(str(countofapp))
                self.ui.MoneyMadeLabel.setText(str(moneymade))




