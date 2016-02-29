
# message categories
SYSTEM = 0
SYSTEM_RESPONSE = 1
SPARQL_QUERY = 2
SPARQL_QUERY_RESPONSE = 3
SPARQL_UPDATE = 4
SPARQL_UPDATE_RESPONSE = 5


class Messenger:
    """Proxy for messaging"""
    categories = {
        SYSTEM: 'system',
        SYSTEM_RESPONSE: 'system-response',
        SPARQL_QUERY: 'sparql-query',
        SPARQL_QUERY_RESPONSE: 'sparql-query-response',
        SPARQL_UPDATE: 'sparql-update',
        SPARQL_UPDATE_RESPONSE: 'sparql-update-response'
    }

    def __init__(self, messagingconfig, addressbook, asterisk):
        self.messagingconfig = messagingconfig
        self.addressbook = addressbook
        self.asterisk = asterisk

    def send(self, contactid, category, body):
        contact = self.addressbook.get_contact(contactid)
        phonenumber = contact['phonenumber']

        message = '{0} {1}'.format(self.categories[category], body)
        self.asterisk.send_sms(phonenumber, message)

    def receive(self, phonenumber, message):
        category, body = message.split(' ', 2)
        sender = self.addressbook.find_contact(phonenumber)

        message = {
            'sender': sender['contactid'],
            'category': category,
            'body': body
        }
        return message
