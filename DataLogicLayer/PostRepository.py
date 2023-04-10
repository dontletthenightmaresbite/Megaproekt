from DataLogicLayer.ConnectionGenerator import *
from DataLogicLayer.Options import *
from DataLogicLayer.Models.imports import *
from DataLogicLayer.Repository import*

class PostRepository(Repository):
    def insert_post(self, name, salary, timeOfWork):
        query = self.options.insert_post + f" '{name}', {salary}, {timeOfWork}"
        self.do(query)
    def DeletePost(self, Id):
        query = self.options.delete_post+ f"'{Id}'"
        self.do(query)

    def GetPostName(self,id):
        query = self.options.get_post_name + f"'{id}'"
        return self.get(query)

    def GetPostSalary(self,id):
        query = self.options.get_post_salary + f"'{id}'"
        return self.get(query)