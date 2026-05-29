from enum import StrEnum


class RabbitEvent(StrEnum):
    SyncCreateProjectSubject = 'push-console_sync.projects.create'
    SyncRemoveProjectSubject = 'push-console_sync.projects.remove'

    SyncCreateAppSubject = 'push-console_sync.apps.create'
    SyncRemoveAppSubject = 'push-console_sync.apps.remove'
