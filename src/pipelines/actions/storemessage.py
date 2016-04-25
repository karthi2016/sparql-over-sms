from repositories import MessageRepo
from services import ServiceBox


class StoreMessage:
    """Stores a message"""
    name = 'StoreMessage'
    description = 'Stores a message'

    @staticmethod
    def execute(token):
        messagerepo = ServiceBox.get_instance(MessageRepo)

        message = token.message
        messageid = '{0}-{1}'.format(message.correlationid, message.category)
        messagerepo.add_message(messageid, message.category, message.sender, message.body)

