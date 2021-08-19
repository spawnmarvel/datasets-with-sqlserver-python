-- https://github.com/Microsoft/sql-server-samples/releases/tag/wide-world-importers-v1.0
-- WideWorldImportersDW-Standard.bak
-- create file WideWorldDbSample and store the .bak there
use [master]
restore database [WideWorldImportersDW]
from disk = 'C:\giti2021\WideWorldDbSample\WideWorldImportersDW-Standard.bak'
with file=1,
move N'WWI_Primary' TO N'C:\giti2021\WideWorldDbSample\\WideWorldImportersDW.mdf',  
move N'WWI_UserData' TO N'C:\giti2021\WideWorldDbSample\\WideWorldImportersDW_UserData.ndf',  
move N'WWI_Log' TO N'C:\giti2021\WideWorldDbSample\\WideWorldImportersDW.ldf',  

nounload, stats = 5
go
