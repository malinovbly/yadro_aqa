import uuid

from general.utils import random_string, random_uuid4
from test_data.common_test_data import CommonTestData


class ProjectTestData(CommonTestData):

    @staticmethod
    def create_valid_data(name=None):
        return {'name': name if name is not None else random_string()}

    @staticmethod
    def random_project_id():
        return random_uuid4()

    @staticmethod
    def create_data_with_unexpected_field():
        request_body = ProjectTestData.create_valid_data()
        request_body.update(ProjectTestData.create_random_data())
        return request_body


project_test_data = ProjectTestData()
