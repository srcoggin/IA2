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
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        Date = self.ui.AppointmentSearchByDateInput.text()
        AllDates = self.ds.SearchAllAppointmentDates()
        if Date not in AllDates:
            self.mw.error()
        else:
            for i in range(1):
                if Date in AllDates:
                    NumbOfMatches = AllDates.count(Date)
                    if NumbOfMatches > 1:
                        self.mw.MoreThanTwoOfThem()
                    else:
                        AppointmentData = self.ds.SelectMatchingAppointmentDate(self.ui.AppointmentSearchByDateInput.text())
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
                        self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for an Appointment with the ID {AppointmentID}, By Searching for its date, at {self.currentdate}, Succsesfully")



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
        
    def SearchByPaid(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        Paid = self.ui.AppointmentSearchByPaidInput.text()
        AllPaid = self.ds.SearchAllAppointmentPaid()
        if Paid not in AllPaid:
            self.mw.error()
        else:
            for i in range(1):
                if Paid in AllPaid:
                    NumbOfMatches = AllPaid.count(Paid)
                    if NumbOfMatches > 1:
                        self.mw.MoreThanTwoOfThem()
                    else:
                        AppointmentData = self.ds.SelectMatchingAppointmentPaid(self.ui.AppointmentSearchByPaidInput.text())
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
                        self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for an Appointment with the ID {AppointmentID}, By Searching for All Paid Appointments, at {self.currentdate}, Succsesfully")

    def AddNewAppointment(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        AppointmentID = self.ui.AppointmentIDInput.text()
        Date = self.ui.AppointmentDateEdit.text()
        Length = self.ui.AppointmentLengthEdit.text()
        Paid = self.ui.AppointmentPaidEdit.text()
        ClinicianID = self.ui.AppointmentClinicianEdit.text()
        PatientID = self.ui.AppointmentPatientID.text()
        ServiceUsed = self.ui.AppointmentServiceUsed.text()
        Result = self.ui.AppointmentResult.text()
        MatchingID = self.ds.SearchAllAppointmentID()
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are you sure!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_clicked = msg.exec()
        if button_clicked == QMessageBox.Yes:
                if AppointmentID in MatchingID:
                    msg.setText("A Clinician Already exists under this ID...")
                    msg.setWindowTitle("Operation Failed!")
                else:
                    Access = self.mw.ClinicianLoginPinPopUpBox(False)
                    if Access == True:
                        try:
                            self.ds.NewAppointmentDS(AppointmentID, Date, Length, Result, ClinicianID, ServiceUsed, PatientID, Paid)
                            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Added a new Appointment with the ID {AppointmentID}, at {self.currentdate}, Succsesfully")
                            self.mw.OperationSuccessful()
                            self.ui.AppointmentIDSpinbox.setValue(int(AppointmentID))
                        except:
                            msg = QMessageBox()
                            msg.setText("The Data provided either contains Null info, or the Login-Pin is not unique")
                            msg.setWindowTitle("This Can't Be Done!")
                            msg.setStandardButtons(QMessageBox.Close)
                            msg.exec()
                    else:
                        self.mw.OperationUnsuccessful()
        elif button_clicked == QMessageBox.No:
            QMessageBox.close
        else:
            QMessageBox.close

    def AppointmentComboBox(self):
        self.ui.AppointmentComboBox.addItems(self.ds.AppointmentDisplayComboBox)

    def EditAppointment(self):
        pass

    def DeleteAppointment(self):
        msg = QMessageBox()
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        AppointmentID = self.ui.DeleteAppointmentInput.text()
        MatchingID = self.ds.SearchAllAppointmentID()
        if AppointmentID not in MatchingID:
            self.mw.error()
        else:
            msg.setText("Are you sure you want to do this?")
            msg.setWindowTitle("Are you sure!")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button_clicked = msg.exec()
            if button_clicked == QMessageBox.Yes:
                Access = self.mw.ClinicianLoginPinPopUpBox(False)
                if Access == True:
                    self.ds.DeleteAppointment(AppointmentID)
                    self.mw.OperationSuccessful()
                    self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Deleted an Appointment with the ID {AppointmentID} from the Data Base, using their ID, at {self.currentdate}, Succsesfully")
                else:
                    self.mw.OperationUnsuccessful()
            else:
                QMessageBox.close
                self.mw.OperationUnsuccessful()
        self.ui.AppointmentIDInput.clear()
        self.ui.AppointmentDateEdit.clear()
        self.ui.AppointmentLengthEdit.clear()
        self.ui.AppointmentPaidEdit.clear()
        self.ui.AppointmentClinicianEdit.clear()
        self.ui.AppointmentPatientID.clear()
        self.ui.AppointmentServiceUsed.clear()
        self.ui.AppointmentResult.clear()
        self.ui.AppointmentIDSpinbox.setValue(0)



    