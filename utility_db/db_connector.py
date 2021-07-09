
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
        try:
            self.cursor.execute("SELECT @@version;") 
            row = self.cursor.fetchone() 
            while row: 
                print(row[0])
                row = self.cursor.fetchone()
        except Exception as e:
            logger.error(e)


    def get_all_bestsellers(self):
        try:
            sql = "SELECT * FROM test.BestSellers;"
            logger.info(sql)
            self.cursor.execute(sql) 
            row = self.cursor.fetchall()
            return row
        except Exception as e:
            logger.error(e) 

    def insert_bestsellers(self,b_name, b_author, b_rating,b_reviews, b_price, b_year, b_genre):
        sql = """INSERT INTO test.BestSellers (b_name, b_author, b_rating, b_reviews, b_price, b_year, b_genre) VALUES (?,?,?,?,?,?, ?)"""
        rv = str(b_name) + "," + str(b_author) + "," + str(b_rating) + "," +str(b_reviews) + "," +str(b_price) + "," +str(b_year) + "," +str(b_genre)
        try:
            self.cursor.execute(sql, b_name, b_author, b_rating,b_reviews, b_price, b_year, b_genre) 
            self.cnxn.commit()
            logger.debug(sql)
        except Exception as e:
            logger.error(rv)
            logger.error(e)
