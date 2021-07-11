use DataSetsDb;
go
IF NOT EXISTS(SELECT * FROM sys.schemas WHERE NAME = "test" ) EXEC('CREATE SCHEMA [test]');
-- or CREATE SCHEMA test;
go

-- create tables
CREATE TABLE test.BestSellers (
	b_id INT IDENTITY (1, 1) PRIMARY KEY,
	b_name VARCHAR (200) NOT NULL,
	b_rating FLOAT NOT NULL,
	b_reviews INT NOT NULL,
	b_price TINYINT NOT NULL,
	b_year DATE NOT NULL, 
	b_genre VARCHAR (20) NOT NULL
	
);

-- create tables
CREATE TABLE test.Authors (
	a_id INT IDENTITY (1, 1) PRIMARY KEY,
	a_name VARCHAR (200) NOT NULL,
	author_book_id INT NOT NULL,
	FOREIGN KEY (author_book_id) REFERENCES test.BestSellers (b_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Remove all rows
-- DELETE FROM [DataSetsDb].[test].[BestSellers]

