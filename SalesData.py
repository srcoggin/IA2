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
    
    #Function to populate a ComboBox with sales data
    def SalesDataComboBox(self):
        # 1. Get data for ComboBox from the database
        data = self.ds.SalesDisplayComboBox()

        # 2. Extract values from keys for simplified display
        values = [key[1:-2] for key in data.keys()]

        # 3. Add extracted values to the QComboBox
        self.ui.SalesDataComboBox.addItems(values)


    # Function to update sales information based on user selection
    def SalesUpdate(self):
        # 1. Get clinician's first and last name from database
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())

        # 2. Check if a valid selection has been made in the ComboBox
        if self.ui.SalesDataComboBox.currentIndex() == 0:
            # Clear UI labels if no valid selection
            self.ui.SpaceTimeLabel.clear()
            self.ui.PaidLabel.clear()
            self.ui.NotPaidLabel.clear()
            self.ui.MostBookedClinicianLabel.clear()
            self.ui.NumberOfAppointmentLabel.clear()
            self.ui.MoneyMadeLabel.clear()
        else:
            # 3. Get the selected item from the ComboBox
            item = self.ui.SalesDataComboBox.currentText()

            # 4. Retrieve sales data based on the selected item
            data = self.ds.SalesDataSearchByComboBox(item)

            # 5. Set the selected item as the current Time Period and place it in the label
            self.ui.SpaceTimeLabel.setText(item)

            # 6. Initialize counters for various sales statistics
            numb = 0  # Paid appointments
            othernumb = 0  # Not paid appointments
            countofapp = 0  # Total appointments
            moneymade = 0  # Total money made

            # 7. Iterate through the retrieved sales data
            for i in data:
                # 8. Count paid and unpaid appointments
                if 1 == i[4]:
                    numb += 1
                if 0 == i[4]:
                    othernumb += 1

                # 9. Extract the Clinician ID from each Appointment
                ClinID = [i[6] for i in data]

                # 10. Use Counter to count occurrences of Clinician ID across all Appointments
                value_counts = Counter(ClinID)

                # 11. Find the most common Clinician ID
                mostcommonvalue = max(value_counts, key=value_counts.get)

                # 12. Call the counting function to add up the total costs of all Clinicians used in the Appointments
                lemoney = self.ds.countingmoney(i[6])

                # 13. Add total money to the total money made variable
                moneymade += lemoney[0][0]

                # 14. Increment the appointments taken counter
                countofapp += 1

            # 15. Update UI labels with calculated statistics
            self.ui.MostBookedClinicianLabel.setText(str(mostcommonvalue))
            self.ui.PaidLabel.setText(str(numb))
            self.ui.NotPaidLabel.setText(str(othernumb))
            self.ui.NumberOfAppointmentLabel.setText(str(countofapp))
            self.ui.MoneyMadeLabel.setText(str(moneymade))

            # 16. Write a log message with Clinician Details, Period Searched, and Date
            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched the sales data of the year: {self.ui.SpaceTimeLabel.text()}, at {self.currentdate}, successfully")


