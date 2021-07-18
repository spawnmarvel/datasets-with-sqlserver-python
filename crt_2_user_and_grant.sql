
-- ****** TEST
-- Creates the login misp with password provided in ''
-- 1.1 
-- CREATE LOGIN misp WITH PASSWORD = '';  

--  1 Creates a database user for the login created above.  
CREATE USER misp FOR LOGIN misp;  
--
GO 
USE DataSetsDb
GO
-- 2 CRUD operations
GRANT SELECT,INSERT, UPDATE, DELETE ON test.BestSellers TO misp
GRANT SELECT,INSERT, UPDATE, DELETE ON test.Authors TO misp

-- 3 GRANT CREATE VIEW, PROCEDURE (before create view and procedure)

GRANT CREATE VIEW TO misp
GRANT CREATE PROCEDURE TO misp
GRANT ALTER ON SCHEMA::test TO misp
GRANT SELECT ON SCHEMA::test TO misp


-- ****** PROD
USE DataSetsDb
GO
GRANT ALTER ON SCHEMA::prod TO misp
GRANT SELECT ON SCHEMA::prod TO misp
--GRANT EXECUTE ON PROC TO USE IT
USE DataSetsDb
GO
GRANT EXECUTE ON OBJECT::prod.InsertBestSellersAndAuthors TO misp

USE DataSetsDb
GO
--CRUD

GRANT SELECT,INSERT, UPDATE, DELETE ON prod.BestSellers TO misp
GRANT SELECT,INSERT, UPDATE, DELETE ON prod.Authors TO misp