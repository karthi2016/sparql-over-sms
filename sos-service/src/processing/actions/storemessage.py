from services import ServiceBox


class StoreMessage:
    """Stores a message"""
    name = 'StoreMessage'
    description = 'Stores a message'

    @staticmethod
    def execute(token):
        messagerepo = ServiceBox.get_instance(MessageRepo)

        message = token.message
        identifier = message.correlationid
        messagerepo.add_message(identifier, 0, message.category, message.sender, message.body)

