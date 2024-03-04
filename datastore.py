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