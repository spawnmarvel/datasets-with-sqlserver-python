--https://docs.microsoft.com/en-us/sql/t-sql/statements/set-nocount-transact-sql?view=sql-server-ver15
-- SET NOCOUNT { ON | OFF }   
-- Stops the message that shows the count of the number of rows affected by a Transact-SQL statement or stored procedure from being returned as part of the result set.
-- setting SET NOCOUNT to ON can provide a significant performance boost, because network traffic is greatly reduced.

CREATE PROCEDURE test.InsertBestSellersAndAuthors(
@tmp_b_name NVARCHAR(300)
,@tmp_a_name NVARCHAR(100)
, @tmp_b_rating FLOAT
, @tmp_b_reviews INT
, @tmp_b_price TINYINT
, @tmp_b_year DATE
, @tmp_b_genre VARCHAR(20))
AS
DECLARE @tmp_author_id INT;


IF EXISTS (SELECT a_id FROM test.Authors WHERE a_name = @tmp_a_name)
BEGIN
	--PRINT 'Insert bestsellers with author @tmp_id';
	SET @tmp_author_id = (SELECT a_id FROM test.Authors WHERE a_name = @tmp_a_name);
	INSERT INTO test.BestSellers (b_name, b_rating, b_reviews, b_price, b_year, b_genre, author_b_id) 
	VALUES (@tmp_b_name, @tmp_b_rating, @tmp_b_reviews, @tmp_b_price, @tmp_b_year, @tmp_b_genre, @tmp_author_id)
END
ELSE
BEGIN
	--PRINT 'Insert bestsellers and author'
	INSERT INTO test.Authors (a_name) VALUES (@tmp_a_name);
	SET @tmp_author_id = (SELECT a_id FROM test.Authors WHERE a_name = @tmp_a_name);
	INSERT INTO test.BestSellers (b_name, b_rating, b_reviews, b_price, b_year, b_genre, author_b_id) 
	VALUES (@tmp_b_name, @tmp_b_rating, @tmp_b_reviews, @tmp_b_price, @tmp_b_year, @tmp_b_genre, @tmp_author_id)
END


--right click SSMS and select Execure stored procedure
--You can then add data and go and test it like this, return value is 0:
USE DataSetsDb
GO

DECLARE	@return_value int

EXEC	@return_value = [test].[InsertBestSellersAndAuthors]
		@tmp_b_name = N'BOOK1',
		@tmp_a_name = N'ESPEN',
		@tmp_b_rating = 2,
		@tmp_b_reviews = 23,
		@tmp_b_price = 1,
		@tmp_b_year = '01-01-2016',
		@tmp_b_genre = N'FUN'

SELECT	'Return Value' = @return_value

GO