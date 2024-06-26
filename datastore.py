import os
import sqlite3
from collections import Counter


class DataStore:
    def __init__(self):
        self.db_file = os.path.join(os.getcwd(), "IA2.db")
        self.db = sqlite3.connect(self.db_file)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    #Patient Functions
    def SearchAllPatientID(self):
        """
        This function selects all patient IDs from the Patients table.

        Args:
            ID: The Patient ID

        Returns:
            A Dictionary with all IDs from the Patients in the DataBase.
        """
        self.cursor.execute(
         """
                SELECT ID FROM Patients
            """
        )
        List = self.cursor.fetchall()
        id = ""
        for i in List:
            id += "{}".format(i)
        return id
    
    def SearchAllDOBS(self):
        self.cursor.execute(
        
         """
                SELECT ID FROM Patients
            """
        )
        List = self.cursor.fetchall()
        id = ""
        for i in List:
            id += "{}".format(i)
        return id

    def SelectMatchingPatient(self, patientid):
        self.cursor.execute(
            """
                SELECT * FROM Patients
                WHERE ID LIKE :patientid
            """,
            {'patientid': patientid}
        )
        List = self.cursor.fetchall()
        return List
    
    def SelectMatchingPatientDateOfBirth(self, dob):
        """
        This function selects all patients from the Patients table where the DateOfBirth field matches the provided 'dob' argument.

        Args:
            dob: A string representing the date of birth in a format compatible with the database's DateOfBirth field.

        Returns:
            A list of dictionaries. Each dictionary represents a patient record with all their information, where the 'dob' argument matches the 
            DateOfBirth DataBase Field.
        """
        self.cursor.execute(
            """
                SELECT * FROM Patients
                WHERE DateOfBirth LIKE :dob
            """,
            {'dob': dob}
        )
        List = self.cursor.fetchall()
        return List
    
    def SelectMatchingPatientName(self, firstname, lastname):
        """
            This function selects all patients from the Patients table where the FirstName field matches the provided 'firstname' argument 
            and the LastName field matches the provided 'lastname' argument.

            Args:
                firstname: A string representing the patient's first name.
                lastname: A string representing the patient's last name.

            Returns:
                A dictionary that contains the matching patients information.
        """
        self.cursor.execute(
            """
                SELECT * FROM Patients
                WHERE FirstName LIKE :firstname AND LastName LIKE :lastname
            """,
            {'firstname': firstname, 'lastname': lastname}
        )
        List = self.cursor.fetchall()
        return List


    
    def MatchingPatientLastName(self):
        self.cursor.execute(
            """
                SELECT LastName FROM Patients
            """,
        )
        List = self.cursor.fetchall()
        id = ""
        for i in List:
                id += "{}".format(i)
        return id

    def MatchingPatientFirstName(self):
        self.cursor.execute(
            """
                SELECT FirstName FROM Patients
            """,
        )
        List = self.cursor.fetchall()
        id = ""
        for i in List:
                id += "{}".format(i)
        return id
    
    def SearchForPatientByDateOfBirth(self, DOB):
        self.cursor.execute(
            """
                SELECT * FROM Patients
                WHERE DateOfBirth LIKE :DOB
            """,
            {"DOB": DOB}
        )
        List = self.cursor.fetchall()
        Date = ""
        for i in List:
                Date += "{}".format(i)
        return Date
    
    def EditPhotoPatient(self, filepath, patientID):
        self.cursor.execute(
            """
                UPDATE Patients SET Photo = :Photo WHERE ID LIKE :patientID
            """,
            {"Photo": filepath, "patientID": patientID}
        )
        self.db.commit()

    def EditPhotoClinician(self, filepath, clinicianID):
        self.cursor.execute(
            """
                UPDATE Clinicians SET Photo = :Photo WHERE ID LIKE :clinicianID
            """,
            {"Photo": filepath, "clinicianID": clinicianID}
        )
        self.db.commit()

    def UpdateDetails(self, FirstName, LastName, Address, PatientID, Weight, Height, DateOfBirth, Photo):
        self.cursor.execute(
            """
                REPLACE INTO Patients (ID, FirstName, Lastname, Address, Weight, Height, DateOfBirth, Photo)
                VALUES (:ID, :FirstName, :LastName, :Address, :Weight, :Height, :DateOfBirth, :Photo)
            """,
            {"ID": PatientID, "FirstName": FirstName, "LastName": LastName, "Address": Address, "Weight": Weight, "Height": Height, "DateOfBirth": DateOfBirth, "Photo": Photo}
        )
        self.db.commit()
    
    def DeletePatient(self, PatientID):
        """
        This function deletes a patient from the Patients table based on their ID.

        Args:
            PatientID: An integer representing the unique ID of the patient to be deleted.
        """
        self.cursor.execute(
            """
                DELETE FROM Patients
                WHERE ID LIKE :PatientID
            """,
            {"PatientID": PatientID}
        )
        self.db.commit()

    def NewPatientDS(self, FirstName, LastName, PatientID, Weight, Height, Address, DateOfBirth):
        """
        This function adds a new patient record to the Patients table.

        Args:
                FirstName: A string representing the patient's first name.
                LastName: A string representing the patient's last name.
                PatientID: An integer representing the unique ID for the new patient.
                Weight: A number representing the patient's weight (kg).
                Height: A number representing the patient's height (cm).
                Address: A string representing the patient's address.
                DateOfBirth: A string representing the patient's date of birth in a format compatible with the database's DateOfBirth field.
        """
        self.cursor.execute(
            """
                INSERT INTO Patients (ID, FirstName, Lastname, Weight, Height, Address, DateOfBirth)
                VALUES (:PatientID, :FirstName, :LastName, :Weight, :Height, :Address, :DateOfBirth)
            """,
            {"PatientID": PatientID, "FirstName": FirstName, "LastName": LastName, 
             "Weight": Weight, "Height": Height, "Address": Address, "DateOfBirth": DateOfBirth}
        )
        self.db.commit()
    
    def PullingPhotoBecauseMyShittyCodeKeepsBuggingButForPatientsThisTime(self,ID):
        self.cursor.execute(
            '''
                SELECT Photo FROM Patients
                WHERE ID = :ID
            ''',
            {"ID": ID}
        )
        List = self.cursor.fetchall()
        Photo = ""
        for i in List:
                Photo += "{}".format(i[0])
        return Photo
    
    
    #Login Page Functions
    def AllLoginPins(self):
        self.cursor.execute(
            """
                SELECT LoginPin FROM Clinicians
            """,
        )
        List = self.cursor.fetchall()
        Pins = ""
        for i in List:
                Pins += "{}".format(i)
        return Pins
    
    def MatchingClinicianFirstName(self, loginpin):
        self.cursor.execute(
            """
                SELECT FirstName FROM Clinicians
                WHERE LoginPin LIKE :loginpin
            """,
            {'loginpin': loginpin}
        )
        List = self.cursor.fetchall()
        Pin = ""
        for i in List:
                Pin += "{}".format(i[0])
        return Pin
    
    def MatchingClinicianLastName(self, loginpin):
        self.cursor.execute(
            """
                SELECT LastName FROM Clinicians
                WHERE LoginPin LIKE :loginpin
            """,
            {'loginpin': loginpin}
        )
        List = self.cursor.fetchall()
        Pin = ""
        for i in List:
                Pin += "{}".format(i[0])
        return Pin
    
    #Clinician Functions
    def SearchAllClinicianID(self):
        self.cursor.execute(
         """
                SELECT ID FROM Clinicians
            """
        )
        List = self.cursor.fetchall()
        id = ""
        for i in List:
            id += "{}".format(i)
        return id
    
    def SelectMatchingClinician(self, clinicianid):
        self.cursor.execute(
            """
                SELECT * FROM Clinicians
                WHERE ID LIKE :clinicianid
            """,
            {'clinicianid': clinicianid}
        )
        List = self.cursor.fetchall()
        return List
    
    def MatchingClinicianRole(self, MatchingRole):
        self.cursor.execute(
            """
                SELECT * FROM Clinicians
                WHERE Role LIKE :MatchingRole
            """,
            {"MatchingRole": MatchingRole}
        )
        List = self.cursor.fetchall()
        return List
    
    def SearchAllRoles(self):
        self.cursor.execute(
            """
                SELECT Role FROM Clinicians
            """
        )
        list = self.cursor.fetchall()
        Role = ""
        for i in list:
            Role += "{}".format(i)
        return Role
    
    def SearchAllDepartments(self):
        self.cursor.execute(
            """
                SELECT Department FROM Clinicians
            """
        )
        list = self.cursor.fetchall()
        Dep = ""
        for i in list:
            Dep += "{}".format(i)
        return Dep
    
    def MatchingClinicianDepartment(self, MatchingDepartment):
        self.cursor.execute(
            """
                SELECT * FROM Clinicians
                WHERE Department LIKE :MatchingDepartment
            """,
            {"MatchingDepartment": MatchingDepartment}
        )
        List = self.cursor.fetchall()
        return List
    
    def DeleteClinician(self, ClinicianID):
        self.cursor.execute(
            """
                DELETE FROM Clinicians
                WHERE ID LIKE :ClinicianID
            """,
            {"ClinicianID": ClinicianID}
        )
        self.db.commit()

    def UpdateClinicianDetails(self, FirstName, LastName, Department, ClinicianID, Role, LoginPin, Services, Cost, Photo):
        self.cursor.execute(
            """
                REPLACE INTO Clinicians (ID, FirstName, Lastname, Department, Role, LoginPin, ServicesProvided, Cost, Photo)
                VALUES (:ID, :FirstName, :LastName, :Department, :Role, :LoginPin, :Services, :Cost, :Photo)
            """,
            {"ID": ClinicianID, "FirstName": FirstName, "LastName": LastName, "Department": Department, "Role": Role, "LoginPin": LoginPin, "Services": Services, "Cost": Cost, "Photo": Photo}
        )
        self.db.commit()


    def NewClinicianDS(self, FirstName, LastName, Department, ClinicianID, Role, LoginPin, Services, Cost):
        self.cursor.execute(
            """
                INSERT INTO Clinicians (ID, FirstName, Lastname, Department, Role, LoginPin, ServicesProvided, Cost)
                VALUES (:ID, :FirstName, :LastName, :Department, :Role, :LoginPin, :Services, :Cost)
            """,
            {"ID": ClinicianID, "FirstName": FirstName, "LastName": LastName, "Department": Department, "Role": Role, "LoginPin": LoginPin, "Services": Services, "Cost": Cost}
        )
        self.db.commit()

    def PullingPhotoBecauseMyShittyCodeKeepsBugging(self,ID):
        self.cursor.execute(
            '''
                SELECT Photo FROM Clinicians
                WHERE ID = :ID
            ''',
            {"ID": ID}
        )
        List = self.cursor.fetchall()
        Photo = ""
        for i in List:
                Photo += "{}".format(i[0])
        return Photo

    #Appointment Functions
    def SearchAllAppointmentID(self):
            self.cursor.execute(
            """
                    SELECT ID FROM Appointments
                """
            )
            List = self.cursor.fetchall()
            id = ""
            for i in List:
                id += "{}".format(i)
            return id
    
    def SearchAllAppointmentDates(self):
            self.cursor.execute(
            """
                    SELECT Date FROM Appointments
                """
            )
            List = self.cursor.fetchall()
            date = ""
            for i in List:
                date += "{}".format(i)
            return date
    
    def SearchAllAppointmentPaid(self):
            self.cursor.execute(
            """
                    SELECT Paid FROM Appointments
                """
            )
            List = self.cursor.fetchall()
            paid = ""
            for i in List:
                paid += "{}".format(i)
            return paid

    def SelectMatchingAppointment(self, appointmentid):
            self.cursor.execute(
                """
                    SELECT * FROM Appointments
                    WHERE ID LIKE :appointmentid
                """,
                {'appointmentid': appointmentid}
            )
            List = self.cursor.fetchall()
            return List
    
    def SelectMatchingAppointmentDate(self, appointmentdate):
            self.cursor.execute(
                """
                    SELECT * FROM Appointments
                    WHERE Date LIKE :appointmentdate
                """,
                {'appointmentdate': appointmentdate}
            )
            List = self.cursor.fetchall()
            return List

    def SelectMatchingAppointmentPaid(self, appointmentpaid):
            self.cursor.execute(
                """
                    SELECT * FROM Appointments
                    WHERE Paid LIKE :appointmentpaid
                """,
                {'appointmentpaid': appointmentpaid}
            )
            List = self.cursor.fetchall()
            return List
    
    def NewAppointmentDS(self, AppointmentID, Date, Length, Result, ClinicianID, ServiceUsed, PatientID, Paid, Year):
        self.cursor.execute(
            """
                INSERT INTO Appointments (ID, Date, Length, Result, CliniciansID, ServiceUsed, PatientID, Paid, Year)
                VALUES (:ID, :Date, :Length, :Result, :ClinicianID, :ServiceUsed, :PatientID, :Paid, :Year)
            """,
            {"ID": AppointmentID, "Date": Date, "Length": Length, "Result": Result, "ClinicianID": ClinicianID, "ServiceUsed": ServiceUsed, "PatientID": PatientID, "Paid": Paid, "Year": Year}
        )
        self.db.commit()

    def DeleteAppointment(self, AppointmentID):
        self.cursor.execute(
            """
                DELETE FROM Appointments
                WHERE ID LIKE :AppointmentID
            """,
            {"AppointmentID": AppointmentID}
        )
        self.db.commit()

    def AppointmentSearchByComboBox(self, AppointmentID):
        self.cursor.execute(
            """
                SELECT * FROM Appointments
                WHERE ID LIKE :AppointmentID
            """,
            {"AppointmentID": AppointmentID}
        )
        List = self.cursor.fetchall()
        return List
    
    def countingmoney(self, clinid):
        self.cursor.execute(
            """
                SELECT Cost FROM Clinicians
                WHERE ID LIKE :clinid
            """,
            {"clinid": clinid}
        )
        List = self.cursor.fetchall()
        return List
    
    def PatientSearchByComboBox(self, PatientID):
        self.cursor.execute(
            """
                SELECT * FROM Patients
                WHERE ID LIKE :PatientID
            """,
            {"PatientID": PatientID}
        )
        List = self.cursor.fetchall()
        return List

    #Combobox functions
    def AppointmentDisplayComboBox(self):
        self.cursor.execute(
            """
                    SELECT ID FROM Appointments
                """
            )
        List = self.cursor.fetchall()
        Display = []
        for i in List:
            Display += [f"ID: {i[0]} Appointment"]
        return Display
    
    def PatientDisplayComboBox(self):
        self.cursor.execute(
            """
                    SELECT ID FROM Patients
                """
            )
        List = self.cursor.fetchall()
        Display = []
        for i in List:
            Display += [f"ID: {i[0]} Patient"]
        return Display
    
    def ClinicianDisplayComboBox(self):
        self.cursor.execute(
            """
                    SELECT ID FROM Clinicians
                """
            )
        List = self.cursor.fetchall()
        Display = []
        for i in List:
            Display += [f"ID: {i[0]} Clinician"]
        return Display
    
    def SalesDisplayComboBox(self):
        self.cursor.execute(
            """
                    SELECT Year FROM Appointments
                """
            )
        List = self.cursor.fetchall()
        Display = []
        for i in List:
            Display += [f"{i}"]
        counters = Counter(Display)
        return counters
    
    def ClinicianSearchByComboBox(self, ClinicianID):
        self.cursor.execute(
            """
                SELECT * FROM Clinicians
                WHERE ID LIKE :ClinicianID
            """,
            {"ClinicianID": ClinicianID}
        )
        List = self.cursor.fetchall()
        return List
    
    def SalesDataSearchByComboBox(self, date):
        self.cursor.execute(
            """
                SELECT *
                FROM Appointments
                WHERE Year = :date
            """,
            {"date": date}
        )
        row = self.cursor.fetchall()
        return row  
    
    #Random update appointment function
    def UpdateAppointmentDetails(self, AppointmentID, Date, Length, Result, Paid, PatientID, CliniciansID, ServiceUsed, Year):
        self.cursor.execute(
            """
                REPLACE INTO Appointments (ID, Date, Length, Result, Paid, PatientID, CliniciansID, ServiceUsed, Year)
                VALUES (:AppointmentID, :Date, :Length, :Result, :Paid, :PatientID, :CliniciansID, :ServiceUsed, :Year)
            """,
            {"AppointmentID": AppointmentID, "Date": Date, "Length": Length, "Result": Result, "Paid": Paid, "PatientID": PatientID, "CliniciansID": CliniciansID, "ServiceUsed": ServiceUsed, "Year": Year}
        )
        self.db.commit()