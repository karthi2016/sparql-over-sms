
class MessagingUoW:
    """description of class"""

    def __init__(self, contactrepo, messagerepo):
        self.contactrepo = contactrepo
        self.messagerepo = messagerepo

    def store_incoming(sender, correlationid, category, position, body):
        pass

