from general.utils import random_string, random_package_name, convert_to_sha256
from test_data.common_test_data import CommonTestData


class AppTestData(CommonTestData):

    @staticmethod
    def create_valid_data(name=None, package_name=None, app_signature=None):
        return {
              'name': name if name is not None else random_string(25),
              'package_name': package_name if package_name is not None else random_package_name(),
              'app_signature': app_signature if app_signature is not None else convert_to_sha256(random_string(25))
        }

    @staticmethod
    def create_invalid_package_names():
        return [
            random_package_name().replace('.', ' '),
            random_package_name().replace('.', '!'),
        ]

    @staticmethod
    def create_package_name_with_reserved_names():
        reserved_names = ['int', 'boolean', 'public',
                          'new', 'class', 'switch',
                          'import', 'if', 'return']
        return '.'.join(reserved_names)


app_test_data = AppTestData()
