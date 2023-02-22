class Options:
    def __init__(self):
        self.get_team_tasks = 'exec GetTeamTasks'
        self.get_worker_opportunities = 'exec GetWorkerOpportunities'
        self.get_full_info_of_worker_by_id = 'exec GetFullInfoOfWorkerById'
        self.tasks_by_worker_id = 'exec TasksByWorkerId'
        self.insert_worker = 'exec InsertWorker'
        self.insert_team = 'exec InsertTeam'
        self.update_worker_team = 'exec UpdateWorkerTeam'
        self.insert_task = 'exec InsertTask'
        self.update_task_worker = 'exec UpdateTaskWorker'
        self.delete_worker = 'exec DeleteWorker'
        self.insert_post = 'exec InsertPost'
        self.insert_opportunity = 'exec InsertOpportunity'
        self.insert_opportunity_in_list_of_opportunities = 'exec InsertOpportunityInListOfOpportunities'
        