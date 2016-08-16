
class MessagingUoW:
    """description of class"""

    def __init__(self, contactrepo, messagerepo):
        self.contactrepo = contactrepo
        self.messagerepo = messagerepo

    def store_incoming(self, sender_address, correlationid, category, position, body):
        # get or create sender/receiver
        sender = self.contactrepo.get_byaddress(sender_address, create_if_nonexist=True)
        receiver = self.contactrepo.get_byname('~self', create_if_nonexist=True)

        self.store(sender, receiver, correlationid, category, position, body)

    def store_outgoing(self, receiver_address, correlationid, category, position, body):
        # get or create sender/receiver
        sender = self.contactrepo.get_byname('~self', create_if_nonexist=True)
        receiver = self.contactrepo.get_byaddress(receiver_address, create_if_nonexist=True)

        self.store(sender, receiver, correlationid, category, position, body)

    def store(self, sender, receiver, correlationid, category, position, body):
        senderid = sender.id
        receiverid = receiver.id

        message = self.messagerepo.create(senderid, receiverid, correlationid, category, position, body)

        # update message flags
        message.complete = True if int(position) is 0 else self.is_complete(message)
        message.save()
        
    def is_complete(self, message):
        messageparts = message.parts

        expectedcount = max({part.position for part in messageparts})
        return len(messageparts) == expectedcount


