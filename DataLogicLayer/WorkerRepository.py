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

    def Get_Worker_Post(self, id):
        query = self.options.get_worker_post + f" {id}"
        return self.get(query)

    def Get_Worker_Salary(self, id):
        query = self.options.get_worker_salary + f" {id}"
        return self.get(query)
    
    def Get_Worked_Time(self, id):
        query = self.options.get_worked_time + f" {id}"
        return self.get(query)
    
    def Update_Worked_Time(self,id,time):
        query = self.options.update_worker_time + f" {id},'{time}'"
        self.do(query)

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

    def team_name_and_members_by_worker_id(self, id):
        query = self.options.team_name_and_members_by_worker_id + f" {id}"
        return self.get(query)
    
    def update_worker_password(self, phoneNumber, password):
        query = self.options.update_worker_password + f" '{phoneNumber}', '{password}'"
        self.do(query)
