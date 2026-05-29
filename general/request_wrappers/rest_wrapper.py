from http import HTTPStatus, HTTPMethod
from json import JSONDecodeError

import allure
import requests
from requests import HTTPError

from general.checkers.general_checkers import check_pydantic_model


@allure.step('Make REST request')
def make_rest_request(
        method=HTTPMethod.POST,
        url=None,
        return_only_status=False,
        headers=None,
        params=None,
        json=None,
        pydantic_model=None,
        **kwargs
):
    try:
        response = requests.request(method, url, headers=headers, params=params, json=json, **kwargs)
        status_code = response.status_code

        if return_only_status:
            return status_code

        if HTTPStatus.OK <= response.status_code <= HTTPStatus.INTERNAL_SERVER_ERROR:
            try:
                response = response.json()
            except JSONDecodeError:
                response = response.text

            if pydantic_model:
                check_pydantic_model(pydantic_model=pydantic_model, response=response)

            return response, status_code
        else:
            print(f'Test failed, response: {response.text}; code: {response.status_code}')
            pass
    except HTTPError as error:
        raise Exception(f"Something went wrong: {error}")
