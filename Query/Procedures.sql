--#################################################################### PROCEDURES ####################################################################--
use UwU

create procedure GetTeamTasks
@id int
as
select Teams.Id, Teams.[Name], Tasks.[Description] from Teams
join Tasks on Tasks.TeamId=Teams.Id
where Teams.Id=@Id
order by TeamId
go

create procedure GetWorkerOpportunities
@id int
as
select W.Id, O.Opportunities, L.Desription from Worker as W
join [Opportunities] as O on W.post = O.PostId
join [ListOfOpportunities] as L on L.Id = O.Opportunities
where W.Id=@id
go

create procedure GetFullInfoOfWorkerById
@id int
as
select * from [Worker] as W
where W.[Id] = @id
go

create procedure TasksByWorkerId
@id int
as
select T.[Id], T.[Description] from [Tasks] as T
where T.[WorkerId] = @id
go

create procedure InsertWorker
@name nvarchar(50),
@teamId int NULL,
@phoneNumber nvarchar(50),
@post int
as
insert [Worker] values (@name, @teamId, @phoneNumber, @post, 0, @phoneNumber) 
go

create procedure InsertTeam
@name nvarchar(25)
as
insert [Teams] values (@name, null)
go

create procedure UpdateWorkerTeam
@workerId int,
@teamId int
as
update [Worker] 
set TeamId = @teamId
where Id = @workerId
go

create procedure InsertTask
@description nvarchar(120),
@workerId int,
@deadline date
as
declare @teamId int
set @teamId = (select [TeamId] from [Worker] where id=@workerId)
insert [Tasks] values (@description, @teamId, @workerId, @deadline)
go

create procedure UpdateTaskWorker
@taskId int,
@workerId int
as
update [Tasks]
set TeamId = (select [TeamId] from [Worker] where id=@workerId), WorkerId = @workerId
where Id = @taskId
go

create procedure DeleteWorker
@id int
as
update Worker
set IsDeleted = 1
where id = @id
update Tasks
set WorkerId = null, TeamId = null
where WorkerId = @id
go

create procedure DeletePost
@id int
as
update Posts
set IsDeleted = 1
where Id = @id
update Worker
set Post = null
where Post = @id
go

create procedure InsertOpportunityInListOfOpportunities
@description nvarchar(120)
as
insert [ListOfOpportunities]  values (@description)
go

create procedure InsertOpportunity
@postId int,
@opportunity int
as
insert [Opportunities] values (@postId, @opportunity)
go

create procedure ChangeTeamLeader
@teamId int,
@workerId int
as
update [Teams]
set LeaderId = null
where LeaderId = @workerId
update [Worker]
set TeamId = @teamId
where id = @workerId
update [Teams]
set LeaderId = @workerId
where id = @teamId
go

create procedure ChangeWorkerTeam
@workerId int,
@teamId int
as
update [Teams]
set LeaderId = null
where LeaderId = @workerId and not (Id = @teamId)
update [Worker]
set TeamId = @teamId
where Id = @workerId
go

create procedure DeleteFromTeam
@id int
as
update [Teams]
set LeaderId = null
where LeaderId = @id
update [Worker]
set TeamId = null
where id = @id
go

create procedure ChangeTaskDescription
@taskId int,
@desc nvarchar(120)
as
update [Tasks]
set Description = @desc
where Id = @taskId
go

create procedure ChangeTaskDeadline
@taskId int,
@deadline date
as
update [Tasks]
set Deadline = @deadline
where Id = @taskId
go

create procedure InsertPost
@name nvarchar(50),
@salary int,
@timeOfWork int
as
insert [Posts] values (@name, @salary, @timeOfWork)
go

create procedure WorkerPasswordAndIdByPhoneNumber
@phoneNumber nvarchar(50)
as
select Id, Password from Worker
where PhoneNumber = @phoneNumber
go

create procedure UpdateWorkerPassword
@phoneNumber nvarchar(50),
@password nvarchar(15)
as
update Worker
set Password=@password
where PhoneNumber=@phoneNumber
go

create procedure IsLeader
@id int
as
select * from Teams where LeaderId=@id
go
