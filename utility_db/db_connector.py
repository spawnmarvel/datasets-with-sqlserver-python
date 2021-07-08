
import pyodbc 
# https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver15
import random
import datetime
from utility_logs.app_logger import Logger

logger = Logger().get()

class DbConnector:

    def __init__(self, database, db_username, db_password):
        self.server = r"localhost\sqlexpress"
        self.database = database
        self.username = db_username
        self.password = db_password
        self.cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+self.server+";DATABASE="+self.database+";UID="+self.username+";PWD="+ self.password)
        self.cursor = self.cnxn.cursor()

    def get_version(self):
        self.cursor.execute("SELECT @@version;") 
        row = self.cursor.fetchone() 
        while row: 
            print(row[0])
            row = self.cursor.fetchone()


    def get_all_bestsellers(self):
        sql = "SELECT * FROM test.BestSellers;"
        logger.info(sql)
        self.cursor.execute(sql) 
        row = self.cursor.fetchall() 
        print(row)

    def insert_bestsellers(b_name, b_author, b_rating, b_price, b_year, b_genre):
        print(b_name)
    # cursor.execute("""INSERT INTO test.BestSellers (b_name, b_author, b_rating, b_price, b_year, b_genre) VALUES (?,?,?,?,?,?)""", "P3","EAR") 
    # cnxn.commit()
