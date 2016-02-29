from connectors import AsteriskConnector
from services import AddressBook, Messenger


class SendSms:
    """Sends a sms"""
    name = "SendSms"
    description = "Send a sms"

    @staticmethod
    def execute(token):
        from webapi import app

        # lookup receiver
        addressbook = AddressBook(app.config['c_contacts'], app.config['f_contacts'])
        contact = addressbook.get_contact(token.message.receiver)

        # compose sms
        content = '{0} {1}'.format(token.message.category, token.message.body)

        # send sms
        asterisk = AsteriskConnector(app.config['c_asterisk'])
        token.result = asterisk.send_sms(contact['phonenumber'], content)









