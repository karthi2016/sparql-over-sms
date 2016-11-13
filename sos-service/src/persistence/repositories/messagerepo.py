from persistence.models import Message, MessagePart


class MessageRepo:
    """description of class"""

    def __init__(self, database):
        self.database = database

    def get_byid(self, messageid):
        try:
            return Message.get(id=messageid)
        except Message.DoesNotExist:
            return None

    def get_bycorrelation(self, correlationid, category):
        try:
            return Message.get(correlationid=correlationid, category=category)
        except Message.DoesNotExist:
            return None

    def create(self, senderid, receiverid, correlationid, category, position, body):
        message = self.get_bycorrelation(correlationid, category)
        if message is None:
            message = Message(sender=senderid, receiver=receiverid, correlationid=correlationid, category=category)
            message.save()

        # create message part for position/body
        if int(position) > 0:
            messagepart = MessagePart(message=message, position=position, body=body)
            messagepart.save()
        else:
            message.body = body
            message.save()

        return message

    def update(self, message):
        db_message = self.get_byid(message.id)
        db_message.__dict__.update(message.__dict__)
        db_message.save()

        return db_message



