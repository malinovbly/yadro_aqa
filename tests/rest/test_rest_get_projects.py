from http import HTTPStatus

import allure
import pytest

from general.checkers.general_checkers import check_rest_response, general_checker
from general.checkers.postgres_checkers import check_postgres_project_exists
from routes.rest.project_routes import (success_request_get_projects,
                                        unsuccess_request_get_projects)
from test_data.enums import ResponseStatus
from test_data.msg_codes import ProjectMsgCodes, CommonMsgCodes


#region Positive tests

@allure.step('Test success get projects')
def test_success_get_projects(auth_user_data):
    response, _ = success_request_get_projects(
        access_token=auth_user_data['access_token'],
    )

    check_rest_response(
        response=response,
        msg_code=ProjectMsgCodes.push_console_projects_successful_getting,
        status=ResponseStatus.OK
    )


@allure.step('Test success get projects new project in response')
def test_success_get_projects_new_project_in_response(auth_user_data, new_project):
    response, _ = success_request_get_projects(
        access_token=auth_user_data['access_token'],
    )

    check_rest_response(
        response=response,
        msg_code=ProjectMsgCodes.push_console_projects_successful_getting,
        status=ResponseStatus.OK
    )

    check_postgres_project_exists(
        user_id=auth_user_data['user_id'], expected=True, project_name=new_project[1])

#endregion

# region Negative tests

@allure.step('Test unsuccess get projects bad access token')
@pytest.mark.parametrize(
    'bad_access_token, expected_status_code, expected_msg_code', [
        ('access_token', HTTPStatus.UNAUTHORIZED, CommonMsgCodes.general_bad_token),
        ('', HTTPStatus.UNAUTHORIZED, CommonMsgCodes.general_unauthorized)
    ]
)
def test_unsuccess_get_projects_bad_access_token(
        bad_access_token, expected_status_code, expected_msg_code):
    response, status_code = unsuccess_request_get_projects(access_token=bad_access_token)

    general_checker(actual=status_code, expected=expected_status_code)
    check_rest_response(
        response=response,
        msg_code=expected_msg_code,
        status=ResponseStatus.ERROR
    )

#endregion
