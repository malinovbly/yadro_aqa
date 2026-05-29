import random
import string
import hashlib
from uuid import UUID

import allure
import grpc
from google.protobuf.json_format import MessageToDict

from config import BASE_URL, GRPC_HOST


#region Auth

def make_auth_header(access_token: str) -> dict[str, str]:
    return {
        'Authorization': f'Bearer {access_token}'
    }


def make_grpc_auth_header(access_token: str) -> dict[str, str]:
    return {
        'authorization': f'Bearer {access_token}'
    }


def random_email() -> str:
    return f'{random_string(5)}@{random_string(5)}.com'


def random_password(length: int = 20) -> str:
    required_uppercase = random.choice(string.ascii_uppercase)
    required_lower_case = random.choice(string.ascii_lowercase)
    required_digit = random.choice(string.digits)
    required_symbol = '?'
    required = required_uppercase + required_lower_case + required_digit + required_symbol
    password = required + ''.join(random.choices(string.ascii_lowercase, k=length - len(required)))
    return password

#endregion

#region App

def random_package_name() -> str:
    parts = []
    for i in range(3):
        parts.append(random_string(10))
    return '.'.join(parts)


def convert_to_sha256(app_signature: str) -> str:
    encoded_str = app_signature.encode('utf-8')
    hashed_str = hashlib.sha256(encoded_str)
    hex_digest = hashed_str.hexdigest()
    return hex_digest

#endregion

#region DB

def make_specific_query(table, base_column_name, base_column_param, **extra):
    """
    Makes query such as:
        SELECT *
        FROM table
        WHERE base_param AND (extra1 OR extra2 OR ...);
    """
    if not extra:
        raise ValueError('At least one extra criterion must be specified')

    base_condition = f'{base_column_name} = %s'
    base_params = [base_column_param]
    extra_conditions, extra_params = [], []

    for key, value in extra.items():
        column_name = 'id' if ('_id' in key) else key
        extra_conditions.append(f'{column_name} = %s')
        extra_params.append(value)

    query = f"""
        SELECT *
        FROM {table}
        WHERE {base_condition} AND ({' OR '.join(extra_conditions)});
    """

    params = base_params + extra_params
    return query, params

#endregion

#region Other

@allure.step('Convert proto msg to dict')
def grpc_msg_to_dict(grpc_msg):
    return MessageToDict(grpc_msg)


def grpc_channel():
    return grpc.insecure_channel(target=GRPC_HOST)


def make_redis_key(key: str, **kwargs) -> str:
    if kwargs:
        return key.format(**kwargs)
    return key


def make_url(path: str, **kwargs) -> str:
    if kwargs:
        return (BASE_URL + path).format(**kwargs)
    return BASE_URL + path


def random_string(length: int = 10) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def random_cyrillic_string(length: int = 10) -> str:
    alph = 'абвгдеёжзиёклмнопрстуфхцчшщъыьэюя'
    return ''.join(random.choices(alph, k=length))


def random_number(length: int = 10) -> str:
    return ''.join(random.choices(string.digits, k=length))


def random_uuid4():
    return str(UUID(int=random.getrandbits(128), version=4))

#endregion
