
import utility_db.db_connector as db_con
import utility_reader.read_datasets as read_data
from utility_logs.app_logger import Logger

logger = Logger().get()
def main():
    logger.info("Main")
    # db_con.get_version()
    db_con.get_all_bestsellers()
    read_data.read_file()

if __name__ == "__main__":
    main()
