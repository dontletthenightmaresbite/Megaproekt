from DataLogicLayer.ConnectionGenerator import *
from DataLogicLayer.Options import *
from DataLogicLayer.Models.imports import *
from DataLogicLayer.Models.Repository import*

class PostRepository(Repository):
    def insert_post(self, name, salary, timeOfWork):
        query = self.options.insert_post + f" '{name}', {salary}, {timeOfWork}"
        self.do(query)
