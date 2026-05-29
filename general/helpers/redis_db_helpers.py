import allure

from general.clients.redis_db import get_redis_data
from test_data.redis_keys import RedisKeys
from general.utils import make_redis_key


@allure.step('Get value key="projects:item" by project_id from redis')
def get_projects_item_by_project_id_from_redis(project_id):
    key = make_redis_key(RedisKeys.PROJECTS_ITEM, project_id=project_id)
    return get_redis_data(key=key)


@allure.step('Get value key="projects:count:user" by user_id from redis')
def get_projects_count_by_user_id_from_redis(user_id):
    key = make_redis_key(RedisKeys.PROJECTS_COUNT, user_id=user_id)
    return get_redis_data(key=key)


@allure.step('Get value key="apps:item" by app_id from redis')
def get_apps_item_by_app_id_from_redis(app_id):
    key = make_redis_key(RedisKeys.APPS_ITEM, app_id=app_id)
    return get_redis_data(key=key)


@allure.step('Get value key="apps:count:project" by project_id from redis')
def get_apps_count_by_project_id_from_redis(project_id):
    key = make_redis_key(RedisKeys.APPS_COUNT, project_id=project_id)
    return get_redis_data(key=key)


@allure.step('Get value key="apps:list:project" by project_id from redis')
def get_apps_list_by_project_id_from_redis(project_id):
    key = make_redis_key(RedisKeys.APPS_LIST, project_id=project_id)
    return get_redis_data(key=key)
