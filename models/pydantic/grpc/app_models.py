from pydantic import Field

from models.pydantic.rest.common_models import CommonModel
from test_data.enums import GrpcErrorCodes


class SuccessDeleteGrpcModel(CommonModel):
    pass


class ErrorDeleteGrpcModel(CommonModel):
    code: GrpcErrorCodes
    error_message: str = Field(alias="errorMessage")


class ResponseDeleteGrpcModel(CommonModel):
    error: ErrorDeleteGrpcModel | None = None
    success: SuccessDeleteGrpcModel | None = None
