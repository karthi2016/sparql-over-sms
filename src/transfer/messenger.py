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

        transfer = self.determine_transfer(receiver)
        if len(message.body) <= transfer.max_bodysize:
            body = self.encode_single(message)
            transfer.send_single(receiver, body)
        else:
            bodies = self.encode_multiple(message, transfer.max_bodysize)
            bodies.reverse()
            transfer.send_multiple(receiver, bodies)

    def receive(self, address, body):
        sender = self.contactrepo.find_contact(address)

        return Message(int(body[0]), body[5:], sender=sender['contactid'], correlationid=body[1:4],
                       position=Messenger.gsmchar_to_numeric(body[4]))

    def receive_stored(self, stored):
        return Message(int(stored['category']), stored['body'], sender=stored['contactid'],
                       correlationid=stored['messageid'])

    @staticmethod
    def encode_single(message):
        return '{0}{1}{2}{3}'.format(message.category, message.correlationid,
                                     Messenger.numeric_to_gsmchar(0), message.body)

    @staticmethod
    def encode_multiple(message, max_bodysize):
        body = message.body
        chunked = [body[i:i + max_bodysize] for i in range(0, len(body), max_bodysize)]

        return ['{0}{1}{2}{3}'.format(message.category, message.correlationid, Messenger.numeric_to_gsmchar(i + 1), x)
                for i, x in enumerate(chunked)]

    @staticmethod
    def determine_transfer(receiver):
        for strategy in transfer_strategies:
            if strategy.is_supported(receiver):
                return strategy

    @staticmethod
    def get_category_counterpart(messagecategory):
        return messagecategory + (1 if messagecategory % 2 is 0 else -1)

    @staticmethod
    def numeric_to_gsmchar(num):
        gsm = '@!#¤%&()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        return gsm[num]

    @staticmethod
    def gsmchar_to_numeric(char):
        gsm = '@!#¤%&()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        return gsm.index(char)




