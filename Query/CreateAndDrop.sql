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
	Email nvarchar(50),
	Post int NOT NULL,
	IsDeleted bit,
	Password nvarchar(15),
	WorkedTime nvarchar(30)
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

use uwu

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
go
use master
drop database UwU