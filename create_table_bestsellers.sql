use DataSetsDb;
go
CREATE SCHEMA test;
go

-- create tables
CREATE TABLE test.BestSellers (
	b_id INT IDENTITY (1, 1) PRIMARY KEY,
	b_name VARCHAR (200) NOT NULL,
	b_author VARCHAR (40) NOT NULL,
	b_rating FLOAT NOT NULL,
	b_reviews INT NOT NULL,
	b_price TINYINT NOT NULL,
	b_year DATE NOT NULL, 
	b_genre VARCHAR (20) NOT NULL
	
);

-- Remove all rows
-- DELETE FROM [DataSetsDb].[test].[BestSellers]

