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

    # NOTE test query
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

    # NOTE Not used due to procedure for insert bestsellers and authors
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

    # NOTE Not used due to procedure for insert bestsellers and authors
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

    # TODO Not used due to procedure for insert bestsellers and authors
    def update_bestsellers(self):
        pass

    # NOTE Delete one row
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

    # NOTE Select all
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

    # NOTE Advanced TSQL

    # NOTE Join bestsellers and authors
    def select_inner_join_bestsellers_authors(self):
        try:
            with self.cnxn:  # ctxmanger close
                sql = """SELECT
                        a.a_id
	                    ,a.a_name
                        ,b.b_id
                        ,b.b_name
                        ,b.b_rating
                        ,b.b_reviews
                        ,b.b_price
                        ,b.b_year
                        ,b.b_genre
                        ,b.author_b_id
                        FROM DataSetsDb.test.Authors as a
                        INNER JOIN DataSetsDb.test.BestSellers as b
                        ON a.a_id = b.author_b_id;"""
                logger.info(sql)
                self.cursor.execute(sql)
                row = self.cursor.fetchall()
                return row
        except Exception as e:
            logger.error(e)

    # NOTE create view if not exists
    def create_or_check_view_bestsellers_authors(self):
        logger.info("Try CREATE VIEW")
        row = ""
        try:
            with self.cnxn:  # ctxmanger close
                sql_check = "SELECT * FROM sys.views WHERE OBJECT_ID=OBJECT_ID('test.BestsellersAndAuthors');"
                logger.info(sql_check)
                self.cursor.execute(sql_check)
                row = self.cursor.fetchall()
                # it returns an empty list of not yet created
                if not row:
                    sql_create = """CREATE VIEW test.BestsellersAndAuthors as
                        SELECT
                        a.a_id
	                    ,a.a_name
                        ,b.b_id
                        ,b.b_name
                        ,b.b_rating
                        ,b.b_reviews
                        ,b.b_price
                        ,b.b_year
                        ,b.b_genre
                        ,b.author_b_id
                        FROM DataSetsDb.test.Authors as a
                        INNER JOIN DataSetsDb.test.BestSellers as b
                        ON a.a_id = b.author_b_id;"""
                    logger.info(sql_create)
                    self.cursor.execute(sql_create)
                    self.cnxn.commit()
                    logger.info("CREATE VIEW done")
                else:
                    # logg the data atr about the view
                    logger.info(row)

                    return row
        except Exception as e:
            logger.error(e)

    # NOTE select view
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

    # NOTE select view order rating
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

    # NOTE Not used due to procedure for insert bestsellers and authors
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

    # NOTE merge test.table to prod.table, beautiful!
    def merge_test_to_prod(self):
        # https://docs.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql?view=sql-server-ver15
        # First we create a mirror of test.table to prod.table
        # Then we do the merge
        logger.info("Try MERGE test to prod")
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

    # NOTE create procedure if not exists
    def create_or_check_procedure_insert_bestsellers(self):
        logger.info("Try CREATE PROCEDURE")
        sql = """CREATE PROCEDURE test.InsertBestSellersAndAuthors(
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
	                            SET @tmp_author_id = (SELECT a_id FROM test.Authors WHERE a_name = @tmp_a_name);
	                            INSERT INTO test.BestSellers (b_name, b_rating, b_reviews, b_price, b_year, b_genre, author_b_id) 
	                            VALUES (@tmp_b_name, @tmp_b_rating, @tmp_b_reviews, @tmp_b_price, @tmp_b_year, @tmp_b_genre, @tmp_author_id)
                            END
                        ELSE
                            BEGIN
	                            INSERT INTO test.Authors (a_name) VALUES (@tmp_a_name);
	                            SET @tmp_author_id = (SELECT a_id FROM test.Authors WHERE a_name = @tmp_a_name);
	                            INSERT INTO test.BestSellers (b_name, b_rating, b_reviews, b_price, b_year, b_genre, author_b_id) 
	                            VALUES (@tmp_b_name, @tmp_b_rating, @tmp_b_reviews, @tmp_b_price, @tmp_b_year, @tmp_b_genre, @tmp_author_id)
                            END;"""
        try:
            with self.cnxn:  # ctxmanger close
                self.cursor.execute(sql)
                self.cnxn.commit()
                logger.info(sql)
                logger.info("CREATE PROCEDURE done")
        except Exception as e:
            logger.error(e)

    # NOTE insert the raw bestsellers with categories.csv
    def procedure_insert_bestsellers(self, b_name, a_name, b_rating, b_reviews, b_price, b_year, b_genre):
        # we must validate all params before execute preocedure
        sql = "EXEC test.InsertBestSellersAndAuthors @tmp_b_name=? , @tmp_a_name=? , @tmp_b_rating=?, @tmp_b_reviews=?,@tmp_b_price=?,@tmp_b_year=?,@tmp_b_genre=?;"
        # we never add the params as str in sql, we add them outside so we bypass SQL Injection
        params = (b_name, a_name, b_rating,
                  b_reviews, b_price, b_year, b_genre)
        try:
            with self.cnxn:  # ctxmanger close
                # before we insert we can validate all params
                self.cursor.execute(sql, params)
                self.cnxn.commit()
                logger.info(sql)
                logger.info(params)
        except Exception as e:
            logger.error(params)
            logger.error(e)
