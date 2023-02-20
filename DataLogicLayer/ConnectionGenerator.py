import mysql.connector
from mysql.connector import Error
import pyodbc

def get_connection():
    try:
        connectionString = 'DRIVER={SQL Server};SERVER=.;DATABASE=UwU'
        return pyodbc.connect(connectionString)
    except Error as err:
        print(err)

'''
class DataBase:
    def Connect(self):
        connection_string='DRIVER={SQL Server};SERVER=.;DATABASE=UwU'
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")
        self.connection = connection

    def Get(self, query : str):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as err:
            print("Query:", query)
            print(f"Error: '{err}'")
        return result

    def Do(self, query : str):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
        except Error as err:
            print("Query:", query)
            print(f"Error: '{err}'")

    def GetFullInfoOfWorkerById(self,TeamId):
        cursor = self.connection.cursor()
        query = 'exec GetFullInfoOfWorkerById' + ' ' + str(TeamId)
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as err:
            print("Query:", query)
            print(f"Error: '{err}'")
        return result
'''