import pyodbc
from utility_logs.app_logger import Logger

logger = Logger().get()


class DbConnector:

    def __init__(self, database, db_username, db_password):
        self.server = r"localhost\sqlexpress"
        self.database = database
        self.username = db_username
        self.password = db_password
        self.cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+self.server +
                                   ";DATABASE="+self.database+";UID="+self.username+";PWD=" + self.password)
        self.cursor = self.cnxn.cursor()

    def get_version(self):
        try:
            with self.cnxn:  # ctxmanger close
                self.cursor.execute("SELECT @@version;")
                row = self.cursor.fetchone()
                while row:
                    print(row[0])
                    row = self.cursor.fetchone()
        except Exception as e:
            logger.error(e)


    def create_or_check_procedure_insert_bestsellers():
        pass

    def select_all_bestsellers(self):
        try:
            with self.cnxn:  # ctxmanger close
                sql = "SELECT * FROM test.BestSellers;"
                logger.info(sql)
                self.cursor.execute(sql)
                row = self.cursor.fetchall()
                return row
        except Exception as e:
            logger.error(e)

    def insert_bestsellers(self, b_name, b_rating, b_reviews, b_price, b_year, b_genre):
        sql = """INSERT INTO test.BestSellers (b_name, b_rating, b_reviews, b_price, b_year, b_genre) VALUES (?,?,?,?,?, ?)"""
        rv = str(b_name) + "," + str(b_rating) + "," + str(b_reviews) + \
            "," + str(b_price) + "," + str(b_year) + "," + str(b_genre)
        try:
            with self.cnxn:  # ctxmanger close
                # before we insert we can validate all params
                self.cursor.execute(sql, b_name, b_rating,
                                    b_reviews, b_price, b_year, b_genre)
                self.cnxn.commit()
                logger.info(sql)
                logger.info(rv)
        except Exception as e:
            logger.error(rv)
            logger.error(e)

    def insert_author(self, a_name, a_book_id):
        sql = """INSERT INTO test.Authors (a_name, author_book_id) VALUES (?,?)"""
        rv = str(a_name) + "," + str(a_book_id)
        try:
            with self.cnxn:  # ctxmanger close
                # before we insert we can validate all params
                self.cursor.execute(sql, a_name, a_book_id)
                self.cnxn.commit()
                logger.info(sql)
                logger.info(rv)
        except Exception as e:
            logger.error(e)

    def update_bestsellers(self):
        pass

    def delete_bestsellers(self, remove_id):
        sql = "DELETE FROM prod.BestSellers where b_id = (?)"
        rv = str(remove_id)
        try:
            with self.cnxn:  # ctxmanger close
                # before we insert we can validate all params
                self.cursor.execute(sql, remove_id)
                self.cnxn.commit()
                logger.info(sql)
                logger.info(rv)
        except Exception as e:
            logger.error(e)

    # advanced TSQL

    def select_inner_join_bestsellers_authors(self):
        try:
            with self.cnxn:  # ctxmanger close
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
    def create_or_check_view_bestsellers_authors(self):
        logger.info("Try CREATE VIEW test.BestsellersAndAuthors")
        row = ""
        try:
            with self.cnxn:  # ctxmanger close
                sql_check = "SELECT * FROM sys.views WHERE OBJECT_ID=OBJECT_ID('test.BestsellersAndAuthors');"
                logger.info(sql_check)
                self.cursor.execute(sql_check)
                row = self.cursor.fetchall()
                # it returns an empty list of not yet created
                if not row:
                    sql_create = """ CREATE VIEW test.BestsellersAndAuthors as
                        SELECT b.b_id
                        ,b.b_name
                        ,b.b_rating
                        ,b.b_reviews
                        ,b.b_price
                        ,b.b_year
                        ,b.b_genre
	                    ,a.a_name
	                    ,a.author_book_id
                        FROM DataSetsDb.test.BestSellers as b
                        INNER JOIN DataSetsDb.test.Authors as a
                        ON b.b_id = a.author_book_id;"""
                    logger.info(sql_create)
                    self.cursor.execute(sql_create)
                    self.cnxn.commit()
                else:
                    # logg the data atr about the view
                    logger.info(row)
                    return row
        except Exception as e:
            logger.error(e)

    def select_view_BestsellersAndAuthors(self):
        try:
            with self.cnxn:  # ctxmanger close
                sql = "SELECT * FROM test.BestsellersAndAuthors;"
                logger.info(sql)
                self.cursor.execute(sql)
                row = self.cursor.fetchall()
                return row
        except Exception as e:
            logger.error(e)

    def select_view_BestsellersAndAuthors_order_by_rating(self):
        try:
            with self.cnxn:  # ctxmanger close #ctxmanger close
                sql = "SELECT * FROM test.BestsellersAndAuthors ORDER BY b_rating DESC;"
                logger.info(sql)
                self.cursor.execute(sql)
                row = self.cursor.fetchall()
                return row
        except Exception as e:
            logger.error(e)

    def insert_select_test_to_prod(self):
        # https://docs.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql?view=sql-server-ver15
        # First we create a mirror of test.table to prod.table in SSMS
        sql = """INSERT prod.BestSellers
                (b_name
                    ,b_rating
                    ,b_reviews
                    ,b_price
                    ,b_year
                    ,b_genre)
                    SELECT
                         b_name
                        ,b_rating
                        ,b_reviews
                        ,b_price
                        ,b_year
                        ,b_genre
                        FROM test.BestSellers
                        WHERE NOT EXISTS (SELECT b_id FROM prod.BestSellers po WHERE po.b_id = test.BestSellers.b_id);"""
        sql_verify_prod = "SELECT COUNT(b_name) FROM prod.BestSellers"
        sql_verify_test = "SELECT COUNT(b_name) FROM test.BestSellers"
        result = {}
        try:
            with self.cnxn:  # ctxmanger close
                self.cursor.execute(sql)
                self.cnxn.commit()
                logger.info(sql)
                logger.info(sql_verify_prod)
                self.cursor.execute(sql_verify_prod)
                row = self.cursor.fetchall()
                result["prod"] = row

                logger.info(sql_verify_test)
                self.cursor.execute(sql_verify_test)
                row = self.cursor.fetchall()
                result["test"] = row
                logger.info(result)
                return result
        except Exception as e:
            logger.error(e)

    def merge_test_to_prod(self):
        # https://docs.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql?view=sql-server-ver15
        # First we create a mirror of test.table to prod.table
        # Then we do the merge
        sql = """MERGE prod.BestSellers AS target
                 USING test.BestSellers AS source
                 ON source.b_id = target.b_id
                 
                 WHEN NOT MATCHED BY target THEN
                    INSERT (b_name
                        ,b_rating
                        ,b_reviews
                        ,b_price
                        ,b_year
                        ,b_genre)
                        VALUES(source.b_name
                        ,source.b_rating
                        ,source.b_reviews
                        ,source.b_price
                        ,source.b_year
                        ,source.b_genre)

                WHEN MATCHED THEN UPDATE SET
                        target.b_name=source.b_name
                        ,target.b_rating=source.b_rating
                        ,target.b_reviews=source.b_reviews
                        ,target.b_price=source.b_price
                        ,target.b_year=source.b_year
                        ,target.b_genre=source.b_genre
                
                WHEN NOT MATCHED BY source THEN
                    DELETE;"""
                    # OUTPUT $action,deleted.*,inserted.*;
        try:
            with self.cnxn:  # ctxmanger close
                self.cursor.execute(sql)
                self.cnxn.commit()
                logger.info(sql)
                logger.info("Merge done")
        except Exception as e:
            logger.error(e)

    # create procedure if not exists
