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
    # na app_ctrl.ctrl_insert_to_bestsellers()
    # fix app_ctrl.ctrl_select_all_bestsellers()
    # na app_ctrl.ctrl_insert_authors()
    # fix app_ctrl.ctrl_select_inner_join_bestsellers_authors()
    # fix app_ctrl.ctrl_create_or_check_view_bestsellers_authors()
    # fix app_ctrl.ctrl_select_view_BestsellersAndAuthors()
    # fic app_ctrl.ctrl_select_view_BestsellersAndAuthors_order_by_rating()
    # na app_ctrl.ctrl_insert_select_test_to_prod()
    # delet id 1
    # na app_ctrl.ctrl_delete_bestsellers(1)
    # alter prod b_id 1, rating to 100, was 4.7, and add an extra row b_id 551 with dummy data, does merge fix it, update 1 and delete 551?= YES

    # 
    # fix app_ctrl.ctrl_merge_test_to_prod()
    # above insert can be replaced with
    app_ctrl.create_or_check_procedure_insert_bestsellers()


if __name__ == "__main__":
    main()
