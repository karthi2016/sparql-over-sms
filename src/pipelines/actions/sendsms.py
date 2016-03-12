from services import ServiceBox
from transfer import Messenger


class SendSms:
    """Sends a sms"""
    name = "SendSms"
    description = "Send a sms"

    @staticmethod
    def execute(token):
        messenger = ServiceBox.get_instance(Messenger)
        messenger.send(token.message)









