from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UserInterface import Ui_Form
from datastore import DataStore
from PyQt5 import QtGui
import datetime





class MainWindow():
    def __init__(self):
        self.currentdate = datetime.datetime.now()
        self.LogFile = open("Log.txt", "a")
        self.main_win = QMainWindow()
        self.ds = DataStore()
        self.ui = Ui_Form()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

        #Login Page Buttons
        self.ui.EnterButton_LoginPage.clicked.connect(self.Login)
        self.ui.SignUp_Button_LoginPage.clicked.connect(self.SignUpPageSelect)
        self.ui.ExitButton_LoginPage.clicked.connect(self.Exit)

        #Sign Up Page Buttons
        self.ui.ExitButton_LoginPage_5.clicked.connect(self.Exit)
        self.ui.LoginButton_LoginPage_5.clicked.connect(self.LoginPageSelect)

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

        #Clinician Page Buttons
        self.ui.ClinicianAppointmentButton.clicked.connect(self.AppointmentPageSelect)
        self.ui.ClinicianPatientsPageButton.clicked.connect(self.PatientsPageSelect)
        self.ui.ClinicianHomePageButton.clicked.connect(self.HomePageSelect)
        self.ui.ExitButtonClinicianPage.clicked.connect(self.Exit)



    #Shows the user interface
    def show(self):
        self.main_win.show()
    #Exits the program
    def Exit(self):
        exit()

    #Error Pop Up Box
    def error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Operation Failed")
        msg.setText("    That Operation Cannot be Computed!        ")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec()

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
    def SignUpPageSelect(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.SignUpPage)

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
            msg.setText(f"Welcome Back {name}!")
            self.LogFile.write(f"\n{name}, has logged into the app at {self.currentdate}")
            self.LogFile.close()
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()

    #Patients Page Functions
    def SearchByIDPatients(self):
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

    def PatientSpinBoxSelected(self):
        if self.ui.PatientIDSpinBox.value() == 0:
            pass
        else:
            if self.ui.PatientIDSpinBox.value() != self.ui.PatientID_edit.text():
                ID = str(self.ui.PatientIDSpinBox.value())
                IDs = self.ds.SearchAllPatientID()
                if ID not in IDs:
                    self.error()
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
        
    def SearchByNamePatients(self):
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

    def DeletePatientData(self):
        PatientID = self.ui.DeletePatientIDInput.text()
        MatchingID = self.ds.SearchAllPatientID()
        if PatientID not in MatchingID:
            self.error()
        else:
            msg = QMessageBox()
            msg.setText("Are you sure you want to do this?")
            msg.setWindowTitle("Are you sure!")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button_clicked = msg.exec()
            if button_clicked == QMessageBox.Yes:
                self.ds.DeletePatient(PatientID)
            elif button_clicked == QMessageBox.No:
                QMessageBox.close
            else:
                QMessageBox.close
            


    def EditPatientData(self):
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
                    self.ds.UpdateDetails(FirstName, LastName, Address, PatientID, Weight, Height)
                    self.ds.DeletePatient(self.ui.PatientIDSpinBox.text())
                elif button_clicked == QMessageBox.No:
                    QMessageBox.close
                else:
                    QMessageBox.close
            else:
                self.ds.UpdateDetails(FirstName, LastName, Address, PatientID, Weight, Height)
        elif button_clicked == QMessageBox.No:
            QMessageBox.close
        else:
            QMessageBox.close

    def AddNewPatient(self):
        pass


