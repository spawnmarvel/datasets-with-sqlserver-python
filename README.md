# datasets-with-sqlserver-python
Having fun with Kaggle data, SQL Server and Python (pyodbc).

## Information
### Links
SQL:

[Microsoft SQL documentation]https://docs.microsoft.com/en-us/sql/?view=sql-server-ver15

[SQL SERVER SSMS] https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15

Must check out this Azure Data Studio stuff

[![Screenshot](x_SSMS_AZ.jpg)

[Kaggle public datasets] https://www.kaggle.com/sootersaalu/amazon-top-50-bestselling-books-2009-2019?select=bestsellers+with+categories.csv

[PyODBC] https://pypi.org/project/pyodbc/

[PyODBC parameters] https://github.com/mkleehammer/pyodbc/wiki/Getting-started#parameters

ODBC supports parameters using a question mark as a place holder in the SQL. 
You provide the values for the question marks by passing them after the SQL.
This is safer than putting the values into the string because the parameters are passed to the database separately, 
protecting against SQL injection attacks. It is also be more efficient if you execute the same SQL repeatedly with different parameters. 
The SQL will be "prepared" only once. (pyodbc keeps only the last prepared statement, so if you switch between statements, each will be prepared multiple times.)

### Database Schemas
* The flat model is for small, simple applications
* The hierarchical model is for nested data, like XML or JSON
* The network model is useful in mapping and spatial data, also for depicting workflows
* The relational model best reflects Object-Oriented Programming applications
* The star schema and snowflake schema are for analyzing large datasets
* https://www.xplenty.com/blog/database-schema-examples/

TODO or Done's:
* DDL, bestsellers, author, f key on id 100%
* Db con 100%
* DB close
* https://stackoverflow.com/questions/3783238/python-database-connection-close
* TCP viewer and Wireshark check call's, close
* Logger 100%
* Datasets 100%
* Read file 100%
* Simulate keyvault 100%
* Insert bestsellers data 100%
* Prepared statment for data 80%
* T-SQL CRUD bestsellers data 50%
* T-SQL Advanced, Views,Joins, Procedure's, Merge etc
* TBD
* Tkinter GUI, MVC

EER of schema test and prod for BestSellers from Kaggle (Amazon books)
* Prod and test is self-explanatory
* Procedure:test.InsertBestSellersAndAuthors, uses the raw Kaggle data as-is
* View:test.BestsellersAndAuthors, joins both tables

## 1 HOW TO bestsellers with categories.csv

1. Create tables with crt_1_tables_bestsellers.sql in SSMS
2. Create user CRUD rights with crt_user.sql in SSMS
3. We use then test.table's first to verify before implementing prod.table's
4. A note about the data:bestsellers with categories.csv from kaggle or here, it is just raw data
* The format must be (b for book, a for author); b_name, a_name, b_rating, b_reviews, b_price, b_year, b_genre.
* We then read the .csv and call the test.InsertBestSellersAndAuthors or (prod.InsertBestSellersAndAuthors) to insert data like this:
* If it exists an author, we get the id and insert the book data, else we insert author and book data.
5. 


## 2 HOW TO bestsellers with new topic tbd
