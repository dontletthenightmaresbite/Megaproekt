--#################################################################### DATABASE CREATE ####################################################################--

create database UwU
go
use UwU
go


CREATE TABLE [Worker] (
	Id int NOT NULL primary key identity,
	Name nvarchar(50),
	TeamId int,
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
	LeaderId int NOT NULL

)
GO
CREATE TABLE [Tasks] (
	Id int NOT NULL primary key identity,
	[Description] nvarchar(120),
	TeamId int,
	WorkerId int,
	Deadline date NOT NULL


)
GO
ALTER TABLE [Worker] WITH CHECK ADD CONSTRAINT [Worker_fk0] FOREIGN KEY ([TeamId]) REFERENCES [Teams]([TeamId])
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
ON UPDATE CASCADE
GO
ALTER TABLE [Teams] CHECK CONSTRAINT [Teams_fk0]
GO

ALTER TABLE [Tasks] WITH CHECK ADD CONSTRAINT [Tasks_fk0] FOREIGN KEY ([TeamId]) REFERENCES [Teams]([TeamId])
ON UPDATE CASCADE
GO
ALTER TABLE [Tasks] CHECK CONSTRAINT [Tasks_fk0]
GO
ALTER TABLE [Tasks] WITH CHECK ADD CONSTRAINT [Tasks_fk1] FOREIGN KEY ([WorkerId]) REFERENCES [Worker]([Id])
ON UPDATE CASCADE
GO
ALTER TABLE [Tasks] CHECK CONSTRAINT [Tasks_fk1]
GO
ALTER TABLE [Tasks] WITH CHECK ADD CONSTRAINT [Tasks_fk2] FOREIGN KEY ([TeamId]) REFERENCES [Teams]([Id])
alter table Teams alter column LeaderId int null

--#################################################################### INSERT ####################################################################--

insert Teams values ('Программисты', Null)

Insert Posts values ('Программист',123,200),
('Директор', 1, 1),
('Тимлид', 24554542, 1235642),
('Бэкендер', 65464342, 15782),
('Дизайнерка', 25633342, 12334512),
('Букалтерка', 42563342, 12312)

insert Worker values 
('Олег','2','98745312',1,null),
('Пурга', '2', '233254424', 1, null),
('Курт', '2', '233255644', 1, null),
('Табис', '2', '56755644', 1, null),
('Читус', '2', '989975644', 1, null),
('Опиумен', '2', '43349975644', 1, null),
('Сундус', '2', '1234975644', 1, null),
('Саранча', '2', '456675644', 1, null),
('Чича', '2', '456975644', 1, null),
('Рудольф', '2', '3456975644', 1, null)

--#################################################################### PROCEDURE ####################################################################--

delete [ListOfOpportunities]
delete [Opportunities]
delete [Posts]
delete [Tasks]
delete [Teams]
delete [Worker]

--#################################################################### PROCEDURE ####################################################################--



--#################################################################### PLAYGROUND ####################################################################--



