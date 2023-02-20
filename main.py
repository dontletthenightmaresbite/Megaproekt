from DataLogicLayer.Repository import *
print(1)

db = Repository()

db.insert_worker(worker("awa", 1, "89997355568", 1))

a = db.get("select * from Worker")

for i in a:
    print(i)