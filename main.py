from utility_controller.app_controlller import AppController
from utility_logs.app_logger import Logger
import json

logger = Logger().get()


def main():
    logger.info("* Main, logs: utility_logs/logs.log")
    logger.info(
        "** When done, set [handler_consoleHandler], level=ERROR, it is now level=INFO. So all that goes to file does also go to std out ")
    app_ctrl = AppController()
    # app_ctrl.ctrl_insert_to_bestsellers()
    # app_ctrl.ctrl_select_all_bestsellers()
    # app_ctrl.ctrl_insert_authors()
    # app_ctrl.ctrl_select_inner_join_bestsellers_authors()
    app_ctrl.ctrl_create_or_check_view_bestsellers_authors()
    app_ctrl.ctrl_select_view_BestsellersAndAuthors()


if __name__ == "__main__":
    main()
