--#################################################################### INSERT ####################################################################--

use UwU

insert Teams values ('Programmers', Null)

Insert Posts values 
('Programmer',123,200),
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

exec InsertTeam 'Программисты'
exec InsertTeam 'Дизайнеры'

exec InsertPost 'Директор', 90000, 8
exec InsertPost 'Тимлид', 60000, 8
exec InsertPost 'Дизайнер', 50000, 8
exec InsertPost 'Программист', 50000, 8

exec InsertWorker 'Director', null, '+79211111111', 'first@mail.ru', 1, '00:00:00'
exec InsertWorker 'Leader', 1, '+79212222222', 'second@mail.ru', 2, '00:00:00'
exec InsertWorker 'Diz1', 1, '+79213333333', 'third@mail.ru', 3, '00:00:00'
exec InsertWorker 'Diz2', 1, '+79214444444', 'fourth@mail.ru', 3, '00:00:00'
exec InsertWorker 'Prog1', 1, '+79215555555', 'fifth@mail.ru', 4, '00:00:00'

exec insertOpportunity 2,2
exec InsertOpportunityInListOfOpportunities 'Управлять людишками'

exec GetWorkerPost 7 
exec [dbo].[UpdateWorkedTime] 2, '00:00:00'

exec InsertTask 'asdasdasfasdfs', 4, '2023-02-22'
--#################################################################### DELETE ####################################################################--

delete [ListOfOpportunities]
delete [Opportunities]
delete [Posts]
delete [Tasks]
delete [Teams]
delete [Worker]
