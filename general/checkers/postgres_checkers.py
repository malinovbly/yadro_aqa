import allure

from general.helpers.postgres_db_helpers import (get_apps_by_project_id_from_pg,
                                                 get_project_by_user_id_and_project_data_from_pg,
                                                 get_app_by_project_id_and_app_data_from_pg,
                                                 get_apps_count_by_project_id_and_app_data_from_pg)
from general.checkers.general_checkers import check_all_dict_values_are_equal, general_checker


@allure.step('Postgres check project created')
def check_postgres_project_data_by_user_id(user_id, expected, project_id=None, project_name=None):
    response = get_project_by_user_id_and_project_data_from_pg(
        user_id=user_id, project_id=project_id, name=project_name)
    project = {} if len(response) == 0 else response[0]
    check_all_dict_values_are_equal(actual=project, expected=expected)


@allure.step('Postgres check project exists')
def check_postgres_project_exists(user_id, expected, project_id=None, project_name=None):
    response = get_project_by_user_id_and_project_data_from_pg(
        user_id=user_id, project_id=project_id, name=project_name)
    actual = len(response) == 1
    general_checker(actual=actual, expected=expected)


@allure.step('Postgres check app exists')
def check_postgres_app_exists(
        project_id, expected, app_id=None, name=None, package_name=None):
    response = get_app_by_project_id_and_app_data_from_pg(
        project_id=project_id, app_id=app_id, name=name, package_name=package_name)
    actual = len(response) == 1
    general_checker(actual=actual, expected=expected)


@allure.step('Postgres check app count')
def check_postgres_app_count(project_id, expected, name=None, package_name=None):
    apps_cnt = get_apps_count_by_project_id_and_app_data_from_pg(
        project_id=project_id, name=name, package_name=package_name)
    general_checker(actual=apps_cnt, expected=expected)
