import allure
from google.protobuf.json_format import MessageToDict

from test_data.rabbitmq_events import RabbitEvent
from proto_files import domain_pb2


@allure.step('Deserialize Rabbit message_body')
def deserialize_rabbit_message_body(message_body, event_type):
    event = None
    match event_type:
        case RabbitEvent.SyncCreateProjectSubject:
            event = domain_pb2.ProjectCreatedEvent()

    event.ParseFromString(message_body)
    des_message_body = MessageToDict(event)

    return des_message_body
