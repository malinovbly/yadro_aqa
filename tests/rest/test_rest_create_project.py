from http import HTTPStatus

import allure
import pytest

from general.checkers.composite_checkers import (composite_success_create_project_checker,
                                                 composite_unsuccess_create_project_checker)
from general.checkers.general_checkers import check_rest_response, general_checker
from general.checkers.postgres_checkers import (check_postgres_project_data_by_user_id,
                                                check_postgres_project_exists)
from routes.rest.project_routes import (success_request_create_project,
                                        unsuccess_request_create_project)
from test_data.enums import ResponseStatus
from test_data.project_test_data import project_test_data
from test_data.msg_codes import CommonMsgCodes, ProjectMsgCodes


#region Positive tests

@allure.step('Test success create project valid name length')
@pytest.mark.xfail(reason='Redis key does not appear after POST request')
@pytest.mark.parametrize('project_specific_valid_length_name',
                         project_test_data.create_valid_length_names())
def test_success_create_project_valid_name_length(
        auth_user_data, project_cleanup, sync_rabbit_queue, project_specific_valid_length_name):
    name = project_specific_valid_length_name

    response, status_code = success_request_create_project(
        name=name,
        access_token=auth_user_data['access_token'],
    )

    try:
        project_cleanup.append(response['data']['project_id'])
    except KeyError:
        pass

    composite_success_create_project_checker(
        response=response,
        status_code=status_code,
        rabbit_queue=sync_rabbit_queue,
        auth_user_id=auth_user_data['user_id'],
        project_name=name
    )


@allure.step('Test success create project symbols only name')
@pytest.mark.xfail(reason='Redis key does not appear after POST request')
def test_success_create_project_symbols_only_name(
        auth_user_data, project_cleanup, sync_rabbit_queue):
    name = project_test_data.create_symbols_only_name()

    response, status_code = success_request_create_project(
        name=name,
        access_token=auth_user_data['access_token'],
    )

    try:
        project_cleanup.append(response['data']['project_id'])
    except KeyError:
        pass

    composite_success_create_project_checker(
        response=response,
        status_code=status_code,
        rabbit_queue=sync_rabbit_queue,
        auth_user_id=auth_user_data['user_id'],
        project_name=name
    )


@allure.step('Test success create project cyrillic name')
@pytest.mark.xfail(reason='Redis key does not appear after POST request')
@pytest.mark.parametrize('project_cyrillic_name', project_test_data.create_cyrillic_names())
def test_success_create_project_cyrillic_name(
        auth_user_data, project_cleanup, sync_rabbit_queue, project_cyrillic_name):
    name = project_cyrillic_name

    response, status_code = success_request_create_project(
        name=name,
        access_token=auth_user_data['access_token'],
    )

    try:
        project_cleanup.append(response['data']['project_id'])
    except KeyError:
        pass

    composite_success_create_project_checker(
        response=response,
        status_code=status_code,
        rabbit_queue=sync_rabbit_queue,
        auth_user_id=auth_user_data['user_id'],
        project_name=name
    )


@allure.step('Test success create project numeric name')
@pytest.mark.xfail(reason='Redis key does not appear after POST request')
@pytest.mark.parametrize('project_numeric_name', project_test_data.create_numeric_names())
def test_success_create_project_numeric_name(
        auth_user_data, project_cleanup, sync_rabbit_queue, project_numeric_name):
    name = project_numeric_name

    response, status_code = success_request_create_project(
        name=name,
        access_token=auth_user_data['access_token'],
    )

    try:
        project_cleanup.append(response['data']['project_id'])
    except KeyError:
        pass

    composite_success_create_project_checker(
        response=response,
        status_code=status_code,
        rabbit_queue=sync_rabbit_queue,
        auth_user_id=auth_user_data['user_id'],
        project_name=name
    )


@allure.step('Test success create project uppercase name')
@pytest.mark.xfail(reason='Redis key does not appear after POST request')
@pytest.mark.parametrize('project_uppercase_name',
                         project_test_data.create_uppercase_names())
def test_success_create_project_uppercase_name(
        auth_user_data, project_cleanup, sync_rabbit_queue, project_uppercase_name):
    name = project_uppercase_name

    response, status_code = success_request_create_project(
        name=name,
        access_token=auth_user_data['access_token'],
    )

    try:
        project_cleanup.append(response['data']['project_id'])
    except KeyError:
        pass

    composite_success_create_project_checker(
        response=response,
        status_code=status_code,
        rabbit_queue=sync_rabbit_queue,
        auth_user_id=auth_user_data['user_id'],
        project_name=name
    )

#endregion

#region Negative tests

@allure.step('Test unsuccess create project invalid name length')
@pytest.mark.parametrize('project_invalid_name_length',
                         project_test_data.create_invalid_length_names())
def test_unsuccess_create_project_invalid_name_length(
        auth_user_data, project_cleanup, project_invalid_name_length):
    name = project_invalid_name_length
    request_body = project_test_data.create_valid_data(name=name)

    response, status_code = unsuccess_request_create_project(
        access_token=auth_user_data['access_token'],
        request_body=request_body
    )

    try:
        project_cleanup.append(response['data']['project_id'])
    except KeyError:
        pass

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    check_rest_response(
        response=response,
        msg_code=CommonMsgCodes.go_validation,
        status=ResponseStatus.ERROR
    )

    check_postgres_project_data_by_user_id(
        user_id=auth_user_data['user_id'],
        expected={},
        project_name=name,
    )


@allure.step('Test unsuccess create project invalid language name')
@pytest.mark.xfail(reason='Creates project but expected 422')
@pytest.mark.parametrize('project_invalid_language_name',
                         project_test_data.create_invalid_language_name())
def test_unsuccess_create_project_invalid_language_name(
        auth_user_data, project_cleanup, project_invalid_language_name):
    name = project_invalid_language_name
    request_body = project_test_data.create_valid_data(name=name)

    response, status_code = unsuccess_request_create_project(
        access_token=auth_user_data['access_token'],
        request_body=request_body
    )

    try:
        project_cleanup.append(response['data']['project_id'])
    except KeyError:
        pass

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    composite_unsuccess_create_project_checker(
        response=response,
        auth_user_id=auth_user_data['user_id'],
        project_name=name,
        msg_code=CommonMsgCodes.go_validation
    )


@allure.step('Test unsuccess create project not unique name')
@pytest.mark.xfail(reason='Returns 500 but expected 409')
def test_unsuccess_create_project_not_unique_name(
        auth_user_data, project_cleanup, new_project):
    name = new_project[1]
    request_body = project_test_data.create_valid_data(name)

    response, status_code = unsuccess_request_create_project(
        access_token=auth_user_data['access_token'],
        request_body=request_body
    )

    try:
        project_cleanup.append(response['data']['project_id'])
    except KeyError, TypeError:
        pass

    general_checker(actual=status_code, expected=HTTPStatus.CONFLICT)
    check_rest_response(
        response=response,
        msg_code=ProjectMsgCodes.test_course_project_already_exists,
        status=ResponseStatus.ERROR
    )

    check_postgres_project_exists(
        user_id=auth_user_data['user_id'], expected=False, project_name=name)


@allure.step('Test unsuccess create project bad access token')
@pytest.mark.parametrize(
    'bad_access_token, expected_status_code, expected_msg_code', [
        ('access_token', HTTPStatus.UNAUTHORIZED, CommonMsgCodes.general_bad_token),
        ('', HTTPStatus.UNAUTHORIZED, CommonMsgCodes.general_unauthorized)
    ]
)
def test_unsuccess_create_project_bad_access_token(
        project_cleanup, bad_access_token, expected_status_code, expected_msg_code):
    request_body = project_test_data.create_valid_data()

    response, status_code = unsuccess_request_create_project(
        access_token=bad_access_token,
        request_body=request_body
    )

    try:
        project_cleanup.append(response['data']['project_id'])
    except KeyError:
        pass

    general_checker(actual=status_code, expected=expected_status_code)
    check_rest_response(
        response=response,
        msg_code=expected_msg_code,
        status=ResponseStatus.ERROR
    )


@allure.step('Test unsuccess create project invalid type')
@pytest.mark.xfail(reason='Returns 500 but expected 422')
@pytest.mark.parametrize('project_invalid_name_type',
                         project_test_data.create_invalid_type_names())
def test_unsuccess_create_project_invalid_name_type(
        auth_user_data, project_cleanup, project_invalid_name_type):
    name = project_invalid_name_type
    request_body = project_test_data.create_valid_data(name)

    response, status_code = unsuccess_request_create_project(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        status_code=HTTPStatus.UNPROCESSABLE_CONTENT
    )

    try:
        project_cleanup.append(response['data']['project_id'])
    except KeyError:
        pass

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    check_rest_response(
        response=response,
        msg_code=CommonMsgCodes.go_validation,
        status=ResponseStatus.ERROR
    )

    auth_user_id = auth_user_data['user_id']
    check_postgres_project_exists(
        user_id=auth_user_id, expected=False, project_name=name)


@allure.step('Test unsuccess create project bad request body')
@pytest.mark.parametrize(
    'bad_request_body, expected_status_code, expected_msg_code', [
        pytest.param(
            project_test_data.create_data_with_unexpected_field(),
            HTTPStatus.BAD_REQUEST,
            CommonMsgCodes.general_bad_request_error,
            marks=pytest.mark.xfail(reason='Returns 201 but expected 400')
        ),
        (
            {},
            HTTPStatus.UNPROCESSABLE_CONTENT,
            CommonMsgCodes.go_validation
        ),
        (
            project_test_data.create_random_data(),
            HTTPStatus.UNPROCESSABLE_CONTENT,
            CommonMsgCodes.go_validation
        ),
    ]
)
def test_unsuccess_create_project_unexpected_field_in_request_body(
        auth_user_data, project_cleanup, bad_request_body, expected_status_code, expected_msg_code):
    response, status_code = unsuccess_request_create_project(
        access_token=auth_user_data['access_token'],
        request_body=bad_request_body
    )

    try:
        project_cleanup.append(response['data']['project_id'])
    except KeyError:
        pass

    general_checker(actual=status_code, expected=expected_status_code)
    check_rest_response(
        response=response,
        msg_code=expected_msg_code,
        status=ResponseStatus.ERROR
    )

    name = next(iter(bad_request_body.values()), '')
    check_postgres_project_exists(
        user_id=auth_user_data['user_id'], expected=False, project_name=name)

#endregion
