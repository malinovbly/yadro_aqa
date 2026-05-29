from pydantic import BaseModel, ConfigDict, Field

from test_data.enums import ResponseStatus


class CommonModel(BaseModel):
    """Model for config"""

    model_config = ConfigDict(extra='forbid')


class BaseResponseModel(CommonModel):
    """Model for base REST responses with fields 'status' and 'msg_code'"""

    status: ResponseStatus
    msg_code: str


class BaseResponseWithDataModel(BaseResponseModel):
    """Model for REST responses with field 'data'"""

    data: None


class BaseResponseWithMetaDataModel(BaseResponseWithDataModel):
    """Model for REST responses with field '_meta'"""

    meta: None = Field(alias='_meta')
