from utilitycontroller.app_controlller import AppController
from utilitylogs.app_logger import Logger
import json

logger = Logger().get()


def main():
    # root = tk.Tk()
    # root.geometry("500x200")
    # app = Application(master=root)
    # app.mainloop()
    logger.info("*** logs: utility_logs/logs.log")
    logger.info(
        "*** When done, set [handler_consoleHandler], level=ERROR, it is now level=INFO. So all that goes to file does also go to std out ")
    app_ctrl = AppController()

    # **** Test
    # NOTE 1 Create the tables and user, grant access directly in SQL SERVER (files crt_1_tables, crt_user_and_grants)

    # NOTE 2 Create the procedure for insert in test
    # app_ctrl.create_or_check_procedure_insert_bestsellers_test()

    # NOTE 3 Read in the bestsellers excel downloaded from kaggle just as it is, do not alter it
    # app_ctrl.ctrl_procedure_insert_bestsellers_test()

    # NOTE 4 Data operations
    # app_ctrl.ctrl_select_all_bestsellers_test()
    # app_ctrl.ctrl_select_inner_join_bestsellers_authors_test()

    # NOTE 4.1 Create a view of of NOTE 4 inner join
    # app_ctrl.ctrl_create_or_check_view_bestsellers_authors_test()
    
    # NOTE 4.2 Data operations
    # app_ctrl.ctrl_select_view_bestsellers_and_authors_test()
    # app_ctrl.ctrl_select_view_bestsellers_and_authors_order_by_rating_test()

    # **** Prod
    # NOTE 1 Grant access directly in SQL SERVER same as done in step Test step 1

    # NOTE 2 Create the procedure for insert in prod
    # app_ctrl.create_or_check_procedure_insert_bestsellers_prod()

    # NOTE 3 Read in the bestsellers excel downloaded from kaggle just as it is, do not alter it
    # app_ctrl.ctrl_procedure_insert_bestsellers_prod()

    # NOTE 4 Create a view of both tables 
    # app_ctrl.ctrl_create_or_check_view_bestsellers_authors_prod()

    # NOTE 4.2 Data operations
    # app_ctrl.ctrl_select_view_bestsellers_and_authors_prod()
    app_ctrl.ctrl_select_view_bestsellers_and_authors_order_by_rating_test()

    # NOTE 5

    # TODO 1: Refactor 50 done, check https://www.python.org/dev/peps/pep-0008/ naming conventions "
    # TODO 2: When above is done, then you can dive into more advanced stuff"
    # TODO 3: Load other Kaggle data and repeat TODO 2"


if __name__ == "__main__":
    logger.info("*** Main started, alter loglevel for handler_consoleHandler when done")
    main()

