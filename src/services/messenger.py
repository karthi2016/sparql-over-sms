
# message categories
SYSTEM = 'system'
SPARQL_QUERY = 'sparql-query'
SPARQL_UPDATE = 'sparql-update'
SPARQL_RESPONSE = 'sparql-response'


class Messenger:
    """Proxy for messaging"""
    categories = {
        SYSTEM: 0,
        SPARQL_QUERY: 1,
        SPARQL_UPDATE: 2,
        SPARQL_RESPONSE: 3
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
        sender = self.addressbook.find_contact(phonenumber)[0]

        message = {
            'sender': sender['contactid'],
            'category': {'{0}'.format(value): key for key, value in self.categories.items()}[category],
            'body': body
        }
        return message
