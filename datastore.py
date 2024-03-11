import os
import sqlite3


class DataStore:
    def __init__(self):
        self.db_file = os.path.join(os.getcwd(), "IA2.db")
        self.db = sqlite3.connect(self.db_file)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    #Patient Functions
    def SearchAllPatientID(self):
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
    
    def UpdateDetails(self, FirstName, LastName, Address, PatientID, Weight, Height):
        self.cursor.execute(
            """
                REPLACE INTO Patients (ID, FirstName, Lastname, Address, Weight, Height)
                VALUES (:ID, :FirstName, :LastName, :Address, :Weight, :Height)
            """,
            {"ID": PatientID, "FirstName": FirstName, "LastName": LastName, "Address": Address, "Weight": Weight, "Height": Height}
        )
        self.db.commit()
    
    def DeletePatient(self, PatientID):
        self.cursor.execute(
            """
                DELETE FROM Patients
                WHERE ID LIKE :PatientID
            """,
            {"PatientID": PatientID}
        )
        self.db.commit()

    def NewPatientDS(self, FirstName, LastName, PatientID, Weight, Height, Address):
        self.cursor.execute(
            """
                INSERT INTO Patients (ID, FirstName, Lastname, Weight, Height, Address)
                VALUES (:PatientID, :FirstName, :LastName, :Weight, :Height, :Address)
            """,
            {"PatientID": PatientID, "FirstName": FirstName, "LastName": LastName, "Weight": Weight, "Height": Height, "Address": Address}
        )
        self.db.commit()
    

    
    
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

    def UpdateClinicianDetails(self, FirstName, LastName, Department, ClinicianID, Role, LoginPin, Services):
        self.cursor.execute(
            """
                REPLACE INTO Clinicians (ID, FirstName, Lastname, Department, Role, LoginPin, ServicesProvided)
                VALUES (:ID, :FirstName, :LastName, :Department, :Role, :LoginPin, :Services)
            """,
            {"ID": ClinicianID, "FirstName": FirstName, "LastName": LastName, "Department": Department, "Role": Role, "LoginPin": LoginPin, "Services": Services}
        )
        self.db.commit()