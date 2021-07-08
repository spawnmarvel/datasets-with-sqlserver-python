import logging
from os import path
from logging.config import fileConfig


class Logger:
    def __init__(self):
        log_file_path = path.join(path.dirname(
            path.abspath(__file__)), 'logging_config.ini')
        fileConfig(log_file_path)
        self.logger = logging.getLogger()

    def get(self):
        """ Returns the actual logger from logging module """
        return self.logger