
from utilitydb.db_connector import DbConnector
from utilityreader.read_datasets import ReadDataSet
from utilitylogs.app_logger import Logger
import json

logger = Logger().get()


class AppController:

    def __init__(self):
        self.con_info = self.read_keyvault()
        self.db_con_worker = DbConnector(
            database=self.con_info["database"], db_username=self.con_info["user"], db_password=self.con_info["password"])
        self.read_dataset_worker = ReadDataSet()
        self.db_con_worker.get_sql_version()

    def read_keyvault(self):
        logger.info("Try retrieve password ")
        connection_info = {}
        try:
            with open("keyvault.json") as fi:
                data = json.load(fi)
                connection_info["user"] = data["user"]
                connection_info["password"] = data["password"]
                connection_info["database"] = data["database"]

                logger.info("Success, retrieved password")
                return connection_info
        except Exception as e:
            logger.error(e)
            logger.error("Failed to retrieved password")
        
    
    def ctrl_select_all_bestsellers_test(self):
        select_rv = self.db_con_worker.select_all_bestsellers_test()
        for s in select_rv:
            logger.info(s)

    def ctrl_select_inner_join_bestsellers_authors_test(self):
        select_rv = self.db_con_worker.select_inner_join_bestsellers_authors_test()
        for s in select_rv:
            logger.info(s)

    def ctrl_create_or_check_view_bestsellers_authors_test(self):
        select_rv = self.db_con_worker.create_or_check_view_bestsellers_authors_test()

    def ctrl_select_view_bestsellers_and_authors_test(self):
        select_rv = self.db_con_worker.select_view_bestsellers_and_authors_test()
        for s in select_rv:
            logger.info(s)

    def ctrl_select_view_bestsellers_and_authors_order_by_rating_test(self):
        select_rv = self.db_con_worker.select_view_bestsellers_and_authors_order_by_rating_test()
        for s in select_rv:
            logger.info(s)


    def create_or_check_procedure_insert_bestsellers_test(self):
        select_rv = self.db_con_worker.create_or_check_procedure_insert_bestsellers_test()

    def ctrl_procedure_insert_bestsellers_test(self):
        logger.info("Try insert bestsellers")
        # read the data csv file
        bestsellers_data = self.read_dataset_worker.read_file(
            "./kaggle-datasets/bestsellers with categories.csv")
        # keep a set of authors for later use, this will be a new table with foreign key anyway
        distinct_authors = set()
        for b in bestsellers_data:
            tmp_name = b[0]
            tmp_author = b[1]
            distinct_authors.add(tmp_author)
            tmp_rating = b[2]
            tmp_reviews = b[3]
            tmp_price = b[4]
            tmp_year = b[5]
            tmp_genre = b[6]
            self.db_con_worker.procedure_insert_bestsellers_test(
                b_name=tmp_name, a_name=tmp_author, b_rating=tmp_rating, b_reviews=tmp_reviews, b_price=tmp_price, b_year=tmp_year, b_genre=tmp_genre)

    def create_or_check_procedure_insert_bestsellers_prod(self):
        select_rv = self.db_con_worker.create_or_check_procedure_insert_bestsellers_prod()

    def ctrl_procedure_insert_bestsellers_prod(self):
        logger.info("Try insert bestsellers")
        # read the data csv file
        bestsellers_data = self.read_dataset_worker.read_file(
            "./kaggle-datasets/bestsellers with categories.csv")
        # keep a set of authors for later use, this will be a new table with foreign key anyway
        distinct_authors = set()
        for b in bestsellers_data:
            tmp_name = b[0]
            tmp_author = b[1]
            distinct_authors.add(tmp_author)
            tmp_rating = b[2]
            tmp_reviews = b[3]
            tmp_price = b[4]
            tmp_year = b[5]
            tmp_genre = b[6]
            self.db_con_worker.procedure_insert_bestsellers_prod(
                b_name=tmp_name, a_name=tmp_author, b_rating=tmp_rating, b_reviews=tmp_reviews, b_price=tmp_price, b_year=tmp_year, b_genre=tmp_genre)

    def ctrl_create_or_check_view_bestsellers_authors_prod(self):
        select_rv = self.db_con_worker.create_or_check_view_bestsellers_authors_prod()

    def ctrl_select_view_bestsellers_and_authors_prod(self):
        select_rv = self.db_con_worker.select_view_bestsellers_and_authors_prod()
        for s in select_rv:
            logger.info(s)

    def ctrl_select_view_bestsellers_and_authors_order_by_rating_prod(self):
        select_rv = self.db_con_worker.select_view_bestsellers_and_authors_order_by_rating_prod()
        for s in select_rv:
            logger.info(s)
