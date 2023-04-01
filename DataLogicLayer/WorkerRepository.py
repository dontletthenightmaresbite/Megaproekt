from DataLogicLayer.ConnectionGenerator import *
from DataLogicLayer.Options import *
from DataLogicLayer.Models.WorkerInputModel import *
from DataLogicLayer.Repository import*

class WorkerRepository(Repository):

    def insert_worker(self, worker):
        query = self.options.insert_worker + f" '{worker.name}', {worker.teamId}, '{worker.phoneNumber}', {worker.post}"
        self.do(query)

    def get_full_info_of_worker_by_id(self, id):
        query = self.options.get_full_info_of_worker_by_id + f" {id}"
        return self.get(query)

    def update_worker_team(self, workerId, teamId):
        query = self.options.update_worker_team + f" {workerId}, {teamId}"
        self.do(query)

    def delete_worker(self, id):
        query = self.options.delete_worker + f" {id}"
        self.do(query)

    def change_worker_team(self, workerId, teamId):
        query = self.options.change_worker_team + f" {workerId}, {teamId}"
        self.do(query)

    def delete_from_team(self, workerId):
        query = self.options.delete_from_team + f" {workerId}"
        self.do(query)
    
    def worker_password_and_id_by_phone_number(self, phoneNumber):
        query = self.options.worker_password_and_id_by_phone_number + f" '{phoneNumber}'"
        return self.get(query)
    
    def is_leader(self, id):
        query = self.options.is_leader + f" {id}"
        return self.get(query)
