from transfer.strategy import transfer_strategies
from transfer.wrappers import Message

MSG_USER = 0
MSG_USER_RESPONSE = 1
MSG_SYSTEM = 2
MSG_SYSTEM_RESPONSE = 3
MSG_SPARQL_QUERY = 4
MSG_SPARQL_QUERY_RESPONSE = 5
MSG_SPARQL_UPDATE = 6
MSG_SPARQL_UPDATE_RESPONSE = 7


class Messenger:
    """A facade for transfering messages"""
    categories = {
        MSG_USER: 'user',
        MSG_USER_RESPONSE: 'user-response',
        MSG_SYSTEM: 'system',
        MSG_SYSTEM_RESPONSE: 'system-response',
        MSG_SPARQL_QUERY: 'sparql-query',
        MSG_SPARQL_QUERY_RESPONSE: 'sparql-query-response',
        MSG_SPARQL_UPDATE: 'sparql-update',
        MSG_SPARQL_UPDATE_RESPONSE: 'sparql-update-response'
    }

    def __init__(self, contactrepo):
        self.contactrepo = contactrepo

    def send(self, message):
        receiver = self.contactrepo.get_contact(message.receiver)
        body = self.compose_body(message)

        transfer = self.determine_transfer(receiver)
        transfer.send_single(receiver, body)

    def receive(self, address, body):
        sender = self.contactrepo.find_contact(address)

        return Message(int(body[0]), body[5:], sender=sender['contactid'], correlationid=body[1:5])

    @staticmethod
    def compose_body(message):
        return '{0}{1}{2}'.format(message.category, message.correlationid, message.body)

    @staticmethod
    def determine_transfer(receiver):
        for strategy in transfer_strategies:
            if strategy.is_supported(receiver):
                return strategy

    @staticmethod
    def get_category_counterpart(messagecategory):
        return messagecategory + (1 if messagecategory % 2 is 0 else -1)


