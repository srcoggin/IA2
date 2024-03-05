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
    
    def MatchingClinicianName(self, loginpin):
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
                Pin += "{}".format(i)
        return Pin
    
