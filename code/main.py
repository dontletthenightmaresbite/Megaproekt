import mysql.connector
from mysql.connector import Error
import pyodbc
from sqlConnector import *
db = DataBase()
print(1)
db.Connect()
print(2)
z=db.Get("select * from Worker")

for i in z:
    print(i)
