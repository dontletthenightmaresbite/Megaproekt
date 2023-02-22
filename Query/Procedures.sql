--#################################################################### PROCEDURES ####################################################################--

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
select W.[Id], W.[Name], W.[PhoneNumber], W.[Post] from [Worker] as W
where W.[TeamId] = @id
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
insert [Worker] values (@name, @teamId, @phoneNumber, @post, 0) 
go

create procedure InsertTeam
@name nvarchar(25),
@leaderId int
as
insert [Teams] values (@name, @leaderId)
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

create procedure InsertPost
@name nvarchar(120),
@salary int,
@timeOfWork int
as
insert [Posts] values (@name, @salary,  @timeOfWork )
go

create procedure InsertOpportunityInListOfOpportunities
@description nvarchar(120)
as
insert [ListOfOpportunities]  values (@description)
go

create procedure InsertOpportunity
@postId int,
@opportunities int
as
insert [Opportunities] values (@postId, @opportunities)
go

