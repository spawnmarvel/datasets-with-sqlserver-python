
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
            print(p)
            logger.info("Succsess retrieved password")
            return p
    except Exception as e:
        logger.error(e)
        logger.error("Failed to retrieved password")

def main():
    logger.info("Main")
    db = "DataSetsDb" 
    user = "misp"
    p = read_keyvault()
    db_con_worker = DbConnector(database=db, db_username=user, db_password=p)
    read_data_worker = ReadDataSet()
    db_con_worker.get_all_bestsellers()
    read_data_worker.read_file()

if __name__ == "__main__":
    main()
