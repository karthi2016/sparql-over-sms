from utilities.messaging import to_response_category


class MessagingUoW:
    """description of class"""

    def __init__(self, agentrepo, messagerepo):
        self.agentrepo = agentrepo
        self.messagerepo = messagerepo

    def store_incoming(self, sender_address, correlationid, category, position, body):
        # get or create sender/receiver
        sender = self.agentrepo.get_byaddress(sender_address, create_if_nonexist=True)
        receiver = self.agentrepo.get_byname('~self', create_if_nonexist=True)

        return self.store(sender, receiver, correlationid, category, position, body)

    def store_outgoing(self, receiver_address, correlationid, category, body):
        # get or create sender/receiver
        sender = self.agentrepo.get_byname('~self', create_if_nonexist=True)
        receiver = self.agentrepo.get_byaddress(receiver_address, create_if_nonexist=True)

        return self.store(sender, receiver, correlationid, category, 0, body)

    def store(self, sender, receiver, correlationid, category, position, body):
        senderid = sender.id
        receiverid = receiver.id

        message = self.messagerepo.create(senderid, receiverid, correlationid, category, position, body)

        # update message flags
        message.complete = True if int(position) is 0 else self.is_complete(message)
        message.save()

        return message

    def is_complete(self, message):
        messageparts = message.parts

        expectedcount = max({part.position for part in messageparts})
        return len(messageparts) == expectedcount

    def is_answered(self, message):
        correlationid = message.correlationid
        responsecategory = to_response_category(message.category)

        response = self.messagerepo.get_bycorrelation(correlationid, responsecategory)
        return response is not None

    def mark_processed(self, message):
        message.processed = True
        message.save()
