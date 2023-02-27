from DataLogicLayer.ConnectionGenerator import *
from DataLogicLayer.Options import *
from DataLogicLayer.Models.imports import *
from DataLogicLayer.Repository import*

class TeamRepository(Repository):

    def insert_team(self, team):
        query = self.options.insert_team + f" '{team.name}', {team.leaderId}"
        self.do(query)
    def change_team_leader(self, teamId, leaderId):
        query = self.options.change_team_leader + f" {teamId}, {leaderId}"
        self.do(query)