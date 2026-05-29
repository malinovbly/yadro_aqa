from http import HTTPStatus, HTTPMethod

import allure

from .auth_routes import get_access_token
from general.paths.api_paths import AppPaths
from general.request_wrappers.rest_wrapper import make_rest_request
from general.utils import (make_url,
                           make_auth_header,
                           random_string,
                           random_package_name,
                           convert_to_sha256)
from models.pydantic.rest.common_models import BaseResponseModel
from models.pydantic.rest.app_models import GetAppModel, GetAppsModel


#region Success requests

@allure.step('Successful request GET Get apps')
def success_request_get_apps(
        project_id: str, access_token: str = None, pydantic_model=GetAppsModel):
    url = make_url(AppPaths.GET_APPS, id=project_id)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    return make_rest_request(
        method=HTTPMethod.GET,
        url=url,
        headers=headers,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request POST Create app')
def success_request_create_app(
        project_id: str,
        access_token: str = None,
        request_body: dict = None,
        name: str = None,
        package_name: str = None,
        app_signature: str = None,
        pydantic_model=BaseResponseModel
):
    url = make_url(AppPaths.CREATE_APP, id=project_id)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    if request_body is None:
        request_body = {
            'name': name if name is not None else random_string(25),
            'package_name': package_name if package_name is not None else random_package_name(),
            'app_signature': app_signature if app_signature is not None else convert_to_sha256(random_string(25))
        }

    return make_rest_request(
        method=HTTPMethod.POST,
        url=url,
        headers=headers,
        json=request_body,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request GET Get app')
def success_request_get_app(
        project_id: str, app_id: str, access_token: str = None, pydantic_model=GetAppModel):
    url = make_url(AppPaths.GET_APP, project_id=project_id, app_id=app_id)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    return make_rest_request(
        method=HTTPMethod.GET,
        url=url,
        headers=headers,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request PUT Update app')
def success_request_update_app(
        project_id: str, app_id: str, name: str = None, access_token: str = None, pydantic_model=BaseResponseModel):
    url = make_url(AppPaths.UPDATE_APP, project_id=project_id, app_id=app_id)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    name = random_string(25) if name is None else name
    request_body = {
        'name': name
    }

    return make_rest_request(
        method=HTTPMethod.PUT,
        url=url,
        headers=headers,
        json=request_body,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request DELETE Delete app')
def success_request_delete_app(
        project_id: str, app_id: str, access_token: str = None, pydantic_model=BaseResponseModel):
    url = make_url(AppPaths.DELETE_APP, project_id=project_id, app_id=app_id)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    return make_rest_request(
        method=HTTPMethod.DELETE,
        url=url,
        headers=headers,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request POST Add signature')
def success_request_add_signature(
        project_id: str, app_id: str, value: str = None, access_token: str = None, pydantic_model=BaseResponseModel):
    url = make_url(AppPaths.CREATE_SIGNATURE, project_id=project_id, app_id=app_id)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    value = convert_to_sha256(random_string(10)) if value is None else value
    request_body = {
        'value': value
    }

    return make_rest_request(
        method=HTTPMethod.POST,
        url=url,
        headers=headers,
        json=request_body,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request DELETE Delete signature')
def success_request_delete_signature(
        project_id: str, app_id: str, signature_id: str, access_token: str = None, pydantic_model=BaseResponseModel):
    url = make_url(AppPaths.DELETE_SIGNATURE, project_id=project_id, app_id=app_id, signature_id=signature_id)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    return make_rest_request(
        method=HTTPMethod.DELETE,
        url=url,
        headers=headers,
        pydantic_model=pydantic_model
    )

#endregion

#region Unsuccess requests

@allure.step('Unsuccessful request GET Get apps')
def unsuccess_request_get_apps(project_id: str, access_token: str = None):
    url = make_url(AppPaths.GET_APPS, id=project_id)
    headers = make_auth_header(access_token)

    return make_rest_request(
        method=HTTPMethod.GET,
        url=url,
        headers=headers
    )


@allure.step('Unsuccessful request POST Create app')
def unsuccess_request_create_app(access_token: str, request_body: dict, project_id: str):
    url = make_url(AppPaths.CREATE_APP, id=project_id)
    headers = make_auth_header(access_token)

    return make_rest_request(
        method=HTTPMethod.POST,
        url=url,
        headers=headers,
        json=request_body
    )

#endregion
