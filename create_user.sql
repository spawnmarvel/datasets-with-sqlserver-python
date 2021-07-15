

-- ****** TEST
-- Creates the login misp with password provided in ''
-- CREATE LOGIN misp WITH PASSWORD = '';  
-- GO

-- Creates a database user for the login created above.  
CREATE USER misp FOR LOGIN misp;  
--
GO 

USE DataSetsDb
GO
--CRUD

GRANT SELECT,INSERT, UPDATE, DELETE ON test.BestSellers TO misp
GRANT SELECT,INSERT, UPDATE, DELETE ON test.Authors TO misp

--GRANT CREATE VIEW, PROCEDURE (before create view)
USE DataSetsDb
GO
GRANT CREATE VIEW TO misp
GRANT CREATE PROCEDURE TO misp

-- The specified schema name "test" either does not exist or you do not have permission to use it (hm, did not have access to schema)
USE DataSetsDb
GO
GRANT ALTER ON SCHEMA::test TO misp
GRANT SELECT ON SCHEMA::test TO misp
--GRANT SELECT ON SCHEMA (after view was created the error was;The SELECT permission was denied on the object 'BestsellersAndAuthors', database 'DataSetsDb', schema 'test'. )

--GRANT EXECUTE ON PROC TO USE IT
USE DataSetsDb
GO
GRANT EXECUTE ON OBJECT::test.InsertBestSellersAndAuthors TO misp
-- ****** PROD
USE DataSetsDb
GO
--CRUD

GRANT SELECT,INSERT, UPDATE, DELETE ON prod.BestSellers TO misp
GRANT SELECT,INSERT, UPDATE, DELETE ON prod.Authors TO misp