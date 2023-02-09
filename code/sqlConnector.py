import mysql.connector
from mysql.connector import Error
import pyodbc


class DataBase:
    def Connect(self):
        connection_string='DRIVER={SQL Server};SERVER=.;DATABASE=App1'
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")
        self.connection = connection

    def Get(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
        return result

    def Do(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")