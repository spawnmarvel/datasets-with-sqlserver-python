
-- ****** TEST
use DataSetsDb;
go
-- IF NOT EXISTS(SELECT * FROM sys.schemas WHERE NAME = "test" ) EXEC('CREATE SCHEMA [test]');
-- or 
CREATE SCHEMA test;
go

-- create tables
-- varchar: Variable-length, non-Unicode character data. The database collation determines which code page the data is stored using.
-- nvarchar: Variable-length Unicode character data. Dependent on the database collation for comparisons.

-- create tables
CREATE TABLE test.Authors (
	a_id INT IDENTITY (1, 1) PRIMARY KEY,
	a_name NVARCHAR (100) NOT NULL
);

CREATE TABLE test.BestSellers (
	b_id INT IDENTITY (1, 1) PRIMARY KEY,
	b_name NVARCHAR (300) NOT NULL,
	b_rating FLOAT NOT NULL,
	b_reviews INT NOT NULL,
	b_price TINYINT NOT NULL,
	b_year DATE NOT NULL, 
	b_genre VARCHAR (20) NOT NULL,
	author_b_id INT NOT NULL,
	FOREIGN KEY (author_b_id) REFERENCES test.Authors (a_id) ON DELETE CASCADE ON UPDATE CASCADE
	
);

-- Remove all rows
-- DELETE FROM [DataSetsDb].[test].[BestSellers]

-- ****** PROD
use DataSetsDb;
go
CREATE SCHEMA prod;
go

-- create tables
CREATE TABLE prod.Authors (
	a_id INT IDENTITY (1, 1) PRIMARY KEY,
	a_name NVARCHAR (100) NOT NULL
);

CREATE TABLE prod.BestSellers (
	b_id INT IDENTITY (1, 1) PRIMARY KEY,
	b_name NVARCHAR (300) NOT NULL,
	b_rating FLOAT NOT NULL,
	b_reviews INT NOT NULL,
	b_price TINYINT NOT NULL,
	b_year DATE NOT NULL, 
	b_genre VARCHAR (20) NOT NULL,
	author_b_id INT NOT NULL,
	FOREIGN KEY (author_b_id) REFERENCES test.Authors (a_id) ON DELETE CASCADE ON UPDATE CASCADE
	
);