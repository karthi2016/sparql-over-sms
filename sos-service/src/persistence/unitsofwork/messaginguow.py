
class MessagingUoW:
    """description of class"""

    def __init__(self, contactrepo, messagerepo):
        self.contactrepo = contactrepo
        self.messagerepo = messagerepo

    def store_incoming(self, sender_ref, correlationid, category, position, body):
        # get or create sender/receiver
        sender = self.contactrepo.get_byref(sender_ref, create_if_nonexist=True)
        receiver = self.contactrepo.get_byname('~self', create_if_nonexist=True)

        self.store(sender, receiver, correlationid, category, position, body)

    def store_outgoing(self, receiver_ref, correlationid, category, position, body):
        # get or create sender/receiver
        sender = self.contactrepo.get_byname('~self', create_if_nonexist=True)
        receiver = self.contactrepo.get_byref(receiver_ref, create_if_nonexist=True)

        self.store(sender, receiver, correlationid, category, position, body)


    def store(self, sender, receiver, correlationid, category, position, body):
        senderid = sender.agentid
        receiverid = receiver.agentid

        message = messagerepo.create(senderid, receiverid, correlationid, category, position, body)

