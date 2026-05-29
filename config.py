import json
import os


def load_config(config_file: str):
    config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), config_file)
    with open(config_file) as f:
        return json.load(f)


def get_config():
    try:
        return load_config('config_local.json')
    except FileNotFoundError:
        return load_config('config.json')


config = get_config()

PUSH_CONSOLE_USER = os.getenv('PUSH_CONSOLE_USER', config['PUSH_CONSOLE_USER'])
PUSH_CONSOLE_PASSWORD = os.getenv('PUSH_CONSOLE_PASSWORD', config['PUSH_CONSOLE_PASSWORD'])
PUSH_CONSOLE_USER_ID = os.getenv('PUSH_CONSOLE_USER_ID', config['PUSH_CONSOLE_USER_ID'])

BASE_URL = config['BASE_URL']
GRPC_HOST = config['GRPC_HOST']

PUSH_CONSOLE_POSTGRES_DB = {
    'host': config['PUSH_CONSOLE_POSTGRES_HOST'],
    'port': config['PUSH_CONSOLE_POSTGRES_PORT'],
    'database': config['PUSH_CONSOLE_POSTGRES_DATABASE'],
    'user': config['PUSH_CONSOLE_POSTGRES_USER'],
    'password': config['PUSH_CONSOLE_POSTGRES_PASSWORD']
}

PUSH_CONSOLE_REDIS_DB = {
    'host': config['PUSH_CONSOLE_REDIS_HOST'],
    'port': config['PUSH_CONSOLE_REDIS_PORT'],
    'password': config['PUSH_CONSOLE_REDIS_PASSWORD']
}

PUSH_CONSOLE_RABBIT = {
    'host': config['PUSH_CONSOLE_RABBIT_HOST'],
    'port': config['PUSH_CONSOLE_RABBIT_PORT'],
    'virtual_host': config['PUSH_CONSOLE_RABBIT_VHOST'],
    'username': config['PUSH_CONSOLE_RABBIT_USER'],
    'password': config['PUSH_CONSOLE_RABBIT_PASSWORD']
}
