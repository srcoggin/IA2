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
                WHERE Id LIKE :patientid
            """,
            {'patientid': patientid}
        )
        List = self.cursor.fetchall()
        return List