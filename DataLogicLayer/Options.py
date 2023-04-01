class Options:
    def __init__(self):
        #Insert
        self.insert_worker = 'exec InsertWorker'
        self.insert_team = 'exec InsertTeam'
        self.insert_task = 'exec InsertTask'
        self.insert_post = 'exec InsertPost'
        self.insert_opportunity_in_list_of_opportunities = 'exec InsertOpportunityInListOfOpportunities'
        self.insert_opportunity = 'exec InsertOpportunity'
        #Get
        self.get_team_tasks = 'exec GetTeamTasks'
        self.get_worker_opportunities = 'exec GetWorkerOpportunities'
        self.get_full_info_of_worker_by_id = 'exec GetFullInfoOfWorkerById'
        self.tasks_by_worker_id = 'exec TasksByWorkerId'
        self.worker_password_and_id_by_phone_number = 'exec WorkerPasswordAndIdByPhoneNumber'
        self.is_leader = 'exec IsLeader'
        #ChangeAbob
        self.delete_post = 'exec DeletePost'
        self.update_worker_team = 'exec UpdateWorkerTeam'
        self.update_task_worker = 'exec UpdateTaskWorker'
        self.delete_worker = 'exec DeleteWorker'
        self.change_team_leader = 'exec ChangeTeamLeader'
        self.change_worker_team = 'exec ChangeWorkerTeam'
        self.delete_from_team = 'exec DeleteFromTeam'
        self.change_task_description = 'exec ChangeTaskDescription'
        self.change_task_deadline = 'exec ChangeTaskDeadline'
        self.update_worker_password = 'exec UpdateWorkerPassword'
