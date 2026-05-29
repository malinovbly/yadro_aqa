import pytest

from general.utils import random_string
from routes.rest.project_routes import (success_request_create_project,
                                        success_request_delete_project,
                                        success_request_get_projects,
                                        success_delete_all_projects)


@pytest.fixture()
def random_project_valid_data():
    return {'name': random_string()}


@pytest.fixture(scope='function')
def new_project(auth_user_data, random_project_valid_data):
    name = random_project_valid_data['name']
    access_token = auth_user_data['access_token']
    response, _ = success_request_create_project(name, access_token)
    project_id = response['data']['project_id']
    yield project_id, name
    success_request_delete_project(project_id, access_token)


@pytest.fixture(scope='function')
def project_cleanup(auth_user_data):
    projects_to_delete = []
    access_token = auth_user_data['access_token']

    yield projects_to_delete

    for project_id in projects_to_delete:
        success_request_delete_project(project_id, access_token)


@pytest.fixture(scope='function')
def projects_count(auth_user_data):
    response, _ = success_request_get_projects(auth_user_data['access_token'])
    projects_cnt = len(response['data'])
    return projects_cnt


@pytest.fixture(scope='function')
def delete_all_projects_after_function():
    yield
    success_delete_all_projects()
