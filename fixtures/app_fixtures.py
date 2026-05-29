import pytest

from general.utils import random_string, random_package_name, convert_to_sha256
from routes.rest.app_routes import success_request_create_app, success_request_get_apps
from routes.rest.project_routes import success_request_create_project, success_request_delete_project


@pytest.fixture()
def random_app_valid_data():
    return {
        'name': random_string(25),
        'package_name': random_package_name(),
        'app_signature': convert_to_sha256(random_string(25))
    }


@pytest.fixture(scope='function')
def new_project_with_app(auth_user_data, random_project_valid_data):
    access_token = auth_user_data['access_token']
    project, _ = success_request_create_project(access_token=access_token)
    project_id = project['data']['project_id']
    app, _ = success_request_create_app(project_id, access_token)
    app_id = success_request_get_apps(project_id, access_token)[0]['data'][0]['id']
    yield project_id, app_id
    success_request_delete_project(project_id, access_token)
