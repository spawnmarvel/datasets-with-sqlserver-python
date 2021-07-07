-- Creates the login AbolrousHazem with password '340$Uuxwp7Mcxo7Khy'.  
CREATE LOGIN misp   
    WITH PASSWORD = 'astring6r473';  
GO

-- Creates a database user for the login created above.  
CREATE USER misp FOR LOGIN misp;  
--
GO 

USE TestGreenWorld
GO

GRANT SELECT,INSERT, UPDATE, DELETE ON test.pump TO misp
GRANT SELECT, INSERT, UPDATE, DELETE ON test.criteria TO misp
