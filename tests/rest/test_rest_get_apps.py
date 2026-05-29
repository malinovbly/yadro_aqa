from http import HTTPStatus

import allure
import pytest

from general.checkers.general_checkers import check_rest_response, general_checker
from routes.rest.app_routes import success_request_get_apps, unsuccess_request_get_apps
from test_data.enums import ResponseStatus
from test_data.msg_codes import AppMsgCodes, CommonMsgCodes
from test_data.project_test_data import project_test_data


#region Positive tests

@allure.step('Test success get apps zero count')
def test_success_get_apps_zero_count(auth_user_data, new_project):
    response, status_code = success_request_get_apps(
        project_id=new_project[0],
        access_token=auth_user_data['access_token']
    )

    general_checker(actual=status_code, expected=HTTPStatus.OK)
    check_rest_response(
        response=response,
        msg_code=AppMsgCodes.push_console_apps_successful_getting,
        status=ResponseStatus.OK
    )

    general_checker(actual=len(response['data']), expected=0)


@allure.step('Test success get apps count 1')
def test_success_get_apps_count_one(auth_user_data, new_project_with_app):
    response, status_code = success_request_get_apps(
        project_id=new_project_with_app[0],
        access_token=auth_user_data['access_token'],
    )

    general_checker(actual=status_code, expected=HTTPStatus.OK)
    check_rest_response(
        response=response,
        msg_code=AppMsgCodes.push_console_apps_successful_getting,
        status=ResponseStatus.OK
    )

    general_checker(actual=len(response['data']), expected=1)

#endregion

#region Negative tests

@allure.step('Test unsuccess get apps project not exists')
def test_unsuccess_get_apps_project_not_exists(auth_user_data):
    response, status_code = unsuccess_request_get_apps(
        project_id=project_test_data.random_project_id(),
        access_token=auth_user_data['access_token']
    )

    general_checker(actual=status_code, expected=HTTPStatus.NOT_FOUND)
    check_rest_response(
        response=response,
        msg_code=AppMsgCodes.push_console_project_not_found,
        status=ResponseStatus.ERROR
    )


@allure.step('Test unsuccess get apps bad access token')
@pytest.mark.parametrize(
    'bad_access_token, expected_msg_code', [
        ('access_token', CommonMsgCodes.general_bad_token),
        ('', CommonMsgCodes.general_unauthorized)
    ]
)
def test_unsuccess_get_apps_bad_access_token(
        new_project_with_app, bad_access_token, expected_msg_code):
    response, status_code = unsuccess_request_get_apps(
        project_id=new_project_with_app[0],
        access_token=bad_access_token
    )

    general_checker(actual=status_code, expected=HTTPStatus.UNAUTHORIZED)
    check_rest_response(
        response=response,
        msg_code=expected_msg_code,
        status=ResponseStatus.ERROR
    )

#endregion
