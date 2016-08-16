from persistence.models import Message, MessagePart


class MessageRepo:
    """description of class"""

    def __init__(self, database):
        self.database = database

    def create(self, senderid, receiverid, correlationid, category, position, body):
        message = self.get_bycorrelation(correlationid, category)
        if message is None:
            message = Message(sender=senderid, receiver=receiverid, correlationid=correlationid, category=category)
            message.save()

        # create message part for position/body
        messagepart = MessagePart(message=message, position=position, body=body)
        messagepart.save()

        return message

    def get_bycorrelation(self, correlationid, category):
        try:
            return Message.get(correlationid=correlationid, category=category)
        except Message.DoesNotExist:
            return None
