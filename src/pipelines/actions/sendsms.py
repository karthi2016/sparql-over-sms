from connectors import AsteriskConnector
from services import AddressBook, Messenger


class SendSms:
    """Sends a sms"""

    @staticmethod
    def execute(message):
        from webapi import app

        # lookup receiver
        addressbook = AddressBook(app.config['c_contacts'], app.config['f_contacts'])
        contact = addressbook.get_contact(message.receiver)

        # compose sms
        categoryid = Messenger.categories[message.category]
        content = '{0} {1}'.format(categoryid, message.body)

        # send sms
        asterisk = AsteriskConnector(app.config['c_asterisk'])
        response = asterisk.send_sms(contact['phonenumber'], content)

        return response







