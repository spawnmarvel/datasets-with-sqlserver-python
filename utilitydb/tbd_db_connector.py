

import pyodbc
from utilitylogs.app_logger import Logger

logger = Logger().get()


class DbConnector:



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


    
    # NOTE Not used due to procedure_insert_bestsellers(), cool
    def insert_select_test_to_prod(self):
        # https://docs.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql?view=sql-server-ver15
        # First we create a mirror of test.table to prod.table in SSMS
        sql = """INSERT prod.BestSellers
                (b_name
                    ,b_rating
                    ,b_reviews
                    ,b_price
                    ,b_year
                    ,b_genre
                    ,author_b_id)
                    SELECT
                         b_name
                        ,b_rating
                        ,b_reviews
                        ,b_price
                        ,b_year
                        ,b_genre
                        ,author_b_id
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


    # FIXME merge test.table to prod.table, beautiful! But not used after procedure, due to insert into two tables
    # Merge tested with one table as code below works
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