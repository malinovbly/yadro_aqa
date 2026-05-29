from http import HTTPStatus, HTTPMethod

import allure

from routes.rest.auth_routes import get_access_token
from general.utils import make_url, make_auth_header, random_string
from general.paths.api_paths import ProjectPaths
from general.request_wrappers.rest_wrapper import make_rest_request
from models.pydantic.rest.common_models import BaseResponseModel
from models.pydantic.rest.project_models import CreateProjectModel, GetProjectModel, GetProjectsModel


#region Success requests

def success_delete_all_projects():
    while True:
        projects, _ = success_request_get_projects()['data']
        if len(projects) == 0:
            break
        for project in projects:
            pr_id = project['project_id']
            success_request_delete_project(pr_id)


@allure.step('Successful request GET Get projects')
def success_request_get_projects(
        access_token: str = None, pydantic_model=GetProjectsModel):
    url = make_url(ProjectPaths.GET_PROJECTS)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    return make_rest_request(
        method=HTTPMethod.GET,
        url=url,
        headers=headers,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request POST Create project')
def success_request_create_project(
        name: str = None, access_token: str = None,
        pydantic_model=CreateProjectModel):
    url = make_url(ProjectPaths.CREATE_PROJECT)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    name = random_string(10) if name is None else name
    request_body = {
        'name': name
    }

    return make_rest_request(
        method=HTTPMethod.POST,
        url=url,
        headers=headers,
        json=request_body,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request GET Get project')
def success_request_get_project(
        project_id: str, access_token: str = None,
        pydantic_model=GetProjectModel):
    url = make_url(ProjectPaths.GET_PROJECT, id=project_id)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    return make_rest_request(
        method=HTTPMethod.GET,
        url=url,
        headers=headers,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request PUT Update project')
def success_request_update_project(
        project_id: str, new_name: str = None, access_token: str = None, pydantic_model=BaseResponseModel):
    url = make_url(ProjectPaths.UPDATE_PROJECT, id=project_id)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    new_name = random_string(10) if new_name is None else new_name
    request_body = {
        'name': new_name
    }

    return make_rest_request(
        method=HTTPMethod.PUT,
        url=url,
        headers=headers,
        json=request_body,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request DELETE Delete project')
def success_request_delete_project(
        project_id: str, access_token: str = None, pydantic_model=BaseResponseModel):
    url = make_url(ProjectPaths.DELETE_PROJECT, id=project_id)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    return make_rest_request(
        method=HTTPMethod.DELETE,
        url=url,
        headers=headers,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request POST Add service token')
def success_request_add_service_token(
        project_id: str, access_token: str = None, pydantic_model=BaseResponseModel):
    url = make_url(ProjectPaths.ADD_SERVICE_TOKEN, id=project_id)

    headers = make_auth_header(
        get_access_token() if access_token is None else access_token)

    return make_rest_request(
        method=HTTPMethod.POST,
        url=url,
        headers=headers,
        pydantic_model=pydantic_model
    )


@allure.step('Successful request DELETE Delete service token')
def success_request_delete_service_token(
        project_id: str, service_token: str, access_token: str = None, pydantic_model=BaseResponseModel):
    url = make_url(ProjectPaths.DELETE_SERVICE_TOKEN, id=project_id, value=service_token)

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

@allure.step('Unsuccessful request POST Create project')
def unsuccess_request_create_project(access_token: str, request_body: dict):
    url = make_url(ProjectPaths.CREATE_PROJECT)
    headers = make_auth_header(access_token)

    return make_rest_request(
        method=HTTPMethod.POST,
        url=url,
        headers=headers,
        json=request_body
    )


@allure.step('Unsuccessful request GET Get projects')
def unsuccess_request_get_projects(access_token: str):
    url = make_url(ProjectPaths.GET_PROJECTS)
    headers = make_auth_header(access_token)

    return make_rest_request(
        method=HTTPMethod.GET,
        url=url,
        headers=headers,
    )

#endregion
