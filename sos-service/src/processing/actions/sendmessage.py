from utilities.messaging import Messenger


class SendMessage:
    """Send a message"""
    name = "SendMessage"
    description = "Send a message"

    @staticmethod
    def execute(token):
        messenger = Messenger()
        messenger.send(token.message)

