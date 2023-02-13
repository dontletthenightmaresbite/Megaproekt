from sqlConnector import *
db = DataBase()
print(1)
db.Connect()
print(2)
z=db.Do("exec GetTeamTasks 1")

for i in z:
    print(i)
