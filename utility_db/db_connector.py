
import pyodbc 
# https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver15
import random
import datetime
from utility_logs.app_logger import Logger

logger = Logger().get()



server = r"localhost\sqlexpress"
database = "DataSetsDb" 
username = "misp" 
password = "astring6r473"
cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+server+";DATABASE="+database+";UID="+username+";PWD="+ password)
cursor = cnxn.cursor()


def get_version():
    cursor.execute("SELECT @@version;") 
    row = cursor.fetchone() 
    while row: 
        print(row[0])
        row = cursor.fetchone()


def get_all_bestsellers():
    sql = "SELECT * FROM test.BestSellers;"
    logger.info(sql)
    cursor.execute(sql) 
    row = cursor.fetchall() 
    print(row)

def insert_bestsellers(b_name, b_author, b_rating, b_price, b_year, b_genre):
    print(b_name)
    # cursor.execute("""INSERT INTO test.BestSellers (b_name, b_author, b_rating, b_price, b_year, b_genre) VALUES (?,?,?,?,?,?)""", "P3","EAR") 
    # cnxn.commit()




