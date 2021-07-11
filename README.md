# datasets-with-sqlserver-python
Having fun with Kaggle data, SQL Server and Python (pyodbc).

## Links 
[SQL SERVER SSMS] https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15

[Kaggle public datasets] https://www.kaggle.com/sootersaalu/amazon-top-50-bestselling-books-2009-2019?select=bestsellers+with+categories.csv

[PyODBC] https://pypi.org/project/pyodbc/

[PyODBC parameters] https://github.com/mkleehammer/pyodbc/wiki/Getting-started#parameters

ODBC supports parameters using a question mark as a place holder in the SQL. 
You provide the values for the question marks by passing them after the SQL.
This is safer than putting the values into the string because the parameters are passed to the database separately, 
protecting against SQL injection attacks. It is also be more efficient if you execute the same SQL repeatedly with different parameters. 
The SQL will be "prepared" only once. (pyodbc keeps only the last prepared statement, so if you switch between statements, each will be prepared multiple times.)


TODO or Done's:
* DDL, bestsellers, author, f key on id
* Db con 
* Logger 
* Datasets
* Read file
* simulate keyvault
* Insert bestsellers data
* T-SQL CRUD bestsellers data
* Prepared statment for data
* T-SQL Advanced
* TBD


[![Screenshot](x_logs_and_join.jpg)