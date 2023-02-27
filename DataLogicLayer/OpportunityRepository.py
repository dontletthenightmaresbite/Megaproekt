from DataLogicLayer.ConnectionGenerator import *
from DataLogicLayer.Options import *
from DataLogicLayer.Models.imports import *
from DataLogicLayer.Models.Repository import*

class OpportunityRepository(Repository):
    def insert_opportunity(self, postId, opportunity):
        query = self.options.insert_opportunity + f" {postId}, {opportunity}"
        self.do(query)

    def insert_opportunity_in_list_of_opportunities(self, description):
        query = self.options.insert_opportunity_in_list_of_opportunities + f" {description}"
        self.do(query)

    def get_worker_opportunities(self, id):
        query = self.options.get_worker_opportunities + f" {id}"
        return self.get(query)