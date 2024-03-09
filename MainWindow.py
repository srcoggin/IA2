from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UserInterface import Ui_Form
from datastore import DataStore
from PyQt5 import QtGui
import datetime
from PyQt5.QtWidgets import *





class MainWindow():
    def __init__(self):
        self.LineEdit = QLineEdit()
        self.currentdate = datetime.datetime.now()
        self.LogFile = open("Log.txt", "a")
        self.main_win = QMainWindow()
        self.ds = DataStore()
        self.ui = Ui_Form()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

        #Login Page Buttons
        self.ui.EnterButton_LoginPage.clicked.connect(self.Login)
        self.ui.ExitButton_LoginPage.clicked.connect(self.Exit)

        #Home Page Buttons
        self.ui.PatientsButton_HomePage.clicked.connect(self.PatientsPageSelect)
        self.ui.ClinicansButton_Homepage.clicked.connect(self.ClinicianPageSelect)
        self.ui.AppointmentsButton_HomePage.clicked.connect(self.AppointmentPageSelect)
        self.ui.ExitButtonHomePage.clicked.connect(self.Exit)

        #Patients Page Buttons
        self.ui.PatientIDSearchButton.clicked.connect(self.SearchByIDPatients)
        self.ui.PatientIDSpinBox.valueChanged.connect(self.PatientSpinBoxSelected)
        self.ui.ExitButton_PatientsPage.clicked.connect(self.Exit)
        self.ui.AppointmentsButton_PatientsPage.clicked.connect(self.AppointmentPageSelect)
        self.ui.ClinicansButton_PatientsPage.clicked.connect(self.ClinicianPageSelect)
        self.ui.HomeButton_PatientsPage.clicked.connect(self.HomePageSelect)
        self.ui.PatientNameSearchButton.clicked.connect(self.SearchByNamePatients)
        self.ui.PatientEditData_Button.clicked.connect(self.EditPatientData)
        self.ui.DeletePatientButton.clicked.connect(self.DeletePatientData)
        self.ui.PatientAddDataButton.clicked.connect(self.AddNewPatient)

        #Clinician Page Buttons
        self.ui.ClinicianAppointmentButton.clicked.connect(self.AppointmentPageSelect)
        self.ui.ClinicianPatientsPageButton.clicked.connect(self.PatientsPageSelect)
        self.ui.ClinicianHomePageButton.clicked.connect(self.HomePageSelect)
        self.ui.ExitButtonClinicianPage.clicked.connect(self.Exit)
        self.ui.ClinicianIDSearchButton.clicked.connect(self.SearchByIDClinician)
        self.ui.ClinicianIDSpinBox.valueChanged.connect(self.ClinicianSpinBoxSelected)
        self.ui.ClinicianRoleSearchButton.clicked.connect(self.SearchClinicianByRole)
        self.ui.ClinicianSearchByDepartmentButton.clicked.connect(self.SearchClinicianByDepartment)
        self.ui.DeleteClinicianButton.clicked.connect(self.DeleteClinicianData)



    #Shows the user interface
    def show(self):
        self.main_win.show()
    #Exits the program
    def Exit(self):
        Name = self.ds.MatchingClinicianName(self.ui.LoginPage_PinEnter.text())
        if self.ui.LoginPage_PinEnter.text() == "":
            pass
        else:
            self.LogFile.write(f"\n{Name}, Logged out of the app, at {self.currentdate}, Succsesfully")
            self.LogFile.close()
        exit()


    #Pop Up Boxes
    def error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Operation Failed")
        msg.setText("    That Operation Cannot be Computed!        ")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec()

    def OperationUnsuccessful(self):
        msg = QMessageBox()
        msg.setWindowTitle("Operation Closed!")
        msg.setText("Operation was not completed.")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec()

    def MoreThanTwoOfThem(self):
        msg = QMessageBox()
        msg.setWindowTitle("Operation Closed!")
        msg.setText("Sorry Dude, theres two or more entries that match this searching condition, and Will is too lazy to code a pop up box where you select which one you'd want to see. so ig you'll just have to try another search method. whoops.")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec()

    def ClinicianLoginPinPopUpBox(self, Access):
        AllLoginPins = self.ds.AllLoginPins()
        text , ok = QInputDialog.getText(self.main_win,'Please Enter your Login Pin','Login Pin = ')
        if ok:
            self.LineEdit.setText(str(text))
            print(self.LineEdit.text())
            LoginPin = self.LineEdit.text()
            if LoginPin not in AllLoginPins:
                msg = QMessageBox()
                msg.setWindowTitle("That Login Pin is wrong!")
                msg.setText("Try Again with a new Pin")
                msg.setStandardButtons(QMessageBox.Close)
                msg.exec()
            else:
                Access = True
                return Access
        else:   
            self.OperationUnsuccessful()


    #Page Selection Functions
    def PatientsPageSelect(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Patients)
    def ClinicianPageSelect(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Clinicians)
    def AppointmentPageSelect(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Appointments)
    def HomePageSelect(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
    def LoginPageSelect(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)


    #Login Page Functions
    def Login(self):
        msg = QMessageBox()
        LoginPin = self.ui.LoginPage_PinEnter.text()
        LoginPinsAvaliable = self.ds.AllLoginPins()
        if LoginPin not in LoginPinsAvaliable:
            msg.setWindowTitle("Login Failed")
            msg.setText("That Login Pin Does Not Match!")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()
        else:
            name = self.ds.MatchingClinicianName(LoginPin)
            self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
            msg.setWindowTitle("Welcome")
            msg.setText(f"Welcome Back, {name}!")
            self.LogFile.write(f"\n{name}, has logged into the app at {self.currentdate}")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()

    #Patients Page Functions
    def SearchByIDPatients(self):
        Name = self.ds.MatchingClinicianName(self.ui.LoginPage_PinEnter.text())
        ID = self.ui.PatientIdSearchInput.text()
        IDs = self.ds.SearchAllPatientID()
        if ID not in IDs:
            self.error()
        else:
            PatientData = self.ds.SelectMatchingPatient(self.ui.PatientIdSearchInput.text())
            for i in PatientData:
                self.ui.PatientFirstName_Edit.setText(i[1])
                self.ui.PatientLastName_edit.setText(i[2])
                self.ui.PatientAddress_edit.setText(str(i[5]))
                self.ui.PatientID_edit.setText(str(i[0]))
                self.ui.PatientHeight_Edit.setText(str(i[3]))
                self.ui.PatientWeight_Edit.setText(str(i[4]))
                if i[6] == "":
                    self.ui.PhotoLabel.setText("Photo Cannot Be Found for this Patient")
                else:
                    self.ui.PhotoLabel.setPixmap(QtGui.QPixmap(f"{i[6]}"))
            if self.ui.PatientIDSpinBox.value() != self.ui.PatientID_edit.text():
                self.ui.PatientIDSpinBox.setValue(int(self.ui.PatientID_edit.text()))
            FirstName = self.ui.PatientFirstName_Edit.text()
            LastName = self.ui.PatientLastName_edit.text()
            self.LogFile.write(f"\n{Name}, has searched for {FirstName} {LastName}, By Searching for their ID, at {self.currentdate}, Succsesfully")

    def PatientSpinBoxSelected(self):
        Name = self.ds.MatchingClinicianName(self.ui.LoginPage_PinEnter.text())
        if self.ui.PatientIDSpinBox.value() == 0:
            pass
        else:
            if self.ui.PatientIDSpinBox.value() != self.ui.PatientID_edit.text():
                ID = str(self.ui.PatientIDSpinBox.value())
                IDs = self.ds.SearchAllPatientID()
                if ID not in IDs:
                    self.error()
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
                        if i[6] == "":
                            self.ui.PhotoLabel.setText("Photo Cannot Be Found for this Patient")
                        else:
                            self.ui.PhotoLabel.setPixmap(QtGui.QPixmap(f"{i[6]}"))
            else:
                print("its broke")
            FirstName = self.ui.PatientFirstName_Edit.text()
            LastName = self.ui.PatientLastName_edit.text()
            self.LogFile.write(f"\n{Name}, has searched for {FirstName} {LastName}, By Scrolling through the SpinBox, at {self.currentdate}, Succsesfully")
        
    def SearchByNamePatients(self):
        Name = self.ds.MatchingClinicianName(self.ui.LoginPage_PinEnter.text())
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
                    if i[6] == "":
                        self.ui.PhotoLabel.setText("Photo Cannot Be Found for this Patient")
                    else:
                        self.ui.PhotoLabel.setPixmap(QtGui.QPixmap(f"{i[6]}"))
                if self.ui.PatientIDSpinBox.value() != self.ui.PatientID_edit.text():
                    self.ui.PatientIDSpinBox.setValue(int(self.ui.PatientID_edit.text()))
        FirstName = self.ui.PatientFirstName_Edit.text()
        LastName = self.ui.PatientLastName_edit.text()
        self.LogFile.write(f"\n{Name}, has searched for {FirstName} {LastName}, By Searching for their name, at {self.currentdate}, Succsesfully")

    def DeletePatientData(self):
        msg = QMessageBox()
        Name = self.ds.MatchingClinicianName(self.ui.LoginPage_PinEnter.text())
        PatientID = self.ui.DeletePatientIDInput.text()
        MatchingID = self.ds.SearchAllPatientID()
        if PatientID not in MatchingID:
            self.error()
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
                self.LogFile.write(f"\n{Name}, has Deleted {FirstName} {LastName} from the Data Base, using their ID, at {self.currentdate}, Succsesfully")
                Access = self.ClinicianLoginPinPopUpBox(False)
                if Access == True:
                    self.ds.DeletePatient(PatientID)
                else:
                    self.OperationUnsuccessful()
            elif button_clicked == QMessageBox.No:
                QMessageBox.close
                self.OperationUnsuccessful()
            else:
                QMessageBox.close
                self.OperationUnsuccessful()
        self.ui.PatientFirstName_Edit.clear()
        self.ui.PatientLastName_edit.clear()
        self.ui.PatientAddress_edit.clear()
        self.ui.PatientID_edit.clear()
        self.ui.PatientHeight_Edit.clear()
        self.ui.PatientWeight_Edit.clear()

        

    def EditPatientData(self):
        Name = self.ds.MatchingClinicianName(self.ui.LoginPage_PinEnter.text())
        FirstName = self.ui.PatientFirstName_Edit.text()
        LastName = self.ui.PatientLastName_edit.text()
        PatientID = self.ui.PatientID_edit.text()
        Address = self.ui.PatientAddress_edit.text()
        Weight = self.ui.PatientWeight_Edit.text()
        Height = self.ui.PatientHeight_Edit.text()
        MatchingID = self.ds.SearchAllPatientID()
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
                    Access = self.ClinicianLoginPinPopUpBox(False)
                    if Access == True:
                        self.LogFile.write(f"\n{Name}, has Edited {FirstName} {LastName}'s Data, at {self.currentdate}, Succsesfully")
                        self.ds.UpdateDetails(FirstName, LastName, Address, PatientID, Weight, Height)
                        self.ds.DeletePatient(self.ui.PatientIDSpinBox.text())
                    else:
                        self.OperationUnsuccessful()
                elif button_clicked == QMessageBox.No:
                    QMessageBox.close
                    self.OperationUnsuccessful()
                else:
                    QMessageBox.close
                    self.OperationUnsuccessful()
            else:
                Access = self.ClinicianLoginPinPopUpBox(False)
                if Access == True:
                    self.ds.UpdateDetails(FirstName, LastName, Address, PatientID, Weight, Height)
                else:
                    self.OperationUnsuccessful()
        elif button_clicked == QMessageBox.No:
            QMessageBox.close
        else:
            QMessageBox.close

    def AddNewPatient(self):
        Name = self.ds.MatchingClinicianName(self.ui.LoginPage_PinEnter.text())
        FirstName = self.ui.PatientFirstName_Edit.text()
        LastName = self.ui.PatientLastName_edit.text()
        PatientID = self.ui.PatientID_edit.text()
        Address = self.ui.PatientAddress_edit.text()
        Weight = self.ui.PatientWeight_Edit.text()
        Height = self.ui.PatientHeight_Edit.text()
        MatchingID = self.ds.SearchAllPatientID()
        msg = QMessageBox()
        msg.setText("Are you sure you want to do this?")
        msg.setWindowTitle("Are you sure!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_clicked = msg.exec()
        if button_clicked == QMessageBox.Yes:
                if PatientID in MatchingID:
                    msg.setText("A Patient Already exists under this ID...")
                    msg.setWindowTitle("Operation Failed!")
                else:
                    Access = self.ClinicianLoginPinPopUpBox(False)
                    if Access == True:
                        self.ds.NewPatientDS(FirstName, LastName, PatientID, Weight, Height, Address)
                        self.LogFile.write(f"\n{Name}, has Added a new Patient, {FirstName} {LastName}, at {self.currentdate}, Succsesfully")
                    else:
                        self.OperationUnsuccessful()
        elif button_clicked == QMessageBox.No:
            QMessageBox.close
        else:
            QMessageBox.close

    #Clinician Functions
    def SearchByIDClinician(self):
        Name = self.ds.MatchingClinicianName(self.ui.LoginPage_PinEnter.text())
        ID = self.ui.ClinicianIDSearchInput.text()
        IDs = self.ds.SearchAllClinicianID()
        if ID not in IDs:
            self.error()
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
                    self.ui.PhotoLabelClinician.setPixmap(QtGui.QPixmap(f"{i[6]}"))
            if self.ui.ClinicianIDSpinBox.value() != self.ui.ClinicianIDEdit.text():
                self.ui.ClinicianIDSpinBox.setValue(int(self.ui.ClinicianIDEdit.text()))
            FirstName = self.ui.ClinicianFirstNameEdit.text()
            LastName = self.ui.ClinicianLastNameEdit.text()
            self.LogFile.write(f"\n{Name}, has searched for {FirstName} {LastName}, By Searching for their ID, at {self.currentdate}, Succsesfully")

    def ClinicianSpinBoxSelected(self):
        Name = self.ds.MatchingClinicianName(self.ui.LoginPage_PinEnter.text())
        if self.ui.ClinicianIDSpinBox.value() == 0:
            pass
        else:
            if self.ui.ClinicianIDSpinBox.value() != self.ui.ClinicianIDEdit.text():
                ID = str(self.ui.ClinicianIDSpinBox.value())
                IDs = self.ds.SearchAllClinicianID()
                if ID not in IDs:
                    self.error()
                    if self.ui.ClinicianIDEdit.text() == "":
                        self.ui.ClinicianIDSpinBox.setValue(int(self.ui.ClinicianIDSpinBox.value()) -1)
                    else:
                        self.ui.ClinicianIDSpinBox.setValue(int(self.ui.ClinicianIDEdit.text()))
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
                            self.ui.PhotoLabelClinician.setPixmap(QtGui.QPixmap(f"{i[6]}"))
            else:
                print("its broke")
            FirstName = self.ui.ClinicianFirstNameEdit.text()
            LastName = self.ui.ClinicianLastNameEdit.text()
            self.LogFile.write(f"\n{Name}, has searched for {FirstName} {LastName}, By Scrolling through the SpinBox, at {self.currentdate}, Succsesfully")

    def SearchClinicianByRole(self):
        name = self.ds.MatchingClinicianName(self.ui.LoginPage_PinEnter.text())
        ClinicianRole = self.ui.ClinicianRoleSearchInput.text()
        AllRoles = self.ds.SearchAllRoles()
        if ClinicianRole not in AllRoles:
            self.error()
        else:
            Numb = 0
            for i in range(1):
                if ClinicianRole in AllRoles:
                    NumbOfMatches = AllRoles.count(ClinicianRole)
                    if NumbOfMatches > 1:
                        self.MoreThanTwoOfThem()
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
                                self.ui.PhotoLabelClinician.setPixmap(QtGui.QPixmap(f"{i[6]}"))
                            if self.ui.ClinicianIDSpinBox.value() != self.ui.ClinicianIDEdit.text():
                                self.ui.ClinicianIDSpinBox.setValue(int(self.ui.ClinicianIDEdit.text()))
                            FirstName = self.ui.ClinicianFirstNameEdit.text()
                            LastName = self.ui.ClinicianLastNameEdit.text()
                            self.LogFile.write(f"\n{name}, has searched for {FirstName} {LastName}, By Searching for their Role, at {self.currentdate}, Succsesfully")

    def SearchClinicianByDepartment(self):
        name = self.ds.MatchingClinicianName(self.ui.LoginPage_PinEnter.text())
        ClinicianDepartment = self.ui.ClinicianSearchByDepartmentInput.text()
        AllDepartments = self.ds.SearchAllDepartments()
        if ClinicianDepartment not in AllDepartments:
            self.error()
        else:
            Numb = 0
            for i in range(1):
                if ClinicianDepartment in AllDepartments:
                    NumbOfMatches = AllDepartments.count(ClinicianDepartment)
                    if NumbOfMatches > 1:
                        self.MoreThanTwoOfThem()
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
                                self.ui.PhotoLabelClinician.setPixmap(QtGui.QPixmap(f"{i[6]}"))
                            if self.ui.ClinicianIDSpinBox.value() != self.ui.ClinicianIDEdit.text():
                                self.ui.ClinicianIDSpinBox.setValue(int(self.ui.ClinicianIDEdit.text()))
                            FirstName = self.ui.ClinicianFirstNameEdit.text()
                            LastName = self.ui.ClinicianLastNameEdit.text()
                            self.LogFile.write(f"\n{name}, has searched for {FirstName} {LastName}, By Searching for their Department, at {self.currentdate}, Succsesfully")

    def DeleteClinicianData(self):
        msg = QMessageBox()
        Name = self.ds.MatchingClinicianName(self.ui.LoginPage_PinEnter.text())
        ClinicianID = self.ui.DeleteClinicianIDInput.text()
        MatchingID = self.ds.SearchAllClinicianID()
        if ClinicianID not in MatchingID:
            self.error()
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
                self.LogFile.write(f"\n{Name}, has Deleted {FirstName} {LastName} from the Data Base, using their ID, at {self.currentdate}, Succsesfully")
                Access = self.ClinicianLoginPinPopUpBox(False)
                if Access == True:
                    self.ds.DeleteClinician(ClinicianID)
                else:
                    self.OperationUnsuccessful()
            else:
                QMessageBox.close
                self.OperationUnsuccessful()
        self.ui.ClinicianFirstNameEdit.clear()
        self.ui.ClinicianLastNameEdit.clear()
        self.ui.ClinicianRoleEdit.clear()
        self.ui.ClinicianServicesEdit.clear()
        self.ui.ClinicianLoginPinEdit.clear()
        self.ui.ClinicianDepartmentEdit.clear()
        self.ui.ClinicianIDEdit.clear()
        self.ui.ClinicianIDSpinBox.setValue(0)