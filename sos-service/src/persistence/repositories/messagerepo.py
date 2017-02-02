from persistence.models import Message, MessagePart


class MessageRepo:
    """description of class"""

    def __init__(self, database):
        self.database = database

    def get_total(self):
        return (Message.select()
                .count())

    def get_all(self, page, items_per_page):
        return (Message.select()
                .order_by(Message.id.desc())
                .paginate(page, items_per_page))

    def get_all_outgoing(self, page, items_per_page):
        # outgoing categories are even numbers < 10
        outgoing = [i for i in range(0, 10, 2)]

        return (Message.select()
                .where(Message.category << outgoing)
                .order_by(Message.id.desc())
                .paginate(page, items_per_page))

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

    def get_outgoing_bycorrelation(self, correlationid):
        # outgoing categories are even numbers < 10
        outgoing = [i for i in range(0, 10, 2)]

        try:
            query = (Message.select()
                     .where(Message.correlationid == correlationid, Message.category << outgoing))

            return query.get()
        except Message.DoesNotExist:
            return None

    def get_incoming_bycorrelation(self, correlationid):
        # incoming categories are even numbers < 10
        incoming = [i for i in range(1, 10, 2)]

        try:
            query = (Message.select()
                     .where(Message.correlationid == correlationid, Message.category << incoming))

            return query.get()
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

    def delete(self, message):
        if message is int:
            message = self.get_byid(message)

        if message.delete_instance() > 0:
            return message

