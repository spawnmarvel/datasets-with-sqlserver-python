
from utility_db.db_connector import DbConnector
from utility_reader.read_datasets import ReadDataSet
from utility_logs.app_logger import Logger
import json

logger = Logger().get()

def read_keyvault():
    logger.info("Try retrieve password ")
    try:
        with open("keyvault.json") as fi:
            data = json.load(fi)
            p = data["password"]
            logger.info("Succsess, retrieved password")
            return p
    except Exception as e:
        logger.error(e)
        logger.error("Failed to retrieved password")


def main():
    logger.info("* Main, logs: utility_logs/logs.log")
    logger.info("** When done, set [handler_consoleHandler], level=ERROR, it is now level=INFO. So all that goes to file does also go to std out ")
    db = "DataSetsDb" 
    user = "misp"
    p = read_keyvault()
    db_con_worker = DbConnector(database=db, db_username=user, db_password=p)
    read_data_worker = ReadDataSet()
    li = read_data_worker.read_file()
    distinct_authors = set()
    for l in li:
        tmp_name = l[0]
        tmp_author = l[1]
        distinct_authors.add(tmp_author)
        tmp_rating = l[2]
        tmp_reviews = l[3]
        tmp_price = l[4]
        tmp_year = l[5]
        tmp_genre = l[6]
        # db_con_worker.insert_bestsellers(b_name=tmp_name, b_rating=tmp_rating,b_reviews=tmp_reviews, b_price=tmp_price, b_year=tmp_year, b_genre=tmp_genre)

    select_rv = db_con_worker.select_all_bestsellers()
    for s in select_rv:
        logger.info(s)

    for s in distinct_authors:
        logger.info(s)
        logger.info(str(len(distinct_authors)))                 

if __name__ == "__main__":
    main()
