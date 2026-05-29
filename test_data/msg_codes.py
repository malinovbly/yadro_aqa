from enum import StrEnum


class CommonMsgCodes(StrEnum):
    general_bad_request_error = 'general_bad_request_error'
    general_bad_token = 'general_bad_token'
    general_unauthorized = 'general_unauthorized'
    go_validation = 'go_validation'
    general_internal = 'general_internal'


class ProjectMsgCodes(StrEnum):
    push_console_projects_successful_getting = 'push_console_projects_successful_getting'
    push_console_project_successful_created = 'push_console_project_successful_created'
    test_course_project_already_exists = 'test_course_project_already_exists'


class AppMsgCodes(StrEnum):
    push_console_app_already_exists = 'push_console_app_already_exists'
    push_console_apps_successful_getting = 'push_console_apps_successful_getting'
    test_course_project_not_found = 'test_course_project_not_found'
    push_console_project_not_found = 'push_console_project_not_found'
    push_console_app_successful_created = 'push_console_app_successful_created'
