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

    def insert_worker(self, worker):
        query = self.options.insert_worker + f" '{worker.name}', {worker.teamId}, \
                                                '{worker.phoneNumber}', {worker.post}"
        self.do(query)

    def insert_team(self, team):
        query = self.options.insert_team + f" '{team.name}', {team.leaderId}"
        self.do(query)
    
    def update_worker_team(self, workerId, teamId):
        query = self.options.update_worker_team + f" {workerId}, {teamId}"
        self.do(query)

    def insert_task(self, task):
        query = self.options.insert_task + f" '{task.description}', {task.workerId}, '{task.deadline}'"
        self.do(query)

    def update_task_worker(self, taskId, workerId):
        query = self.options.update_task_worker + f" {taskId}, {workerId}"
        self.do(query)

    def delete_worker(self, id):
        query = self.options.delete_worker + f" {id}"
        self.do(query)
