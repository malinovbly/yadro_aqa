from enum import StrEnum


class ResponseStatus(StrEnum):
    OK = 'OK'
    ERROR = 'ERROR'


class UserRole(StrEnum):
    USER = 'USER'
    BLOCKED = 'BLOCKED'
    SUPER_ADMIN = 'SUPER_ADMIN'


class UserQueryParam(StrEnum):
    ROLE = 'role'


class GrpcErrorCodes(StrEnum):
    ERROR_CODE_UNSPECIFIED = 'ERROR_CODE_UNSPECIFIED'
    BAD_REQUEST = 'BAD_REQUEST'
    BAD_TOKEN = 'BAD_TOKEN'
    NOT_FOUND = 'NOT_FOUND'
    ACCESS_DENIED = 'ACCESS_DENIED'
    CONFLICT = 'CONFLICT'
    INTERNAL_ERROR = 'INTERNAL_ERROR'
