from DataLogicLayer.ConnectionGenerator import *
from DataLogicLayer.Options import *
from DataLogicLayer.Models.imports import *

class Repository:
    def __init__(self):
        self.options = Options()
    
    def do(self, query):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
        except Error as err:
            print(err,f'\n{query}')
        connection.close()

    def get(self, query):
        cursor = get_connection().cursor()
        cursor.execute(query)
        return cursor.fetchall()


