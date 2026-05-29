import allure
import pytest
from pydantic import ValidationError

from test_data.enums import ResponseStatus


@allure.step('General check')
def general_checker(actual, expected):
    assert actual == expected, (
            f'Actual result: {actual}\n'
            f'Expected result: {expected}'
    )


@allure.step('Check REST response')
def check_rest_response(response, msg_code, status=ResponseStatus.ERROR):
    """Check REST response fields, which are always present"""
    general_checker(actual=response['msg_code'], expected=msg_code)
    general_checker(actual=response['status'], expected=status)


@allure.step('Check pydantic model')
def check_pydantic_model(pydantic_model, response: dict):
    try:
        return pydantic_model(**response)
    except ValidationError as error:
        # Падение через pytest.fail нужно для allure отчета, чтобы упавший шаг был красным
        # Если перехват через try не делать, падение в отчете будет желтым
        # Красное падение - ошибка на стороне сервера, желтая - ошибка на стороне нашего кода
        # Несоответствие ответа модели мы считаем за ошибку бека
        pytest.fail(str(error))


@allure.step('Check dict values')
def check_all_dict_values_are_equal(actual: dict, expected: dict):
    """Check all dict values are equal"""

    if len(expected.keys()) == 0 and len(actual.keys()) == 0:
        assert len(actual.keys()) == 0, (
            f'Actual result: {actual} vs Expected: {expected}'
        )

    for key in expected.keys():
        actual_value = actual.get(key)
        expected_value = expected.get(key)
        assert actual_value == expected_value, (
            f'Key: {key}. Actual: {actual_value} vs Expected: {expected_value}'
        )
