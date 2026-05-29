import allure
import grpc
import pytest

from general.checkers.general_checkers import check_pydantic_model
from general.utils import grpc_msg_to_dict


@allure.step('Make gRPC request')
def make_grpc_request(
        stub, message, metadata, pydantic_model):
    try:
        response = stub(message, metadata=metadata)
        response_dict = grpc_msg_to_dict(response)

        if pydantic_model:
            check_pydantic_model(pydantic_model=pydantic_model, response=response_dict)

        return response_dict

    except grpc.RpcError as error:
        pytest.fail(f'gRPC request error: {error}')
