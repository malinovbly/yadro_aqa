import uuid
from uuid import UUID
from datetime import datetime
from typing import List

from models.pydantic.rest.common_models import CommonModel, BaseResponseWithDataModel


class AppSignatureModel(CommonModel):
    """Model for app`s field 'app_signature'"""

    id: UUID
    value: str


class AppDataModel(CommonModel):
    """Model for app`s field 'data'"""

    id: UUID
    name: str
    created_at: datetime
    package_name: str


class AppDataWithAppSignaturesModel(AppDataModel):
    """Model for app`s field 'data' with 'app_signatures'"""

    app_signatures: List[AppSignatureModel] | None = None


class GetAppModel(BaseResponseWithDataModel):
    """Model for REST response GET app"""

    data: AppDataWithAppSignaturesModel


class GetAppsModel(BaseResponseWithDataModel):
    """Model for REST response GET apps"""

    data: List[AppDataWithAppSignaturesModel]


if __name__ == '__main__':
    r = {
      "status": "OK",
      "msg_code": "push_console_apps_successful_getting",
      "data": [
        {
          "id": uuid.uuid4(),
          "name": "string",
          "created_at": "2026-04-26T15:05:02.635Z",
          "package_name": "string",
          "app_signatures": [
            {
              "id": uuid.uuid4(),
              "value": "string"
            }
          ]
        }
      ]
    }
    c = GetAppsModel(**r)
