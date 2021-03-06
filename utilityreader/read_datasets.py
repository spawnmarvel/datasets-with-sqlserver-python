from csv import reader
from utilitylogs.app_logger import Logger

logger = Logger().get()


class ReadDataSet:

    def __init__(self):
        pass

    def read_file(self, file_with_data):
        li = []
        c = 0
        logger.info("Read file")
        try:
            with open(file_with_data, "r", encoding="utf-8") as fi:
                csv_reader = reader(fi)
                for row in csv_reader:
                    if c == 0:
                        # We do not need the header
                        pass
                    else:
                        li.append(row)
                    c = c + 1
            logger.info("Appended " + str(c) + " rows")
            return li
        except Exception as e:
            print(e)
