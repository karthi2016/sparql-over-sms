from utilities.messaging import MessengerFactory


class SendMessage:
    """Send a message"""
    name = "SendMessage"
    description = "Send a message"

    @staticmethod
    def execute(token):
        message = token.message

        messenger = MessengerFactory.get_messenger(message.receiver)
        messenger.send(message)

