from utility_controller.app_controlller import AppController
from utility_logs.app_logger import Logger
import json

logger = Logger().get()


def main():
    # root = tk.Tk()
    # root.geometry("500x200")
    # app = Application(master=root)
    # app.mainloop()
    logger.info("* Main, logs: utility_logs/logs.log")
    logger.info(
        "** When done, set [handler_consoleHandler], level=ERROR, it is now level=INFO. So all that goes to file does also go to std out ")
    app_ctrl = AppController()

    # Flow of order
    # NOTE 1 Create the tables, user ande grant access directly in SQL SERVER
    # NOTE 2 Create the procedure for insert in test
    # app_ctrl.create_or_check_procedure_insert_bestsellers()
    # NOTE 3 Read in the bestsellers excel downloaded from kaggle just as it is, no alter it, insert both or just one table
    # app_ctrl.ctrl_procedure_insert_bestsellers()
    # NOTE 4 Get all
    # app_ctrl.ctrl_select_all_bestsellers()
    # app_ctrl.ctrl_select_view_BestsellersAndAuthors_order_by_rating()
    # NOTE 4.1 Join both authors and bestsellers
    # app_ctrl.ctrl_select_inner_join_bestsellers_authors()
    # NOTE 4.2 Create a view of of 4.1
    # app_ctrl.ctrl_create_or_check_view_bestsellers_authors()
    # NOTE 5 Get data from the view
    # app_ctrl.ctrl_select_view_BestsellersAndAuthors()

    # NOTE 6 Update prod schema with the bestsellers data
    # app_ctrl.create_or_check_procedure_insert_bestsellers_prod()
    # NOTE 6.1 Read in the bestsellers excel downloaded from kaggle just as it is, no alter it, insert both or just one table
    # app_ctrl.ctrl_procedure_insert_bestsellers_prod()
    # NOTE 6.2
    # app_ctrl.ctrl_create_or_check_view_bestsellers_authors_prod()
    

    # TODO 1: Refactor, organize, test **** prod in class, steps and sequence, use this just for make tables and insert data, ETL"
    # TODO 2: When above is done, then you can dive into more advanced stuff"
    # TODO 3: Load other Kaggle data and repeat TODO 2"


if __name__ == "__main__":
    main()
    logger.info("*** Main started, alter loglevel for handler_consoleHandler when done")

