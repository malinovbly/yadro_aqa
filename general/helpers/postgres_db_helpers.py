import allure

from general.clients.postgres_db import execute_postgres_select_all, execute_postgres_select_count
from general.utils import make_specific_query


@allure.step('Get all projects data by user_id from postgres')
def get_projects_by_user_id_from_pg(user_id):
    query = f"""
        SELECT *
        FROM projects
        WHERE creator_id='{user_id}';
    """
    result = execute_postgres_select_all(query=query)
    return result


@allure.step('Get project data by project_id from postgres')
def get_project_by_user_id_and_project_data_from_pg(user_id, **kwargs):
    """
    Get project by it`s id or name and user_id from postgres

    Args:
        user_id: user id
        **kwargs: project_id / name
    """

    query, params = make_specific_query(
        table='projects', base_column_name='creator_id', base_column_param=user_id, **kwargs)

    result = execute_postgres_select_all(query=query, params=tuple(params))
    return result


@allure.step('Get all apps data by project_id from postgres')
def get_apps_by_project_id_from_pg(project_id):
    query = f"""
        SELECT *
        FROM apps
        WHERE project_id='{project_id}';
    """
    result = execute_postgres_select_all(query=query)
    return result


@allure.step('Get app by it`s data and project_id from postgres')
def get_app_by_project_id_and_app_data_from_pg(project_id, **kwargs):
    """
    Get app by it`s data and project_id from postgres

    Args:
        project_id: project id
        **kwargs: app_id / name / package_name / app_signature
    """

    query, params = make_specific_query(
        table='apps', base_column_name='project_id', base_column_param=project_id, **kwargs)

    result = execute_postgres_select_all(query=query, params=tuple(params))
    return result


@allure.step('Get apps count by app data and project_id from postgres')
def get_apps_count_by_project_id_and_app_data_from_pg(project_id, **kwargs):
    """
    Get apps count by app data and project_id from postgres

    Args:
        project_id: project id
        **kwargs: app_id / name / package_name / app_signature
    """

    query, params = make_specific_query(
        table='apps', base_column_name='project_id', base_column_param=project_id, **kwargs)

    query.replace('*', 'count(1)')

    result = execute_postgres_select_count(query=query, params=tuple(params))
    return result
