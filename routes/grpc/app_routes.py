import allure
from google.protobuf.json_format import ParseDict

from general.request_wrappers.grpc_wrapper import make_grpc_request
from general.utils import grpc_channel, make_grpc_auth_header
from models.pydantic.grpc.app_models import ResponseDeleteGrpcModel
from proto_files.push_console_pb2 import DeleteAppRequest
from proto_files.push_console_pb2_grpc import DeleteStub


@allure.step('gRPC request delete app')
def grpc_request_delete_app(
        access_token, message, pydantic_model=ResponseDeleteGrpcModel):
    stub = DeleteStub(grpc_channel()).DeleteApp
    parsed_message = ParseDict(js_dict=message, message=DeleteAppRequest())
    metadata = list(make_grpc_auth_header(access_token=access_token).items())

    response = make_grpc_request(
        stub=stub,
        message=parsed_message,
        metadata=metadata,
        pydantic_model=pydantic_model,
    )
    return response

