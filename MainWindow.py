from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UserInterface import Ui_Form
from datastore import DataStore
import datetime
from PyQt5.QtWidgets import *
import datetime
from Patients import Patients
from Clinicians import Clinicians
from Appointmenets import Appointments
from SalesData import Sales




class NewMainWindow():
    def __init__(self):
        self.LineEdit = QLineEdit()
        self.currentdate = datetime.datetime.now()
        self.LogFile = open("Log.txt", "a")
        self.main_win = QMainWindow()
        self.ds = DataStore()
        self.ui = Ui_Form()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)
        self.PP = Patients(self.ds, self.ui, self, self.LogFile)
        self.CP = Clinicians(self.ds, self.ui, self, self.LogFile)
        self.AP = Appointments(self.ds, self.ui, self, self.LogFile)
        self.SD = Sales(self.ds, self.ui, self, self.LogFile)
        self.ui.AppointmentComboBox.addItem("Please Select an Appointment")
        self.ui.PatientComboBox.addItem("Please Select a Patient")
        self.ui.ClinicianComboBox.addItem("Please Select a Clinician")
        self.ui.SalesDataComboBox.addItem("Please Select a Period")
        self.AP.AppointmentComboBox()
        self.PP.PatientComboBox()
        self.CP.ClinicianComboBox()
        self.SD.SalesDataComboBox()
        self.thesuperlazyfunction()

        #Login Page Buttons
        self.ui.EnterButton_LoginPage.clicked.connect(self.Login)
        self.ui.ExitButton_LoginPage.clicked.connect(self.Exit)

        #Home Page Buttons
        self.ui.PatientsButton_HomePage.clicked.connect(self.PatientsPageSelect)
        self.ui.ClinicansButton_Homepage.clicked.connect(self.ClinicianPageSelect)
        self.ui.AppointmentsButton_HomePage.clicked.connect(self.AppointmentPageSelect)
        self.ui.ExitButtonHomePage.clicked.connect(self.Exit)

        #Patients Page Buttons
        self.ui.PatientIDSearchButton.clicked.connect(self.PP.SearchByIDPatients)
        self.ui.PatientIDSpinBox.valueChanged.connect(self.PP.PatientSpinBoxSelected)
        self.ui.ExitButton_PatientsPage.clicked.connect(self.Exit)
        self.ui.AppointmentsButton_PatientsPage.clicked.connect(self.AppointmentPageSelect)
        self.ui.ClinicansButton_PatientsPage.clicked.connect(self.ClinicianPageSelect)
        self.ui.HomeButton_PatientsPage.clicked.connect(self.HomePageSelect)
        self.ui.PatientNameSearchButton.clicked.connect(self.PP.SearchByNamePatients)
        self.ui.PatientEditData_Button.clicked.connect(self.PP.EditPatientData)
        self.ui.DeletePatientButton.clicked.connect(self.PP.DeletePatientData)
        self.ui.PatientAddDataButton.clicked.connect(self.PP.AddNewPatient)
        self.ui.PatientDateOfBirthEdit.textChanged.connect(self.PP.ChangeDateTimeToLineEdit)
        self.ui.PatientDateOfBirthDateEdit.dateTimeChanged.connect(self.PP.LineEditToChangeDate)
        self.ui.PatientEditPhoto_Button.clicked.connect(self.PP.ChangePatientPhoto)
        self.ui.PatientComboBox.currentIndexChanged.connect(self.PP.ChangedPatientComboBox)

        #Clinician Page Buttons
        self.ui.ClinicianAppointmentButton.clicked.connect(self.AppointmentPageSelect)
        self.ui.ClinicianPatientsPageButton.clicked.connect(self.PatientsPageSelect)
        self.ui.ClinicianHomePageButton.clicked.connect(self.HomePageSelect)
        self.ui.ExitButtonClinicianPage.clicked.connect(self.Exit)
        self.ui.ClinicianIDSearchButton.clicked.connect(self.CP.SearchByIDClinician)
        self.ui.ClinicianIDSpinBox.valueChanged.connect(self.CP.ClinicianSpinBoxSelected)
        self.ui.ClinicianRoleSearchButton.clicked.connect(self.CP.SearchClinicianByRole)
        self.ui.ClinicianSearchByDepartmentButton.clicked.connect(self.CP.SearchClinicianByDepartment)
        self.ui.DeleteClinicianButton.clicked.connect(self.CP.DeleteClinicianData)
        self.ui.ClinicianDataEditButton.clicked.connect(self.CP.EditClinicianData)
        self.ui.AddNewClinicianButton.clicked.connect(self.CP.AddNewClinician)
        self.ui.ClinicianPhotoEditButton.clicked.connect(self.CP.ChangeClinicianPhoto)
        self.ui.ClinicianComboBox.currentIndexChanged.connect(self.CP.ChangedClinicianComboBox)

        #Appointmenet Page Buttons
        self.ui.HomePageAppointmentButton.clicked.connect(self.HomePageSelect)
        self.ui.PatientsPageAppointmentButton.clicked.connect(self.PatientsPageSelect)
        self.ui.CliniciansPageAppointmentButton.clicked.connect(self.ClinicianPageSelect)
        self.ui.ExitButtonAppointmentPage.clicked.connect(self.Exit)
        self.ui.SearchByAppointmentIDButton.clicked.connect(self.AP.SearchAppointmentsByID)
        self.ui.AppointmentIDSpinbox.valueChanged.connect(self.AP.AppointmentSpinBoxSelected)
        self.ui.AppointmentDateEdit.textChanged.connect(self.AP.ChangeDateTimeToLineEdit)
        self.ui.AppointmentDateEdit_2.dateTimeChanged.connect(self.AP.LineEditToChangeDate)
        self.ui.AppointmentSearchByDateButton.clicked.connect(self.AP.SearchByDate)
        self.ui.AppointmentAddButton.clicked.connect(self.AP.AddNewAppointment)
        self.ui.DeleteAppointmentButton.clicked.connect(self.AP.DeleteAppointment)
        self.ui.AppointmentSearchByPaidButton.clicked.connect(self.AP.SearchByPaid)
        self.ui.AppointmentComboBox.currentIndexChanged.connect(self.AP.ChangedAppointmentComboBox)
        self.ui.AppointmentDataEditButton.clicked.connect(self.AP.EditAppointment)
        self.ui.SalesDataButton.clicked.connect(self.SalesDataPageSelect)

        #Sales Data Page Buttons
        self.ui.ExitButton_SalesDataPage.clicked.connect(self.Exit)
        self.ui.SalesDataComboBox.currentIndexChanged.connect(self.SD.SalesUpdate)
        self.ui.AboutMeButton.clicked.connect(self.AboutMePopUpBox)
        self.ui.SalesDataHomePageButton.clicked.connect(self.HomePageSelect)
        self.ui.SalesDataPatientsPageButton.clicked.connect(self.PatientsPageSelect)
        self.ui.SalesDataAppointmentsPageButton.clicked.connect(self.AppointmentPageSelect)
        self.ui.SalesDataCliniciansPageButton.clicked.connect(self.ClinicianPageSelect)


    #The Function where im too lazy to just remove the little "s"'s from the GUI so i just clear the labels instead
    def thesuperlazyfunction(self):
        self.ui.SpaceTimeLabel.clear()
        self.ui.PaidLabel.clear()
        self.ui.NotPaidLabel.clear()
        self.ui.MostBookedClinicianLabel.clear()
        self.ui.NumberOfAppointmentLabel.clear()
        self.ui.MoneyMadeLabel.clear()

    #Shows the user interface
    def show(self):
        self.main_win.show()

    #Exits the program
    def Exit(self):
        ClinFirstName = self.ds.MatchingClinicianFirstName(self.ui.LoginPage_PinEnter.text())
        ClinLastName = self.ds.MatchingClinicianLastName(self.ui.LoginPage_PinEnter.text())
        if self.ui.LoginPage_PinEnter.text() == "":
            pass
        else:
            self.LogFile.write(f"\n{ClinFirstName} {ClinLastName}, Logged out of the app, at {self.currentdate}, Succsesfully")
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
    
    def OperationSuccessful(self):
        msg = QMessageBox()
        msg.setWindowTitle("Operation Complete!")
        msg.setText("Operation was completed!")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec()

    def MoreThanTwoOfThem(self):
        msg = QMessageBox()
        msg.setWindowTitle("Operation Closed!")
        msg.setText("Sorry Dude, theres two or more entries that match this searching condition, and Will is too lazy to code a pop up box where you select which one you'd want to see. so ig you'll just have to try another search method. whoops.")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec()

    def ClinicianLoginPinPopUpBox(self, Access):
        EnteredLoginPin = self.ui.LoginPage_PinEnter.text()
        text , ok = QInputDialog.getText(self.main_win,'Please Enter your Login Pin','Login Pin = ')
        if ok:
            self.LineEdit.setText(str(text))
            LoginPin = self.LineEdit.text()
            if LoginPin != EnteredLoginPin:
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
    
    def AboutMePopUpBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("About me!")
        msg.setText("Thank you for having a look at my IA2!, this code is pretty rough in parts but I tried my best. Please have a look at some other repo's I have on Github, such as my previous Assesments (IA1, FIA3, ...etc) Hopefully this stuff lands me a job somewhere.")
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
    def SalesDataPageSelect(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.SalesDataPage)
        msg = QMessageBox()
        msg.setText("This Sales Data is only updated every time the App is opened and closed. (Not Updated in real time)")
        msg.setWindowTitle("Warning!")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec()


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
            FirstName = self.ds.MatchingClinicianFirstName(LoginPin)
            LastName = self.ds.MatchingClinicianLastName(LoginPin)
            self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
            msg.setWindowTitle("Welcome")
            msg.setText(f"Welcome Back, {FirstName} {LastName}!")
            self.LogFile.write(f"\n{FirstName} {LastName}, has logged into the app at {self.currentdate}")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()