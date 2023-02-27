from DataLogicLayer.ConnectionGenerator import *
from DataLogicLayer.Options import *
from DataLogicLayer.Models.imports import *
from DataLogicLayer.Repository import*

class TaskRepository(Repository):

    def insert_task(self, task):
        query = self.options.insert_task + f" '{task.description}', {task.workerId}, '{task.deadline}'"
        self.do(query)

    def get_team_tasks(self, id):
        query = self.options.get_team_tasks + f" {id}"
        return self.get(query)

    def tasks_by_worker_id(self, id):
        query = self.options.tasks_by_worker_id + f" {id}"
        return self.get(query)
    def update_task_worker(self, taskId, workerId):
        query = self.options.update_task_worker + f" {taskId}, {workerId}"
        self.do(query)
    def change_task_description(self, taskId, desc):
        query = self.options.change_task_description + f" {taskId}, '{desc}'"
        self.do(query)
    def change_task_deadline(self, taskId, deadline):
        query = self.options.change_task_deadline + f" {taskId}, '{deadline}'"
        self.do(query)