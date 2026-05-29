from http import HTTPMethod, HTTPStatus

import allure

from config import PUSH_CONSOLE_USER, PUSH_CONSOLE_PASSWORD
from general.paths.api_paths import AuthPaths
from general.request_wrappers.rest_wrapper import make_rest_request
from general.utils import make_url, make_auth_header, random_password
from models.pydantic.rest.common_models import BaseResponseModel
from models.pydantic.rest.users_models import GetLoginModel


def get_access_token():
    response, status_code = success_request_login()
    access_token = response['data']['access_token']
    return access_token


@allure.step('Successful request POST Login')
def success_request_login(pydantic_model=GetLoginModel):
    url = make_url(AuthPaths.LOGIN)

    request_body = {
        'email': PUSH_CONSOLE_USER,
        'password': PUSH_CONSOLE_PASSWORD
    }

    return make_rest_request(
        method=HTTPMethod.POST,
        url=url,
        json=request_body,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request POST Logout')
def success_request_logout(access_token: str, pydantic_model=BaseResponseModel):
    url = make_url(AuthPaths.LOGOUT)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    return make_rest_request(
        method=HTTPMethod.POST,
        url=url,
        headers=headers,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request POST Change password')
def success_request_change_password(
        access_token: str, new_password: str = None, pydantic_model=BaseResponseModel):
    url = make_url(AuthPaths.CHANGE_PASSWORD)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    new_password = random_password(20) if new_password is None else new_password
    request_body = {
        'old_password': PUSH_CONSOLE_PASSWORD,
        'new_password': new_password
    }

    return make_rest_request(
        method=HTTPMethod.POST,
        url=url,
        headers=headers,
        json=request_body,
        pydantic_model=pydantic_model
    )
