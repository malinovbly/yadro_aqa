from datetime import datetime
from uuid import UUID

from pydantic import EmailStr, Field

from models.pydantic.rest.common_models import BaseResponseWithDataModel, CommonModel
from test_data.enums import UserRole


class GetUsersDataModel(CommonModel):
    id: UUID
    email: EmailStr
    company_name: str = Field(min_length=1, max_length=255)
    created_at: datetime = Field(description='Дата создания записи в бд')
    role: UserRole | None


class GetLoginDataModel(CommonModel):
    user_id: UUID
    access_token: str
    refresh_token: str
    user_role: UserRole


class GetLoginModel(BaseResponseWithDataModel):
    data: GetLoginDataModel


class GetUsersModel(BaseResponseWithDataModel):
    data: list[GetUsersDataModel]
