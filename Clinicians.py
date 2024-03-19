from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UserInterface import Ui_Form
from PyQt5 import QtGui
import datetime
from PyQt5.QtWidgets import *
import datetime
from UserInterface import Ui_Form
from datastore import DataStore
from tkinter import *
from tkinter import filedialog

class Clinicians():
    def __init__(self, datastore: DataStore, UI: Ui_Form, MW, Log):
        self.LineEdit = QLineEdit()
        self.currentdate = datetime.datetime.now()
        self.main_win = QMainWindow()
        self.ds = datastore
        self.ui = UI
        self.mw = MW
        self.LogFile = Log

        
    #Clinician Functions
    def SearchByIDClinician(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        ID = self.ui.ClinicianIDSearchInput.text()
        IDs = self.ds.SearchAllClinicianID()
        if ID not in IDs:
            self.mw.error()
        else:
            ClinicianData = self.ds.SelectMatchingClinician(int(self.ui.ClinicianIDSearchInput.text()))
            for i in ClinicianData:
                self.ui.ClinicianFirstNameEdit.setText(i[1])
                self.ui.ClinicianLastNameEdit.setText(i[2])
                self.ui.ClinicianLoginPinEdit.setText(str(i[3]))
                self.ui.ClinicianRoleEdit.setText(i[4])
                self.ui.ClinicianDepartmentEdit.setText(str(i[5]))
                self.ui.ClinicianIDEdit.setText(str(i[0]))
                self.ui.ClinicianServicesEdit.setText(i[6])
                if i[7] == "":
                    self.ui.PhotoLabelClinician.setText("Photo Cannot Be Found for this Patient")
                else:
                    self.ui.PhotoLabelClinician.setPixmap(QtGui.QPixmap(f"{i[7]}"))
            if self.ui.ClinicianIDSpinBox.value() != self.ui.ClinicianIDEdit.text():
                self.ui.ClinicianIDSpinBox.setValue(int(self.ui.ClinicianIDEdit.text()))
            FirstName = self.ui.ClinicianFirstNameEdit.text()
            LastName = self.ui.ClinicianLastNameEdit.text()
            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for {FirstName} {LastName}, By Searching for their ID, at {self.currentdate}, Succsesfully")

    def ClinicianSpinBoxSelected(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        if self.ui.ClinicianIDSpinBox.value() == 0:
            pass
        else:
            if self.ui.ClinicianIDSpinBox.value() != self.ui.ClinicianIDEdit.text():
                ID = str(self.ui.ClinicianIDSpinBox.value())
                IDs = self.ds.SearchAllClinicianID()
                if ID not in IDs:
                    self.mw.error()
                    if self.ui.ClinicianIDEdit.text() == "":
                        x = self.ui.ClinicianIDSpinBox.value()
                        y = int(self.ui.ClinicianIDEdit.text())
                        dif = x - y 
                        self.ui.ClinicianIDSpinBox.setValue(int(self.ui.ClinicianIDSpinBox.value()) -dif)
                    else:
                        x = self.ui.ClinicianIDSpinBox.value()
                        y = int(self.ui.ClinicianIDEdit.text())
                        dif = x - y 
                        self.ui.ClinicianIDSpinBox.setValue(int(self.ui.ClinicianIDSpinBox.value()) -dif)
                        if self.ui.ClinicianIDSpinBox.value() != int(self.ui.ClinicianIDEdit.text()):
                            x = self.ui.ClinicianIDSpinBox.value()
                            y = int(self.ui.ClinicianIDEdit.text())
                            dif = x - y
                            self.ui.ClinicianIDSpinBox.setValue(int(self.ui.ClinicianIDSpinBox.value()) - dif)

                else:
                    ClinicianData = self.ds.SelectMatchingClinician(self.ui.ClinicianIDSpinBox.value())
                    for i in ClinicianData:
                        self.ui.ClinicianFirstNameEdit.setText(i[1])
                        self.ui.ClinicianLastNameEdit.setText(i[2])
                        self.ui.ClinicianLoginPinEdit.setText(str(i[3]))
                        self.ui.ClinicianRoleEdit.setText(i[4])
                        self.ui.ClinicianDepartmentEdit.setText(str(i[5]))
                        self.ui.ClinicianIDEdit.setText(str(i[0]))
                        self.ui.ClinicianServicesEdit.setText(i[6])
                        if i[7] == "":
                            self.ui.PhotoLabelClinician.setText("Photo Cannot Be Found for this Patient")
                        else:
                            self.ui.PhotoLabelClinician.setPixmap(QtGui.QPixmap(f"{i[7]}"))
            else:
                print("its broke")
            FirstName = self.ui.ClinicianFirstNameEdit.text()
            LastName = self.ui.ClinicianLastNameEdit.text()
            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for {FirstName} {LastName}, By Scrolling through the SpinBox, at {self.currentdate}, Succsesfully")
    
    
    def SearchClinicianByRole(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        ClinicianRole = self.ui.ClinicianRoleSearchInput.text()
        AllRoles = self.ds.SearchAllRoles()
        if ClinicianRole not in AllRoles:
            self.mw.error()
        else:
            for i in range(1):
                if ClinicianRole in AllRoles:
                    NumbOfMatches = AllRoles.count(ClinicianRole)
                    if NumbOfMatches > 1:
                        self.mw.MoreThanTwoOfThem()
                    else:
                        ClinicianData = self.ds.MatchingClinicianRole(ClinicianRole)
                        for i in ClinicianData:
                            self.ui.ClinicianFirstNameEdit.setText(i[1])
                            self.ui.ClinicianLastNameEdit.setText(i[2])
                            self.ui.ClinicianLoginPinEdit.setText(str(i[3]))
                            self.ui.ClinicianRoleEdit.setText(i[4])
                            self.ui.ClinicianDepartmentEdit.setText(str(i[5]))
                            self.ui.ClinicianIDEdit.setText(str(i[0]))
                            self.ui.ClinicianServicesEdit.setText(i[6])
                            if i[7] == "":
                                self.ui.PhotoLabelClinician.setText("Photo Cannot Be Found for this Clinician")
                            else:
                                self.ui.PhotoLabelClinician.setPixmap(QtGui.QPixmap(f"{i[7]}"))
                            if self.ui.ClinicianIDSpinBox.value() != self.ui.ClinicianIDEdit.text():
                                self.ui.ClinicianIDSpinBox.setValue(int(self.ui.ClinicianIDEdit.text()))
                            FirstName = self.ui.ClinicianFirstNameEdit.text()
                            LastName = self.ui.ClinicianLastNameEdit.text()
                            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for {FirstName} {LastName}, By Searching for their Role, at {self.currentdate}, Succsesfully")

    def SearchClinicianByDepartment(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        ClinicianDepartment = self.ui.ClinicianSearchByDepartmentInput.text()
        AllDepartments = self.ds.SearchAllDepartments()
        if ClinicianDepartment not in AllDepartments:
            self.mw.error()
        else:
            Numb = 0
            for i in range(1):
                if ClinicianDepartment in AllDepartments:
                    NumbOfMatches = AllDepartments.count(ClinicianDepartment)
                    if NumbOfMatches > 1:
                        self.mw.MoreThanTwoOfThem()
                    else:
                        ClinicianData = self.ds.MatchingClinicianDepartment(ClinicianDepartment)
                        for i in ClinicianData:
                            self.ui.ClinicianFirstNameEdit.setText(i[1])
                            self.ui.ClinicianLastNameEdit.setText(i[2])
                            self.ui.ClinicianLoginPinEdit.setText(str(i[3]))
                            self.ui.ClinicianRoleEdit.setText(i[4])
                            self.ui.ClinicianDepartmentEdit.setText(str(i[5]))
                            self.ui.ClinicianIDEdit.setText(str(i[0]))
                            self.ui.ClinicianServicesEdit.setText(i[6])
                            if i[7] == "":
                                self.ui.PhotoLabelClinician.setText("Photo Cannot Be Found for this Clinician")
                            else:
                                self.ui.PhotoLabelClinician.setPixmap(QtGui.QPixmap(f"{i[7]}"))
                            if self.ui.ClinicianIDSpinBox.value() != self.ui.ClinicianIDEdit.text():
                                self.ui.ClinicianIDSpinBox.setValue(int(self.ui.ClinicianIDEdit.text()))
                            FirstName = self.ui.ClinicianFirstNameEdit.text()
                            LastName = self.ui.ClinicianLastNameEdit.text()
                            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has searched for {FirstName} {LastName}, By Searching for their Department, at {self.currentdate}, Succsesfully")

    def DeleteClinicianData(self):
        msg = QMessageBox()
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        ClinicianID = self.ui.DeleteClinicianIDInput.text()
        MatchingID = self.ds.SearchAllClinicianID()
        if ClinicianID not in MatchingID:
            self.mw.error()
        else:
            msg.setText("Are you sure you want to do this?")
            msg.setWindowTitle("Are you sure!")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button_clicked = msg.exec()
            if button_clicked == QMessageBox.Yes:
                ClinicianData = self.ds.SelectMatchingClinician(self.ui.DeleteClinicianIDInput.text())
                for i in ClinicianData:
                    self.ui.ClinicianFirstNameEdit.setText(i[1])
                    self.ui.ClinicianLastNameEdit.setText(i[2])
                FirstName = self.ui.ClinicianFirstNameEdit.text()
                LastName = self.ui.ClinicianLastNameEdit.text()
                self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Deleted {FirstName} {LastName} from the Data Base, using their ID, at {self.currentdate}, Succsesfully")
                Access = self.mw.ClinicianLoginPinPopUpBox(False)
                if Access == True:
                    self.ds.DeleteClinician(ClinicianID)
                    self.mw.OperationSuccessful()
                    self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Deleted {FirstName} {LastName} from the Data Base, using their ID, at {self.currentdate}, Succsesfully")
                else:
                    self.mw.OperationUnsuccessful()
            else:
                QMessageBox.close
                self.mw.OperationUnsuccessful()
        self.ui.ClinicianFirstNameEdit.clear()
        self.ui.ClinicianLastNameEdit.clear()
        self.ui.ClinicianRoleEdit.clear()
        self.ui.ClinicianServicesEdit.clear()
        self.ui.ClinicianLoginPinEdit.clear()
        self.ui.ClinicianDepartmentEdit.clear()
        self.ui.ClinicianIDEdit.clear()
        self.ui.ClinicianIDSpinBox.setValue(0)

    def EditClinicianData(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        FirstName = self.ui.ClinicianFirstNameEdit.text()
        LastName = self.ui.ClinicianLastNameEdit.text()
        ClinicianID = self.ui.ClinicianIDEdit.text()
        Role = self.ui.ClinicianRoleEdit.text()
        LoginPin = self.ui.ClinicianLoginPinEdit.text()
        Department = self.ui.ClinicianDepartmentEdit.text()
        Services = self.ui.ClinicianServicesEdit.text()
        MatchingID = self.ds.SearchAllClinicianID()
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are you sure!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_clicked = msg.exec()
        if button_clicked == QMessageBox.Yes:
            if ClinicianID not in MatchingID:
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
                            self.ds.UpdateClinicianDetails(FirstName, LastName, Department, ClinicianID, Role, LoginPin, Services)
                            self.ds.DeleteClinician(self.ui.ClinicianIDSpinBox.text())
                            self.ui.ClinicianIDSpinBox.setValue(int(self.ui.ClinicianIDEdit.text()))
                            self.mw.OperationSuccessful()
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
            else:
                Access = self.mw.ClinicianLoginPinPopUpBox(False)
                if Access == True:
                    self.ds.UpdateClinicianDetails(FirstName, LastName, Department, ClinicianID, Role, LoginPin, Services)
                    self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Edited {FirstName} {LastName}'s Data, at {self.currentdate}, Succsesfully")
                    self.ui.ClinicianIDSpinBox.setValue(int(self.ui.ClinicianIDEdit.text()))
                    self.mw.OperationSuccessful()
                else:
                    self.mw.OperationUnsuccessful()
        elif button_clicked == QMessageBox.No:
            QMessageBox.close
        else:
            QMessageBox.close

    def AddNewClinician(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        FirstName = self.ui.ClinicianFirstNameEdit.text()
        LastName = self.ui.ClinicianLastNameEdit.text()
        ClinicianID = self.ui.ClinicianIDEdit.text()
        Role = self.ui.ClinicianRoleEdit.text()
        Department = self.ui.ClinicianDepartmentEdit.text()
        LoginPin = self.ui.ClinicianLoginPinEdit.text()
        Services = self.ui.ClinicianServicesEdit.text()
        MatchingID = self.ds.SearchAllClinicianID()
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are you sure!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_clicked = msg.exec()
        if button_clicked == QMessageBox.Yes:
                if ClinicianID in MatchingID:
                    msg.setText("A Clinician Already exists under this ID...")
                    msg.setWindowTitle("Operation Failed!")
                else:
                    Access = self.mw.ClinicianLoginPinPopUpBox(False)
                    if Access == True:
                        try:
                            self.ds.NewClinicianDS(FirstName, LastName, Department, ClinicianID, Role, LoginPin, Services)
                            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, has Added a new Patient, {FirstName} {LastName}, at {self.currentdate}, Succsesfully")
                            self.mw.OperationSuccessful()
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

    def ChangeClinicianPhoto(self):
        try:
            filepathforphoto = filedialog.askopenfilename(initialdir="C:", title="Please Choose A Photo", filetypes=(("jpg files", "*.jpg"),("png file", "*.png")))
            self.ds.EditPhotoClinician(str(filepathforphoto), self.ui.ClinicianIDEdit.text())
            print(filepathforphoto)
            self.ui.PhotoLabelClinician.setPixmap(QtGui.QPixmap(f"{filepathforphoto}"))
        except:
            self.mw.error()