import pytest

from general.clients.rabbitmq import create_rabbit_queue


@pytest.fixture(scope='function')
def sync_rabbit_queue():
    return create_rabbit_queue()


@pytest.fixture(scope='function')
def async_rabbit_queue():
    return create_rabbit_queue(routing_key='async')
