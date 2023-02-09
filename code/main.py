from sqlConnector import *
db = DataBase()
print(1)
db.Connect()
print(2)
z=db.Get("select * from Worker")
a=db.Get("select * from Worker")
z=db.Get("select * from Worker")

for i in z:
    print(i)

for i in a:
    print(i)
