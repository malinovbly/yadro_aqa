from http import HTTPStatus

import pytest
import allure

from general.checkers.composite_checkers import composite_success_create_app_checker
from general.checkers.general_checkers import check_rest_response, general_checker
from general.checkers.postgres_checkers import check_postgres_app_exists, check_postgres_app_count
from routes.rest.app_routes import (success_request_create_app,
                                    unsuccess_request_create_app)
from test_data.app_test_data import app_test_data
from test_data.enums import ResponseStatus
from test_data.msg_codes import CommonMsgCodes, AppMsgCodes
from test_data.project_test_data import project_test_data


#region Positive tests

@allure.step('Test success create app valid name length')
@pytest.mark.xfail(reason='Redis key does not appear after POST request')
@pytest.mark.parametrize('app_valid_length_name',
                         app_test_data.create_valid_length_names())
def test_success_create_app_valid_name_length(
        auth_user_data, new_project, app_valid_length_name):
    name = app_valid_length_name
    request_body = app_test_data.create_valid_data(name=name)

    response, _ = success_request_create_app(
        project_id=new_project[0],
        access_token=auth_user_data['access_token'],
        request_body=request_body
    )

    # success_request_get_apps(project_id=new_project[0], access_token=auth_user_data['access_token'])

    composite_success_create_app_checker(
        response=response,
        project_id=new_project[0],
        app_name=name
    )

@allure.step('Test success create app symbols only name')
@pytest.mark.xfail(reason='Redis key does not appear after POST request')
def test_success_create_app_symbols_only_name(auth_user_data, new_project):
    name = app_test_data.create_symbols_only_name()
    request_body = app_test_data.create_valid_data(name=name)

    response, _ = success_request_create_app(
        project_id=new_project[0],
        access_token=auth_user_data['access_token'],
        request_body=request_body
    )

    composite_success_create_app_checker(
        response=response,
        project_id=new_project[0],
        app_name=name
    )


@allure.step('Test success create app cyrillic name')
@pytest.mark.xfail(reason='Redis key does not appear after POST request')
@pytest.mark.parametrize('app_cyrillic_name', app_test_data.create_cyrillic_names())
def test_success_create_app_cyrillic_name(
        auth_user_data, new_project, app_cyrillic_name):
    name = app_cyrillic_name
    request_body = app_test_data.create_valid_data(name=name)

    response, _ = success_request_create_app(
        project_id=new_project[0],
        access_token=auth_user_data['access_token'],
        request_body=request_body
    )

    composite_success_create_app_checker(
        response=response,
        project_id=new_project[0],
        app_name=name
    )


@allure.step('Test success create app numeric name')
@pytest.mark.xfail(reason='Redis key does not appear after POST request')
@pytest.mark.parametrize('app_numeric_name', app_test_data.create_numeric_names())
def test_success_create_app_numeric_name(
        auth_user_data, new_project, app_numeric_name):
    name = app_numeric_name
    request_body = app_test_data.create_valid_data(name=name)

    response, _ = success_request_create_app(
        project_id=new_project[0],
        access_token=auth_user_data['access_token'],
        request_body=request_body
    )

    composite_success_create_app_checker(
        response=response,
        project_id=new_project[0],
        app_name=name
    )


@allure.step('Test success create app uppercase name')
@pytest.mark.xfail(reason='Redis key does not appear after POST request')
@pytest.mark.parametrize('app_uppercase_name',
                         app_test_data.create_uppercase_names())
def test_success_create_app_uppercase_name(
        auth_user_data, new_project, app_uppercase_name):
    name = app_uppercase_name
    request_body = app_test_data.create_valid_data(name=name)

    response, _ = success_request_create_app(
        project_id=new_project[0],
        access_token=auth_user_data['access_token'],
        request_body=request_body
    )

    composite_success_create_app_checker(
        response=response,
        project_id=new_project[0],
        app_name=name
    )

#endregion

#region Negative tests

@allure.step('Test unsuccess create app invalid name length')
@pytest.mark.xfail(reason='Returns push_console_app_successful_created but expected go_validation')
@pytest.mark.parametrize('app_invalid_name_length',
                         app_test_data.create_invalid_length_names())
def test_unsuccess_create_app_invalid_name_length(
        auth_user_data, new_project, app_invalid_name_length):
    name = app_invalid_name_length
    request_body = app_test_data.create_valid_data(name=name)

    response, status_code = unsuccess_request_create_app(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        project_id=new_project[0]
    )

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    check_rest_response(
        response=response,
        msg_code=CommonMsgCodes.go_validation,
        status=ResponseStatus.ERROR
    )

    check_postgres_app_exists(
        project_id=new_project[0],
        expected=False,
        name=name
    )


@allure.step('Test unsuccess create app project id not exist')
def test_unsuccess_create_app_project_id_not_exist(auth_user_data):
    request_body = app_test_data.create_valid_data()
    project_id = project_test_data.random_project_id()

    response, status_code = unsuccess_request_create_app(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        project_id=project_id
    )

    general_checker(actual=status_code, expected=HTTPStatus.NOT_FOUND)
    check_rest_response(
        response=response,
        msg_code=AppMsgCodes.push_console_project_not_found,
        status=ResponseStatus.ERROR
    )


@allure.step('Test unsuccess create app invalid language name')
@pytest.mark.xfail(reason='Returns general_internal but expected go_validation')
def test_unsuccess_create_app_invalid_language_name(
        auth_user_data, new_project):
    name = app_test_data.create_invalid_language_name()
    request_body = app_test_data.create_valid_data(name=name)

    response, status_code = unsuccess_request_create_app(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        project_id=new_project[0]
    )

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    check_rest_response(
        response=response,
        msg_code=CommonMsgCodes.go_validation,
        status=ResponseStatus.ERROR
    )

    check_postgres_app_exists(
        project_id=new_project[0],
        expected=False,
        name=name
    )


@allure.step('Test unsuccess create app invalid package name symbols')
@pytest.mark.parametrize('invalid_package_name',
                         [app_test_data.create_symbols_only_name()])
def test_unsuccess_create_app_invalid_package_name_symbols(
        auth_user_data, new_project, invalid_package_name):
    package_name = invalid_package_name
    request_body = app_test_data.create_valid_data(package_name=package_name)

    response, status_code = unsuccess_request_create_app(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        project_id=new_project[0]
    )

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    check_rest_response(
        response=response,
        msg_code=CommonMsgCodes.go_validation,
        status=ResponseStatus.ERROR
    )

    check_postgres_app_exists(
        project_id=new_project[0],
        expected=False,
        package_name=package_name
    )


@allure.step('Test unsuccess create app package name starts not allowed characters')
@pytest.mark.parametrize('symbol_to_add', ['_', '.', '1'])
def test_unsuccess_create_app_package_name_starts_with_not_allowed_characters(
        auth_user_data, new_project, symbol_to_add):
    package_name = symbol_to_add + app_test_data.create_valid_data()['package_name']
    request_body = app_test_data.create_valid_data(package_name=package_name)

    response, status_code = unsuccess_request_create_app(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        project_id=new_project[0]
    )

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    check_rest_response(
        response=response,
        msg_code=CommonMsgCodes.go_validation,
        status=ResponseStatus.ERROR
    )

    check_postgres_app_exists(
        project_id=new_project[0],
        expected=False,
        package_name=package_name
    )


@allure.step('Test unsuccess create app package name has no periods')
@pytest.mark.xfail(reason='Returns push_console_app_successful_created but expected go_validation')
def test_unsuccess_create_app_package_name_has_no_periods(auth_user_data, new_project):
    package_name = app_test_data.create_valid_data()['name']
    request_body = app_test_data.create_valid_data(package_name=package_name)

    response, status_code = unsuccess_request_create_app(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        project_id=new_project[0]
    )

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    check_rest_response(
        response=response,
        msg_code=CommonMsgCodes.go_validation,
        status=ResponseStatus.ERROR
    )

    check_postgres_app_exists(
        project_id=new_project[0],
        expected=False,
        package_name=package_name
    )


@allure.step('Test unsuccess create app package name has reserved names')
@pytest.mark.xfail(reason='Returns push_console_app_successful_created but expected go_validation')
def test_unsuccess_create_app_package_name_has_reserved_names(auth_user_data, new_project):
    package_name = app_test_data.create_package_name_with_reserved_names()
    request_body = app_test_data.create_valid_data(package_name=package_name)

    response, status_code = unsuccess_request_create_app(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        project_id=new_project[0]
    )

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    check_rest_response(
        response=response,
        msg_code=CommonMsgCodes.go_validation,
        status=ResponseStatus.ERROR
    )

    check_postgres_app_exists(
        project_id=new_project[0],
        expected=False,
        package_name=package_name
    )


@allure.step('Test unsuccess create app bad app signature')
def test_unsuccess_create_bad_app_signature(auth_user_data, new_project):
    app_signature = app_test_data.create_valid_data()['name']
    request_body = app_test_data.create_valid_data(app_signature=app_signature)

    response, status_code = unsuccess_request_create_app(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        project_id=new_project[0]
    )

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    check_rest_response(
        response=response,
        msg_code=CommonMsgCodes.go_validation,
        status=ResponseStatus.ERROR
    )

    check_postgres_app_exists(
        project_id=new_project[0],
        expected=False,
        name=request_body['name']
    )


@allure.step('Test unsuccess create app not unique name or package name')
@pytest.mark.xfail(reason='Returns 500 but expected 409')
@pytest.mark.parametrize('field_to_check', ['name', 'package_name'])
def test_unsuccess_create_app_not_unique_name_or_package_name(auth_user_data, new_project, field_to_check):
    request_body = app_test_data.create_valid_data()
    value = request_body[field_to_check]
    success_request_create_app(
        project_id=new_project[0],
        access_token=auth_user_data['access_token'],
        request_body=request_body,
    )

    request_body = app_test_data.create_valid_data()
    request_body[field_to_check] = value
    response, status_code = unsuccess_request_create_app(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        project_id=new_project[0]
    )

    general_checker(actual=status_code, expected=HTTPStatus.CONFLICT)
    check_rest_response(
        response=response,
        msg_code=AppMsgCodes.push_console_app_already_exists,
        status=ResponseStatus.ERROR
    )

    if field_to_check == 'name':
        check_postgres_app_count(project_id=new_project[0], expected=1, name=value)
    elif field_to_check == 'package_name':
        check_postgres_app_count(project_id=new_project[0], expected=1, package_name=value)


@allure.step('Test unsuccess create app bad access token')
@pytest.mark.parametrize(
    'bad_access_token, expected_msg_code', [
        ('access_token', CommonMsgCodes.general_bad_token),
        ('', CommonMsgCodes.general_unauthorized)
    ]
)
def test_unsuccess_create_app_bad_access_token(
        new_project, bad_access_token, expected_msg_code):
    request_body = app_test_data.create_valid_data()

    response, status_code = unsuccess_request_create_app(
        access_token=bad_access_token,
        request_body=request_body,
        project_id=new_project[0]
    )

    general_checker(actual=status_code, expected=HTTPStatus.UNAUTHORIZED)
    check_rest_response(
        response=response,
        msg_code=expected_msg_code,
        status=ResponseStatus.ERROR
    )

    check_postgres_app_exists(
        project_id=new_project[0],
        expected=False,
        name=request_body['name']
    )


@allure.step('Test unsuccess create app invalid field type')
@pytest.mark.xfail(reason='Returns 500 but expected 422')
@pytest.mark.parametrize('field_to_change', ['name', 'package_name', 'app_signature'])
@pytest.mark.parametrize('invalid_type', app_test_data.create_invalid_type_names())
def test_unsuccess_create_app_invalid_field_type(
        auth_user_data, new_project, field_to_change, invalid_type):
    request_body = app_test_data.create_valid_data()
    request_body[field_to_change] = invalid_type

    response, status_code = unsuccess_request_create_app(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        project_id=new_project[0]
    )

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    check_rest_response(
        response=response,
        msg_code=CommonMsgCodes.go_validation,
        status=ResponseStatus.ERROR
    )

    check_postgres_app_exists(
        project_id=new_project[0],
        expected=False,
        name=request_body['name']
    )


@allure.step('Test unsuccess create app wrong field in request body')
@pytest.mark.xfail(reason='Returns 500 but expected 422')
def test_unsuccess_create_app_wrong_field_in_request_body(auth_user_data, new_project):
    valid_data = app_test_data.create_valid_data()
    invalid_data = app_test_data.create_random_data()
    request_body = valid_data.update(invalid_data)

    response, status_code = unsuccess_request_create_app(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        project_id=new_project[0]
    )

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    check_rest_response(
        response=response,
        msg_code=CommonMsgCodes.go_validation,
        status=ResponseStatus.ERROR
    )

    check_postgres_app_exists(
        project_id=new_project[0],
        expected=False,
        name=request_body['name']
    )


@allure.step('Test unsuccess create app not all fields provided')
@pytest.mark.parametrize('field_to_remove', ['name', 'package_name', 'app_signature'])
def test_unsuccess_create_app_not_all_fields_provided(
        auth_user_data, new_project, field_to_remove):
    request_body = app_test_data.create_valid_data()
    request_body.pop(field_to_remove)

    response, status_code = unsuccess_request_create_app(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        project_id=new_project[0]
    )

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    check_rest_response(
        response=response,
        msg_code=CommonMsgCodes.go_validation,
        status=ResponseStatus.ERROR
    )

    if field_to_remove != 'name':
        check_postgres_app_exists(project_id=new_project[0], expected=False, name=request_body['name'])
    else:
        check_postgres_app_exists(project_id=new_project[0], expected=False, package_name=request_body['package_name'])


@allure.step('Test unsuccess create app empty request body')
def test_unsuccess_create_app_empty_request_body(auth_user_data, new_project):
    request_body = {}

    response, status_code = unsuccess_request_create_app(
        access_token=auth_user_data['access_token'],
        request_body=request_body,
        project_id=new_project[0]
    )

    general_checker(actual=status_code, expected=HTTPStatus.UNPROCESSABLE_CONTENT)
    check_rest_response(
        response=response,
        msg_code=CommonMsgCodes.go_validation,
        status=ResponseStatus.ERROR
    )

#endregion
