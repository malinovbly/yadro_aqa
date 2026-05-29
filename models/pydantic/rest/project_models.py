from typing import List
from uuid import UUID

from pydantic import Field

from models.pydantic.rest.common_models import (CommonModel,
                                                BaseResponseWithDataModel,
                                                BaseResponseWithMetaDataModel)
from models.pydantic.rest.app_models import AppDataModel


class ProjectMetaDataModel(CommonModel):
    """Model for field '_meta'"""

    current_page: int
    page_count: int
    per_page: int
    total_count: int


class ProjectIdModel(CommonModel):
    """Model for project`s 'id'"""

    project_id: UUID


class ProjectNameModel(CommonModel):
    """Model for project`s 'name'"""

    name: str


class ProjectIdNameModel(ProjectIdModel, ProjectNameModel):
    """Model for project`s 'id' and 'name'"""

    pass


class GetProjectDataModel(ProjectIdNameModel):
    """Model for field 'data' in REST response GET project"""

    service_tokens: List[str]
    apps: List[AppDataModel]


class CreateProjectModel(BaseResponseWithDataModel):
    """Model for REST response POST project"""

    data: ProjectIdModel


class GetProjectModel(BaseResponseWithDataModel):
    """Model for REST response GET project"""

    data: GetProjectDataModel


class GetProjectsModel(BaseResponseWithMetaDataModel):
    """Model for REST response GET projects"""

    data: List[ProjectIdNameModel]
    meta: ProjectMetaDataModel = Field(alias='_meta')


if __name__ == '__main__':
    # r1 = {
    #   "status": "OK",
    #   "msg_code": "push_console_project_successful_getting",
    #   "data": {
    #     "project_id": "aed0409e-e927-4ebd-ab46-354abd5057be",
    #     "name": "string",
    #     "service_tokens": [
    #       "string"
    #     ],
    #     "apps": [
    #       {
    #         "id": "aed0409e-e927-4ebd-ab46-354abd5057be",
    #         "name": "string",
    #         "created_at": "2026-04-26T15:36:55.427Z",
    #         "package_name": "string"
    #       }
    #     ]
    #   }
    # }
    # c1 = GetProjectModel(**r1)

    # r2 = {
    #   "status": "OK",
    #   "msg_code": "push_console_projects_successful_getting",
    #   "data": [
    #     {
    #       "project_id": "aed0409e-e927-4ebd-ab46-354abd5057be",
    #       "name": "string"
    #     },
    #     {
    #       "project_id": "aed0409e-e927-4ebd-ab46-354abd5057be",
    #       "name": "string"
    #     }
    #   ]
    # }
    # c2 = GetProjectsModel(**r2)

    r3 = {'_meta': {'current_page': 1, 'page_count': 1, 'per_page': 20, 'total_count': 0}, 'data': [], 'msg_code': 'push_console_projects_successful_getting', 'status': 'OK'}
    c3 = GetProjectsModel(**r3)
