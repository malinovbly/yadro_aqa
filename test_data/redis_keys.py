from enum import StrEnum


class RedisKeys(StrEnum):
    PROJECTS_ITEM = 'projects:item:{project_id}'
    PROJECTS_COUNT = 'projects:count:user:{user_id}'

    APPS_ITEM = 'apps:item:{app_id}'
    APPS_COUNT = 'apps:count:project:{project_id}'
    APPS_LIST = 'apps:list:project:{project_id}'
