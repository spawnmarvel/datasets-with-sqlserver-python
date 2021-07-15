-- https://docs.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver15

-- check indexes our table, sp_helpindex is a system stored procedure which lists the information of all the indexes on a table or view
EXEC sp_helpindex 'test.BestSellers'
-- PK__BestSell__4E29C30D7AB5B978	clustered, unique, primary key located on PRIMARY	b_id

-- When we create a pk we get an index like this, and there can only be one clustred index pr table

-- if you run this, you get error:
CREATE CLUSTERED INDEX idx_b_name on DataSetsDb.test.BestSellers (b_name); 

-- Msg 1902, Level 16, State 3, Line 2
-- Cannot create more than one clustered index on table 'DataSetsDb.test.BestSellers'. 
-- Drop the existing clustered index 'PK__BestSell__4E29C30D7AB5B978' before creating another.
-- Completion time: 2021-07-15T16:57:06.3324630+02:00
