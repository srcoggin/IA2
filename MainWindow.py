from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UserInterface import Ui_Form
from datastore import DataStore
from PyQt5 import QtGui





class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ds = DataStore()
        self.ui = Ui_Form()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

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


