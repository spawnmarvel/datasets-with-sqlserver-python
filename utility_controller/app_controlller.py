
from utility_db.db_connector import DbConnector
from utility_reader.read_datasets import ReadDataSet
from utility_logs.app_logger import Logger
import json

logger = Logger().get()


class AppController:

    def __init__(self):
        self.con_info = self.read_keyvault()
        self.db_con_worker = DbConnector(
            database=self.con_info["database"], db_username=self.con_info["user"], db_password=self.con_info["password"])
        self.read_dataset_worker = ReadDataSet()

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

    # Not used, see ctrl_procedure_insert_bestsellers()
    def ctrl_insert_to_bestsellers(self):
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
            self.db_con_worker.insert_bestsellers(
                b_name=tmp_name, b_rating=tmp_rating, b_reviews=tmp_reviews, b_price=tmp_price, b_year=tmp_year, b_genre=tmp_genre)

    def ctrl_select_all_bestsellers(self):
        select_rv = self.db_con_worker.select_all_bestsellers()
        for s in select_rv:
            logger.info(s)

    def ctrl_delete_bestsellers(self, r_id):
        select_rv = self.db_con_worker.delete_bestsellers(r_id)

    def ctrl_insert_authors(self):
        logger.info("Try insert authors")
        authors_bestsellers_data = self.read_dataset_worker.read_file(
            "./kaggle-datasets/bestsellers with categories authors.csv")
        for a in authors_bestsellers_data:
            tmp_name = a[0]
            tmp_a_book_id = a[1]
            self.db_con_worker.insert_author(
                a_name=tmp_name, a_book_id=tmp_a_book_id)

    def ctrl_select_inner_join_bestsellers_authors(self):
        select_rv = self.db_con_worker.select_inner_join_bestsellers_authors()
        for s in select_rv:
            logger.info(s)

    def ctrl_create_or_check_view_bestsellers_authors(self):
        select_rv = self.db_con_worker.create_or_check_view_bestsellers_authors()

    def ctrl_select_view_BestsellersAndAuthors(self):
        select_rv = self.db_con_worker.select_view_BestsellersAndAuthors()
        for s in select_rv:
            logger.info(s)

    def ctrl_select_view_BestsellersAndAuthors_order_by_rating(self):
        select_rv = self.db_con_worker.select_view_BestsellersAndAuthors_order_by_rating()
        for s in select_rv:
            logger.info(s)

    def ctrl_insert_select_test_to_prod(self):
        select_rv = self.db_con_worker.insert_select_test_to_prod()

    def ctrl_merge_test_to_prod(self):
        select_rv = self.db_con_worker.merge_test_to_prod()

    def create_or_check_procedure_insert_bestsellers(self):
        select_rv = self.db_con_worker.create_or_check_procedure_insert_bestsellers()

    def ctrl_procedure_insert_bestsellers(self):
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
            self.db_con_worker.procedure_insert_bestsellers(
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
