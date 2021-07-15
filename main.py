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
    # NOTE 1 Create the tables directly in SQL SERVER
    # NOTE 2
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
    # NOTE 3 Read in the bestsellers excel downloaded from kaggle just as it is, no alter it, insert both or just one table
    # app_ctrl.ctrl_procedure_insert_bestsellers_prod()
    # TODO delet id 1
    # app_ctrl.ctrl_delete_bestsellers(1)
    

    # TODO 7 Merge test.table to prod.table
    # app_ctrl.ctrl_merge_test_to_prod()
    # TODO 8 After merge, alter some row in test and do merge again to verify that it works as it should, (it does btw)
    # TODO 9 Create procedure of merge, yea!!!
    # TODO Get more advanced Kaggle data and do DDL, table, procedure insert, merge test prod and complex query, yea


if __name__ == "__main__":
    main()
