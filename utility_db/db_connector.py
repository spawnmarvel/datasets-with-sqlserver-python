
from logging import log
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

    def select_all_bestsellers(self):
        try:
            sql = "SELECT * FROM test.BestSellers;"
            logger.info(sql)
            self.cursor.execute(sql) 
            row = self.cursor.fetchall()
            return row
        except Exception as e:
            logger.error(e) 

    def insert_bestsellers(self,b_name, b_rating,b_reviews, b_price, b_year, b_genre):
        sql = """INSERT INTO test.BestSellers (b_name, b_rating, b_reviews, b_price, b_year, b_genre) VALUES (?,?,?,?,?, ?)"""
        rv = str(b_name) + "," + str(b_rating) + "," +str(b_reviews) + "," +str(b_price) + "," +str(b_year) + "," +str(b_genre)
        try:
            # before we insert we can validate all params
            self.cursor.execute(sql, b_name, b_rating,b_reviews, b_price, b_year, b_genre) 
            self.cnxn.commit()
            logger.info(sql)
            logger.info(rv)
        except Exception as e:
            logger.error(rv)
            logger.error(e)
    
    def insert_author(self,a_name, a_book_id):
        sql = """INSERT INTO test.Authors (a_name, author_book_id) VALUES (?,?)"""
        rv = str(a_name) + "," +  str(a_book_id)
        try:
            # before we insert we can validate all params
            self.cursor.execute(sql, a_name, a_book_id)
            self.cnxn.commit()
            logger.info(sql)
            logger.info(rv)
        except Exception as e:
            logger.error(e)

    def update_bestsellers(self):
        pass
    
    def delete_bestsellers(self):
        pass


    # advanced TSQL

    def select_inner_join_bestsellers_authors(self):
        try:
            sql = """SELECT b.b_id
                ,b.b_name
                ,b.b_rating
                ,b.b_reviews
                ,b.b_price
                ,b.b_year
                ,b.b_genre
	            ,a.a_id
	            ,a.a_name
	            ,a.author_book_id
                FROM DataSetsDb.test.BestSellers as b
                INNER JOIN DataSetsDb.test.Authors as a
                ON b.b_id = a.author_book_id ORDER BY a.a_name DESC;"""
            logger.info(sql)
            self.cursor.execute(sql) 
            row = self.cursor.fetchall()
            return row
        except Exception as e:
            logger.error(e) 

    # create view if not exists
    # create procedure if not exists
