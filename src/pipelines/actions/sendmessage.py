from services import ServiceBox
from transfer import Messenger


class SendMessage:
    """Send a message"""
    name = "SendMessage"
    description = "Send a message"

    @staticmethod
    def execute(token):
        messenger = ServiceBox.get_instance(Messenger)
        messenger.send(token.message)

