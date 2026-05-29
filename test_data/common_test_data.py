import string

from general.utils import random_string, random_cyrillic_string, random_number


class CommonTestData:

    @staticmethod
    def create_valid_length_names(min_length=5, max_length=50, rnd_length=25):
        return [
            random_string(min_length),
            random_string(max_length),
            random_string(rnd_length)
        ]

    @staticmethod
    def create_uppercase_names(min_length=5, max_length=50, rnd_length=25):
        names = [
            random_string(min_length),
            random_string(max_length),
            random_string(rnd_length)
        ]
        return [name.upper() for name in names]

    @staticmethod
    def create_symbols_only_name():
        return string.punctuation

    @staticmethod
    def create_cyrillic_names(min_length=5, max_length=50, rnd_length=25):
        return [
            random_cyrillic_string(min_length),
            random_cyrillic_string(max_length),
            random_cyrillic_string(rnd_length)
        ]

    @staticmethod
    def create_numeric_names(min_length=5, max_length=50, rnd_length=25):
        return [
            random_number(min_length),
            random_number(max_length),
            random_number(rnd_length)
        ]

    @staticmethod
    def create_invalid_length_names(min_length=4, max_length=51):
        return [
            random_string(min_length),
            random_string(max_length)
        ]

    @staticmethod
    def create_invalid_language_name():
        return ['你好你好你好你好你好']

    @staticmethod
    def create_invalid_type_names():
        return [
            [], {}, (1,), 1.0, 1, True
        ]

    @staticmethod
    def create_random_data():
        return {'random_data': random_string()}
