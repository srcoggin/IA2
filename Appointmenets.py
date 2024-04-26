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
        # 1. Gathers the Clinicians details to write into the log file
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        ID = self.ui.SearchByAppointmentIDInput.text()
        IDs = self.ds.SearchAllAppointmentID()
        # 2. Checks to see if the inputed ID is in the database
        if ID not in IDs:
            self.mw.error()
        else:
            # 3. Prints the data into the following Line Edits
            AppointmentData = self.ds.SelectMatchingAppointment(int(self.ui.SearchByAppointmentIDInput.text()))
            for i in AppointmentData:
                self.ui.AppointmentIDInput.setText(str(i[0]))
                self.ui.AppointmentDateEdit.setText(i[1])
                self.ui.AppointmentLengthEdit.setText(str(i[2]))
                self.ui.AppointmentPaidEdit.setText(str(i[4]))
                self.ui.AppointmentClinicianEdit.setText(str(i[6]))
                self.ui.AppointmentPatientID.setText(str(i[5]))
                self.ui.AppointmentServiceUsed.setText(i[7])
                self.ui.AppointmentResult.setText(i[3])
                list = i[1].split('/')
                self.ui.AppointmentDateEdit_2.setDateTime(QDateTime(datetime.datetime(int(list[2]), int(list[1]), int(list[0]))))
            # 4. Checks to see if QSpinbox Value matches current Appointment Selected
            if self.ui.AppointmentIDSpinbox.value() != self.ui.AppointmentIDInput.text():
                self.ui.AppointmentIDSpinbox.setValue(int(self.ui.AppointmentIDInput.text()))
            AppointmentID = self.ui.AppointmentIDInput.text()
            # 5. Writes interaction into log file
            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for an Appointment with the ID {AppointmentID}, By Searching for their ID, at {self.currentdate}, Succsesfully")

    def SearchByDate(self):
        # 1. Gathers the Clinicians details to write into the log file
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        Date = self.ui.AppointmentSearchByDateInput.text()
        AllDates = self.ds.SearchAllAppointmentDates()
        # 2. Checks to see if the data is present in the database
        if Date not in AllDates:
            self.mw.error()
        else:
            # 3.Checks to see if two or more appointments hold the same date
            for i in range(1):
                if Date in AllDates:
                    NumbOfMatches = AllDates.count(Date)
                    if NumbOfMatches > 1:
                        # 3.5 if there is more than one appointment with the same date, i get lazy
                        self.mw.MoreThanTwoOfThem()
                    else:
                        #4. populates the field with the data pulled from matching date in database
                        AppointmentData = self.ds.SelectMatchingAppointmentDate(self.ui.AppointmentSearchByDateInput.text())
                        for i in AppointmentData:
                            self.ui.AppointmentIDInput.setText(str(i[0]))
                            self.ui.AppointmentDateEdit.setText(i[1])
                            self.ui.AppointmentLengthEdit.setText(str(i[2]))
                            self.ui.AppointmentPaidEdit.setText(str(i[4]))
                            self.ui.AppointmentClinicianEdit.setText(str(i[6]))
                            self.ui.AppointmentPatientID.setText(str(i[5]))
                            self.ui.AppointmentServiceUsed.setText(i[7])
                            self.ui.AppointmentResult.setText(i[3])
                            list = i[1].split('/')
                            self.ui.AppointmentDateEdit_2.setDateTime(QDateTime(datetime.datetime(int(list[2]), int(list[1]), int(list[0]))))
                        #5. corrects the QSpinBox to make sure the value matches the Appointment selected
                        if self.ui.AppointmentIDSpinbox.value() != self.ui.AppointmentIDInput.text():
                            self.ui.AppointmentIDSpinbox.setValue(int(self.ui.AppointmentIDInput.text()))
                        AppointmentID = self.ui.AppointmentIDInput.text()
                        #6. logs interaction in the log.txt file
                        self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for an Appointment with the ID {AppointmentID}, By Searching for its date, at {self.currentdate}, Succsesfully")



    def AppointmentSpinBoxSelected(self):
        #1. Gathers Clinician details for use in logging interactions
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        #2. checks to see if the value selected is a valid ID
        if self.ui.AppointmentIDSpinbox.value() == 0:
            self.ui.AppointmentIDInput.clear()
            self.ui.AppointmentDateEdit.clear()
            self.ui.AppointmentLengthEdit.clear()
            self.ui.AppointmentPaidEdit.clear()
            self.ui.AppointmentClinicianEdit.clear()
            self.ui.AppointmentPatientID.clear()
            self.ui.AppointmentServiceUsed.clear()
            self.ui.AppointmentResult.clear()
        else:
            if self.ui.AppointmentIDSpinbox.value() != self.ui.AppointmentIDInput.text():
                ID = str(self.ui.AppointmentIDSpinbox.value())
                IDs = self.ds.SearchAllAppointmentID()
                #3. checks to see if the ID exists in the database
                if ID not in IDs:
                    self.mw.error()
                    if self.ui.AppointmentIDInput.text() == "":
                        #3.5 just resets the spinbox back to its previous value if that ID does not exist
                        self.ui.AppointmentIDSpinbox.setValue(int(self.ui.AppointmentIDSpinbox.value()) -1)
                    else:
                        self.ui.AppointmentIDSpinbox.setValue(int(self.ui.AppointmentIDInput.text()))
                else:
                    #4. populates the fields with the relevant data
                    AppointmentData = self.ds.SelectMatchingAppointment(self.ui.AppointmentIDSpinbox.value())
                    for i in AppointmentData:
                        self.ui.AppointmentIDInput.setText(str(i[0]))
                        self.ui.AppointmentDateEdit.setText(i[1])
                        self.ui.AppointmentLengthEdit.setText(str(i[2]))
                        self.ui.AppointmentPaidEdit.setText(str(i[4]))
                        self.ui.AppointmentClinicianEdit.setText(str(i[6]))
                        self.ui.AppointmentPatientID.setText(str(i[5]))
                        self.ui.AppointmentServiceUsed.setText(i[7])
                        self.ui.AppointmentResult.setText(i[3])
                        list = i[1].split('/')
                        self.ui.AppointmentDateEdit_2.setDateTime(QDateTime(datetime.datetime(int(list[2]), int(list[1]), int(list[0]))))
                    #5. matches the spinbox value with the correct value? which it should be correct anyway?? but... whatever it stays
                    if self.ui.AppointmentIDSpinbox.value() != self.ui.AppointmentIDInput.text():
                        self.ui.AppointmentIDSpinbox.setValue(int(self.ui.AppointmentIDInput.text()))
                    AppointmentID = self.ui.AppointmentIDInput.text()
                    #6. logs interaction into the log file
                    self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for an Appointment with the ID {AppointmentID}, By Scrolling through the SpinBox, at {self.currentdate}, Succsesfully")

    def ChangeDateTimeToLineEdit(self):
        #1. checks to see if the QLine Edit is empty or not
        if self.ui.AppointmentDateEdit.text() == "":
            pass
        elif self.ui.AppointmentDateEdit.text() != "":
            try:
                #2. just changes the date so that the QDateTime Widget and QLineEdit show the same value
                LineEdit = self.ui.AppointmentDateEdit.text().split('/')
                self.ui.AppointmentDateEdit_2.setDateTime(QDateTime(datetime.datetime(int(LineEdit[2]), int(LineEdit[1]), int(LineEdit[0]))))
            except:
                #3. this only is called when the value in the QLineEdit is before 17/12/1758
                print("No Can Do!!")
        else:
            print("No Can Do!")
    
    def LineEditToChangeDate(self):
        try:
            #1. just changes the date so that the QDateTime Widget and QLineEdit show the same value
            DateEdit = str(self.ui.AppointmentDateEdit_2.text())
            self.ui.AppointmentDateEdit.setText(DateEdit)
        except:
            #2. this only is called when the value in the QLineEdit is before 17/12/1758
            print("Not A Chance!")
        
    def SearchByPaid(self):
        #1. Gathers Clinician details for use in logging interactions
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        Paid = self.ui.AppointmentSearchByPaidInput.text()
        AllPaid = self.ds.SearchAllAppointmentPaid()
        #2. checks to see if there are Appointments that have been paid
        if Paid not in AllPaid:
            self.mw.error()
        else:
            for i in range(1):
                if Paid in AllPaid:
                    NumbOfMatches = AllPaid.count(Paid)
                    #3. checks if there is more than two appointments paid for. (will is lazy)
                    if NumbOfMatches > 1:
                        self.mw.MoreThanTwoOfThem()
                    else:
                        #4. populates the fields with the relevant data
                        AppointmentData = self.ds.SelectMatchingAppointmentPaid(self.ui.AppointmentSearchByPaidInput.text())
                        for i in AppointmentData:
                            self.ui.AppointmentIDInput.setText(str(i[0]))
                            self.ui.AppointmentDateEdit.setText(i[1])
                            self.ui.AppointmentLengthEdit.setText(str(i[2]))
                            self.ui.AppointmentPaidEdit.setText(str(i[4]))
                            self.ui.AppointmentClinicianEdit.setText(str(i[6]))
                            self.ui.AppointmentPatientID.setText(str(i[5]))
                            self.ui.AppointmentServiceUsed.setText(i[7])
                            self.ui.AppointmentResult.setText(i[3])
                            list = i[1].split('/')
                            self.ui.AppointmentDateEdit_2.setDateTime(QDateTime(datetime.datetime(int(list[2]), int(list[1]), int(list[0]))))
                        if self.ui.AppointmentIDSpinbox.value() != self.ui.AppointmentIDInput.text():
                            self.ui.AppointmentIDSpinbox.setValue(int(self.ui.AppointmentIDInput.text()))
                        AppointmentID = self.ui.AppointmentIDInput.text()
                        #5. logs interaction in .txt file
                        self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for an Appointment with the ID {AppointmentID}, By Searching for All Paid Appointments, at {self.currentdate}, Succsesfully")

    def AddNewAppointment(self):
        #1. Gathers Clinician details for use in logging interactions
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        #2. Assigns the QLineEdits to variables for easier handeling
        AppointmentID = self.ui.AppointmentIDInput.text()
        Date = self.ui.AppointmentDateEdit.text()
        Length = self.ui.AppointmentLengthEdit.text()
        Paid = self.ui.AppointmentPaidEdit.text()
        ClinicianID = self.ui.AppointmentClinicianEdit.text()
        PatientID = self.ui.AppointmentPatientID.text()
        ServiceUsed = self.ui.AppointmentServiceUsed.text()
        Result = self.ui.AppointmentResult.text()
        MatchingID = self.ds.SearchAllAppointmentID()
        Year = self.ui.AppointmentDateEdit.text().split('/')
        msg = QMessageBox()
        #3. gathers conformation from user
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are you sure!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_clicked = msg.exec()
        if button_clicked == QMessageBox.Yes:
                #4. checks to see if there is already an appointment under the ID used
                if AppointmentID in MatchingID:
                    msg.setText("A Clinician Already exists under this ID...")
                    msg.setWindowTitle("Operation Failed!")
                    msg.setStandardButtons(QMessageBox.Close)
                    msg.exec()
                else:
                    Access = self.mw.ClinicianLoginPinPopUpBox(False)
                    if Access == True:
                        #5. if successful, adds all details to data base
                        try:
                            self.ds.NewAppointmentDS(AppointmentID, Date, Length, Result, ClinicianID, ServiceUsed, PatientID, Paid, Year[0])
                            #6. writes interaction into .txt file
                            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Added a new Appointment with the ID {AppointmentID}, at {self.currentdate}, Succsesfully")
                            self.mw.OperationSuccessful()
                            self.ui.AppointmentIDSpinbox.setValue(int(AppointmentID))
                            data = [f"ID: {AppointmentID} Appointment"]
                            self.ui.AppointmentComboBox.addItems(data)
                            self.ui.AppointmentComboBox.setCurrentIndex(AppointmentID)
                        except:
                            #5.5 this could run if one of the fields of data hasn't been entered
                            msg = QMessageBox()
                            msg.setText("The Data provided contains Null info")
                            msg.setWindowTitle("This Can't Be Done!")
                            msg.setStandardButtons(QMessageBox.Close)
                            msg.exec()
                    else:
                        self.mw.OperationUnsuccessful()
        #7. wraps up function by closing all pop up boxes
        elif button_clicked == QMessageBox.No:
            QMessageBox.close
        else:
            QMessageBox.close

    def AppointmentComboBox(self):
        #1. gathers data from database
        data = self.ds.AppointmentDisplayComboBox()
        #2. lists the IDs from lowest to highest
        sorteddata = sorted(data, reverse=False)
        #3. adds them to the combobox
        self.ui.AppointmentComboBox.addItems(sorteddata)

    def ChangedAppointmentComboBox(self):
        #1. gathers clinician details for logging purposes
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        #2. checks to see if the combobox is empty
        if self.ui.AppointmentComboBox.count() == 0:
            pass
        #3. checks to see if the combobox value is 0 (this clears the all the QLineEdits)
        elif self.ui.PatientComboBox.count() != 0:
            if self.ui.AppointmentComboBox.currentIndex() == 0:
                    self.ui.AppointmentIDInput.clear()
                    self.ui.AppointmentDateEdit.clear()
                    self.ui.AppointmentLengthEdit.clear()
                    self.ui.AppointmentPaidEdit.clear()
                    self.ui.AppointmentClinicianEdit.clear()
                    self.ui.AppointmentPatientID.clear()
                    self.ui.AppointmentServiceUsed.clear()
                    self.ui.AppointmentResult.clear()
                    self.ui.AppointmentIDSpinbox.setValue(0)
            else:
                #4. pulls the first value (the appointment ID)
                item = self.ui.AppointmentComboBox.currentText()
                value = [item.split(':')[1].strip()[0]]
                self.ds.AppointmentSearchByComboBox(value[0])
                AppointmentData = self.ds.AppointmentSearchByComboBox(value[0])
                for i in AppointmentData:
                    #5. populates the feilds based on the ID selected
                    self.ui.AppointmentIDInput.setText(str(i[0]))
                    self.ui.AppointmentDateEdit.setText(i[1])
                    self.ui.AppointmentLengthEdit.setText(str(i[2]))
                    self.ui.AppointmentPaidEdit.setText(str(i[4]))
                    self.ui.AppointmentClinicianEdit.setText(str(i[6]))
                    self.ui.AppointmentPatientID.setText(str(i[5]))
                    self.ui.AppointmentServiceUsed.setText(i[7])
                    self.ui.AppointmentResult.setText(i[3])
                    list = i[1].split('/')
                    self.ui.AppointmentDateEdit_2.setDateTime(QDateTime(datetime.datetime(int(list[2]), int(list[1]), int(list[0]))))
                if self.ui.AppointmentIDSpinbox.value() != self.ui.AppointmentIDInput.text():
                    #6. corrects the ID spinbox
                    self.ui.AppointmentIDSpinbox.setValue(int(self.ui.AppointmentIDInput.text()))
                    #7. logs the interaction in the .txt file
                    self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for an Appointment with the ID {self.ui.AppointmentIDInput.text()}, at {self.currentdate}, Succsesfully")
        else:
            print("shit, we broke it")

    def EditAppointment(self):
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
        NewDate = Date.split('/')
        Year = NewDate[2]
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are you sure!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_clicked = msg.exec()
        if button_clicked == QMessageBox.Yes:
            if AppointmentID not in MatchingID:
                msg = QMessageBox()
                msg.setText("Would you like to Insert this as a new entry? (!This will delete the previous entry!)")
                msg.setWindowTitle("There is no entry under this ID")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                button_clicked = msg.exec()
                if button_clicked == QMessageBox.Yes:
                    Access = self.mw.ClinicianLoginPinPopUpBox(False)
                    if Access == True:
                        try:
                            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Edited an Appointments Data with the ID {AppointmentID}, at {self.currentdate}, Succsesfully")
                            self.ds.UpdateAppointmentDetails(AppointmentID, Date, Length, Result, Paid, PatientID, ClinicianID, ServiceUsed, Year)
                            self.ds.DeleteAppointment(self.ui.AppointmentIDSpinbox.text())
                            self.mw.OperationSuccessful()
                            self.ui.AppointmentComboBox.clear()
                            self.ui.AppointmentComboBox.addItem("Please Select an Appointment")
                            data = self.ds.AppointmentDisplayComboBox()
                            sorteddata = sorted(data, reverse=False)
                            self.ui.AppointmentComboBox.addItems(sorteddata)
                        except:
                            msg = QMessageBox()
                            msg.setText("The Data provided contains Null info")
                            msg.setWindowTitle("This Can't Be Done!")
                            msg.setStandardButtons(QMessageBox.Close)
                            msg.exec()
                    else:
                        self.mw.OperationUnsuccessful()
                elif button_clicked == QMessageBox.No:
                    QMessageBox.close
                    self.mw.OperationUnsuccessful()
                else:
                    QMessageBox.close
                    self.mw.OperationUnsuccessful()
                if self.ui.AppointmentComboBox.currentIndex() != 0:
                    Access = self.mw.ClinicianLoginPinPopUpBox(False)
                    if Access == True:
                        try:
                            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Edited an Appointments Data with the ID {AppointmentID}, at {self.currentdate}, Succsesfully")
                            self.ds.UpdateAppointmentDetails(AppointmentID, Date, Length, Result, Paid, PatientID, ClinicianID, ServiceUsed, Year)
                            self.mw.OperationSuccessful()
                            self.ui.AppointmentComboBox.clear()
                            self.ui.AppointmentComboBox.addItem("Please Select an Appointment")
                            data = self.ds.AppointmentDisplayComboBox()
                            sorteddata = sorted(data, reverse=False)
                            self.ui.AppointmentComboBox.addItems(sorteddata)
                        except:
                            msg = QMessageBox()
                            msg.setText("The Data provided contains Null info")
                            msg.setWindowTitle("This Can't Be Done!")
                            msg.setStandardButtons(QMessageBox.Close)
                            msg.exec()
            else:
                Access = self.mw.ClinicianLoginPinPopUpBox(False)
                if Access == True:
                    try:
                        self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Edited an Appointments Data with the ID {AppointmentID}, at {self.currentdate}, Succsesfully")
                        self.ds.UpdateAppointmentDetails(AppointmentID, Date, Length, Result, Paid, PatientID, ClinicianID, ServiceUsed, Year)
                        self.mw.OperationSuccessful()
                        self.ui.AppointmentComboBox.clear()
                        self.ui.AppointmentComboBox.addItem("Please Select an Appointment")
                        data = self.ds.AppointmentDisplayComboBox()
                        sorteddata = sorted(data, reverse=False)
                        self.ui.AppointmentComboBox.addItems(sorteddata)
                    except:
                            msg = QMessageBox()
                            msg.setText("The Data provided contains Null info")
                            msg.setWindowTitle("This Can't Be Done!")
                            msg.setStandardButtons(QMessageBox.Close)
                            msg.exec()
                else:
                    self.mw.OperationUnsuccessful()
        elif button_clicked == QMessageBox.No:
            QMessageBox.close
        else:
            QMessageBox.close

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
                    self.ui.AppointmentComboBox.setCurrentIndex(int(self.ui.DeleteAppointmentInput.text()))
                    index = self.ui.AppointmentComboBox.currentIndex()
                    self.ui.AppointmentComboBox.removeItem(index)
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



    