from utility_controller.app_controlller import AppController
from utility_logs.app_logger import Logger
import json

logger = Logger().get()


def main():
    logger.info("* Main, logs: utility_logs/logs.log")
    logger.info("** When done, set [handler_consoleHandler], level=ERROR, it is now level=INFO. So all that goes to file does also go to std out ")
    app_ctrl = AppController()
    app_ctrl.read_keyvault()
    # app_ctrl.insert_to_bestsellers()
    # app_ctrl.select_from_bestsellers()
    # app_ctrl.insert_to_authors()
    app_ctrl.select_from_inner_join_bestsellers_authors()


if __name__ == "__main__":
    main()
