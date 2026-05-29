import allure

from general.helpers.redis_db_helpers import (get_projects_item_by_project_id_from_redis,
                                              get_apps_item_by_app_id_from_redis,
                                              get_apps_list_by_project_id_from_redis)
from .general_checkers import check_all_dict_values_are_equal, general_checker


def find_app_in_list(app_list: list, app_name=None):
    app = None
    for item in app_list:
        if item['name'] == app_name:
            app = item
    return app


@allure.step('Redis check')
def check_redis_data(actual, expected):
    if isinstance(expected, dict):
        check_all_dict_values_are_equal(actual, expected)
        return
    if isinstance(expected, int):
        general_checker(actual, expected)


@allure.step('Redis check project created')
def check_redis_project_data(project_id, expected):
    response = get_projects_item_by_project_id_from_redis(project_id)
    check_redis_data(response, expected)


@allure.step('Redis check project exists')
def check_redis_project_exists(project_id, expected):
    response = get_projects_item_by_project_id_from_redis(project_id)
    general_checker(response is not None, expected)


@allure.step('Redis check app data')
def check_redis_app_data(app_id, expected):
    response = get_apps_item_by_app_id_from_redis(app_id)
    check_redis_data(response, expected)


@allure.step('Redis check app exists in list')
def check_redis_app_exists_in_list(project_id, app_name, expected):
    response = get_apps_list_by_project_id_from_redis(project_id)
    app = find_app_in_list(response, app_name)
    general_checker(app is not None, expected)
