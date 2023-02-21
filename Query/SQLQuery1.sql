--#################################################################### PLAYGROUND ####################################################################--
use UwU


--#################################################################### INSERT ####################################################################--

insert Teams values ('Programmers', Null)

Insert Posts values ('Programmer',123,200),
('Director', 1, 1),
('TeamLid', 24554542, 1235642),
('Backender', 65464342, 15782),
('Designer', 25633342, 12334512),
('Accauntant', 42563342, 12312)

insert Worker values 
('Oleg', '2','98745312',1,null),
('Purga', '2', '233254424', 1, null),
('Curt', '2', '233255644', 1, null),
('Tabis', '2', '56755644', 1, null),
('Chitus', '2', '989975644', 1, null),
('Opiumman', '2', '43349975644', 1, null),
('Sundus', '2', '1234975644', 1, null),
('Sarancha', '2', '456675644', 1, null),
('Chicha', '2', '456975644', 1, null),
('Rudolf', '2', '3456975644', 1, null)

insert Tasks values
('Visit the job', 1, 13, '2023-02-14'),
('Make some amazing staff', 1, 14, '2023-02-17'),
('Do nothing', 1, 15, '2023-02-11'),
('Print Hello World', 1, 16, '2023-02-19'),
('Call for asking some help', 1, 17, '2023-02-17'),
('Create the app', 1, 18, '2023-02-22')

--#################################################################### DELETE ####################################################################--

delete [ListOfOpportunities]
delete [Opportunities]
delete [Posts]
delete [Tasks]
delete [Teams]
delete [Worker]

--#################################################################### PROCEDURE ####################################################################--
create procedure GetTeamTasks
@id int
as
select Teams.Id, Teams.[Name], Tasks.[Description] from Teams
join Tasks on Tasks.TeamId=Teams.Id
where Teams.Id=@Id
order by TeamId

create procedure GetWorkerOpportunities
@id int
as
select W.Id, O.Opportunities, L.Desription from Worker as W
join [Opportunities] as O on W.post = O.PostId
join [ListOfOpportunities] as L on L.Id = O.Opportunities
where W.Id=@id

create procedure GetFullInfoOfWorkerById
@id int
as
select W.[Id], W.[Name], W.[PhoneNumber], W.[Post] from [Worker] as W
where W.[TeamId] = @id

create procedure TasksByWorkerId
@id int
as
select T.[Id], T.[Description] from [Tasks] as T
where T.[WorkerId] = @id

create procedure InsertWorker
@name nvarchar(50),
@teamId int NULL,
@phoneNumber nvarchar(50),
@post int
as
insert [Worker] values (@name, @teamId, @phoneNumber, @post, 0) 

create procedure InsertTeam
@name nvarchar(25),
@leaderId int
as
insert [Teams] values (@name, @leaderId)

create procedure UpdateWorkerTeam
@workerId int,
@teamId int
as
update [Worker] 
set TeamId = @teamId
where Id = @workerId

create procedure InsertTask
@description nvarchar(120),
@workerId int,
@deadline date
as
declare @teamId int
set @teamId = (select [TeamId] from [Worker] where id=@workerId)
insert [Tasks] values (@description, @teamId, @workerId, @deadline)

create procedure UpdateTaskWorker
@taskId int,
@workerId int
as
update [Tasks]
set TeamId = (select [TeamId] from [Worker] where id=@workerId), WorkerId = @workerId
where Id = @taskId

create procedure DeleteWorker
@id int
as
update Worker
set IsDeleted = 1
where id = @id
update Tasks
set WorkerId = null, TeamId = null
where WorkerId = @id

create procedure InsertPost
@name nvarchar(120),
@salary int,
@timeOfWork int
as
insert [Posts] values (@name, @salary,  @timeOfwork )

create procedure InsertOpportunityInListOfOpportunities
@description nvarchar(120)
as
insert [ListOfOpportunities]  values (description)

create procedure InsertOpportunity
@postId int,
@opportunities int
as
insert [Opportunities] values (@postId, @opportunities)
--#################################################################### DATABASE CREATE ####################################################################--

create database UwU
go
use UwU
go


CREATE TABLE [Worker] (
	Id int NOT NULL primary key identity,
	Name nvarchar(50),
	TeamId int NULL,
	PhoneNumber nvarchar(50),
	Post int NOT NULL,
	IsDeleted bit

)
GO
CREATE TABLE [Posts] (
	Id int NOT NULL primary key identity,
	Name nvarchar(50),
	Salary int,
	TimeOfWork int

)
GO
CREATE TABLE [Opportunities] (
	PostId int,
	Opportunities int
)
GO
CREATE TABLE [ListOfOpportunities] (
	Id int NOT NULL primary key identity,
	Desription nvarchar(25)

)
GO
CREATE TABLE [Teams] (
	Id int NOT NULL primary key identity,
	[Name] nvarchar(25),
	LeaderId int NULL

)
GO
CREATE TABLE [Tasks] (
	Id int NOT NULL primary key identity,
	[Description] nvarchar(120),
	TeamId int NULL,
	WorkerId int NULL,
	Deadline date NOT NULL


)
GO

ALTER TABLE [Worker] WITH CHECK ADD CONSTRAINT [Worker_fk0] FOREIGN KEY ([TeamId]) REFERENCES [Teams]([Id])
ON UPDATE CASCADE
GO
ALTER TABLE [Worker] CHECK CONSTRAINT [Worker_fk0]
GO
ALTER TABLE [Worker] WITH CHECK ADD CONSTRAINT [Worker_fk1] FOREIGN KEY ([Post]) REFERENCES [Posts]([Id])
ON UPDATE CASCADE
GO
ALTER TABLE [Worker] CHECK CONSTRAINT [Worker_fk1]
GO

ALTER TABLE [Opportunities] WITH CHECK ADD CONSTRAINT [Opportunities_fk0] FOREIGN KEY ([PostId]) REFERENCES [Posts]([Id])
ON UPDATE CASCADE
GO
ALTER TABLE [Opportunities] CHECK CONSTRAINT [Opportunities_fk0]
GO
ALTER TABLE [Opportunities] WITH CHECK ADD CONSTRAINT [Opportunities_fk1] FOREIGN KEY ([Opportunities]) REFERENCES [ListOfOpportunities]([Id])
ON UPDATE CASCADE
GO
ALTER TABLE [Opportunities] CHECK CONSTRAINT [Opportunities_fk1]
GO

ALTER TABLE [Teams] WITH CHECK ADD CONSTRAINT [Teams_fk0] FOREIGN KEY ([LeaderId]) REFERENCES [Worker]([Id])
ON UPDATE NO ACTION
GO
ALTER TABLE [Teams] CHECK CONSTRAINT [Teams_fk0]
GO

ALTER TABLE [Tasks] WITH CHECK ADD CONSTRAINT [Tasks_fk0] FOREIGN KEY ([TeamId]) REFERENCES [Teams]([Id])
ON UPDATE CASCADE
GO
ALTER TABLE [Tasks] CHECK CONSTRAINT [Tasks_fk0]
GO
ALTER TABLE [Tasks] WITH CHECK ADD CONSTRAINT [Tasks_fk1] FOREIGN KEY ([WorkerId]) REFERENCES [Worker]([Id])
ON UPDATE NO ACTION
GO
ALTER TABLE [Tasks] CHECK CONSTRAINT [Tasks_fk1]
GO

--#################################################################### DATABASE DROP ####################################################################--

ALTER TABLE [Tasks] DROP CONSTRAINT [Tasks_fk1]
ALTER TABLE [Tasks] DROP CONSTRAINT [Tasks_fk0]
ALTER TABLE [Teams] DROP CONSTRAINT [Teams_fk0]
ALTER TABLE [Opportunities] DROP CONSTRAINT [Opportunities_fk1]
ALTER TABLE [Opportunities] DROP CONSTRAINT [Opportunities_fk0]
ALTER TABLE [Worker] DROP CONSTRAINT [Worker_fk1]
ALTER TABLE [Worker] DROP CONSTRAINT [Worker_fk0]

DROP TABLE [Worker]
DROP TABLE [Opportunities]
DROP TABLE [Posts]
DROP TABLE [ListOfOpportunities]
DROP TABLE [Teams]
DROP TABLE [Tasks]
