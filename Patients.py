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
from tkinter import filedialog

class Patients():
    def __init__(self, datastore: DataStore, UI: Ui_Form, MW, Log):
        self.LineEdit = QLineEdit()
        self.currentdate = datetime.datetime.now()
        self.main_win = QMainWindow()
        self.ds = datastore
        self.ui = UI
        self.mw = MW
        self.LogFile = Log
        

        #Patients Page Functions
    def SearchByIDPatients(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        ID = self.ui.PatientIdSearchInput.text()
        IDs = self.ds.SearchAllPatientID()
        if ID not in IDs:
            self.mw.error()
        else:
            PatientData = self.ds.SelectMatchingPatient(self.ui.PatientIdSearchInput.text())
            for i in PatientData:
                self.ui.PatientFirstName_Edit.setText(i[1])
                self.ui.PatientLastName_edit.setText(i[2])
                self.ui.PatientAddress_edit.setText(str(i[5]))
                self.ui.PatientID_edit.setText(str(i[0]))
                self.ui.PatientHeight_Edit.setText(str(i[3]))
                self.ui.PatientWeight_Edit.setText(str(i[4]))
                self.ui.PatientDateOfBirthEdit.setText(i[7])
                list = i[7].split('/')
                self.ui.PatientDateOfBirthDateEdit.setDateTime(QDateTime(datetime.datetime(int(list[2]), int(list[1]), int(list[0]))))
                if i[6] == "":
                    self.ui.PhotoLabel.setText("Photo Cannot Be Found for this Patient")
                else:
                    self.ui.PhotoLabel.setPixmap(QtGui.QPixmap(f"{i[6]}"))
            if self.ui.PatientIDSpinBox.value() != self.ui.PatientID_edit.text():
                self.ui.PatientIDSpinBox.setValue(int(self.ui.PatientID_edit.text()))
            FirstName = self.ui.PatientFirstName_Edit.text()
            LastName = self.ui.PatientLastName_edit.text()
            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for {FirstName} {LastName}, By Searching for their ID, at {self.currentdate}, Succsesfully")

    def ChangePatientPhoto(self):
        try:
            ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
            ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
            filepathforphoto = filedialog.askopenfilename(initialdir="C:", title="Please Choose A Photo", filetypes=(("jpg files", "*.jpg"),("png file", "*.png")))
            self.ds.EditPhotoPatient(str(filepathforphoto), self.ui.PatientID_edit.text())
            self.ui.PhotoLabel.setPixmap(QtGui.QPixmap(f"{filepathforphoto}"))
            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has edited a Patients photo, who has the ID {self.ui.PatientID_edit.text()}, at {self.currentdate}, Succsesfully")
        except:
            self.mw.error()


    def PatientSpinBoxSelected(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        if self.ui.PatientIDSpinBox.value() == 0:
            self.ui.PatientFirstName_Edit.clear()
            self.ui.PatientLastName_edit.clear()
            self.ui.PatientAddress_edit.clear()
            self.ui.PatientID_edit.clear()
            self.ui.PatientHeight_Edit.clear()
            self.ui.PatientWeight_Edit.clear()
            self.ui.PatientDateOfBirthEdit.clear()
            self.ui.PhotoLabel.clear()
        else:
            if self.ui.PatientIDSpinBox.value() != self.ui.PatientID_edit.text():
                ID = str(self.ui.PatientIDSpinBox.value())
                IDs = self.ds.SearchAllPatientID()
                if ID not in IDs:
                    self.mw.error()
                    if self.ui.PatientID_edit.text() == "":
                        self.ui.PatientIDSpinBox.setValue(int(self.ui.PatientIDSpinBox.value()) -1)
                    else:
                        self.ui.PatientIDSpinBox.setValue(int(self.ui.PatientID_edit.text()))
                else:
                    PatientData = self.ds.SelectMatchingPatient(self.ui.PatientIDSpinBox.value())
                    for i in PatientData:
                        self.ui.PatientFirstName_Edit.setText(i[1])
                        self.ui.PatientLastName_edit.setText(i[2])
                        self.ui.PatientAddress_edit.setText(str(i[5]))
                        self.ui.PatientID_edit.setText(str(i[0]))
                        self.ui.PatientHeight_Edit.setText(str(i[3]))
                        self.ui.PatientWeight_Edit.setText(str(i[4]))
                        self.ui.PatientDateOfBirthEdit.setText(i[7])
                        list = i[7].split('/')
                        self.ui.PatientDateOfBirthDateEdit.setDateTime(QDateTime(datetime.datetime(int(list[2]), int(list[1]), int(list[0]))))
                        if i[6] == "":
                            self.ui.PhotoLabel.setText("Photo Cannot Be Found for this Patient")
                        else:
                            self.ui.PhotoLabel.setPixmap(QtGui.QPixmap(f"{i[6]}"))
            else:
                print("its broke")
            FirstName = self.ui.PatientFirstName_Edit.text()
            LastName = self.ui.PatientLastName_edit.text()
            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for {FirstName} {LastName}, By Scrolling through the SpinBox, at {self.currentdate}, Succsesfully")
        
    def SearchByNamePatients(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        msg = QMessageBox()
        FirstName = self.ui.PatientFirstNameSearchInput.text()
        LastName = self.ui.PatientLastNameSearchInput.text()
        MatchingFirstName = self.ds.MatchingPatientFirstName()
        MatchingLastName = self.ds.MatchingPatientLastName()
        if FirstName not in MatchingFirstName:
            msg.setWindowTitle("Operation Failed")
            msg.setText("That First Name does not exist!")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        else:
            if LastName not in MatchingLastName:
                msg.setWindowTitle("Operation Failed")
                msg.setText("That Last Name does not exist!")
                msg.setStandardButtons(QMessageBox.Close)
                msg.exec()
            else:
                PatientData = self.ds.SelectMatchingPatientName(FirstName, LastName)
                for i in PatientData:
                    self.ui.PatientFirstName_Edit.setText(i[1])
                    self.ui.PatientLastName_edit.setText(i[2])
                    self.ui.PatientAddress_edit.setText(str(i[5]))
                    self.ui.PatientID_edit.setText(str(i[0]))
                    self.ui.PatientHeight_Edit.setText(str(i[3]))
                    self.ui.PatientWeight_Edit.setText(str(i[4]))
                    self.ui.PatientDateOfBirthEdit.setText(i[7])
                    list = i[7].split('/')
                    self.ui.PatientDateOfBirthDateEdit.setDateTime(QDateTime(datetime.datetime(int(list[2]), int(list[1]), int(list[0]))))
                    if i[6] == "":
                        self.ui.PhotoLabel.setText("Photo Cannot Be Found for this Patient")
                    else:
                        self.ui.PhotoLabel.setPixmap(QtGui.QPixmap(f"{i[6]}"))
                if self.ui.PatientIDSpinBox.value() != self.ui.PatientID_edit.text():
                    self.ui.PatientIDSpinBox.setValue(int(self.ui.PatientID_edit.text()))
        FirstName = self.ui.PatientFirstName_Edit.text()
        LastName = self.ui.PatientLastName_edit.text()
        self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for {FirstName} {LastName}, By Searching for their name, at {self.currentdate}, Succsesfully")

    def DeletePatientData(self):
        msg = QMessageBox()
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        PatientID = self.ui.DeletePatientIDInput.text()
        MatchingID = self.ds.SearchAllPatientID()
        if PatientID not in MatchingID:
            self.mw.error()
        else:
            msg.setText("Are you sure you want to do this?")
            msg.setWindowTitle("Are you sure!")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button_clicked = msg.exec()
            if button_clicked == QMessageBox.Yes:
                PatientData = self.ds.SelectMatchingPatient(self.ui.DeletePatientIDInput.text())
                for i in PatientData:
                    self.ui.PatientFirstName_Edit.setText(i[1])
                    self.ui.PatientLastName_edit.setText(i[2])
                FirstName = self.ui.PatientFirstName_Edit.text()
                LastName = self.ui.PatientLastName_edit.text()
                Access = self.mw.ClinicianLoginPinPopUpBox(False)
                if Access == True:
                    self.ds.DeletePatient(PatientID)
                    self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Deleted {FirstName} {LastName} from the Data Base, using their ID, at {self.currentdate}, Succsesfully")
                    self.mw.OperationSuccessful()
                    self.ui.PatientComboBox.setCurrentIndex(int(self.ui.DeletePatientIDInput.text()))
                    index = self.ui.PatientComboBox.currentIndex()
                    self.ui.PatientComboBox.removeItem(index)
                else:
                    self.mw.OperationUnsuccessful()
            elif button_clicked == QMessageBox.No:
                QMessageBox.close
                self.mw.OperationUnsuccessful()
            else:
                QMessageBox.close
                self.mw.OperationUnsuccessful()
        self.ui.PatientFirstName_Edit.clear()
        self.ui.PatientLastName_edit.clear()
        self.ui.PatientAddress_edit.clear()
        self.ui.PatientID_edit.clear()
        self.ui.PatientHeight_Edit.clear()
        self.ui.PatientWeight_Edit.clear()
        self.ui.PatientIDSpinBox.setValue(0)

        

    def EditPatientData(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        FirstName = self.ui.PatientFirstName_Edit.text()
        LastName = self.ui.PatientLastName_edit.text()
        PatientID = self.ui.PatientID_edit.text()
        Address = self.ui.PatientAddress_edit.text()
        Weight = self.ui.PatientWeight_Edit.text()
        Height = self.ui.PatientHeight_Edit.text()
        MatchingID = self.ds.SearchAllPatientID()
        DateOfBirth = self.ui.PatientDateOfBirthDateEdit.text()
        Photo = self.ds.PullingPhotoBecauseMyShittyCodeKeepsBuggingButForPatientsThisTime(PatientID)
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are you sure!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_clicked = msg.exec()
        if button_clicked == QMessageBox.Yes:
            if PatientID not in MatchingID:
                msg = QMessageBox()
                msg.setText("Would you like to Insert this as a new entry? (!This will delete the previous entry!)")
                msg.setWindowTitle("There is no entry under this ID")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                button_clicked = msg.exec()
                if button_clicked == QMessageBox.Yes:
                    Access = self.mw.ClinicianLoginPinPopUpBox(False)
                    if Access == True:
                        try:
                            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Edited {FirstName} {LastName}'s Data, at {self.currentdate}, Succsesfully")
                            self.ds.UpdateDetails(FirstName, LastName, Address, PatientID, Weight, Height, DateOfBirth, Photo)
                            self.ds.DeletePatient(self.ui.PatientIDSpinBox.text())
                            self.mw.OperationSuccessful()
                            self.ui.PatientComboBox.clear()
                            self.ui.PatientComboBox.addItem("Please Select a Patient")
                            data = self.ds.PatientDisplayComboBox()
                            sorteddata = sorted(data, reverse=False)
                            self.ui.PatientComboBox.addItems(sorteddata)
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
                if self.ui.PatientComboBox.currentIndex() != 0:
                    Access = self.mw.ClinicianLoginPinPopUpBox(False)
                    if Access == True:
                        try:
                            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Edited {FirstName} {LastName}'s Data, at {self.currentdate}, Succsesfully")
                            self.ds.UpdateDetails(FirstName, LastName, Address, PatientID, Weight, Height, DateOfBirth, Photo)
                            self.mw.OperationSuccessful()
                            self.ui.PatientComboBox.clear()
                            self.ui.PatientComboBox.addItem("Please Select a Patient")
                            data = self.ds.PatientDisplayComboBox()
                            sorteddata = sorted(data, reverse=False)
                            self.ui.PatientComboBox.addItems(sorteddata)
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
                        self.ds.UpdateDetails(FirstName, LastName, Address, PatientID, Weight, Height, DateOfBirth, Photo)
                        self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Edited {FirstName} {LastName}'s Data, at {self.currentdate}, Succsesfully")
                        self.mw.OperationSuccessful()
                        self.ui.PatientComboBox.clear()
                        self.ui.PatientComboBox.addItem("Please Select a Patient")
                        data = self.ds.PatientDisplayComboBox()
                        sorteddata = sorted(data, reverse=False)
                        self.ui.PatientComboBox.addItems(sorteddata)
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

    def AddNewPatient(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        FirstName = self.ui.PatientFirstName_Edit.text()
        LastName = self.ui.PatientLastName_edit.text()
        PatientID = self.ui.PatientID_edit.text()
        Address = self.ui.PatientAddress_edit.text()
        Weight = self.ui.PatientWeight_Edit.text()
        Height = self.ui.PatientHeight_Edit.text()
        MatchingID = self.ds.SearchAllPatientID()
        DateOfBirth = self.ui.PatientDateOfBirthEdit.text()
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are you sure!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_clicked = msg.exec()
        if button_clicked == QMessageBox.Yes:
                if PatientID in MatchingID:
                    msg.setText("A Patient Already exists under this ID...")
                    msg.setWindowTitle("Operation Failed!")
                    msg.setStandardButtons(QMessageBox.Close)
                    msg.exec()
                else:
                    Access = self.mw.ClinicianLoginPinPopUpBox(False)
                    if Access == True:
                        try:
                            self.ds.NewPatientDS(FirstName, LastName, PatientID, Weight, Height, Address, DateOfBirth)
                            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Added a new Patient, {FirstName} {LastName}, at {self.currentdate}, Succsesfully")
                            self.mw.OperationSuccessful()
                            data = [f"ID: {PatientID} Patient"]
                            self.ui.PatientComboBox.addItems(data)
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

    def ChangeDateTimeToLineEdit(self):
        if self.ui.PatientDateOfBirthEdit.text() == "":
            pass
        elif self.ui.PatientDateOfBirthEdit.text() != "":
            try:
                LineEdit = self.ui.PatientDateOfBirthEdit.text().split('/')
                self.ui.PatientDateOfBirthDateEdit.setDateTime(QDateTime(datetime.datetime(int(LineEdit[2]), int(LineEdit[1]), int(LineEdit[0]))))
            except:
                print("No Can Do!!")
        else:
            print("No Can Do!!")
    
    def LineEditToChangeDate(self):
        try:
            DateEdit = str(self.ui.PatientDateOfBirthDateEdit.text())
            self.ui.PatientDateOfBirthEdit.setText(DateEdit)
        except:
            print("Not A Chance!")
            
    def PatientComboBox(self):
        data = self.ds.PatientDisplayComboBox()
        sorteddata = sorted(data, reverse=False)
        self.ui.PatientComboBox.addItems(sorteddata)

    def ChangedPatientComboBox(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        if self.ui.PatientComboBox.count() == 0:
            pass
        elif self.ui.PatientComboBox.count() != 0:
            if self.ui.PatientComboBox.currentIndex() == 0:
                self.ui.PatientFirstName_Edit.clear()
                self.ui.PatientLastName_edit.clear()
                self.ui.PatientAddress_edit.clear()
                self.ui.PatientID_edit.clear()
                self.ui.PatientHeight_Edit.clear()
                self.ui.PatientWeight_Edit.clear()
                self.ui.PatientIDSpinBox.setValue(0)
                self.ui.PatientDateOfBirthEdit.clear()
                self.ui.PhotoLabel.clear()
            else:
                item = self.ui.PatientComboBox.currentText()
                value = [item.split(':')[1].strip()[0]]
                self.ds.PatientSearchByComboBox(value[0])
                PatientData = self.ds.PatientSearchByComboBox(value[0])
                for i in PatientData:
                    self.ui.PatientFirstName_Edit.setText(i[1])
                    self.ui.PatientLastName_edit.setText(i[2])
                    self.ui.PatientAddress_edit.setText(str(i[5]))
                    self.ui.PatientID_edit.setText(str(i[0]))
                    self.ui.PatientHeight_Edit.setText(str(i[3]))
                    self.ui.PatientWeight_Edit.setText(str(i[4]))
                    self.ui.PatientDateOfBirthEdit.setText(i[7])
                    list = i[7].split('/')
                    self.ui.PatientDateOfBirthDateEdit.setDateTime(QDateTime(datetime.datetime(int(list[2]), int(list[1]), int(list[0]))))
                if self.ui.PatientIDSpinBox.value() != self.ui.PatientID_edit.text():
                    self.ui.PatientIDSpinBox.setValue(int(self.ui.PatientID_edit.text()))
                    self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for {self.ui.PatientFirstName_Edit.text()} {self.ui.PatientLastName_edit.text()}, by using the ComboBox, at {self.currentdate}, Succsesfully")
        else:
            print("shit, we broke it")
