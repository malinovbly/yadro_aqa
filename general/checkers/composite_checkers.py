from http import HTTPStatus

from general.checkers.general_checkers import check_rest_response, general_checker
from general.checkers.postgres_checkers import check_postgres_project_data_by_user_id, check_postgres_app_exists
from general.checkers.rabbit_checkers import check_rabbit_event
from general.checkers.redis_checkers import check_redis_project_data, check_redis_app_exists_in_list
from test_data.enums import ResponseStatus
from test_data.msg_codes import ProjectMsgCodes, AppMsgCodes
from test_data.rabbitmq_events import RabbitEvent


def composite_success_create_project_checker(
        response, status_code, rabbit_queue, auth_user_id, project_name):
    """
    Check success create project:
      - REST response
      - Postgres project data
      - Rabbitmq sync event
      - Redis project data
    """

    general_checker(actual=status_code, expected=HTTPStatus.CREATED)

    check_rest_response(
        response=response,
        msg_code=ProjectMsgCodes.push_console_project_successful_created,
        status=ResponseStatus.OK
    )

    project_id = response['data']['project_id']
    expected = {
        'creator_id': auth_user_id,
        'id': project_id,
        'name': project_name
    }

    check_postgres_project_data_by_user_id(
        user_id=auth_user_id,
        expected=expected,
        project_id=project_id
    )

    check_rabbit_event(
        project_id=project_id,
        queue_name=rabbit_queue,
        expected_event_type=RabbitEvent.SyncCreateProjectSubject
    )

    check_redis_project_data(
        project_id=project_id,
        expected=expected
    )


def composite_unsuccess_create_project_checker(
        response, auth_user_id, project_name, msg_code):
    """
    Check unsuccess create project:
      - REST response
      - Postgres project data is None
    """

    check_rest_response(
        response=response,
        msg_code=msg_code,
        status=ResponseStatus.ERROR
    )

    check_postgres_project_data_by_user_id(
        user_id=auth_user_id,
        expected={},
        project_name=project_name,
    )


def composite_success_create_app_checker(
        response, project_id, app_name):
    """
    Check success create app:
      - REST response
      - Postgres app data
      - Redis app data
    """

    check_rest_response(
        response=response,
        msg_code=AppMsgCodes.push_console_app_successful_created,
        status=ResponseStatus.OK
    )

    check_postgres_app_exists(
        project_id=project_id,
        expected=True,
        name=app_name
    )

    check_redis_app_exists_in_list(
        project_id=project_id,
        app_name=app_name,
        expected=True
    )
