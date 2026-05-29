from enum import StrEnum


class AuthPaths(StrEnum):
    LOGIN = '/auth/login'
    LOGOUT = '/auth/logout'
    CHANGE_PASSWORD = '/auth/password/change'


class ProjectPaths(StrEnum):
    GET_PROJECTS = '/projects'
    CREATE_PROJECT = '/projects'
    GET_PROJECT = '/projects/{id}'
    UPDATE_PROJECT = '/projects/{id}'
    DELETE_PROJECT = '/projects/{id}'
    ADD_SERVICE_TOKEN = '/projects/{id}/service-tokens'
    DELETE_SERVICE_TOKEN = '/projects/{id}/service-tokens/{value}'


class AppPaths(StrEnum):
    GET_APPS = '/projects/{id}/apps'
    CREATE_APP = '/projects/{id}/apps'
    GET_APP = '/projects/{project_id}/apps/{app_id}'
    UPDATE_APP = '/projects/{project_id}/apps/{app_id}'
    DELETE_APP = '/projects/{project_id}/apps/{app_id}'
    CREATE_SIGNATURE = '/projects/{project_id}/apps/{app_id}/signatures'
    DELETE_SIGNATURE = '/projects/{project_id}/apps/{app_id}/signatures/{signature_id}'
