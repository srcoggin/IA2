from PyQt5.QtWidgets import QMainWindow
import datetime
from PyQt5.QtWidgets import *
import datetime
from PyQt5.QtCore import QDateTime
from UserInterface import Ui_Form
from datastore import DataStore





class Appointments():
    def __init__(self, datastore: DataStore, UI: Ui_Form, MW, Log):
        self.LineEdit = QLineEdit()
        self.currentdate = datetime.datetime.now()
        self.LogFile = open("Log.txt", "a")
        self.main_win = QMainWindow()
        self.ds = datastore
        self.ui = UI
        self.mw = MW
        self.LogFile = Log

    def SearchAppointmentsByID(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        ID = self.ui.SearchByAppointmentIDInput.text()
        IDs = self.ds.SearchAllAppointmentID()
        if ID not in IDs:
            self.mw.error()
        else:
            AppointmentData = self.ds.SelectMatchingAppointment(int(self.ui.SearchByAppointmentIDInput.text()))
            for i in AppointmentData:
                self.ui.AppointmentIDInput.setText(str(i[0]))
                self.ui.AppointmentDateEdit.setText(i[1])
                self.ui.AppointmentLengthEdit.setText(str(i[2]))
                self.ui.AppointmentPaidEdit.setText(str(i[4]))
                self.ui.AppointmentClinicianEdit.setText(str(i[5]))
                self.ui.AppointmentPatientID.setText(str(i[6]))
                self.ui.AppointmentServiceUsed.setText(i[7])
                self.ui.AppointmentResult.setText(i[3])
                list = i[1].split('/')
                self.ui.AppointmentDateEdit_2.setDateTime(QDateTime(datetime.datetime(int(list[2]), int(list[1]), int(list[0]))))
            if self.ui.AppointmentIDSpinbox.value() != self.ui.AppointmentIDInput.text():
                self.ui.AppointmentIDSpinbox.setValue(int(self.ui.AppointmentIDInput.text()))
            AppointmentID = self.ui.AppointmentIDInput.text()
            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for an Appointment with the ID {AppointmentID}, By Searching for their ID, at {self.currentdate}, Succsesfully")

    def SearchByDate(self):
        pass



    def AppointmentSpinBoxSelected(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        if self.ui.AppointmentIDSpinbox.value() == 0:
            pass
        else:
            if self.ui.AppointmentIDSpinbox.value() != self.ui.AppointmentIDInput.text():
                ID = str(self.ui.AppointmentIDSpinbox.value())
                IDs = self.ds.SearchAllAppointmentID()
                if ID not in IDs:
                    self.mw.error()
                    if self.ui.AppointmentIDInput.text() == "":
                        self.ui.AppointmentIDSpinbox.setValue(int(self.ui.AppointmentIDSpinbox.value()) -1)
                    else:
                        self.ui.AppointmentIDSpinbox.setValue(int(self.ui.AppointmentIDInput.text()))
                else:
                    AppointmentData = self.ds.SelectMatchingAppointment(self.ui.AppointmentIDSpinbox.value())
                    for i in AppointmentData:
                        self.ui.AppointmentIDInput.setText(str(i[0]))
                        self.ui.AppointmentDateEdit.setText(i[1])
                        self.ui.AppointmentLengthEdit.setText(str(i[2]))
                        self.ui.AppointmentPaidEdit.setText(str(i[4]))
                        self.ui.AppointmentClinicianEdit.setText(str(i[5]))
                        self.ui.AppointmentPatientID.setText(str(i[6]))
                        self.ui.AppointmentServiceUsed.setText(i[7])
                        self.ui.AppointmentResult.setText(i[3])
                        list = i[1].split('/')
                        self.ui.AppointmentDateEdit_2.setDateTime(QDateTime(datetime.datetime(int(list[2]), int(list[1]), int(list[0]))))
                    if self.ui.AppointmentIDSpinbox.value() != self.ui.AppointmentIDInput.text():
                        self.ui.AppointmentIDSpinbox.setValue(int(self.ui.AppointmentIDInput.text()))
                    AppointmentID = self.ui.AppointmentIDInput.text()
                    self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for an Appointment with the ID {AppointmentID}, By Scrolling through the SpinBox, at {self.currentdate}, Succsesfully")

    def ChangeDateTimeToLineEdit(self):
        try:
            LineEdit = self.ui.AppointmentDateEdit.text().split('/')
            self.ui.AppointmentDateEdit_2.setDateTime(QDateTime(datetime.datetime(int(LineEdit[2]), int(LineEdit[1]), int(LineEdit[0]))))
        except:
            print("No Can Do!!")
    
    def LineEditToChangeDate(self):
        try:
            DateEdit = str(self.ui.AppointmentDateEdit_2.text())
            self.ui.AppointmentDateEdit.setText(DateEdit)
        except:
            print("Not A Chance!")
        


    