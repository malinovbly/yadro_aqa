from enum import StrEnum


class AuthPaths(StrEnum):
    LOGIN = '/push-console/api/v1/auth/login'
    LOGOUT = '/push-console/api/v1/auth/logout'
    CHANGE_PASSWORD = '/push-console/api/v1/auth/password/change'


class ProjectPaths(StrEnum):
    GET_PROJECTS = '/push-console/api/v1/projects'
    CREATE_PROJECT = '/push-console/api/v1/projects'
    GET_PROJECT = '/push-console/api/v1/projects/{id}'
    UPDATE_PROJECT = '/push-console/api/v1/projects/{id}'
    DELETE_PROJECT = '/push-console/api/v1/projects/{id}'
    ADD_SERVICE_TOKEN = '/push-console/api/v1/projects/{id}/service-tokens'
    DELETE_SERVICE_TOKEN = '/push-console/api/v1/projects/{id}/service-tokens/{value}'


class AppPaths(StrEnum):
    GET_APPS = '/push-console/api/v1/projects/{id}/apps'
    CREATE_APP = '/push-console/api/v1/projects/{id}/apps'
    GET_APP = '/push-console/api/v1/projects/{project_id}/apps/{app_id}'
    UPDATE_APP = '/push-console/api/v1/projects/{project_id}/apps/{app_id}'
    DELETE_APP = '/push-console/api/v1/projects/{project_id}/apps/{app_id}'
    CREATE_SIGNATURE = '/push-console/api/v1/projects/{project_id}/apps/{app_id}/signatures'
    DELETE_SIGNATURE = '/push-console/api/v1/projects/{project_id}/apps/{app_id}/signatures/{signature_id}'
