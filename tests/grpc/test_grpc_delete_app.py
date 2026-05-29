import allure
import pytest

from general.checkers.general_checkers import general_checker
from general.checkers.postgres_checkers import check_postgres_app_exists
from general.utils import random_uuid4
from routes.grpc.app_routes import grpc_request_delete_app
from test_data.enums import GrpcErrorCodes


#region Positive tests

@allure.step('Test success grpc delete app')
def test_success_grpc_delete_app(auth_user_data, new_project_with_app):
    message = {
        'project_id': new_project_with_app[0],
        'app_id': new_project_with_app[1],
    }

    response = grpc_request_delete_app(
        access_token=auth_user_data['access_token'],
        message=message
    )

    general_checker(actual=response['success'], expected={})

    check_postgres_app_exists(
        project_id=new_project_with_app[0],
        expected=False,
        app_id=new_project_with_app[1],
    )

#endregion

#region Negative tests

@allure.step('Test unsuccess grpc delete app bad app_id')
@pytest.mark.parametrize(
    'bad_app_id, error', [
        (random_uuid4(), GrpcErrorCodes.NOT_FOUND),
        ('', GrpcErrorCodes.BAD_REQUEST),
        (None, GrpcErrorCodes.BAD_REQUEST),
    ]
)
def test_unsuccess_grpc_delete_app_bad_app_id(auth_user_data, new_project_with_app, bad_app_id, error):
    message = {
        'project_id': new_project_with_app[0],
        'app_id': bad_app_id,
    }

    response = grpc_request_delete_app(
        access_token=auth_user_data['access_token'],
        message=message
    )

    general_checker(actual=response.get('error', {}).get('code'), expected=error)

    check_postgres_app_exists(
        project_id=new_project_with_app[0],
        expected=True,
        app_id=new_project_with_app[1],
    )


@allure.step('Test unsuccess grpc delete app bad project_id')
@pytest.mark.parametrize(
    'bad_project_id, error', [
        (random_uuid4(), GrpcErrorCodes.NOT_FOUND),
        ('', GrpcErrorCodes.BAD_REQUEST),
        (None, GrpcErrorCodes.BAD_REQUEST),
    ]
)
def test_unsuccess_grpc_delete_app_bad_project_id(auth_user_data, new_project_with_app, bad_project_id, error):
    message = {
        'project_id': bad_project_id,
        'app_id': new_project_with_app[1],
    }

    response = grpc_request_delete_app(
        access_token=auth_user_data['access_token'],
        message=message
    )

    general_checker(actual=response.get('error', {}).get('code'), expected=error)

    check_postgres_app_exists(
        project_id=new_project_with_app[0],
        expected=True,
        app_id=new_project_with_app[1],
    )

#endregion
