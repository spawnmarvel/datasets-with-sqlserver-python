from csv import reader
from utility_logs.app_logger import Logger

logger = Logger().get()


class ReadDataSet:

    def __init__(self):
        pass
    
    def read_file(self):
        li = []
        c = 0
        logger.info("Read file")
        try:
            with open("./kaggle-datasets/bestsellers with categories.csv", "r", encoding="utf-8") as fi:
                csv_reader = reader(fi)
                for row in csv_reader:
                    li.append(row)
                    c = c +1
            logger.info("Appended " + str(c) + " rows")
        except Exception as e:
            print(e)
