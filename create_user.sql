-- Creates the login misp with password provided in ''
-- CREATE LOGIN misp WITH PASSWORD = '';  
-- GO

-- Creates a database user for the login created above.  
CREATE USER misp FOR LOGIN misp;  
--
GO 

USE DataSetsDb
GO

GRANT SELECT,INSERT, UPDATE, DELETE ON test.BestSellers TO misp
