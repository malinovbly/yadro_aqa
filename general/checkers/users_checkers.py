import allure

from .general_checkers import check_all_dict_values_are_equal


@allure.step('Check user data')
def check_user_data(response: dict, data_from_db: dict):
    check_all_dict_values_are_equal(response, data_from_db)
