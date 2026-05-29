import pytest

from general.utils import random_email, random_password
from routes.rest.auth_routes import success_request_login, success_request_logout
from config import PUSH_CONSOLE_USER, PUSH_CONSOLE_PASSWORD, PUSH_CONSOLE_USER_ID


@pytest.fixture()
def random_user_data():
    return {
        'email': random_email(),
        'password': random_password()
    }


@pytest.fixture()
def valid_user_data():
    return {
        'email': PUSH_CONSOLE_USER,
        'password': PUSH_CONSOLE_PASSWORD
    }


@pytest.fixture()
def user_id():
    return PUSH_CONSOLE_USER_ID


@pytest.fixture(scope='function')
def auth_user_data():
    response, _ = success_request_login()
    access_token = response['data']['access_token']
    yield response['data']
    success_request_logout(access_token)
